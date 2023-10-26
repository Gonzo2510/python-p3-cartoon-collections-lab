def roll_call_dwarves(dwarves):
    count = 1
    for dwarf in dwarves:
        print(f"{count}. {dwarf}")
        count += 1
def summon_captain_planet(planeteer_calls ):
    proper = []
    for word in planeteer_calls:
        proper.append(word.capitalize() + "!")
    #print(proper)
    return proper

def long_planeteer_calls(l):
    answer = False
    for word in l:
        if len(word) > 4:
            answer = True
    return(answer)

def find_the_cheese(ingredients):
    cheese = ['cheddar', 'gouda', 'camembert']
    answer = None
    for ingredient in ingredients:
        if ingredient in cheese:
            print(ingredient)
            answer = ingredient
    return(answer)



#roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])
#summon_captain_planet(["earth", "wind", "fire", "water", "heart"])
#long_planeteer_calls(["axe", "earth", "wind", "fire"])
find_the_cheese(['banana', 'cheddar', 'sock'])