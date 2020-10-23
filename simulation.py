import random
from matplotlib import pyplot
from randomwalks import UsualDrunk, MasochistDrunk
from randomwalks import drunkTest

if __name__ == "__main__":
    random.seed(0)
    walkLenghts = [10000, 20000, 30000, 40000]
    
    means1 = drunkTest(walkLenghts, 100, UsualDrunk)
    means2 = drunkTest(walkLenghts, 100, MasochistDrunk)

    pyplot.plot(walkLenghts, means1, "-b", label='UsualDrunk')
    pyplot.plot(walkLenghts, means2, "-r", label='MasochistDrunk')

    pyplot.legend(loc="upper left")
    pyplot.xlabel('Number of steps')
    pyplot.ylabel('Distance from origin')
    pyplot.title('Mean Distance from Origin (100 trials)')
    
    pyplot.savefig('figure-1.png')
    pyplot.show()