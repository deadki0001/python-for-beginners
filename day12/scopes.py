enemies = 1

def increase_enemies():
    """Increases enemy count""" 
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope - Exist within functions

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
#     drink_potion()    
#     print(potion_strength)

# Global Scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()