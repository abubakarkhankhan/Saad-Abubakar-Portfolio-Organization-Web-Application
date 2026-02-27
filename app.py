from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'novaedge_secret_key_2024'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Database initialization
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contact_messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  message TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS chatbot_logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_message TEXT NOT NULL,
                  bot_response TEXT NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO contact_messages (name, email, message) VALUES (?, ?, ?)",
                  (name, email, message))
        conn.commit()
        conn.close()
        
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message', '').lower()
    
    # Simple rule-based responses
    if 'course' in user_msg or 'program' in user_msg:
        bot_response = "We offer Web Development, Graphic Design, Python Basics, and Office Skills courses!"
    elif 'fee' in user_msg or 'price' in user_msg or 'cost' in user_msg:
        bot_response = "Our courses range from PKR 5,000 to PKR 15,000. Contact us for details!"
    elif 'time' in user_msg or 'timing' in user_msg or 'schedule' in user_msg:
        bot_response = "Classes run Monday-Friday, 9 AM - 5 PM. Weekend batches also available!"
    elif 'location' in user_msg or 'address' in user_msg or 'where' in user_msg:
        bot_response = "We're located at Tech Plaza, Main Boulevard, Lahore, Pakistan."
    elif 'contact' in user_msg or 'phone' in user_msg or 'email' in user_msg:
        bot_response = "Contact us: +92-300-1234567 | info@novaedge.edu.pk"
    elif 'hello' in user_msg or 'hi' in user_msg or 'hey' in user_msg:
        bot_response = "Hello! Welcome to NovaEdge Skills Academy. How can I help you today?"
    else:
        bot_response = "I can help you with courses, fees, timings, location, and contact info. What would you like to know?"
    
    # Store in database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO chatbot_logs (user_message, bot_response) VALUES (?, ?)",
              (user_msg, bot_response))
    conn.commit()
    conn.close()
    
    return jsonify({'response': bot_response})

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == '1234':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contact_messages ORDER BY id DESC")
    messages = c.fetchall()
    conn.close()
    
    return render_template('dashboard.html', messages=messages)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
