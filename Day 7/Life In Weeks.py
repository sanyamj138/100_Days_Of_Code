def lifeInWeeks(age):
    year = 90 * (365//7)
    age = age * (365//7)
    print(year - age)

age = int(input("Give me your age: "))
lifeInWeeks(age)