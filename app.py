from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return logged_in()
    else:
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    user = get_user(request.form['username'])
    if user == None:
        add_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logged-in')
def logged_in(): 
    '''
    if request.method == 'GET':
        return 'You just made a GET request!'
    else:
        return update_food(request.form["fav_food"], login_session['name'] )
'''
    return render_template('logged.html')

#update the user's favorite food using the function you made in databases.py.
@app.route('/update-food', methods=['GET', 'POST'])
def food_function():
    if request.method == 'GET':
        return render_template('logged.html', fav_food =None)
    else:
        update_food(request.form["fav_food"], login_session['name'] )
        return render_template('logged.html', fav_food =request.form["fav_food"])




@app.route('/logout')
def logout():
    login_session['logged_in'] = False
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
