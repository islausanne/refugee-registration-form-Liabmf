from flask import Flask, request, render_template, redirect, url_for
import json
import os


app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/register')
def register():
    return render_template('register.html')

# Handle form submission (students will add JSON save code here)
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    lname = request.form['lname']
    age = request.form['age']
    country = request.form['gender']
    dob = request.form['dob']
    gender = request.form['country']

    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []
    data.append({'name': name, 'lname': lname, 'age': age, 'gender': gender, 'dob': dob, 'country': country})

    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('view_registrations'))

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