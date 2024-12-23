from big_car import BigCar
from small_car import SmallCar

# Question 3:
c1: SmallCar = SmallCar()
print(c1.steel_unit, c1.rubber_unit)

# Question 4:
c2: BigCar = BigCar()
print(c2.steel_unit, c2.rubber_unit)

# Question 5:
print(c1)

# Question 6:
print(c2)

# Question 8:
dictionnaire: dict[str, object] = {"c1": c1,
                                   "c2": c2}

# Question 9:
for i in dictionnaire:
    print(f"{i}: {dictionnaire[i]}")

# Question 10:
dictionnaire["c3"] = SmallCar()

# Question 11:
c3 = dictionnaire["c3"]

# Question 12:
dictionnaire["c2"] = c3

# Question 13:
del dictionnaire["c3"]
for i in dictionnaire:
    print(f"{i}: {dictionnaire[i]}")
