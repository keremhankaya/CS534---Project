import countries
import human
import random

class Simulation:
    day = 0
    incubatedPeople = list()
    healtyPeople = list()
    def __init__(self, worldDimension, peopleInTheWorld, infectedPeoplePercentage):
        self.worldDimension = worldDimension
        self.world = countries.World(worldDimension)

        self.peopleInTheWorld = peopleInTheWorld
        self.totalInfectedPeople = self.calculateInfectedPeople(peopleInTheWorld, infectedPeoplePercentage)
        self.totalNotInfectedPeople = self.peopleInTheWorld - self.totalInfectedPeople

        self.runSimulation()

    def calculateInfectedPeople(self, peopleInTheWorld, infectedPeoplePercentage):
        return int( (peopleInTheWorld * infectedPeoplePercentage) / 100)

    def generateRandomCountry(self):
        return random.randrange(0, (self.worldDimension*self.worldDimension))

    def generatePeople(self):
        for i in range(0, self.totalNotInfectedPeople):
            self.healtyPeople.append(human.Human(human.HumanState.healty))
        for i in range(0, self.totalInfectedPeople):
            self.incubatedPeople.append(human.Human(human.HumanState.incubation))

    def randomlyDistributePeople(self):
        for person in range(0, self.totalInfectedPeople):
            self.world.WorldList[self.generateRandomCountry()].addPerson(self.incubatedPeople.pop())
        for person in range(0, self.totalNotInfectedPeople):
            self.world.WorldList[self.generateRandomCountry()].addPerson(self.healtyPeople.pop())

    def initializeCountries(self):
        self.generatePeople()
        self.randomlyDistributePeople()

        for country in self.world.WorldList:
            print(country)
            print(country.numberOfPeople())
            print(country.numberOfIncubatedPeople())

    def travel(self):
        self.world.travel()

    def oneDay(self):
        self.travel()
        self.day +=1
        #self.totalInfectedPeople += 1

    def runSimulation(self):
        self.initializeCountries()
        return
        while (self.totalInfectedPeople < self.peopleInTheWorld):
            self.oneDay()
            self.day = self.day + 1
