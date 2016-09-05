# tax_level.py
#Theo Allnutt 2016
#This script opens a usearch otu table output and parses the taxonomy column (last column)
#to extract each taxonomy level separately. Levels are denoted by d:,p:,c:,o:,f:,g: before the name.
#input file is e.g. otutab.txt from:
#usearch -usearch_global trimmed.fa -db otus_tax.fa -strand both -id 0.97 -otutabout otutab.txt -biomout otutab.biom 
#usage:
#python tax_level.py otu_table.txt

#output tables are made in the current directory with -p, -c, -o, -f, -g suffix
