
import re
import csv

with open("data.csv", mode="w", newline='') as cfile:
    writer = csv.writer(cfile)
    writer.writerow(["Year", "Code", "Planet"])  # Header

    with open("alien_logs.txt", "r") as file:
        
        for line in file:
            if line.lower().startswith("[log]"):
                print(line.strip())
            
            dic = {}
            match = re.search(r"Year:(\d{4})", line)
            if match:
                print(match.group(1))
                dic["Year"] = match.group(1)
            match = re.search(r"Code=([A-Z]{2}-(\d{5}))", line)
            if match:
                print(match.group(1))
                dic["Code"] = match.group(1)
            match = re.search(r"Planet=([^\s|]+)", line)
            if match:
                print(match.group(1))     
                dic["Planet"] = match.group(1)
            
            if all(key in dic for key in ["Year", "Code", "Planet"]):
                    writer.writerow([dic["Year"], dic["Code"], dic["Planet"]])
            
print("Data written to data.csv successfully.")



