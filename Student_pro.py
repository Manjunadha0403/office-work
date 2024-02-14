# Python program for student profiles
# writing to CSV 


import csv 
	
# field names for Header Section
fields = ['Name','Gender','Course','Dept','Id_No','University','Year'] 
	
# data rows of csv file 
rows = [ ['manju','M','Engg', 'Mech','420','KL_UNI','3'], 
		['Shakeena','F','Phrm','B.Phrm','852','PDV_UNI','4'],
		['Arjun', 'M','P.G','M.Tech','965','ANNA_UNI','2'],
		['Sanju', 'M','Degree','B.Com','753','AU_UNI','1'],
		['Sahasra','F','Medical','MBBS','123','KKH_UNI','2'], 
		['Preethi', 'F','Polytech','ECE','654','GI_UNI','3'],] 
	
# name of csv file 
filename = "student_pro.csv"
	
# writing to csv file 
with open(filename, 'w') as csvfile: 
# creating a csv writer object 
	csvwriter = csv.writer(csvfile) 
		
# writing the fields 
	csvwriter.writerow(fields) 
		
# writing the data rows 
	csvwriter.writerows(rows) 
