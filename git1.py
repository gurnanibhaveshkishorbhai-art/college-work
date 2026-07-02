units = int(input("Enter electricity units: "))

if units <= 100:
    amount = units * 1.5
    fixed = 25

elif units <= 200:
    amount = (100 * 1.5) + (units - 100) * 2.5
    fixed = 50

elif units <= 300:
    amount = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4
    fixed = 75

else:
    amount = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (units - 300) * 5
    fixed = 100

total = amount + fixed

print("Energy Charge =", amount)
print("Fixed Charge =", fixed)
print("Total Bill =", total)