import random

death_probability = 25
class LifeState:
    dead, alive = range(2)

class InfectionState:
    def run(self):
        assert 0, "run not implemented"
    def next(self, input):
        assert 0, "next not implemented"

class Healty(InfectionState):
    def run(self): pass
        #print("Healty")

    def next(self, input):
        if input == Human.healty:
            return Human.incubation
        else:
            return Human.visiblyinfectious

class Incubation(InfectionState):
    def run(self): pass
        #print("Incubation")

    def next(self, input):
        if incubationCompleted == True:
            return Human.visiblyinfectious
        else:
            return Human.incubation

class VisiblyInfectious(InfectionState):
    def run(self):
        print("VisiblyInfectious")

    def next(self, input):
        if visiblyInfectiousCompleted == True:
            if deathProcessCompleted == False:
                if dieOrLive() == LifeState.alive:
                    return Humman.visiblyinfectious
                else:
                    return Human.death
            else:
                return Human.immune
        else:
            return Human.visiblyinfectious

    def dieOrLive(self):
        chance = random.randrange(0,99)
        if chance < death_probability:
            return LifeState.dead
        else:
            return LifeState.alive

class Death(InfectionState):
    def run(self):
        print("Death")

    def next(self, input):
        return Human.death

class Immune(InfectionState):
    def run(self):
        print("Immune")

    def next(self, input):
        if immuneProcessComleted:
            return Human.healty
        else:
            return Human.immune
