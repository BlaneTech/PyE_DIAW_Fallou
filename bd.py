import mysql.connector
from mysql.connector import Error 
import traiteData
dico = traiteData.dataForSql
list_date = traiteData.dateSqlFormat
config = {
        'host': '127.0.0.1',
        'database':'PYTHON01',
        'user':'root',
        'password':'6wdGPPpOe!'
    }
try:    
    dbConnect = mysql.connector.connect(**config)
    # if dbConnect.is_connected():
except Error:
    print("Erreur lors de la connection à MYSQL")
curseur = dbConnect.cursor()
list_id_devoir= list()
list_nomClassse = list()
etudiant = "INSERT INTO ETUDIANT (numero_ETUDIANT, nom_ETUDIANT, prenom_ETUDIANT, dateNais_ETUDIANT,nom_CLASSE) VALUES (%s,%s,%s,%s,%s)"
devoir = "INSERT INTO DEVOIR(numero_DEVOIR, note_DEVOIR,nom_MATIERE) VALUES (%s,%s,%s)"
classe = "INSERT INTO CLASSE (nom_CLASSE) VALUES (%s)"
matiere = "INSERT INTO MATIERE (nom_MATIERE) VALUES (%s)"
faire = "INSERT INTO FAIRE (numero_ETUDIANT, id_DEVOIR) VALUES (%s,%s)"
suivre = "INSERT INTO SUIVRE (numero_ETUDIANT, nom_MATIERE,noteExamen_CONCERNER) VALUES (%s,%s,%s)"

# insertion dans matiere
for key in dico[1]['note'].keys():
    if key in ["francais", "Francais"]:
        key = "FRANÇAIS"
    elif key == "anglais":
        key = "ANGLAIS"
    elif key == "Math":
        key = "MATH"
    curseur.execute(matiere,(key,))

#insertion dans la table  classe
for i in range(1,len(dico)):
    if dico[i]['classe'] not in list_nomClassse:
            list_nomClassse.append(dico[i]['classe'])
for name in range(len(list_nomClassse)):
    curseur.execute(classe,(list_nomClassse[name],))
# insertion dans etudiant
for i in range(1,len(dico)):
    curseur.execute(etudiant, (dico[i]['numero'],dico[i]['nom'],dico[i]['prenom'],list_date[i],dico[i]['classe']))
    
    # insertion  dans la table devoir
    for key in dico[i]['note'].keys():
        for j in range(len(dico[i]['note'][key]['devoir'])):
            curseur.execute(devoir,(j+1,dico[i]['note'][key]['devoir'][j],key))

#insertion dans la table faire
curseur.execute("SELECT id_DEVOIR FROM DEVOIR")
for idDevoir in curseur.fetchall():
    list_id_devoir.append(idDevoir)
num_id = 0
for i in range(1,len(dico)):
    for key1 in dico[i]['note'].keys():
        for k in range(len(dico[i]['note'][key1]['devoir'])):
            curseur.execute(faire,(dico[i]['numero'],list_id_devoir[num_id][0]))
            num_id+=1
#insertion dans suivre
for i in range(1,len(dico)):
    for key2 in dico[i]['note'].keys():
        curseur.execute(suivre,(dico[i]['numero'],key2,dico[i]['note'][key2]['examen']))
        # num_idm += len(dico[i]['note'][key2]['devoir'])

dbConnect.commit()
dbConnect.close()
# print(traiteData.dataForSql)