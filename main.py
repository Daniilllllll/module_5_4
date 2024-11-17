#
#
#
#
#
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        obj = super().__new__(cls)
        cls.houses_history.append(house_name)
        return obj

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        floor = 0
        print(f"{self.name} имеет {self.number_of_floors} этажей, едем на {new_floor}!")
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"В здании {self.name} такого этажа не существует!")
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        itog = str(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
        return itog

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __del__(self):
        print(self.name, "снесён, но останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))
#
# # __eq__
# print(h1 == h2)
#
# # __add__
# h1 = h1 + 10
# print(h1)
# print(h1 == h2)
#
# # __iadd__
# h1 += 10
# print(h1)
#
# # __radd__
# h2 = 10 + h2
# print(h2)
#
# # __gt__
# print(h1 > h2)
#
# # __ge__
# print(h1 >= h2)
#
# # __lt__
# print(h1 < h2)
#
# # __le__
# print(h1 <= h2)
#
# # __ne__
# print(h1 != h2)
