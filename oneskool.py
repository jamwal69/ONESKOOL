import csv


jobs_csv = open('small.csv','r')


reader = csv.reader(jobs_csv)

skills = []

for row in reader:
  
    skill_set = row[1].split(',')
   
    for skill in skill_set:
        
        if skill not in skills:
            
            skills.append(skill)

jobs_csv.close()

skill_count = {}


for skill in skills:
    
    skill_count[skill] = 0

jobs_csv = open('small.csv','r')


reader = csv.reader(jobs_csv)


for row in reader:
    
    skill_set = row[1].split(',')
   
    for skill in skill_set:
      
        skill_count[skill] += 1


jobs_csv.close()


output_csv = open('skills_count.csv','w',newline='')


writer = csv.writer(output_csv)

writer.writerow(['Skill','Count'])


for skill in skills:
    
    writer.writerow([skill,skill_count[skill]])

output_csv.close()