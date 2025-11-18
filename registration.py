from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/register')
def register():
    return render_template('register.html')

# Handle form submission (students will add JSON save code here)
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    country = request.form['country']
    age = request.form['age']
    medical = request.form['medical']

    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []
    data.append({'name': name, 'country': country, 'age': age, 'medical': medical})

    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('index'))

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