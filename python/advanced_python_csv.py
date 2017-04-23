import csv

f = open("faculty.csv", "r")

faculty = list(csv.reader(f))
data = faculty[1:]

emails = []
for row in data:
    emails.append(row[3].strip())
    
with open("emails.csv", "w") as f:
    writer = csv.writer(f, lineterminator = '\n')
    for email in emails:
        writer.writerow([email])
