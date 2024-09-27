from app import app
from forms import RegistrationForm, LoginForm
from models import User

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have successfully registered!")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("You have successfully logged in!")
            return redirect(url_for("home"))
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("You have successfully logged out!")
    return redirect(url_for("home"))
