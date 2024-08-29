from .acceuil import app, render_template, getAllUser, request, redirect
from .models import load_user, login_user, login_required, connexion, User, insert, deconnexion
from pprint import pprint


@app.route("/")
@app.route("/login", methods=['GET'])
def login_page():
    return render_template("/views/login.html")


@app.route("/logout", methods=['GET'])
def logout_page():
    deconnexion()
    return render_template("/views/login.html")

@app.route("/login", methods=['POST'])
def login():
    # Connexion
    login = request.form['login']
    if connexion(login) :
        return redirect("/home")
    return render_template("/views/login.html")

@app.route("/signup", methods=['GET'])
def inscription_page():
    return render_template("/views/signup.html")

@app.route("/signup", methods=['POST'])
def inscription():
    user = User(
        request.form['username'],
        request.form['name'],
        request.form['login'],
        ''
    )
    pprint(locals())
    if not connexion(user.login):
        insert(user)
    login_user(user)
    return redirect("/home")

@app.errorhandler(404) 
def not_found(e): 
  return render_template("/views/_404.html")

@app.errorhandler(401) 
def not_found(e): 
  return render_template("/views/_unauthorized.html") 
