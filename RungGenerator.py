from Npp import *
# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script

editor.beginUndoAction()

text = editor.getSelText()
bufferText = text
editor.deleteBack()
itemIter = 0

class RungSet:
	def __init__(self, numberOfLists):
		self.staticVarNo = 0
		self.staticVars = []
		self.listVarNo = 0
		self.listVars = []
		self.listVarNo = numberOfLists
	def get_rungSet(self):
		self.staticVars = list(notepad.prompt("Provide static variables", "Static Variables:", "Variables that don't change in every rung.").split(','))
		for i in range(0, self.listVarNo):
			self.listVars.append([])
			attempts = 0
			while True:
				self.listVars[i] = getList(attempts, str(self.staticVars), str(i+1))
				if self.listVars[i] != -1:
					break
				else:
					attempts += 1
					
	def get_placeHolders(self):
		self.s_placeHolders = []
		self.l_placeHolders = []
		self.listPlaceHolderPairs = []
		for i in range(0,len(self.staticVars)):
			self.s_placeHolders.append(("*S" + str(i+1) + "*"))
		for g in range(0, len(self.listVars)):
			self.l_placeHolders.append("*L" + str(g+1) + "*")
		for h in range(0, len(self.listVars)):
			self.listPlaceHolderPairs.append([])
			for j in range(len(self.listVars[h])):
				self.listPlaceHolderPairs[h].append([self.l_placeHolders[h],self.listVars[h][j]])
		
	def printRungs(self, txt):
		txt1 = txt
		self.get_placeHolders()		
		for h in range(0, len(self.staticVars)):
			txt1 = txt1.replace(self.s_placeHolders[h], self.staticVars[h])
			buffer = txt1
		for i in range(len(self.listPlaceHolderPairs[0])):
			result = buffer
			for g in range(len(self.listPlaceHolderPairs)):			
				result = result.replace(self.listPlaceHolderPairs[g][i][0], self.listPlaceHolderPairs[g][i][1])
			print result

def getList(attempts, sVars, listNo):
#This function parses out a string into a list and then checks to see if the items are series.
	if attempts != 0:
		prompt = "Please re-enter the values\nPlease provide list # " + listNo + " for " + sVars + " static variables.\n\nAttempt #: " + str(attempts)
	else:
		prompt = "Please provide list # " + listNo + " for " + sVars + " static variables."
	a = notepad.prompt(prompt, "List Variables:")
	b = list(a.split(','))
	c = []
	try:
		for i in b:
			if "-" in i:
				g = i.split('-')
				t = g
				for h in range(int(g[0]),int(g[1])+1):
					c.append(str(h))
				g = None	
			else:
				c.append(i)
		return c
	except:
		notepad.messageBox(str(t) + " is not a valid range for a series.\nPlease try again.","Error")
		return -1
	

#number of lists doesn't change, so get it once for the whole program execution
while True:
	attempts = 0
	if attempts != 0: prompt = "How many list variables do you need for each set of static variables?\nAttempt #: " + str(self.staticVars)
	else: prompt = "How many lists do you need for each set of static variables?"
	numberOfLists = notepad.prompt(prompt, "Number of lists:", "ex. 2")
	if numberOfLists.isdigit() == False:
		notepad.messageBox(str(numberOfLists) + " is not a valid integer.", "Error")
		attempts += 1
	else:
		numberOfLists = int(numberOfLists)
		break

# Get the number of 'Sets' of data, or rather the number of sets of static variables		
noOfRungSets = int(notepad.prompt("How many sets of rungs do you need?", "Number of sets:", "ex. 2"))
Sets = [RungSet(numberOfLists) for i in range(noOfRungSets)]		#create a list of 'RungSets'


for i in Sets:
	i.get_rungSet()		#get all the rungset static variables and list variables

for i in Sets:
	i.printRungs(text)	#print out the rungs in sequence


# End the undo action, so Ctrl-Z will undo the above two actions
editor.endUndoAction()