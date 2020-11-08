from flask import Flask,session,redirect
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from flask_mail import Mail,Message
from flask_mysqldb import MySQL



app=Flask(__name__)
app.config['SECRET_KEY']='qwerty@123'
print(app.config)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'venkatstark3918@gmail.com'
app.config['MAIL_PASSWORD'] = 'Venkat200%'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
mysql = MySQL(app)

@app.route("/db")
def db():
    cursor=mysql.connection.cursor()
    cursor.execute('select * from User')
    result=cursor.fetchall()
    return str(result)

@app.route("/mail")
def index():
    msg = Message('Hello', sender = 'venkatstark3918@gmail.com', recipients = [])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


@app.route('/register', methods=['GET', 'POST'])
def register_page():        
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':      
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
      
        
        cursor = mysql.connection.cursor()
        cursor.execute(f"insert into user values('{email}','{username}','{password}')")
        mysql.connection.commit()
        cursor.close()
        
        data = "user added successfully"
        return render_template("login.html", data=data)


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def user_login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor=mysql.connection.cursor()
        cursor.execute(f"select * from user where username='{username}'")
        result=cursor.fetchone()
        if result is None:
            return render_template('login.html')
        elif result[1]==username and password==result[2]:
            session['user'] = username

            return render_template('home.html')

        

       

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return redirect(url_for('user_login'))



         
@app.errorhandler(404)
def page_not_found(error):
    return render_template('my_error_page.html'), 404 


    

@app.route('/home')

def home():
    return render_template("home.html")

@app.route('/chooseus')

def chooseus():
    return render_template("choose us.html")

@app.route('/contact')

def contact():
    return render_template("contact.html")

@app.route('/women')

def women():
    return render_template("women.html")

@app.route('/men')

def men():
    return render_template("men.html")

@app.route('/kids')

def kids():
    return render_template("kids.html")

@app.route('/traditional')

def traditional():
    return render_template("traditional.html")

@app.route('/top')

def top():
    return render_template("top wear.html")

@app.route('/winter')

def winter():
    return render_template("winter wear.html")

@app.route('/shirtandtrousers')

def shirtsandtrousers():
    return render_template("shirtsandtrousers.html")

@app.route('/denimwear')

def denimwear():
    return render_template("denimwear.html")

@app.route('/lounge')

def lounge():
    return render_template("lounge wear.html")

@app.route('/fashion')

def fashion():
    return render_template("kids fashion.html")

@app.route('/party')

def party():
    return render_template("kids partywear.html")

@app.route('/topwear')

def topwear():
    return render_template("kids topwear.html")






if __name__=='__main__':
    app.run(debug=True)