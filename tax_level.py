import sys


#Theo Allnutt 2016
#This script opens a usearch otu table output and parses the taxonomy column (last column)
#to extract each taxonomy level separately. Levels are denoted by d:,p:,c:,o:,f:,g: before the name.
#input file is e.g. otutab.txt from:
#usearch -usearch_global trimmed.fa -db otus_tax.fa -strand both -id 0.97 -otutabout otutab.txt -biomout otutab.biom 
#usage:
#python tax_level.py otu_table.txt

#output tables are made in the current directory with -p, -c, -o, -f, -g suffixes

def find1(a,b):
	for p in a:
		if b in p:
			return a.index(p)
			
		

f = open(sys.argv[1],'r')

name1 = sys.argv[1].split("/")[-1].split(".")[0]
print name1


#n.b. taxa = d:,p:,c:,o:,f:,g:


samples=[]

for i in f:
	if i[0]=="#":
		samples=i.split("\t")[1:]
		n=len(samples)-1
		
	else:
		break


levels=["p:","c:","o:","f:","g:"]

for level in levels:
	data={}
	
	f.seek(0)
	for i in f:
		
		if i[0]<>"#":
		
			k = i.split("\t")[1:-1]
			c=-1
			for x in k:
				c=c+1
				x=int(x.split(".")[0])
				k[c]=x
			
		
			tax = i.split("\t")[-1].split(",")
			tax[-1]=tax[-1].rstrip("\n")
		
			pos=find1(tax,level)
			
			
			
			if pos:
				name=tax[pos].split(":")[-1]
				
				if name not in data.keys():
					
					data[name]=k
					
				else:
					for x in range(0,len(k)):
						data[name][x]=data[name][x]+k[x]
					
			else:
				
			#add to unclassified
				if "unclassified" in data.keys():
					for x in range(0,len(k)):
						
						data["unclassified"][x]=data["unclassified"][x]+k[x]
						
				else:
					data["unclassified"]=k
	
			#print level, tax,pos,k
	print "unclassified", data["unclassified"]
	
	g=open(name1+"-"+level[0]+".txt",'w')
	
	g.write("\t"+"\t".join(str(x) for x in samples))
	for i in data.keys():

		g.write(i+"\t"+"\t".join(str(x) for x in data[i])+"\n")
			