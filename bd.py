from http.client import ImproperConnectionState
import mysql.connector
from mysql.connector import Error 
from statistics import mean
import traiteData

dico = traiteData.dataForSql
list_date = traiteData.dateSqlFormat

# -----------connexion à la base de donnée----------------
config = {
        'host': '127.0.0.1',
        'database':'PYTHON01',
        'user':'root',
        'password':'PASSWORD'
    }
try:    
    dbConnect = mysql.connector.connect(**config)
    # if dbConnect.is_connected():
except Error:
    print("Erreur lors de la connection à MYSQL")
curseur = dbConnect.cursor()
list_id_devoir= list()
list_nomClassse = list()
listMatiere=[]

etudiant = "INSERT INTO ETUDIANT (numero_ETUDIANT, nom_ETUDIANT, prenom_ETUDIANT, dateNais_ETUDIANT,id_CLASSE) VALUES (%s,%s,%s,%s,%s)"
note = "INSERT INTO NOTE(valeur, type,id_ETUDIANT,id_MATIERE) VALUES (%s,%s,%s,%s)"
classe = "INSERT INTO CLASSE (nom_CLASSE) VALUES (%s)"
matiere = "INSERT INTO MATIERE (nom_MATIERE) VALUES (%s)"
moyenne = "INSERT INTO MOYENNE (valeur_MOYENNE, id_ETUDIANT) VALUES (%s,%s)"

# ----------------------insertion dans matiere----------------------
for key in dico[1]['note'].keys():
    if key not in listMatiere:
        listMatiere.append(key)
    curseur.execute(matiere,(key,))
# print(listMatiere)

#--------------------insertion dans la table  classe-------------------------
for i in range(1,len(dico)):
    if dico[i]['classe'] not in list_nomClassse:
            list_nomClassse.append(dico[i]['classe'])
for name in range(len(list_nomClassse)):
    curseur.execute(classe,(list_nomClassse[name],))

 # insertion dans etudiant
for i in range(1,len(dico)):
    if dico[i]['classe'] in list_nomClassse:
        idClasse = list_nomClassse.index(dico[i]['classe'])+1
    curseur.execute(etudiant, (dico[i]['numero'],dico[i]['nom'],dico[i]['prenom'],list_date[i],idClasse))
    
# -------------------insertion  dans la table devoir----------------------
ww=0
sumMoy=0
typeNote = ["DEVOIR","EXAMEN"]
for i in range(1,len(dico)):
    for key in dico[i]['note'].keys():
        if key in ["Francais","francais","Français","français"]:
            idMatiere = listMatiere.index("Francais")
        elif  key in ["Anglais","ANGLAIS"]:
            idMatiere = listMatiere.index("Anglais")
        elif key in ["Math","math"]:
            idMatiere = listMatiere.index("Math")
        else:
            idMatiere = listMatiere.index(key)
        for j in range(len(dico[i]['note'][key]['devoir'])):
            curseur.execute(note,(dico[i]['note'][key]['devoir'][j],typeNote[0],i,idMatiere+1))
            ww+=1
            if ww == len(dico[i]['note'][key]['devoir']):
                curseur.execute(note,(dico[i]['note'][key]['examen'],typeNote[1],i,idMatiere+1))
                # pass
        ww=0
#------------------- calcul et insertion dans moyenne------------------------------
        moyPartiel = (mean(dico[i]['note'][key]['devoir']) + 2*dico[i]['note'][key]['examen'])/3
        sumMoy+=moyPartiel
    moyGen = (sumMoy/6).__round__(2)
    sumMoy=0
    curseur.execute(moyenne,(moyGen,i))

dbConnect.commit()
dbConnect.close()
# print(traiteData.dataForSql)