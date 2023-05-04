"""
SCOPE
"""

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# # LOCAL SCOPE
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# GLOBAL SCOPE
# player_health = 10
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()

# BLOCK SCOPE
"""Python has no Block Scope"""
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
def choose_enemy():
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)
choose_enemy()
"""
Even though {new_enemy} was created inside 
if block. It will still be callable from
outside the if block, because Python does not tie
a variable to a block where it is created as
Except if said block is a function.
If a block was created inside a function, any variables created 
in the block will dwell inside the function but not strictly
inside the block.
In the example above, new enemy cannot be called outside choose_enemy()
but it can be called outside the if block where it was created. C'est fini.
"""
