# WHY MIGHT WE WANT TO RAISE AN ERROR?
# Suppose we input 47m for height in the bmi program below. The program will still run,
# But that makes no sense, when the person is not Godzilla.

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError(f"{height} meters is too high for a human!")

bmi = weight / height ** 2
print(bmi)

# We raise errors where program could run successfully but give inaccurate results



