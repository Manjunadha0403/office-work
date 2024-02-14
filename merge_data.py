"""Data Mergeing by common fields data in dict method and the output is save in csv file"""
import csv

# Student Dictionaries
dict_s = {
    "Name": ["Manju", "Shakeena", "Arjun", "Sanju", "Sahasra", "Preethi"],
    "University": ["KL_UNI", "PDV_UNI", "ANNA_UNI", "AU_UNI", "KKH_UNI", "GI_UNI"],
    "Dept": ["Mech", "B.Phrm", 'M.Tech', "B.Com", "MBBS", "ECE"],
    "Gender": ['M', 'F', 'M', 'M', 'F', 'F'],
}

# College Dictionaries
dict_c = {
    "clg_name": ["KL_Engg", "Anna_Engg", "Padma_Pharm", "Kakkathiya", "Andhara", "GI_Engg"],
    "University": ["KL_UNI", "PDV_UNI", "ANNA_UNI", "AU_UNI", "KKH_UNI", "GI_UNI"],
    "City": ["Hyd", "Chn", "Tpty", "Wgrl", "Vizag", "BGL"],
    "Code": ["KLCET", "ANCET", "PDPH", "KHTM", "AUCD","GIECT"]
}

def Merge(dict_s, dict_c):
    return dict_c.update(dict_s)

# Merge the dictionaries
Merge(dict_s, dict_c)

#New/Destination csv file to Write the result of the operation 
filename = "21.csv"

with open(filename, mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    
# Write header
    csv_writer.writerow(dict_c.keys())  
    
# Find the maximum length among the lists
    max_length = max(len(values) for values in dict_c.values())
    
# Write data vertically
    for i in range(max_length):
        csv_writer.writerow([dict_c[key][i] if i < len(dict_c[key]) else '' for key in dict_c.keys()])

print(f"\nDictionary values written to '{filename}' CSV file.")
