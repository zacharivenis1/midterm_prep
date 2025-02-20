text = "this is the text that will be used, it will also have numbers such as 1,2,3,4,5,6,7,8,9, the text will also be used"

numbers=[1,2,3,4,5,6,7,8,9]

print(dir("hello"))

print("hi".capitalize())
print(text.capitalize())

print("My name".find('name'))

#finding occurances
poz = 0

'''
while True:
    text.find('the',poz)
    if poz == -1:
        break
    print(f"Found 'this' in position {poz}")
    poz+=1
'''

print("THIS IS BIG".lower())

text_1 = 'the cat is a rat'

print(text_1.replace('c','r'))

s = "I enjoy going to the movies"
split_s = s.split()
print("! ".join(split_s))

print(s.title())

print(s.upper().capitalize())

a = ("abcdefghijklmnopqrstuvwxyz")

print(a[0:2], a[2:4])
print(a[1:5:3])

print(a[::-1])

b = "cat"

b = 'r' + b[1:]
print(b)

