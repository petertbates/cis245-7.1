#Peter Bates
#CIS 245 Assignment 7.1 - Virtual Garage

options = ['power mirrors' , 'power locks' , 'remote start' , 'backup camera' , 
	'bluetooth' , 'cruise control' , 'heated seats' , 'cup holders']

def mainMenu():
	prompt = 'To add a car, type "car"'
	prompt += '\nTo add a pickup, type "pickup"'
	prompt += '\nTo finish and exit, type "finish": '
	selection = input(prompt).lower()
	while selection != "car" and selection != "pickup" and selection != "finish":
		selection = input('Please enter "car", "pickup", or "finish": ')
		selection = selection.lower()
	return selection

class Vehicle:
	def __init__(self):
		pass
	def getColor(self):
		self.color = input("Please enter your vehicle's color: ")
	def getYear(self):
		self.year = input("Please enter your vehicle's year: ")
	def getMake(self):
		self.make = input("Please enter your vehicle's make: ")	
	def getModel(self):
		self.model = input("Please enter your vehicle's model: ")
	def getFuelType(self):
		self.fuelType = input("Please enter your vehicle's fuel type: ")
	def getOptions(self):
		'''We slice the full options list to the remaining options, then add them if chosen'''
		self.remainingOptions = options[:]
		self.options = []
		optionSelect = ''
		
		while (optionSelect != 'done'):
			optionPrompt = '\nHere are the options available for your vehicle:'
			for option in self.remainingOptions:
				optionPrompt += '\n\t'
				optionPrompt += option
			optionPrompt += '\nPlease choose an option to add to your vehicle.'
			optionPrompt += '\nOr, when finished, enter "done": '
			optionSelect = input(optionPrompt)
			optionSelect = optionSelect.lower()

			if (optionSelect in self.remainingOptions):
				self.options.append(optionSelect)
				self.remainingOptions.remove(optionSelect)
			elif (optionSelect == 'done'):
				pass
			else:
				print ('\nPlease choose one of the options, or type "done"')
	
class Car(Vehicle):
	def __init__(self):
		self.vehicleType = "car"
	def getEngineSize(self):
		self.engineSize = input("Please enter your car's engine size: ")
	def getNumDoors(self):
		self.numDoors = input("Please enter your car's number of doors: ")
	def getDescription(self):
		self.description = ''
		self.vehicleValues = [self.color.lower() , self.year , self.make.title() , 
				self.model.lower() , self.fuelType.lower(), self.vehicleType]
		for value in self.vehicleValues:
			if value != '':
				self.description += ' '
				self.description += value
		'''Adding A or An to the beginning of the string'''
		vowels = "aeiou"
		if self.description[1] in vowels:
			self.description = "An" + self.description
		else:
			self.description = "A" + self.description

		'''Add engine size, number of doors, both, or neither'''
		if self.engineSize and self.numDoors:
			self.description += ' with a '
			self.description += self.engineSize
			self.description += ' size engine and '
			self.description += self.numDoors
			self.description += ' doors.'
		elif self.engineSize or self.numDoors:
			if self.engineSize:
				self.description += ' with a '
				self.description += self.engineSize
				self.description += ' size engine.'
			else:
				self.description += ' with '
				self.description += self.numDoors
				self.description += ' doors.'
		else:
			self.description += '.'
		'''Add options to a new line'''
		if len(self.options) > 0:
			self.description +='\nIt also comes with '
			optionCount = 0
			while (optionCount+1) < len(self.options):
				self.description += self.options[optionCount]
				if len(self.options) == 2:
					self.description += ' '
				else:
					self.description += ', '
				optionCount += 1
			if len(self.options) > 1:
				self.description += 'and '
			self.description += self.options[optionCount]
			self.description += '.'
		else:
			pass
		self.description += '\n'

class Pickup(Vehicle):
	def __init__(self):
		self.vehicleType = "pickup"
	def getCabStyle(self):
		self.cabStyle = input("Please enter your pickup's cab style: ")
	def getBedLength(self):
		self.bedLength = input("Please enter your pickup's bed length: ")
	def getDescription(self):
		self.description = ''
		self.vehicleValues = [self.color.lower() , self.year , self.make.title() , 
				self.model.lower() , self.fuelType.lower(), self.vehicleType]
		for value in self.vehicleValues:
			if value != '':
				self.description += ' '
				self.description += value
		'''Adding A or An to the beginning of the string'''
		vowels = "aeiou"
		if self.description[1] in vowels:
			self.description = "An" + self.description
		else:
			self.description = "A" + self.description

		'''Add cab style, bed length, both, or neither'''
		if self.cabStyle and self.bedLength:
			self.description += ' with a '
			self.description += self.cabStyle
			self.description += ' style cab and a '
			self.description += self.bedLength
			self.description += ' bed length.'
		elif self.cabStyle or self.bedLength:
			if self.cabStyle:
				self.description += ' with a '
				self.description += self.cabStyle
				self.description += ' style cab.'
			else:
				self.description += ' with a '
				self.description += self.bedLength
				self.description += ' bed length.'
		else:
			self.description += '.'

		'''Add options to a new line'''
		if len(self.options) > 0:
			self.description +='\nIt also comes with '
			optionCount = 0
			while (optionCount+1) < len(self.options):
				self.description += self.options[optionCount]
				if len(self.options) == 2:
					self.description += ' '
				else:
					self.description += ', '
				optionCount += 1
			if len(self.options) > 1:
				self.description += 'and '
			self.description += self.options[optionCount]
			self.description += '.'
		else:
			pass
		self.description += '\n'

#Begin output
print ("Welcome to your garage!")
#starting with 0 vehicles in the garage
vehicles = []

menuSelect = mainMenu()

while menuSelect != "finish":
	if menuSelect == "car":
		vehicles.append(Car())
		vehicles[-1].getColor()
		vehicles[-1].getYear()
		vehicles[-1].getMake()
		vehicles[-1].getModel()
		vehicles[-1].getFuelType()
		vehicles[-1].getEngineSize()
		vehicles[-1].getNumDoors()
		vehicles[-1].getOptions()
		vehicles[-1].getDescription()
	elif menuSelect == "pickup":
		vehicles.append(Pickup())
		vehicles[-1].getColor()
		vehicles[-1].getYear()
		vehicles[-1].getMake()
		vehicles[-1].getModel()
		vehicles[-1].getFuelType()
		vehicles[-1].getCabStyle()
		vehicles[-1].getBedLength()
		vehicles[-1].getOptions()
		vehicles[-1].getDescription()
	print('\n')
	menuSelect = mainMenu()

#When done adding vehicles

if len(vehicles) != 0:
	print("\nThank you, in your garage you have these vehicles:")
	for vehicle in vehicles:
		print(vehicle.description)
else:
	print("There are no vehicles in your garage TT")
#bigSad

#Credit where Credit is Due:
#https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/
#This was the most helpful resource on lists of objects

#this is a trial with git