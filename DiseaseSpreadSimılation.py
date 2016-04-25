import math
import numpy
import simulation
import random

#Input variables
WorldDimension = 3
PeopleInTheWorld = 10000
InitialInfectedPeoplePercentage = 3

def initializeSystem():
    new = simulation.Simulation(WorldDimension, PeopleInTheWorld, InitialInfectedPeoplePercentage)
    #print(new.totalInfectedPeople)


initializeSystem()
#print(random.gauss(2.5,0.2))
