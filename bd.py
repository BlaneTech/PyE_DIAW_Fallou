import mysql.connector
from mysql.connector import Error 
import traiteData
dico = traiteData.dataForSql
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
list_id_matiere = list()
etudiant = "INSERT INTO ETUDIANT (numero_ETUDIANT, nom_ETUDIANT, prenom_ETUDIANT, dateNais_ETUDIANT) VALUES (%s,%s,%s,%s)"
devoir = "INSERT INTO DEVOIR(numero_DEVOIR, note_DEVOIR) VALUES (%s,%s)"
classe = "INSERT INTO CLASSE (numero_ETUDIANT, nom_CLASSE) VALUES (%s,%s)"
matiere = "INSERT INTO MATIERE (nom_MATIERE,id_DEVOIR) VALUES (%s,%s)"
faire = "INSERT INTO FAIRE (numero_ETUDIANT, id_DEVOIR) VALUES (%s,%s)"
suivre = "INSERT INTO SUIVRE (numero_ETUDIANT, id_MATIERE,noteExamen_CONCERNER) VALUES (%s,%s,%s)"
for i in range(1,len(dico)):
    curseur.execute(etudiant, (dico[i]['numero'],dico[i]['nom'],dico[i]['prenom'],dico[i]['date']))

    curseur.execute(classe,(dico[i]['numero'],dico[i]['classe']))

    for key in dico[i]['note'].keys():
        for j in range(len(dico[i]['note'][key]['devoir'])):
            curseur.execute(devoir,(j+1,dico[i]['note'][key]['devoir'][j],))

curseur.execute("SELECT id_DEVOIR FROM DEVOIR")
for idDevoir in curseur.fetchall():
    list_id_devoir.append(idDevoir)
num_id = 0
for i in range(1,len(dico)):
    for key1 in dico[i]['note'].keys():
        for k in range(len(dico[i]['note'][key1]['devoir'])):
            curseur.execute(matiere,(key1,list_id_devoir[num_id][0]))
            curseur.execute(faire,(dico[i]['numero'],list_id_devoir[num_id][0]))
            num_id+=1
    
curseur.execute("SELECT id_MATIERE FROM MATIERE")
for idMatiere in curseur.fetchall():
    list_id_matiere.append(idMatiere)
    list_id_matiere.sort()
num_idm = 0

for i in range(1,len(dico)):
    for key2 in dico[i]['note'].keys():
        curseur.execute(suivre,(dico[i]['numero'],list_id_matiere[num_idm][0],dico[i]['note'][key2]['examen']))
        num_idm += len(dico[i]['note'][key2]['devoir'])

dbConnect.commit()
dbConnect.close()
# print(traiteData.dataForSql)