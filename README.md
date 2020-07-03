# MovieFlix2020_E16128_SITARAS_ALEXANDROS

## Απαλλακτική Εργασία Πληροφοριακών Συστημάτων Σιταράς Αλέξανδρος 

## Υλοποίηση  του Πληροφοριακού Συστήματος MovieFlix 

###### Όλα τα παρακάτω αφορούν λειτουργικό σύστημα Ubuntu

**Ανοίγουμε το _terminal_**

**Εγκατάσταση Docker** 

  1.sudo apt-get update

  2.sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

  3.curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 

  4.sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

  5.sudo apt-get update

  6.sudo apt install docker-ce

**Εγκατάσταση docker-compose**

  1.sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

  2.sudo chmod +x /usr/local/bin/docker-compose

  3.docker-compose --version 


**Αφού έχουμε κατεβάσει τα αρχεία του repository στον υπολογιστή μας (clone)**

**-Για να τρέξει το σύστημα κάνουμε τα παρακάτω βήματα στο _terminal_**

   1.Με την εντολή cd να μπούμε μέσα στον φάκελο MovieFlix2020_E16128_SITARAS_ALEXANDROS-master

   2.Τρέχουμε την εντολή docker-compose build

   3.Τρέχουμε την εντολή docker-compose up

**Το σύστημα τώρα είναι έτοιμο και τρέχει _localhost:5003_**

**##ADMIN##**

**Έχει δημιουργηθεί ένας admin με στοιχεία email:admin@admin.com , name:admin , password:admin και αυτό γιατί εγγραφή στο συστημα κάνουν μόνο απλή χρήστες**

**-Αρχικό endpoint είναι το : localhost:5003/loginusers**

    1.Εισάγουμε email και password
  
    2.Πατάμε Login
  
  **Αν τα στοιχεία είναι λάθος εμφανίζεται "Invalid values" και πατάμε πίσω να ξαναβάλουμε.Ενώ αν είναι σωστά μας μεταφέρει στο endpoint: localhost:5003/movflixadmin/<user>**
  
**-Endpoint : localhost:5003/movflixadmin/<user>**
  
  *-Υπάρχουν οι εξής επιλογές ως admin στο κεντρικό μενού του*
    
    1.User mode : που τον μεταφέρει στο endpoind: localhost:5003/movflix/<user>  όπου εκεί είναι το menu του απλού χρήστη ,που θα εξειγήθεί στον SIMPLE USER παρακάτω τί μπορεί να κάνεί. Αυτό υπάρχει γιατί ένας admin μπορεί να κάνει όλες τις λειτουργείς ενός απλου user.
    
    2.Add Movie : που τον μεταφέρει στο endpoint: localhost:5003/movflixadmin/addmovie 
    
    3.Delete Movie : που τον μεταφέρει στο endpoint: localhost:5003/movflixadmin/delmovie
    
    4.See and modify users : που τον μεταφέρει στο endpoint: localhost:5003/movflixadmin/modusers/<user>

**-Endpoint : localhost:5003/movflixadmin/addmovie**

    1.Εισάγει απαραίτητα τίτλο και τουλάχιστον έναν πρωταγονιστή(με κόμμα και χωρίς κενά) ,και αν θέλει έτος και πλοκή ταινίας
  
    2.Πατάει Add
  
    3.Εμφανίζετε 'The movie adding successfully'

**-Endpoint : localhost:5003/movflixadmin/delmovie**

    1.Εισάγει τίτλο ταινίας
  
    2.Πατάει delete και αν υπάρχει διαγράφετε , αν όμως υπάρχουν και άλλες με ίδιο τίτλο τότε το σύστημα διαγράφει αυτή με το μικρότερο έτος
  
    3.Εμφανίζετε 'Delete Succesful'
  
**-Endpoint : localhost:5003/movflixadmin/modusers/<user>**

  *-Eδώ υπάρχει η δυνατότητα να διαχειριστεί τους simple users*
    
    1.link button : "Change category to admin" το οποίο τον μετατρέπει τον user σε admin
    
    2.link button : "Delete this user" το οποιο διαγράφει τον user μαζί και κάθε σχόλιό του αν είχε
    
    3.link button : "See and delete comments" το οποίο τον μεταφέρει στο endpoind : localhost:5003/movflixadmin/modusers/deletecom/<user> (το <user> είνια του simple user που επιλέχθηκε
    
**-Endpoint : localhost:5003/movflixadmin/modusers/deletecom/<user>**    
    
   *Ο Admin βλέπει όλα τα σχόλια αυτού του χρήστη συνοδευόμενο από κάθε ταινία (τίτλο και έτος)* 
    
    1.Έχει την δυνατότητα να διαγράψει όποιο σχόλιό του θέλει με το link button : "Delete comment"
    
    2.αν το κάνει εμφανίζεται "Delete Successful"

**-Endpoint : localhost:5003/movflixadmin/update/<user>/<id>**
  
    1.Εισάγει ότι θέλει να κάνει update , (τίτλο ,year,actors)
    
    2.Στους actors έχει τρεις επιλογές
      
      1.Να προσθέσει κάποιον/ους ,γραφοντας τον/τους με κόμα και στο τέλος τον αριθμό "1" (με κόμα παλι)
      
      2.Να εισάγει κάποιον/ους και να διαγραφουν οι προηγούμενοι , γραφοντας τον/τους με κόμα και στο τέλος τον αριθμό "2" (με κόμα παλι)
      
      3.Να διαγράψει κάποιον/ους ήδη υπάρχοντες ,γραφοντας τον/τους με κόμα και στο τέλος τον αριθμό "3" (με κόμα παλι)
    
    3.Αφου ολοκληρώσει πατάει το button "Update" 
    


**##SIMPLE USER**

**-Αρχικά πρέπει να κάνει εγγραφή έτσι πηγένει στο endpoint : localhost:5003/registusers**

**-Endpoint : localhost:5003/registusers** 
 
    1.Αν έχει ήδη λογαριασμο υπάρχει link button : "Log in" το οποίο τον μεταφέρει στο endpoint: ndpoint : localhost:5003/loginusers για να συνδεθεί
 
    2.Αλλιώς εισάγει email , name ,password
 
    3.Πατάει Register και αν δέν υπάρχει άλλος χρήστης με το ίδιο email πραγματοποιείτε εγγραφή 
 
    4.Με επιτυχή εγγραφη τον μεταφέρει στο endpoint :ndpoint : localhost:5003/loginusers (κανει σύνδεση όπως περιγράψαμε στον ADMIN , αλλιώς εμφανίζεται 'This email allready exist from another user!Try something else'
 
**-Endpoint : localhost:5003/loginusers**
 
    1.Αν σε περίπτωση που δεν έχει λογαριασμό θέλει να κάνει regist υπάρχει link button: "Sing up here" που τον μεταφέρει στο endpoint : localhost:5003/registuser
 
    2.Αν κάνει σωστό login ,τον μεταφέρει στο menu ενός simple user στο endpoint : localhost:5003/movflix/<user> 

**-Endpoint : localhost:5003/movflix/<user>**

    1.Υπάρχει η δυνατότητα να διαγράψει τον λογαριασμό του με ένα link button: "Delete my account" οπου τον μεταφέρει σε ένα endpoint : localhost:5003/movflix/delacc/<user>
  
    2.Μπορεί να κάνει αναζήτηση ταινιών αρκεί στο "search movie by:" να πληκτρολογήσει με τί θέλει( title,year ή actor) αν γράψει κάτι απο τις τρεις επιλογές και πατήσει το Search τον μεταφέρει στa endpoint: localhost:5003/movflix/searchtitle/<user> (για title) , localhost:5003/movflix/searchyear/<user> (για year) και localhost:5003/movflix/searchactor/<user> (για actor)
  
      3.Με το πάτημα ενός link button: See στο σημείο που λέει "My comments and ratings" , τον μεταφέρει στο endpoint: localhost:5003/movflix/seecomrat/<user>  , για να δει τα comments ή τα ratings του
  
  
**-Endpoint: localhost:5003/movflix/searchtitle/<user>** 
  
    1.Βάζει ένα τίτλο
  
    2.Πατάει Search
  
    3.Αν υπάρχει εμφανίζονται όλες οι ταινίες με αυτόν τον τίτλο 
  
**-Endpoint: localhost:5003/movflix/searchyear/<user>**
  
    1.Βάζει ένα έτος
  
    2.Πατάει Search
  
    3.Αν υπάρχει εμφανίζονται όλες οι ταινίες με αυτό το έτος
  
**-Endpoint: localhost:5003/movflix/searchactor/<user>** 
  
    1.Βάζει ένα actor
  
    2.Πατάει Search
  
    3.Αν υπάρχει εμφανίζονται όλες οι ταινίες με αυτόν τον actor
  

**######Οι ταινίες που εμφανίζονται στα 3 παραπάνω endpoints ειναι σε html , για κάθε μία απ αυτες υπάρχουν οι παρακάτω δυνατότητες στους users**
  
    1.Να δώσει το rating του πατόντας ένα απο τα link button : "1","2","3","4","5" ,σε περίπτωση που έχει ξανα πατήσει αναβαθμίζεται με την νέα του βαθμολογία
  
    2.Να κάνει comments πατόντας το link button: "Add a comment" που τον μεταφέρει στο endpoint: localhost:5003/addcomment/<user>/<id>  (το id είναι της ταινίας που θα μπεί το σχόλιο)** 

**######Οι ADMIN εδώ έχουν μια παραπάνω λειτουργεία που εμφανίζεται μόνο σε αυτούς στο τέλος κάθε ταινίας**
     
     -Μπορεί να κάνει update κάποια απο τις movies που έχουν αναζητηθεί πατόντας το link button: "Update Movie" το οποίο τον μεταφέρει στο endpoint: localhost:5003/movflixadmin/update/<user>/<id> (το id της ταινίας που θα γίνει update)
  
  
**-Endpoint: localhost:5003/addcomment/<user>/<id>**
 
    1.Εισάγει το σχόλιο που θέλει και πατάει το button "Submit"
  
    2.Εμφανίζεται "Comment Added"


**-Endpoint : localhost:5003/movflix/seecomrat/<user>**

    
    1.Στο "What do you want to see" μπορεί να εισάγει το "mycomments" (για τα σχόλια του) ή "myratings" (για τις βαθμολογίες του ) 
    
    2.Αν έχει εισάγει "mycomments" τότε του εμφανίζονται όλα τα comments του με τον τίτλο και το έτος κάθε ταινίας , αλλιώς εμφανίζεται "No comments"
    
    2.Αν έχει εισάγει "myratings" τότε αν έχει ratings του εμφανίζονται όλα τα ratings του με τον τίτλο και το έτος κάθε ταινίας , αλλιώς εμφανίζεται "No ratings"

**######Τα ratings και τα comments που εμφανίζονται παραπάνω ειναι σε html , για κάθε μία απ αυτες υπάρχουν οι παρακάτω δυνατότητες στους users**

             1.Για τα comments , με το link button 'Delete comment' μπορεί να διαγράψει όποιο δικό του σχόλιο θέλει από όποια ταινία θέλει .Αυτόματα ενημερώνεται και η ταινία.
             2.Για τα ratings , με το link button 'Delete rating' μπορεί να διαγράψει όποια δική του βαθμολογία θέλει από όποια ταινία έχει κάνει .Αυτόματα ενημερώνεται και η ταινία.


**-Endpoint : localhost:5003/movflix/delacc/<user>**
 
    1.Εισάγει yes ή no στο "Answer"
  
    2.Πατάει submit .
  
    3.Αν εισάγει 'no' μεταφέρεται πίσω στο menu με endpoint : localhost:5003/movflix/<user>
  
    4.Αν εισάγει 'yes' τότε ο λογαριασμός του διαγράφεται, μαζί και όλα τα σχόλια του απ της ταινίες και μεταφέρεται στο endpoint: localhost:5003/registusers

