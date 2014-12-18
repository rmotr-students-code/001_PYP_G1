""" Script used for setting up a new class folder layout.

    Steps:
    1) pull from github (not implemented)
    2) create class-<number> folder, where <number> is the last class number + 1, or 1 if it's the first class
    3) create a README.md file inside the class folder describing class information (topic, date, etc)
    4) create 'in-class-work' and 'assignments' folders
"""
import os
from datetime import datetime

print('Setting up a new class...')

# calculate the proper number for the new class
classes = [d.split(' ')[0] for d in os.listdir(os.curdir) if d.startswith('class-')]
if classes:
    last_class = sorted(classes)[-1]
    last_class_number = int(last_class.split('-')[1])
else:
    last_class_number = 0

# ask for class topic
class_topic = raw_input('Enter the new class topic (ex: modules and packages): ')

new_class_folder = 'class-{} ({})'.format(last_class_number + 1, class_topic)

# creating new class folder    
print('Creating new "{}" folder...'.format(new_class_folder))
os.makedirs(os.path.join(os.curdir, new_class_folder))
with open(os.path.join(os.curdir, new_class_folder, 'README.md'), 'w+') as f:
    f.write('class number: {}\n'.format(last_class_number + 1))
    f.write('date: {}\n'.format(datetime.now().strftime('%a %d %b %Y - %H:%M')))
    f.write('topic: {}\n'.format(class_topic))

print('Creating internal content of the new class..')

# creating 'in-class-work' folder
os.makedirs(os.path.join(os.curdir, new_class_folder, 'in-class-work'))
with open(os.path.join(os.curdir, new_class_folder, 'in-class-work/in-class-work.py'), 'w+') as f:
    f.write('# Everything starts here...')

# creating 'assignments' folder
os.makedirs(os.path.join(os.curdir, new_class_folder, 'assignments'))
with open(os.path.join(os.curdir, new_class_folder, 'assignments/README.md'), 'w+') as f:
    f.write('Your assignments will be saved here')
    
print('Done.')