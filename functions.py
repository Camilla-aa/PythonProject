#Functions/Methods - A block of codes used to
# perform a task

#Standard - Library Functions

y = max(45, 78, 89, 43, 2, 456, 7895, 56)
print("The largest number is", y)

print()

x = min(45, 78, 89, 43, 2, 456, 7895, 56)
print("The least number is", x)

print()
#User-defined functions
def name():
    print("Camilla")
name() #calling a function

def add():
    print(10+20)
add()

#parameter/variable
#arguments/values
def dog(name, breed, age):
    print(name, breed, age)

dog("Bob","German Shepherd",4)
dog("Mary","Chihuahua",2)
dog("Peter", "Siberian Husky", 3)

#A program to display details of five employees at eMobilis
#Use a user-defined functions with the help of parameters and arguments
#Details- fullname, position,gender,age
print()
def staff(fullname, position, gender, age):
    print(fullname, position, gender, age)

staff("George Walker","Data Scientist","Male","30")
staff("Martin Homes","MIT Expert","Male","33")
staff("Cindy Kales","Software Engineer","Female","27")
staff("Mark Washington","Web Developer","Male","40")
staff("Ariana Green","Cyber Security Expert","Female","26")




