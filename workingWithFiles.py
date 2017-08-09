class Person(object):
	def __init__(self, name, occupation, age):
		self.name = name
		self.occupation = occupation
		self.age = age

def listPersons():
	person1 = Person("Adam", "Consultant", "26")
	person2 = Person("Elliott", "Trainer", "23")
	person3 = Person("Richard", "Junior Software Dev", "26")
	person4 = Person("Will", "Video Games Dev", "28")
	person5 = Person("Arjun", "Android Dev", "25")
	listToReturn = [person1, person2, person3, person4, person5]
	return listToReturn

def saveList():
	file = open("person.txt","w")
	listOfPeople = listPersons()
	for i in listOfPeople:
		file.write(i.name + "," + i.occupation + "," + i.age + ";")
	file.close()
	
def readList():
	file = open("person.txt","r")
	listRaw = file.read().split(";")
	listOfPeople = []
	for i in listRaw:
		if i != "":
			tempList = i.split(",")
			print(tempList)
			tempPerson = Person(tempList[0], tempList[1], tempList[2])
			listOfPeople = listOfPeople + [tempPerson]
	return listOfPeople
listOfPersons = readList()
print(listOfPersons[0].name)