from flask import Flask
from flask import render_template, redirect, flash
from app.config import Config
from app.forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Asset Metrix'}

    return render_template('homepage.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('Login.html', title='Sign In', form=form)

if __name__ == "__main__":
    app.run(debug=True)
