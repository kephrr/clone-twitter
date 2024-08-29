from flask import Flask, render_template, redirect, url_for, request 
from datetime import datetime
app = Flask(__name__)
app.config.from_pyfile("../config.py")
from pprint import pprint
from .models import login_required, current_user, getCommentsByTweetId,getsuggestionUsers,getTweetById, insert,getTweetsByUser,getTweetsFilteredByContent, getAllTweets, getUserById, getAllUser, Tweet, Commentaire


@app.route("/home")
@login_required
def home(content=[]):
    users=getsuggestionUsers()
    if content ==[]:
        content = TweetsDto(getAllTweets())
        content.reverse()
    return render_template("/views/home.html",current_user=current_user, users=users, tweets=content)


@app.route("/account")
@login_required
def myAccount(content=[]):
    users=getsuggestionUsers()
    if content ==[]:
        content = TweetsDto(getTweetsByUser(current_user))
        content.reverse()
    return render_template("/views/account.html",current_user=current_user, users=users, tweets=content)


@app.route("/account/<int:id>")
@login_required
def account(id, content=[]):
    user = getUserById(id)
    users=getsuggestionUsers()
    if content ==[]:
        content = TweetsDto(getTweetsByUser(user))
        content.reverse()
    return render_template("/views/account.html",current_user=user, users=users, tweets=content)

# PUBLIER UN TWEET

@app.route("/home/add-tweet", methods=['POST'])
@login_required
def tweet():
    content = request.form['content']
    date = datetime.now()
    insert(Tweet(current_user.id, content, date))
    return redirect("/home")



# FAIRE UNE RECHERCHE DE TWEETS

@app.route("/search", methods=['POST'])
@login_required
def search():
    filter = request.form['filter']
    content = TweetsDto(getTweetsFilteredByContent(filter))
    return render_template("/views/search.html",current_user=current_user,tweets=content)

# FAIRE UNE RECHERCHE DE TWEETS

@app.route("/search", methods=['GET'])
@login_required
def search_():
    return render_template("/views/search.html")

@app.route("/tweet-details/<int:id>",methods=['POST', 'GET'])
@login_required
def tweet_details(id):
    tweet = getTweetById(id)
    date=tweet.date.strftime("%I:%M %p · %d %b %Y")
    author = getUserById(tweet.id_user)
    comments = CommentsDto(getCommentsByTweetId(tweet.id))
    pprint(locals())
    return render_template("/views/tweet-details.html",current_user=current_user, comments=comments, id_tweet=id, author=author, subject=tweet, date=date)


@app.route("/tweet-details/add-comment", methods=['POST'])
@login_required
def add_comment():
    response = request.form
    id_tweet=response['id_tweet']
    insert(Commentaire(response['id_user'], id_tweet,response['content']))
    return redirect("/tweet-details/"+id_tweet)


def TweetsDto(tweets):
    content = []
    for tweet in tweets :
        user = getUserById(tweet.id_user)
        tweet = dict(
                    name=user.name, 
                    username=user.username, 
                    pp_url=user.pp_url, 
                    tweet_content=tweet.content,
                    date=tweet.date.strftime("%d/%m/%y"),
                    type=tweet.type,
                    img_url='', 
                    id_user=user.id,
                    id_tweet=tweet.id
                    )
        content.append(tweet)
    return content

def CommentsDto(comments):
    content = []
    for comment in comments :
        user = getUserById(comment.id_user)
        tweet = getTweetById(comment.id_tweet)
        content.append(dict(
                    name=user.name, 
                    username=user.username, 
                    pp_url=user.pp_url, 
                    content=comment.content,
                    img_url='', 
                    id_user=user.id,
                    id_tweet=tweet.id
                    ))
    return content