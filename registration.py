"""
This is a refugee registration form, where refugees can enter in their data and then view their own and other entries
"""
from flask import Flask, request, render_template, redirect, url_for
import json
import os


app = Flask(__name__)

#this is an app route, an app route is basically a page on the website, the '/' shows what comes after the slash in the URL
# (in this case nothing as it's my homepage)
@app.route('/')
def menu():
    return render_template('menu.html')

#this is another app route, this takes the user to the registration page where the form is
@app.route('/register')
def register():
    return render_template('register.html')

# This handles form submission, its basically saying to save the users answers until the variables
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    lname = request.form['lname']
    age = request.form['age']
    country = request.form['gender']
    dob = request.form['dob']
    gender = request.form['country']
    email = request.form['email']
    number = request.form['number']
    family = request.form['family']
    medical = request.form['medical']
    anything = request.form['anything']

    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
#and then here is where it appends the data that has just been saved as a variable and saves it as a list under the variable name 'data'
    else:
        data = []
    data.append({'name': name, 'lname': lname, 'age': age, 'gender': gender, 'dob': dob, 'country': country, 'email': email, 'number': number, family: family, 'medical': medical, anything: anything})

    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('menu'))

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/view')
def view_registrations():
    with open('registrations.json', 'r') as file:
        data = json.load(file)
    return render_template('view.html', registrations=data)

    return render_template('view.html', registrations=[])



if __name__ == '__main__':
    app.run(debug=True)