from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
import pyodbc

app = Flask(__name__)
app.secret_key = 'your_secret_key'


# SQL Server connection details
server = 'localhost'
database = 'myprogram'

conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"


def get_connection():
    return pyodbc.connect(conn_str)

@app.route('/')
def index():

    return render_template('registration.html')

def checkUsername(name: str) -> bool:
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE UserName = ?", (name,))
        existing_user = cursor.fetchone()
        cursor.close()
        conn.close()
        return existing_user is not None
    except Exception as e:
        print("DEBUG: Exception in checkUsername() ->", e)
        return False


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":  
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            return render_template('registration.html', error="Password do not match!")

        try:
            if checkUsername(username):
                error = "Username already exists!"
                return render_template('registration.html', error=error, show_register= True)
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
            conn.commit()
            conn.close()
            session['username']= username
            return redirect(url_for('login'))

        except Exception as e:
            print("DEBUG: Exception occurred ->", e)  # This line helps print error clearly
            return f"Error: {str(e)}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['login_username']
        password = request.form['login_password']
        
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            session['username'] = username
            return redirect(url_for('todo'))  
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')


@app.route("/registration")
def registration():
    return render_template("registration.html")




@app.route('/todo')
def todo():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('to-do.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (content) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('todo'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('todo'))



if __name__ == '__main__':
    app.run(debug=True) 