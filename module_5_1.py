class House:
    pass
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.go_to


    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if 1 <= self.new_floor and  self.new_floor <= self.number_of_floors:
            for i in range(1,new_floor+1):
                print(i)

        elif self.new_floor > self.number_of_floors:
            print(f"Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)