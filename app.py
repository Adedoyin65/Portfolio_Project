from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import SignUp, LoginForm

app = Flask(__name__)
app.config[SECRET_KEY] = d89c34230b2f5b3aff7c6b6f9f8dadd8
app.config[SQLALCHEMY_DATABASE_URI] = sqlite:///site.db
app.config[SQLALCHEMY_TRACK_MODIFICATIONS] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default=default.jpg)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.image_file})"

@app.route("/")
@app.route("/home")
def home():
    return render_template(home.html, title=Home)

@app.route("/about")
def about():
    return render_template(about.html, title=About)

@app.route("/register", methods=[GET,POST])
def register():
    form = SignUp()
    if form.validate_on_submit():
        return redirect(url_for(home))
    return render_template(register.html, title=register, form=form)

@app.route("/login", methods=[GET,POST])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == ogunyemidaniel65@gmail.com and form.password.data == password:
            return redirect(url_for(home))
        else:
            flash(fLogin not successful, danger)
    return render_template(login.html, title=login, form=form)

@app.route("/user")
def user_page():
    return render_template(user.html, title=User Page)


@app.route("/logout")
def logout():
    return redirect(url_for(home))

if __name__ == __main__:
    app.run(debug=True)
