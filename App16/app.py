import flask as fk
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = fk.Flask(__name__)
app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    print(fk.request.method)
    if fk.request.method == "POST":
        first_name = fk.request.form["first_name"]
        last_name = fk.request.form["last_name"]
        email = fk.request.form["email"]
        date = fk.request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = fk.request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name,
                    email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit()
        fk.flash("Form successfully sent FAILED YOU!", "success")
    return fk.render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
