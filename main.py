import classes.const as const
from classes.Car import Car
if __name__ == "__main__":
    number_plates = ["a123456", "b123456", "c123456", "d123456", "e123456", "f123456", "g123456", "h123456", "i123456", "j123456", "k123456", "l123456", "m123456", "n123456"]
    carsArr = []
    for i in number_plates:
        carsArr.append(Car(i))

    ###try to park each car from carArr#####
    for i in carsArr:
        print(str(i))
        i.park()
        pass

    print("MAIN")
    pass