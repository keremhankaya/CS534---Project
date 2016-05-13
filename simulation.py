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

        """for country in self.world.WorldList:
            print(country)
            print(country.numberOfPeople())
            print(country.numberOfIncubatedPeople())"""

    def showStateStatistics(self, state):
            print(self.world.numberOfPeopleInStateWorld(state))

    def showStatistics(self):
        print("healty:")
        self.showStateStatistics(human.HumanState.healty)
        print("incubation:")
        self.showStateStatistics(human.HumanState.incubation)
        print("visiblyinfectious:")
        self.showStateStatistics(human.HumanState.visiblyinfectious)
        print("death:")
        self.showStateStatistics(human.HumanState.death)
        print("immune:")
        self.showStateStatistics(human.HumanState.immune)
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("---------------------------------------------------")

    def travel(self):
        self.world.travel()

    def nextStates(self):
        self.world.nextStates()

    def oneDay(self):
        self.travel()
        self.nextStates()
        self.day +=1
        #self.totalInfectedPeople += 1

    def runSimulation(self):
        self.initializeCountries()
        self.showStatistics()
        while (self.day < 10):
            self.oneDay()
            self.showStatistics()
