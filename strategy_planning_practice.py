# Strategy Planning Example

class Train:
    def move(self):
        print("Travelling by Train")


class Flight:
    def move(self):
        print("Travelling by Flight")


class Ship:
    def move(self):
        print("Travelling by Ship")


class Trip:
    def __init__(self, transport):
        self.transport = transport

    def begin_trip(self):
        self.transport.move()


print("Choose Your Transport")
print("1. Train")
print("2. Flight")
print("3. Ship")

option = int(input("Enter Your Choice: "))

if option == 1:
    travel_plan = Trip(Train())
elif option == 2:
    travel_plan = Trip(Flight())
elif option == 3:
    travel_plan = Trip(Ship())
else:
    print("Invalid Choice")
    exit()

travel_plan.begin_trip()

'''
OUTPUT:

Choose Your Transport
1. Train
2. Flight
3. Ship
Enter Your Choice: 2

Travelling by Flight
'''
