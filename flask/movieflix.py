from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response ,render_template ,url_for
import json

client = MongoClient('mongodb://mongodb:27017/')



db = client['MovieFlix']
users = db['Users']
movies = db['Movies']



# Initiate Flask App
app = Flask(__name__)
           

@app.route('/loginusers', methods=['POST','GET'])
def login_users():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['psw']
        
        if users.find({"email": email}).count() != 0 :
            user = users.find_one({"email": email})
            if user['password'] == password :
                loguser = user['email'] 
                
                if user['category'] == "admin" :
                    return redirect(url_for('mov_flix_admin', usr = loguser))
                else:    
                    return redirect(url_for('mov_flix', usr = loguser ))
        else:
            return 'Try again. Icorrect values'
            
    return render_template('login.html')
 
@app.route('/registusers', methods=['POST','GET'])
def regist_users():
    if request.method == "POST":
    
        email = request.form['email']
        username = request.form['name']
        password = request.form['psw']
        if users.find({"email": email}).count() == 0 :
            comments = None
            cat = "simple user"
                # Add user
            users.insert({'name' : username, 'email' : email, 'password' : password, 'comments': comments, 'category': cat})
            return redirect(url_for('login_users'))
        else:
            return 'This email allready exist from another user!Try something else'
             
    return render_template('register.html')



@app.route('/movflix/<usr>', methods=['GET','POST'])
def mov_flix(usr):  

    if request.method == "POST":
        ans = request.form['ans']

        if ans == "title" :
            return redirect(url_for('search_title' , usr = usr))
        elif ans == "year" :
            return redirect(url_for('search_year' , usr = usr))
        elif ans == "actor" :
            return redirect(url_for('search_actor' , usr = usr))
        
    return render_template('movflix.html' , usr = usr  )
  

@app.route('/addcomment/<usr>/<id>', methods=['GET','POST'])
def add_comment(usr,id):
   
    if request.method == "POST":
        com = request.form['com']
        
        printcom =  usr ,com #ayto poy emfanizei stis tainies
        commentsuser = []
        
        comments = []
        movie = movies.find_one({"_id": ObjectId(id)})
        
        usercom = movie['_id'] , com #krataei to id tis tainias kai to comment poy ekane
        
        user = users.find_one({"email": usr})
         
        #user
        if user['comments'] is None : #an den exei allo comments
            commentsuser.append(usercom) 
        else :
            for item in user['comments'] :
                commentsuser.append(item) #an exei ki alla ta bazei sth lista 
                
            commentsuser.append(usercom)  #meta bazei kai to kainourgio
        #movie
        if movie['comments'] is None : #an adeia apo comments to bazei kateuthian
            comments.append(printcom) 
        else :
            for item in movie['comments'] :
                comments.append(item) #an exei ki alla ta bazei sth lista 
                
            comments.append(printcom)  #meta bazei kai toy xrhsth
        
        users.update_one({'email': usr},{'$set':{'comments': commentsuser }})
        movies.update_one({'_id': ObjectId(id)},{'$set':{'comments': comments }})
    
        return 'Comment Added'
    return render_template('addcomment.html')


@app.route('/addrating/<usr>/<id>/<int:rate>', methods=['GET'])
def add_rating(usr,id,rate):
    if request.method == "GET":
        i = 0 #metraei ta append gia to mod
        y=0 #blepei an exei xana psifisei ,etsi de bazei to printrate
        finalrate = 0
        rating = []
        printrate = usr , rate
        movie = movies.find_one({"_id": ObjectId(id)})
        
        if movie['rating'] is None :
            finalrate = rate # o protos pou psifizei
            
            rating.append(printrate)
            i = 1
             
        else :
            
            for item in movie['rating'] :
                if item[0] == usr : #an drei ton user ,dld an exei xana psifisei
                    newrate = usr , rate #alazei to idi yparxon rate toy xrhsth
                    rating.append(newrate)
                    y=1 #exei psifisei
                    i = i + 1 
                else : 
                    if item[0] != "finalrate" :#de bazoume to finalrate
                        rating.append(item)
                        i = i + 1

            if y == 0 : #dld den exei psifisei        
                rating.append(printrate) # balto sth lista rating
                i = i + 1
             
            for item in rating :
                finalrate = finalrate + item[-1]
                   

        finalrate = finalrate / i 
        f = "finalrate" ,finalrate
        rating.append(f) #teleutaio to finalrate
            
        movies.update_one({'_id': ObjectId(id)},{'$set':{'rating': rating }})
    return 'Rating added'

@app.route('/movflix/searchtitle/<usr>', methods=['POST','GET'])
def search_title(usr):
    
    if request.method == "POST":
        
        title = request.form['title']
        

        if movies.find({"title": title}).count() != 0 :
            movie = movies.find({"title": title})

            user = users.find({"email": usr}) #briskei ton user
            for item in user:
                cat = item['category'] #krataei to categorh
                
            return render_template('searchres.html', movie = movie , usr = usr , cat = cat)
    
    return render_template('searchtitle.html')


@app.route('/movflix/searchyear/<usr>', methods=['POST','GET'])
def search_year(usr):
    if request.method == "POST":
    
        year = request.form['year']
        
        if movies.find({"year": year}).count() != 0 :
            movie = movies.find({"year": year})
            
            user = users.find({"email": usr}) #briskei ton user
            for item in user:
                cat = item['category'] #krataei to categorh
            
            return render_template('searchres.html', movie = movie, usr = usr, cat = cat)
          
    return render_template('searchyear.html')

@app.route('/movflix/searchactor/<usr>', methods=['POST','GET'])
def search_actor(usr):
    if request.method == "POST":
    
        actor = request.form['actor']
        mov = movies.find({})
        movie = []
        for item in mov :
            x = 0   # 0 gia kathe tainia , an ginei 1 de tha ginei delete 
            for item2 in item['actors'] : #exei 1 item alla einai se morfh [['xx','xxx']]
                
                for item3 in item2 :  #pairnei to ['xx','xxx']
                    if item3 == actor :
                        movie.append(item)
                        

        user = users.find({"email": usr}) #briskei ton user
        for item2 in user:
            cat = item2['category'] #krataei to categorh
            
        return render_template('searchres.html', movie = movie, usr = usr ,cat =cat)
    
    return render_template('searchactor.html')


@app.route('/movflix/seecomrat/<usr>', methods=['POST','GET'])
def see_com_rat(usr):
    if request.method == "POST":
        see = request.form['see']
        if see == "mycomments":
            comandmov = None #sxolio me tainia poy tha emfanisei to html
            commov = []
     
            movie = movies.find({})

            for item in movie :
                a = 0 # an ginei 1 tote ton brhke kai ara exei comment (gia kathe tainia)
                if item['comments'] is not None :
                    
                    for item2 in item['comments']: #na dei an exei kanei kapou comment
                        if item2[0] == usr :
                            a=1 
                
                    if a == 1 : #ton exei brei ,dld exei comments
                
                        for item2 in item['comments']:
                            if item2[0] == usr :
                                comandmov = item2[-1] ,item['_id'], item ['year'] ,item['title']
                                commov.append(comandmov)
            if comandmov is not None :           
                return render_template('seecomres.html' ,commov = commov ,usr = usr ,delcom = None, delmov = None)
            else :#den exei brei se kamia tainia sxolio 
                return 'No comments'
        
        if see == "myratings":
            ratandmov = None
            ratmov = []
            movie = movies.find({})
            
            
            for item in movie :
                a = 0 # an ginei 1 tote ton brhke kai ara exei rating
                if item['rating'] is not None :
                
                    for item2 in item['rating']: #na dei an exei kanei rate
                        if item2[0] == usr :
                            a=1 
                
                    if a == 1 : #ton exei brei ,dld exei rating
                           
                        for item2 in item['rating']:
                            if item2[0] == usr :
                                ratandmov = item2[-1] ,item['_id'], item ['year'], item['title']
                                ratmov.append(ratandmov)
            if ratandmov is not None :                        
                return render_template('seeratres.html' ,ratmov = ratmov ,usr = usr ,delrat = None, delmov = None)
            else :
                return 'No ratings'
    return render_template('seecomrat.html')
 
@app.route('/movflix/seecomrat/<usr>/<delcom>/<delmov>', methods=['POST','GET'])
def del_com(usr , delcom , delmov):
    comments = []
    movie = movies.find({})
    x=0
    i=0
    for item in movie : # na brei thn movie gia na thn kanei update
        if item['_id'] == ObjectId(delmov) :
            for item2 in item['comments'] :
                if item2[-1] == delcom and item2[0] == usr :
                    x=1
                else :
                    i = i +1 #posa sxolia metraei
                    comments.append(item2)
            if i == 0 : #kanena sxolio
                comments = None

            movies.update_one({'_id': ObjectId(item['_id'])},{'$set':{'comments': comments }})

    #diagafei kai to sxolio apo ta sxolia sto user
    user = users.find_one({"email": usr})
    commentsuser = []
    q = 0 #metraei ta comments toy 
    for item in user['comments'] : 
        if item[0] != ObjectId(delmov) :  #an to proto poy exoyme ta id apo ta comments den einai ths tainia poy diagrafete to sxolio                 
            commentsuser.append(item) #bazei sth lista to comment
            q = q +1
    
    if q == 0 :  #an dld den exei balei sth lista allo comments         
        commentsuser = None
    users.update_one({'email': usr},{'$set':{'comments': commentsuser }})
    return 'Delete Successful'

@app.route('/movflix/seecomrat/<usr>/<int:delrat>/<delmov>', methods=['POST','GET'])
def del_rat(usr , delrat , delmov):
    rating = []
    x=0
    movie = movies.find({})
    for item in movie :
        if item['_id'] == ObjectId(delmov) :
            finalrate = 0
            i=0 # metraei ta rating gia to mod
            for item2 in item['rating']:
                
                if item2[-1] == delrat and item2[0] == usr :
                    x=1
                else :
                    rating.append(item2)
                   
            for item3 in rating :
                if item3[0] != "finalrate" :
                    
                    i = i + 1
                    finalrate = finalrate + item3[-1]
            if i != 0 :        
                finalrate = finalrate / i 
                f = "finalrate" ,finalrate
                rating.append(f)
            else : #an den exei sxolia 
                rating = None
              
            movies.update_one({'_id': ObjectId(item['_id'])},{'$set':{'rating': rating }})    
                               
    
    return 'Delete Successful'

@app.route('/movflix/delacc/<usr>', methods=['POST','GET'])
def del_acc(usr):
    
    if request.method == "POST":
        ans = request.form['ans']
        if ans == "no" :
            return redirect(url_for('mov_flix' , usr = usr)) 
        elif ans == "yes" :
            user = users.find({})
            for item in user :
                if item['email'] == usr : 
                    users.delete_one({'email': usr})

            #diagrafei kai ta comments toy 

            
            movie = movies.find({})
            
            for item in movie : # na brei thn movie gia na thn kanei update
                comments = []
                
                i=0
                if item['comments'] != None :
                    for item2 in item['comments'] :
                    
                        if item2[0] != usr :
                            i = i +1 #posa sxolia metraei
                            comments.append(item2)
                    if i == 0 : #kanena sxolio
                        comments = None

                    movies.update_one({'_id': ObjectId(item['_id'])},{'$set':{'comments': comments }})

            return redirect(url_for('regist_users'))        
    return render_template('delacc.html')    



# admin

@app.route('/movflixadmin/<usr>', methods=['GET','POST'])
def mov_flix_admin(usr): 
    
    return render_template('movflixadmin.html' , usr = usr  )


@app.route('/movflixadmin/addmovie', methods=['GET','POST'])
def add_movie():
    if request.method == "POST":
    
        title = request.form['title']
        year = request.form['year']
        if year == "" :
            year = None #an de balei kati na to kanei None 
        act = request.form['actors']
        actors = []
        actors.append(act.split(','))
        description = request.form['desc']
        rating = None
        comments = None
        movies.insert({'title' : title, 'year' : year, 'actors': actors, 'description': description, 'rating': rating, 'comments': comments})
        return 'The movie adding succesfully'
           
    return render_template('addmovie.html')

@app.route('/movflixadmin/delmovie', methods=['GET','POST'])
def del_movie():
    if request.method == "POST":
        title = request.form['title']
        
        if movies.find({"title": title}).count() != 0 :
            movie = movies.find({'title': title})
            minyear = [] #lista na krataei ta year
            for item in movie :
                if item['year'] != None : #giati mporei na mhn exei balei year den pernontai ipopsin
                    minyear.append(int(item['year']))
                
            minyear.sort()
            delyear = minyear[0]
            #na brei thn tainia
            delmovie = movies.find({'title': title}) 
            for item2 in delmovie :
                if item2['year'] != None :
                    delmovyear = int(item2['year'])
                    if delmovyear == delyear and item2['title'] == title :
                        mid = item2['_id'] #to id gia thn diagrafh

            movies.delete_one({'_id': ObjectId(mid)})

            return 'Delete Succesful'

    return render_template('delmovie.html')

@app.route('/movflixadmin/update/<usr>/<id>', methods=['GET','POST'])
def update(usr, id):

    movie = movies.find_one({"_id" : ObjectId(id)})
    for item in movie['actors']:
        movactors = item

    if request.method == "POST":
        title = request.form['title']
        year = request.form['year']
        act = request.form['actors']
        actors = []
        description = request.form['desc']
        
        #elenxoi gia osa ebale na ginoun update else bazei ta yparxwn
        if year != "" :
            movies.update_one({'_id': ObjectId(id)},{'$set':{'year': year }}) 
                     
        if title != "" :
            movies.update_one({'_id': ObjectId(id)},{'$set':{'title': title }})
        if act != "" :
            actors.append(act.split(','))
            for item in actors : #pernei thn agili sto actor
                aclist = item

            if aclist[-1] == "1" :
                actupd = []
                actupdfinal = []
                del aclist[-1] # diagrafei to "1"
                actupd = aclist
                for item in movie['actors'] : #pernei thn agili mesa sto actors
                    for item2 in item :
                        actupd.append(item2)  #telikh morfh ['xx','xxx']
                
                actupdfinal.append(actupd) ##telikh morfh [['xx','xxx']] thn opoia theloyme
                 
                movies.update_one({'_id': ObjectId(id)},{'$set':{'actors': actupdfinal }})

            elif aclist[-1] == "2" : #diagrafei kai eisagei ta  nea
                actupd = []
                del aclist[-1]
                actupd.append(aclist)
                movies.update_one({'_id': ObjectId(id)},{'$set':{'actors': actupd }})  
            
            elif aclist[-1] == "3" : # diagrafei osa toy pei
                actupd = []
                actupdfinal = []
                for item in movie['actors'] : #gia kathe ena apo ta palia actor
                    
                    for item2 in item :
                        if item2 not in aclist: #an den einai mesa sthn lista poy egrapse 
                            actupd.append(item2)  #ta bazei sthn nea lista 
                
                actupdfinal.append(actupd) #gia na parei thn morfh poy theloyme [['xx']]   
                
                movies.update_one({'_id': ObjectId(id)},{'$set':{'actors': actupdfinal }})
               

        if year != "" :
            movies.update_one({'_id': ObjectId(id)},{'$set':{'year': year }})
    
    return render_template('update.html', movactors = movactors)        


@app.route('/movflixadmin/modusers/<usr>', methods=['GET','POST'])
def mod_users(usr):

    moduser = []
    user = users.find({})
    for item in user:
        if item['category'] != "admin" : #an den einai diaxiristis
            moduser.append(item)
            
    return render_template('modusers.html', moduser = moduser)


@app.route('/movflixadmin/modusers/changecat/<id>', methods=['GET','POST'])
def change_cat(id):

    users.update_one({'_id': ObjectId(id)},{'$set':{'category': "admin" }})
    return 'Category changed successfully'

@app.route('/movflixadmin/modusers/deletecom/<usr>', methods=['GET','POST'])
def delete_com(usr):

    comandmov = None
    commov = []
     
    movie = movies.find({})

    for item in movie :
        a = 0 # an ginei 1 tote ton brhke kai ara exei comment (gia kathe tainia)
        if item['comments'] is not None :
                    
            for item2 in item['comments']: #na dei an exei kanei kapou comment
                if item2[0] == usr :
                    a=1 
                
            if a == 1 : #den ton exei brei ,dld den exei comments
                
                for item2 in item['comments']:
                    if item2[0] == usr :
                        comandmov = item2[-1] ,item['_id'], item ['year'] ,item['title']
                        commov.append(comandmov)
    if comandmov is not None : #den exei brei se kamia tainia sxolio           
        return render_template('seecomres.html' ,commov = commov ,usr = usr ,delcom = None, delmov = None)
    else :
        return 'No comments'


@app.route('/movflixadmin/modusers/deleteuser/<id>', methods=['GET','POST'])
def delete_user(id):

    
    user = users.find_one({"_id": ObjectId(id)})
    usr = user['email']
    movie = movies.find({})
            
    for item in movie : # na brei thn movie gia na thn kanei update
        comments = []
                
        i=0
        if item['comments'] != None :
            for item2 in item['comments'] :
                    
                if item2[0] != usr :
                    i = i +1 #posa sxolia metraei
                    comments.append(item2)
            if i == 0 : #kanena sxolio
                comments = None

            movies.update_one({'_id': ObjectId(item['_id'])},{'$set':{'comments': comments }})
    
    users.delete_one({'_id': ObjectId(id)})

    return 'The user deleted successfully'       

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
