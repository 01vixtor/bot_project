from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from app import db
from models import User, BotConfig
from forms import LoginForm, ConfigForm

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("main.dashboard"))
        flash("Login inválido")
    return render_template("login.html", form=form)

@main.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    config = BotConfig.query.first()
    if not config:
        config = BotConfig(message_text="Mensagem padrão")
        db.session.add(config)
        db.session.commit()
    
    form = ConfigForm(obj=config)
    if form.validate_on_submit():
        form.populate_obj(config)
        db.session.commit()
        flash("Configurações salvas")
        return redirect(url_for("main.dashboard"))

    return render_template("dashboard.html", form=form, config=config)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))
