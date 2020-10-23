import random

class Location(object):
    
    def __init__(self, x, y):
        """
        Represent a location
        Args:
            x (float): x position
            y (float): y position
        """
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY

        return Location(self.x, self.y)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5 

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class Drunk(object):
    
    def __init__(self, name = None):
        """
        Base class for represent a drunk
        Args:
            name (str): drunk name
        """
        self.name = name
    
    def __str__(self):
        if self.name is None:
            return "Anonymous"
        return self.name

class UsualDrunk(Drunk):

    def takeStep(self):
        choices = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        return random.choice(choices)

class MasochistDrunk(Drunk):
    
    def takeStep(self):
        choices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]
        
        return random.choice(choices)

class Field(object):
    
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Drunk already exists")
        else:
            self.drunks[drunk] = loc
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk does not exists")
        else:
            return self.drunks[drunk]
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk does not exists')
        
        xDist, yDist = drunk.takeStep()

        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)
    
def walk(f, d, numSteps):
    """
    Simulate a single walk
    Args:
        f (Field): field
        d (Drunk): drunk
        numSteps (integer): walk length
    """

    start = f.getLoc(d)

    for _ in range(numSteps):
        f.moveDrunk(d)

    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrials, dClass):
    drunk = dClass()
    origin = Location(0, 0)
    distances = []

    for _ in range(numTrials):
        f = Field()
        f.addDrunk(drunk, origin)

        w = walk(f, drunk, numSteps)

        distances.append(round(w, 1))
    
    return distances


def drunkTest(walkLengths, numTrials, dClass):
    means = []
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        mean = round(sum(distances)/len(distances), 4)
        means.append(mean)

        print(dClass.__name__, 'random walks of', numSteps, 'steps')
        print('Mean = ', mean)
        print('Max = ', max(distances))
        print('Min = ', min(distances))
    
    return means