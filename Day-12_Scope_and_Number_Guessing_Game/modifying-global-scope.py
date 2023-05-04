enemies = 4

# def increase_enemies():
#     global enemies
#     enemies += 2
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")

"""WARNING!!!"""
"""NEVER MODIFY A GLOBAL VARIABLE WITHIN A FUNCTION. It is bug-ridden and error-prone"""
"""Do this instead"""
def increase_enemies():
    return enemies + 1
print(increase_enemies())

"""Still however, global scope can be very useful as we will see in next video. Global scope and constants"""
