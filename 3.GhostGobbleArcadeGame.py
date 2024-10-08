"""Instructions

In this exercise, you need to implement some rules from Pac-Man, the classic 1980s-era arcade-game.

You have four rules to implement, all related to the game states.

"Do not worry about how the arguments are derived, just focus on combining the arguments to return the intended result."

Task 1: Define if Pac-Man eats a ghost
 Define the eat_ghost() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man is able to eat a ghost. The function should return True only if Pac-Man has a power pellet active and is touching a ghost.

Task 2: Define if Pac-Man scores
 Define the score() function that takes two parameters (if Pac-Man is touching a power pellet and if Pac-Man is touching a dot) and returns a Boolean value if Pac-Man scored. The function should return True if Pac-Man is touching a power pellet or a dot.

Task 3: Define if Pac-Man loses
 Define the lose() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man loses. The function should return True if Pac-Man is touching a ghost and does not have a power pellet active.

Task 4: Define if Pac-Man wins
 Define the win() function that takes three parameters (if Pac-Man has eaten all of the dots, if Pac-Man has a power pellet active, and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man wins. The function should return True if Pac-Man has eaten all of the dots and has not lost based on the parameters defined in part 3.
 
"""

def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost: return True
    return False


def score(touching_power_pellet, touching_dot):
    if touching_power_pellet or touching_dot: return True
    return False


def lose(power_pellet_active, touching_ghost):
    if not power_pellet_active and touching_ghost: return True
    return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots and not lose(power_pellet_active, touching_ghost): return True
    return False