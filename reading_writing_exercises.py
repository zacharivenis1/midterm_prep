'''
diary = open('diary.txt','a')

entry_number = 0

while True:
    text = input('Submit your entry and press q to exit')
    entry_number = entry_number + 1
    if text == 'q':
        break
    else:
        diary.write(str(entry_number) +": " + text+"\n")


diary = open('diary.txt','r')

for line in diary:
    print(line)
'''

import random

doc = open('text_doc.txt', 'a')
s = 0
line_number = 0
# creates a sum of the random numbers
for i in range(0, 10):
    line_number = line_number + 1
    s = s + random.randint(1, 101)
    doc.write(str(line_number) + ': ' + str(s) + '\n')

with open('text_doc.txt', 'r') as fp:
    print(fp.read())


