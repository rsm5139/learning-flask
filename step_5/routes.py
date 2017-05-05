from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import Login, Register

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learning_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

app.secret_key = 'MY~SECRET~A0Zr98j/3yX R~XH!jmN]LWX/,?R'

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if 'email' in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data
            
            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session["email"] = form.email.data
                return redirect(url_for("index"))
            else:
                return redirect(url_for("login"))
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = Register()
    if 'email' in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        if form.validate() == False:
            return render_template("register.html", form=form)
        else:
            new_user = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()
            session['email'] = new_user.email
            return redirect(url_for("index"))
    return render_template("register.html", form=form)

@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("index"))

@app.route("/secret")
def secret():
    if 'email' not in session:
        return redirect(url_for("login"))
    return render_template("secret.html")

if __name__ == "__main__":
    app.run(debug=True)