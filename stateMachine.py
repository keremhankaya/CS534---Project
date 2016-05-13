import random
import human

death_probability = 25
class LifeState:
    dead, alive = range(2)

class InfectionState:
    processLimit = 0
    processTime = 0
    def run(self):
        assert 0, "run not implemented"
    def next(self):
        assert 0, "next not implemented"
    def doesStateCompleted(self, processLimit):
        self.processTime += 1
        if self.processTime >= processLimit:
            self.processTime = 0
            return True
        else:
            return False

class Healty(InfectionState):
    def __init__(self):
        self.processLimit = 0

    def run(self): pass
        #print("Healty")

    def next(self):
        return self

class Incubation(InfectionState):
    def __init__(self):
        self.processLimit = 6 #days

    def run(self): pass
        #print("Incubation")

    def next(self):
        if self.doesStateCompleted(self.processLimit) == True:
            return human.HumanState.visiblyinfectious
        else:
            return self

class VisiblyInfectious(InfectionState):
    def __init__(self):
        self.processLimit = 8 #days
        self.dyingProcessLimit = 3 #days
        self.dyingProcessTime = 0
    def run(self):
        print("VisiblyInfectious")

    def doesDyingStateCompleted(self):
        self.dyingProcessTime += 1
        if self.dyingProcessTime >= self.dyingProcessLimit:
            self.dyingProcessTime = 0
            return True
        else:
            return False

    def next(self):
        if self.doesStateCompleted(self.processLimit) == True:
            if self.doesDyingStateCompleted() == False:
                if self.dieOrLive() == LifeState.alive:
                    return self
                else:
                    return human.HumanState.death
            else:
                return human.HumanState.immune
        else:
            return self

    def dieOrLive(self):
        chance = random.randrange(0,100)
        if chance < death_probability:
            return LifeState.dead
        else:
            return LifeState.alive

class Death(InfectionState):
    def __init__(self):
        self.processLimit = -1 #forever

    def run(self):
        print("Death")

    def next(self):
        return self

class Immune(InfectionState):
    def __init__(self):
        self.processLimit = 2

    def run(self):
        print("Immune")

    def next(self):
        if self.doesStateCompleted(self.processLimit):
            return human.HumanState.healty
        else:
            return self
