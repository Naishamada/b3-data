CREATE DATABASE IF NOT EXISTS rna;
USE rna;
CREATE TABLE IF NOT EXISTS rna.data ( id MEDIUMINT NOT NULL AUTO_INCREMENT, rna_id varchar(255), 
rna_id_ex varchar(255), siret varchar(255),
 gestion varchar(255), date_creat varchar(255), date_publi varchar(255), 
 nature varchar(255),  groupement varchar(255), titre varchar(255), 
 objet varchar(255), objet_social1 varchar(255),  objet_social2 varchar(255), 
 adr1 varchar(255), adr2 varchar(255), adr3 varchar(255),  adrs_codepostal int(255),
  libcom varchar(255), adrs_codeinsee varchar(255),   dir_civilite varchar(255),
 siteweb varchar(255), observation varchar(255), position varchar(255), 
 rup_mi varchar(255), maj_time varchar(255),PRIMARY KEY (id));