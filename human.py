from stateMachine import *

class Human:
    def __init__(self, initialState):
        self.currentState = initialState
        self.currentState.run()
        #self.country = country
        self.moving_day = -1
    # Template method:
    def next_day(self, inputs):
        self.currentState.next()
        """for i in inputs:
            print(i)
            self.currentState = self.currentState.next(i)
            self.currentState.run()
        """
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
