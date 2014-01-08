from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/personal/')
def personal():
    return render_template('personal.html')

@app.route('/resume/')
def resume():
    return redirect(url_for('static',filename='resources/resume.pdf'))

if __name__ == '__main__':
    app.run(debug=True)