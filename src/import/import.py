import csv
import mysql.connector

link = mysql.connector.connect(
    host="localhost",
    database='rna',
    user="root",
    port="3306",
    password=""

)



# csv.reader(open("data/rna_import_20221101_dpt_01.csv", "r"))
cur=link.cursor()
with open('data/rna_import_20221101_dpt_01.csv', 'r', encoding='ISO-8859-1') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        print(row[0])
        cur.execute(
            "INSERT INTO data (rna_id, rna_id_ex ,siret,gestion,date_creat,date_publi,nature,groupement,titre,objet,objet_social1,objet_social2,adr1,adr2,adr3,adrs_codepostal,libcom,adrs_codeinsee,dir_civilite,siteweb,observation,position,rup_mi,maj_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (row[0],  row[1],  row[2],  row[3],  row[4],  row[5],  row[6],  row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23])
        )
        link.commit()

link.close()