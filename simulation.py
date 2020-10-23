from randomwalks import UsualDrunk, Field, Location
from randomwalks import walk

if __name__ == "__main__":
    drunk = UsualDrunk("khairi")
    field = Field()
    start = Location(0, 0)
    field.addDrunk(drunk, start)

    for i in range(10):
        distance = walk(field, drunk, i)
        print("steps: {}, distance: {}".format(i, distance))