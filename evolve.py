import random
import time

sample = {}
fitness = {}

global population
population = 100

def switch(myList):
	index1 = random.randint(0, 9)
	index2 = random.randint(0, 9)
	
	val1 = myList[index1]
	val2 = myList[index2]
	
	myList[index1] = val2
	myList[index2] = val1
	
	return myList
	

def take(myList):
	index1 = random.randint(0, 9)
	index2 = random.randint(0, 9)
	
	amount = random.randint(0, myList[index1])
	
	myList[index1] = myList[index1] - amount
	myList[index2] = myList[index2] + amount
	
	return myList

def mutate(toMutate):
	choice = random.randint(0,1)
	
	if choice == 1:
		return switch(toMutate)
	else:
		return take(toMutate)

for i in range(100):
	sample[i] = []
	fitness[i] = 0
	for j in range(10):
		sample[i].append(10)

def getFitnessFromSample(myDict):
	myFitness = {}
	myFitnessList = []
	for i in myDict:
		myFitness[myDict[i][9]] = myDict[i]
		
	myFitnessList = myFitness.items()
	myFitness = dict(sorted(myFitnessList, reverse=True))
	
	return myFitness

def eliminateBadOnes(myDict):
	myNewDict = myDict.items()
	myNewDict = dict(sorted(myNewDict))
	
	myDict = myNewDict.items()
	myDict = dict(myDict)
	
	count = 0
	for i in myDict:
		if count > 4:
			del myNewDict[i]
		count += 1
	return myNewDict

def doOneRun(mySample):
	myFitness = getFitnessFromSample(mySample)
	
	mySample = myFitness.items()
	mySample = dict(mySample)
	
	mySample = eliminateBadOnes(mySample)
	
	toMutate = mySample.items()
	
	mutated = []
	
	for i in range(100):	
		for i in toMutate:
			currentAppend = []
			for j in i[1]:
				currentAppend.append(j)
				
			mutated.append(i[1])
			mutated.append(mutate(currentAppend))
		
		
		sample = {}
		count = 0
		for i in mutated:
			mySample[count + 1] = i
			count += 1
	return mySample
		

def evolve(times):
        sample = {}
        for i in range(100):
                sample[i] = []
                fitness[i] = 0
                for j in range(10):
                        sample[i].append(10)
                        
        for i in range(times):
                sample = doOneRun(sample)

        sample = getFitnessFromSample(sample)
        sample = sorted(sample.items(), reverse=True)

        return sample


stuff = evolve(1000)

for i in stuff:
        print i
