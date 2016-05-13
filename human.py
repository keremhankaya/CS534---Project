from stateMachine import *
import random

afterTravelGetSickRate = 40
class Human:
    def __init__(self, initialState):
        self.currentState = initialState
        self.currentState.run()
        #self.country = country
        self.moving_day = 6 #means not qulified for travelling

    def next_day(self):
        self.currentState = self.currentState.next()

    def isInTravelState(self):
        if (self.currentState == HumanState.healty) or (self.currentState == HumanState.incubation) or (self.currentState == HumanState.immune):
            return True
        else:
            return False

    def decideMovingDay(self):
        self.moving_day = random.randrange(1,6)
        return False

    def isAvailableTravel(self):
        if self.isInTravelState() == True:
            self.moving_day -= 1
            if self.moving_day > 0:
                self.decideMovingDay()
            else:
                self.afterTravelAction()
                return True
        else:
            return False

    def afterTravelAction(self):
        if random.randrange(0,100) > afterTravelGetSickRate: pass
        else:
            self.currentState = HumanState.visiblyinfectious

class HumanState(Human):
    def __init__(self):
        # Initial state
        Human.__init__(self, HumanState.healty)

# Static variable initialization:
HumanState.healty = Healty()
HumanState.incubation = Incubation()
HumanState.visiblyinfectious = VisiblyInfectious()
HumanState.death = Death()
HumanState.immune = Immune()
