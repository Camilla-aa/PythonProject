#While loop

count = 10 #Set first value(initialize)
while count <=15:#condition
    print(count)
    count +=1 #means values are increasing by 1
print()
#Program2
number = 105
while number >= 100:
    print("Number is", number)
    number -=1

# For loop
for num in range(20,26,2):
    print(num)
print()
languages = ["Python","C++","Java","JavaScript"]
for lang in languages:
    print(lang)

#Breaks and continue statements
#Break - breaks out of a loop

print()
for i in range(10):
    if i > 5:
        break
    print(i)

print()
#Continue statements - used to end the current iteration and continue to the next one
for i in range(10):
    if i == 5:
        continue
    print(i)


