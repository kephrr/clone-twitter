
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

for user in data_users : 
        us =(user['name'],user['username'],user['login'],user['pp_url'],user['certified'])
        # us.id=user['id']
      #  db.session.add(us)
   # db.session.commit()


