from .acceuil import app
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user



login_manager = LoginManager(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id:int):
    return User.query.get(user_id)

convention ={
    "ix":'ix_%(column_0_label)s',
    "uq":'uq_%(table_name)s_%(column_0_name)s',
    "ck":'ck_%(table_name)s_%(constraint_name)s',
    "fk":'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    "pk":'pk_%(table_name)s',
}
metadata = MetaData(naming_convention=convention)
db=SQLAlchemy(app)
migrate=Migrate(app,db, render_as_batch=True)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    login = db.Column(db.String(200), unique=True, nullable=False)
    pp_url = db.Column(db.Text, nullable=True)
    certified = db.Column(db.Boolean, default=False)
    etat = db.Column(db.Boolean, default=True)
    lien = db.Column(db.Text, nullable=True)
    tweets = db.relationship("Tweet",backref="user",lazy=False)
    description = db.relationship("Description", backref="user", lazy=False)
    profession = db.relationship("Profession",backref="user",lazy=False)
    localisation = db.relationship("Localisation", backref="user", lazy=False)

    def __init__(self, name, username, login, pp_url, certified=False, etat=True):
        super().__init__()
        self.name = name
        self.username = username
        self.login = login
        self.pp_url = pp_url
        self.certified = certified
        self.etat = etat

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=True)
    type = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    img_url = db.Column(db.Text, nullable=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    commentaire = db.relationship("Commentaire", backref="user", lazy=False)
    like = db.relationship("Like", backref="user", lazy=False)

    def __init__(self, id_user, content, date, type=1) :
        super().__init__()
        self.id_user = id_user
        self.content = content
        self.date = date
        self.type = type
    def Dto(self) :
        return "User : "+ str(self.id_user) +"\n Content : "+ self.content+"\n Date : "+ str(self.date)

class Description(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.Text, nullable=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Localisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.Text, nullable=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Profession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.Text, nullable=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Commentaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    # date = db.Column(db.DateTime, nullable=False)
    id_tweet = db.Column(db.Integer, db.ForeignKey('tweet.id'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __init__(self, id_user,id_tweet, content ) :
        super().__init__()
        self.id_user = id_user
        self.id_tweet = id_tweet
        self.content = content
        # self.date = date

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_tweet = db.Column(db.Integer, db.ForeignKey('tweet.id'), nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    id_tweet = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    etat = db.Column(db.Boolean, nullable=False, default=False)
    upvote = db.Column(db.Integer)
# with app.app_context():
    #db.create_all()
    


def getAllUser():
    return User.query.all()

def getUserById(id:int):
    return User.query.filter_by(id=id).first()

def getAllTweets():
    return Tweet.query.all()

def getTweetsByUser(user:User):
    return Tweet.query.filter_by(id_user=user.id).all()

def getTweetById(id:int):
    return Tweet.query.filter_by(id=id).first()

def getCommentsByTweetId(id:int):
    return Commentaire.query.filter_by(id_tweet=id).all()

def getsuggestionUsers():
    return User.query.limit(3).all()

def insert(object):
    db.session.add(object)
    db.session.commit()

def addUser(user:User):
    db.session(user)
    db.session.commit()

def connexion(login):
    userByName = User.query.filter_by(username=login).first()
    userByLogin = User.query.filter_by(login=login).first()
    # Sauvegarder l'utilisateur connecte
    if userByName :
        login_user(userByName)
        return True
    if userByLogin :
        login_user(userByLogin)
        return True
    return False 

def deconnexion():
    logout_user()

def getTweetsFilteredByContent(filter:str):
    tweets = getAllTweets()
    tweetsFiltered = []
    for tweet in tweets : 
        if(filter.lower() in tweet.content.lower()):
            tweetsFiltered.append(tweet)
    return tweetsFiltered

data_users =[
    {
    "id" : 1,
    "name": "KREATIIVE",
    "username":"kreatiive_",
    "login":"kephnze@gmail.com",
    "pp_url":"../../static/img/natsu.png",
    "certified":False
    },    {
    "id" : 2,
    "name": "Koumooo",
    "username":"KoumoBur",
    "login":"koumodetente@gmail.com",
    "pp_url":"../../static/img/sherine.png",
    "certified":False
    },    {
    "id" : 3,
    "name": "Shérine FCB",
    "username":"sherineafcb",
    "login":"sherineafcb@gmail.com",
    "pp_url":"../../static/img/natsu.png",
    "certified":False
    },    {
    "id" : 4,
    "name": "Lonni",
    "username":"kidlonni",
    "login":"lonni@gmail.com",
    "pp_url":"../../static/img/banner.png",
    "certified":False
    },
]



