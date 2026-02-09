Age = 18 #Integer
Weight = 45.78 #Float
Greeting = "Hello there" #String
isMammal = True #Boolean

#Datastructures -Multiple elements in one variable
fruits = ["Banana", "Apple", "Orange", "Mango"] #List - Ordered and changeable -Different datatypes
courses = ["MIT", "Data Science", "Cybersecurity"] #Array -Similar datatypes
cars = ("Ford", "Mercedes", "Mazda", "Mitsubishi") #Tuple - Ordered and unchangeable
countries = {"Tanzania", "India", "Italy"} #Set - Unordered and unchangeable
student = {
    "Firstname": "Jeff",
    "Course": "MIT",
    "Age": 18,
    "Nationality": "Kenya",
}# Dictionary - Key value pair

print("Student is", Age ,"years old")
print(Weight)
print("Is animal a mammal ?:", isMammal)
print(fruits)
print(countries)

#Typecasting- Converting one datatype to another
print(float(Age))
print(int(Weight))  
