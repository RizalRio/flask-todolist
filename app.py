import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from datetime import date, datetime
from sqlalchemy import Date as SqlDate

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'kunci_rahasia_super_aman_buatan_rizal'  # Ganti dengan random string yang panjang

db = SQLAlchemy(app)

# --- SETUP FLASK-LOGIN ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Kalau user belum login, lempar ke sini

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- MODELS ---
# Model User (Baru)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    # Relasi: Satu User punya banyak Todo
    todos = db.relationship('Todo', backref='owner', lazy=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    deadline = db.Column(SqlDate, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    # Foreign Key: Todo ini punya siapa?
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

CATEGORIES = ["Pekerjaan", "Kuliah", "Pribadi", "Urgent", "Lainnya"]

# --- HELPER ---
def parse_date(date_str):
    if not date_str: return None
    try: return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError: return None

# --- AUTH ROUTES (Baru) ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Cek apakah username sudah ada
        if User.query.filter_by(username=username).first():
            flash('Username sudah dipakai, cari yang lain ya!', 'warning')
            return redirect(url_for('register'))
        
        # Hash password sebelum simpan (Security First!)
        hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password_hash=hashed_pw)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Akun berhasil dibuat! Silakan login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        # Cek user ada DAN password cocok
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash(f'Selamat datang kembali, {user.username}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Username atau password salah.', 'warning')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('login'))

# --- APP ROUTES (Diproteksi) ---
@app.route('/')
@login_required  # <-- Proteksi: Hanya user login yang bisa akses
def index():
    status = request.args.get('status', 'all')
    category_filter = request.args.get('category')
    search_query = request.args.get('q', '')

    # Query hanya ambil Todo milik current_user
    query = Todo.query.filter_by(user_id=current_user.id)

    if search_query:
        query = query.filter(Todo.task.ilike(f'%{search_query}%'))

    if status == 'active':
        query = query.filter_by(done=False)
    elif status == 'completed':
        query = query.filter_by(done=True)

    if category_filter:
        query = query.filter_by(category=category_filter)

    todos = query.order_by(
        db.case((Todo.deadline.is_(None), 1), else_=0),
        Todo.deadline
    ).all()

    return render_template(
        'index.html',
        todos=todos,
        current_status=status,
        current_category=category_filter,
        search_query=search_query,
        categories=CATEGORIES,
        today=date.today(),
        user=current_user # Kirim data user ke template
    )

@app.route('/add', methods=['POST'])
@login_required
def add():
    task = request.form.get('task')
    deadline_str = request.form.get('deadline')
    category = request.form.get('category') or None

    if task:
        deadline = parse_date(deadline_str)
        # Penting: Masukkan user_id saat create
        new_todo = Todo(task=task, deadline=deadline, category=category, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()
        flash('Tugas berhasil ditambahkan!', 'success')
        
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
@login_required
def toggle(id):
    # Get todo milik user yang login saja (prevensi user lain edit punya orang)
    todo = Todo.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    todo = Todo.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(todo)
    db.session.commit()
    flash('Tugas dihapus.', 'warning')
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    todo = Todo.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    
    if request.method == 'POST':
        new_task = request.form.get('task', '').strip()
        deadline_str = request.form.get('deadline')
        category = request.form.get('category') or None

        if new_task:
            todo.task = new_task
            todo.deadline = parse_date(deadline_str)
            todo.category = category
            db.session.commit()
            flash('Tugas diupdate.', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit.html', todo=todo, categories=CATEGORIES)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)