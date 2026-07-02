from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret_finance_key"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            conn.close()
            return redirect(url_for('dashboard'))
        else:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            
            new_user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            session['user_id'] = new_user['id']
            session['username'] = new_user['username']
            conn.close()
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    user_id = session['user_id']
    
    transactions = conn.execute('SELECT * FROM transactions WHERE user_id = ? ORDER BY date DESC', (user_id,)).fetchall()
    
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'Income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'Expense')
    balance = total_income - total_expense
    
    # NEW: Group expenses for the Pie Chart
    category_data = {}
    for t in transactions:
        if t['type'] == 'Expense':
            cat = t['category']
            category_data[cat] = category_data.get(cat, 0) + t['amount']
            
    chart_labels = list(category_data.keys())
    chart_values = list(category_data.values())
    
    conn.close()
    
    return render_template('dashboard.html', 
                           username=session['username'], 
                           balance=balance, 
                           income=total_income, 
                           expense=total_expense,
                           transactions=transactions,
                           chart_labels=chart_labels,
                           chart_values=chart_values)

@app.route('/add', methods=['POST'])
def add_transaction():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    amount = request.form['amount']
    category = request.form['category']
    trans_type = request.form['type']
    user_id = session['user_id']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO transactions (user_id, amount, category, type) VALUES (?, ?, ?, ?)', 
                 (user_id, amount, category, trans_type))
    conn.commit()
    conn.close()
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)