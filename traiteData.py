import csv
import itertools
from my_function import del_empty
from my_function import name_validation
from my_function import level_validation
from my_function import num_validation

# print("""\t\t MENU PROJET:
# 1. Afficher les données valides
# 2. Afficher les données invalides
# 3. Afficher les données aprés calcul des moyennes""")
# choix = int(input("Veuillez choisir un chiffre parmi ceux ci-dessus: "))
choix=3
# print("\n")
if choix == 2:
    pass
    # print("\t\t\t Ci-dessous données invalides:\n")
    with open("projectData.csv", "r") as f:
        file = csv.reader(f)
        liste_note = list()
        invalidList = list()
        listeValide = list()
        for row in file:
            # del(row[0])
            num = str(row[1])
            lastName = str(row[2])
            firstName = str(row[3])
            dateNais = str(row[4]).strip()
            level = "".join(str(row[5]).strip().split())
            note = "".join(str(row[6]).strip("#").split())

            if (
                del_empty(num, lastName, firstName, dateNais, level, note)
                and num_validation(num)
                and name_validation(lastName, firstName)
                and level_validation(level)
            ):
                for j in range(len(dateNais)):
                    if dateNais[j] in ["/", ".", ":", " "] and "-" not in dateNais:
                        dateNais = dateNais.replace(dateNais[j], "-")
                        # note=note.replace(',','.')
                        liste_note.append([num, lastName, firstName, dateNais, level, note])
            else:
                # if invalid_num(num) and invalid_name(lastName,firstName) and invalid_level(level):
                invalidList.append([num, lastName, firstName, dateNais, level, note])
        # if liste[i]:
        for i in range(len(invalidList)):
        # if change(liste[i][5]):
             print(i, invalidList[i])
    f.close()
    # print(len(dateNais))
    with open("valide_data.csv", "w") as data:
        valid_data = csv.writer(data)
        valid_data.writerow(["numero", "nom", "prenom", "date", "classe", "note"])
        for elt in liste_note:
            valid_data.writerow([elt[0], elt[1], elt[2], elt[3], elt[4], elt[5]])
        data.close()
elif choix == 1:
    pass
    # print("\t\t\t Ci-dessous les données valides:\n")
    with open("valide_data.csv", "r") as d:
        valide = csv.reader(d)
        for line in valide:
            print(line)
elif choix == 3:
    dataForSql = list()
    liste_date = []
    # print("\t\t\t Ci_dessous les données aprés calcul des moyennes\n")
    with open("valide_data.csv", "r") as d:
        valide = csv.reader(d)
        for line in valide:
            if "," in line[5]:
                line[5] = line[5].replace(",", ".")
            no = line[5]
            noo = "".join(no.split("#"))
            split_noo = " ".join(noo.split("["))
            fal = " ".join(split_noo.split("]"))
            liste_note = fal.split(" ")
            del liste_note[-1]
            plain_list_iter = iter(liste_note)
            plain_list_dict_object = itertools.zip_longest(
                plain_list_iter, plain_list_iter, fillvalue=None
            )
            plain_list_dict = dict(plain_list_dict_object)
            for key in plain_list_dict.keys():
                plain_list_dict[key] = plain_list_dict[key].split(":")
                plain_list_dict[key][0] = plain_list_dict[key][0].split(";")
                plain_list_dict[key][0] = list(map(float, plain_list_dict[key][0]))
                plain_list_dict[key][1] = float(plain_list_dict[key][1])
                # print(plain_list_dict[key][0])
                noteg ={"devoir":plain_list_dict[key][0], "examen":plain_list_dict[key][1]}
                plain_list_dict[key] = noteg
                # moyD = sum(plain_list_dict[key][0]) / len(plain_list_dict[key][0])
                # moyM = ((moyD + 2 * plain_list_dict[key][1]) / 3).__round__(2)
                # plain_list_dict[key] = moyM
            # moyen = {"Moy_G": (sum(plain_list_dict.values()) / 6).__round__(2)}
            # plain_list_dict.update(moyen)
            line[5] = plain_list_dict
            line = {"numero":line[0],"nom":line[1],"prenom":line[2],"date":line[3],"classe":line[4],"note":line[5]}
            dataForSql.append(line)
            # print(line[5].keys())
   # print(dataForSql)
    ff=[]
    dateSqlFormat=[]
    for dat in range(len(dataForSql)):
       liste_date.append(dataForSql[dat]['date'])
    for k in range(len(liste_date)):
       ff.append(liste_date[k].split('-'))
       ff[k].reverse()
       dateSqlFormat.append("-".join(ff[k]))
    # print(dateSqlFormat)
        # print(line[5]['Math'][0])
        # for line in line[5].items():
        #     print(line)
else:
    print("Oups! entré invalide")
       # listeValide.append(line)
        #for i in listeValide:
#with open("data_prosscess.csv","w") as data_process:
 #   donnee = csv.writer(data_process)
  #  for i in listeValide:
   #     donnee.writerow(i[0])



