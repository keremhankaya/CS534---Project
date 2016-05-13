import math
import simulation
import random

#Input variables
WorldDimension = 3
PeopleInTheWorld = 1000
InitialInfectedPeoplePercentage = 10
#deathProbability = 25 #defined in stateMachine

def initializeSystem():
    newSimulation = simulation.Simulation(WorldDimension, PeopleInTheWorld, InitialInfectedPeoplePercentage)
    #print(new.totalInfectedPeople)


initializeSystem()
