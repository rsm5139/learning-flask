from flask import Flask, render_template, request
from models import db, SocialApp
from forms import CommentForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learning_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.secret_key = 'MY~SECRET~A0Zr98j/3yX R~XH!jmN]LWX/,?R'

@app.route("/", methods=["GET", "POST"])
def index():
    form = CommentForm()
    
    if request.method == "POST":
        if form.validate() == False:
            pass
        else:
            new_comment = SocialApp(form.name.data, form.comment.data)
            db.session.add(new_comment)
            db.session.commit()
    
    comments = SocialApp.query.all()
    return render_template("index.html", form=form, comments=comments)

if __name__ == "__main__":
    app.run(debug=True)