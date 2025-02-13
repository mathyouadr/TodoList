import sqlite3
#connection to the database
con = sqlite3.connect('task.db')
cur = con.cursor()

#creation of the table if she wasn't created
cur.execute('CREATE TABLE IF NOT EXISTS Tache (id INTEGER PRIMARY KEY, what TEXT)')

#Default menu
while True: 
    choix = input("Si vous voulez ajouter une tache saissez 1 , pour voir vos tache saisissez 2, pour supprimer une tache 3 et pour quitter saisissez 4 : ")

    if choix == "1":
        #add a task 
        tasktoadd = input("Veuillez saisir la tache à ajouter : ")
        cur.execute("INSERT INTO Tache (what) VALUES (?)", (tasktoadd,))
        con.commit()
        print("Tache ajoutée avec succès")
    #print all tasks
    elif choix == "2":
        for row in cur.execute('SELECT * FROM tache'):
            print(row)
    elif choix == "3":
        tasktodelete = input("Veuillez saisir l'id de la tache à supprimer : ")
        cur.execute("DELETE FROM Tache WHERE id = ?", (tasktodelete,))
        con.commit()
        print("Tache supprimée avec succès")

    #shutdown the program
    elif choix == "4":
        print("Au revoir")
        break
    else:
        print("Veuillez saisir 1,2,3 ou 4")
