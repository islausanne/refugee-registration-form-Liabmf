from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/view')
def view():
    return render_template('view.html')


if __name__ == '__main__':
    app.run(debug=True)