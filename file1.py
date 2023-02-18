import csv
import sys
skills_count = {}
skills_source = {}
for small.csv in sys.argv[1:]:
  with open(small.csv, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    if header != ['roles', 'companies', 'locations', 'experience', 'skills', 'date_posted']:
      print(f'Error: incorrect header in file {small.csv}')
      continue
    for i, row in enumerate(reader): 
      skills = row[4].split(',')
      for skill in skills:
        skill = skill.strip()      
        skills_count[skill] = skills_count.get(skill, 0) + 1       
        if skill not in skills_source:
          skills_source[skill] = []
        skills_source[skill].append(f'{small.csv}:{i+2}')
with open('skills.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['skill', 'roles', 'count', 'sources'])
  for skill, count in skills_count.items():
    writer.writerow([skill, '', count, ', '.join(skills_source[skill])])