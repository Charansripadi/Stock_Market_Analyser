from flask import Flask, render_template, request, send_from_directory
import pymysql as sql
def sql_connect():
    conn = sql.connect(
        host="localhost",
        user="root",
        password="SSrings90@",
        database="demo1"
    )
    c = conn.cursor()
    return conn, c
app = Flask(__name__)
@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/result')
def result():
    return render_template('result.html')
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/student')
def student():
    return render_template('student.html')
@app.route('/signin',methods=['POST'])
def deb():
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        print(username,password
        )
        conn, c = sql_connect()
        c.execute("INSERT INTO yy(username,password) VALUES (%s,%s)",(username, password))
        conn.commit()
        return render_template('result.html')
@app.route('/google')
def google():
    return render_template('google.html')
@app.route('/amazon')
def amazon():
    return render_template('microsoft.html')
@app.route('/abc')
def abc():
    return render_template('abc.html')
@app.route('/spacex')
def spacex():
    return render_template('spacex.html')
@app.route('/udemy')
def udemy():
    return render_template('udemy.html')
@app.route('/list')
def list():
    return render_template('list.html')
@app.route('/login',methods=['POST'])
def ldb():
    if request.method== 'POST':
        username = request.form['username']
        password = request.form['password']
        conn, c = sql_connect()
        if c.execute("SELECT * FROM yy WHERE username=%s and password=%s",(username, password)):
            conn.commit()
            return render_template('result.html')
        else:
            return render_template('validate.html')
@app.route("/images/<path:images>")
def serve_image(images):
    return send_from_directory("images", images)
if __name__ == '__main__':
    app.run(debug=True)
