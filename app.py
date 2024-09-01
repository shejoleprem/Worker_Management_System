from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        passw = request.form['password']

        query = "SELECT name, password FROM users WHERE name=? AND password=?"
        cursor.execute(query, (name, passw))
        results = cursor.fetchall()
        connection.close()

        if len(results) == 0:
            message = "User not found or incorrect credentials."
        else:
            return redirect(url_for('admin'))  # Redirect to another route (e.g., admin page)

    return render_template('index.html', message=message)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/Templates/register_worker.html',methods=['GET', 'POST'])
def register_worker1():
    print("hii")
    return render_template('register_worker.html')

@app.route('/register_worker', methods=['GET', 'POST'])
def register_worker():
    if request.method == 'POST':
        connad = sqlite3.connect('worker_data.db')
        cursad = connad.cursor()

        wname = request.form['name']
        wqual = request.form['qualification']
        wplace = request.form['place']
        print(wname)
        print(wqual)
        print(wplace)

        # Correct SQL syntax and parameterized query to avoid SQL injection
        query = "INSERT INTO workers (name, qualification, place) VALUES (?, ?, ?)"
        cursad.execute(query, (wname, wqual, wplace))

        # Commit the transaction to save changes
        connad.commit()
        connad.close()

        # Redirect to a success page or back to the registration page
        return redirect(url_for('register_worker'))
    
    return render_template('register_worker.html')


@app.route('/view_worker', methods=['GET', 'POST'])
def worker_details():
    print("Hii")
    workers = get_workers_details()
    
    return render_template('worker_details.html', workers=workers)

def get_workers_details():
    # Connect to SQLite databas+e
    conn = sqlite3.connect('worker_data.db')
    cursor = conn.cursor()
    
    # Execute a query to fetch all workers
    cursor.execute("SELECT * FROM workers")
    workers = cursor.fetchall()
    print("in details")
    # Close the connection
    conn.close()
    
    # Return the workers as a list of dictionaries
    return [
        {
            'name': row[0],
            'qualification': row[1],
            'place': row[2],
            'Test1': row[3],
            'Test2': row[4]
        }
        for row in workers
    ]


if __name__ == '__main__':
    app.run(debug=True, port=8080)
