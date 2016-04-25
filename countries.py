import human

class Position:
    def __init__(self, y_position, x_position):
        self.y_position = y_position
        self.x_position = x_position

class Country:
    def __init__(self, y_position, x_position):
        self.position = Position(y_position, x_position)
        self.NationList = list()

    def createNation(self, people): pass

    def addPerson(self, person):
        self.NationList.append(person)

    def isThereAnySickPeople(self):
        for person in self.NationList:
            if person.currentState != human.HumanState.healty:
                return True

        return False

    def numberOfVisiblySickPeople(self):
        number = 0
        for person in self.NationList:
            if (person.currentState == human.HumanState.visiblyinfectious) or (person.currentState == human.HumanState.death):
                number +=1
        return number

    def numberOfPeople(self):
        return len(self.NationList)

    def numberOfIncubatedPeople(self):
        number = 0
        for person in self.NationList:
            if person.currentState == human.HumanState.incubation:
                number +=1
        return number

class World:
    def __init__(self, dimension):
        self.dimension = dimension
        self.WorldList = list()
        self.neighborVisiblySickList = list()
        for y in range(0, dimension):
            for x in range(0, dimension):
                self.WorldList.append(Country(y,x))

    def addPerson(self, index, person):
        self.WorldList[index].addPerson(person)

    def isNeighbor(self, country1, country2):
        x_distance = abs( (country1.position.x_position - country2.position.x_position) % self.dimension)
        y_distance = abs( (country1.position.y_position - country2.position.y_position) % self.dimension)
        if( ((y_distance == 1) and (x_distance == 0)) or ((y_distance == 0) and (x_distance == 1)) ):
            return True
        else:
            return False

    def normalizeIndexAndAddToList(self, position):
        squareDimension = self.dimension * self.dimension
        index = (position + squareDimension) % squareDimension
        self.neighborVisiblySickList.append(self.WorldList[index].numberOfVisiblySickPeople())
        return index

    def switch(self, imput):
        return {
            0 : self.northIndex,
            1 : self.southIndex,
            2 : self.westIndex,
            3 : self.eastIndex,
        }[x]

    def bestTravelPlace(self, country):
        countryIndex = (country.position.y_position * self.dimension) + country.position.x_position
        self.northIndex = self.normalizeIndexAndAddToList(countryIndex - self.dimension)
        self.southIndex = self.normalizeIndexAndAddToList(countryIndex + self.dimension)
        self.westIndex = self.normalizeIndexAndAddToList(countryIndex - 1)
        self.eastIndex = self.normalizeIndexAndAddToList(countryIndex + 1)
        minIndex = self.neighborVisiblySickList.index(min(neighborVisiblySickList))
        return self.switch(minIndex)

    def travel(self): pass
