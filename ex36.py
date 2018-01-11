from sys import exit

import random

def random_roll(world):

    if "1d3" in world['roll']:
        return random.randint(1, 3)

    elif "1d6" in world['roll']:
        return random.randint(1, 6)

    elif "2d3" in world['roll']:
        return random.randint(1, 3) + random.randint(1, 3)

    elif "1d4" in world['roll']:
        return random.randint(1, 4)

    elif "2d5" in world['roll']:
        return random.randint(1, 5) + random.randint(1, 5)

    elif "1d10" in world['roll']:
        return random.randint(1, 10)

    elif "3d3" in world['roll']:
        return random.randint(1, 3) + random.randint(1, 3) + random.randint(1, 3)

    else:
        print("not sure I understand")
def new():
    player = {}

    player['health'] = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    player['strength'] = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    player['dex'] = random.randint(1, 6) + random.randint(1, 6) +random.randint(1, 6)
    player['magic'] = random.randint(1, 6) + random.randint(1,6) + random.randint(1, 6)
    player['gold'] = 100
    player['melee_weapon'] = "1d3"
    #function (options = {}) {
     #}
    player['ranged_weapon'] = "Spit"
    player['attack_spell'] = "Prayer"
    player['defense_spell'] = "Prayer"
    player['armor'] = 10 + ((player['dex'] - 10)/2)
    start(player)


    #fight(player, monster)





def start(player):
    world = {}
    world['roll'] = "1d3"
    world['damage'] = random_roll(world)



    #health = player.get('health')
    #print(f"{random3()}")
    #print(f"{random3()}")
    #print(f"{random3()}")
    #print(f"{random3()}")
    print("Type help for command options")
    print(f"""Here are your stats.
    Health:{player.get('health')}
    Strength:{player.get('strength')}
    Dexterity:{player.get('dex')}
    Magic:{player.get('magic')}
    Armor:{player.get('armor')}""")
    print(f"""You are standing at the gates of your hometown.
having decided to be an adventurer. you have {player['gold']} gold,
after selling all your possessions.""")

    travel(player, world)

def travel(player, world):

    monster = {}
    monster['fighting'] = "time"
    monster['spider_health'] = 6
    monster['spider_gold'] = random.randint(1, 10) + random.randint(1, 10)
    monster['spider_ac'] = 14
    monster['spider_attack'] = "3d3"

    choice = input("Where do you want to go?> ").lower()

    if "forest" in choice or "south" in choice:
        old_forest(player, monster, world)

    elif "look" in choice:
        print ("""you see the old forest to the south full of
giant spiders, wolves, and a great amount of prey.
the town is fairly small has a shop, a tavern, and
a church. the mountians are to the east, the ocean
is to the west, north is swamp land. where do you go?""")
        travel(player, world)

    elif "shop" in choice:
        shop(player, world)
    #elif "church" in choice:
        #church()
    #elif "tavern" in choice:
        #tavern()

    else:
        print("I'm not sure I understand.")

def old_forest(player, monster, world):
    print("The forest is dark and full of webs.")
    a = random.randint(1,3)

    if a == 1:
        print("A giant spider jumps out of the forest,\n Do you fight?")
        x = input("> ").lower()

        if "fight" in x or "yes" in x:
            monster['fighting'] = 'spider'
            fight(player, monster, world)

        else:
            print("You die running away you coward.")
            print("do you want to start over")
            choice = input("> ").lower()

            if "yes" in choice:
                new()

            if "no" in choice:
                exit(0)

    elif a == 2:
        print("A branch breaking startles you, it's just a white buck.")
        travel(player, world)

    else:
        print("You enjoy a nice peacefull walk through the forest.")
        travel(player, world)

def shop(player, world):
    print("""\"Welcome to Joe's shop. We have anything one could need for
starting an adventure.\"
Short sword 1d6 30g
Bastard sword 1d10 100g
Sparks 2d3 40g
Healing 1d4 30g
Short bow 1d6 35g
Long bow 2d5 100g
Leather armor 1 ac 30g
Plate armor 4 ac 100g""")

    s = input("what would you like to buy.> ").lower()

    if s == "short sword":

        if player['gold'] >= 30:
            player['gold'] -=30
            print("You are now the proud owner of a Short sword.")
            player['melee_weapon'] = "1d6"
            travel(player, world)

        else:
            print(f"Sorry you only have {player['gold']} gold.")
            travel(player, world)

    elif s == "bastard sword":

        if player['gold'] >= 100:
            player['gold'] -= 100
            print("you now have one sweet Bastard sword!")
            player['melee_weapon'] = "1d10"
            travel(player, world)

        else:
            print(f"You only have a measly {player['gold']} gold.")
            travel(player, world)

    elif s == "sparks":

        if player['gold'] >= 40:
            player['gold'] -= 40
            player['attack_spell'] = "2d3"
            print("you can now cast Sparks.")
            travel(player, world)

        else:
            print(f"You can't afford that spell you only have {player['gold']} gold.")
            travel(player, world)

    elif s == "healing":

        if player['gold'] >= 30:
            player['gold'] -= 30
            player['defense_spell'] = "1d4"
            print("You now have Healing added to your repertoire.")
            travel(player, world)

        else:
            print("You don't have the required funds, you have {player['gold']} gold left.")
            travel(player, world)

    elif s == "short bow":

        if player['gold'] >= 30:
            player['gold'] -= 30
            player['ranged_weapon'] = "1d6"
            print("You now own a puny Short bow.")
            travel(player, world)

        else:
            print(f"You don't have the needed coins for that you only have {player['gold']} gold in your purse.")
            travel(player, world)

    elif s == "long bow":

        if player['gold'] >= 100:
            player['gold'] -= 100
            player['ranged_weapon'] = "2d5"
            print("You can now stick spiders with arrows, from your long bow.")
            travel(player, world)

        else:
            print(f"You don't have the gold for this transaction. only {player['gold']} gold left.")
            travel(player, world)

    elif s == "leather armor":

        if player['gold'] >= 30:
            player['gold'] -= 30
            player['armor'] += 1
            print("You now have leather armor protecting you.")
            travel(player, world)

        else:
            print(f"Your card has been declined only {player['gold']} funds left.")
            travel(player, world)

    elif s == "plate armor":

        if player['gold'] >= 100:
            player['gold'] -= 100
            player['armor'] += 4
            print("The plate is cold and heavy on your shoulders, you feel well proteced.")
            travel(player, world)

        else:
            print(f"""You are Stuck with Shitty armor you will die a painful death,
            only {player['gold']} gold left.""")
            travel(player, world)

    else:
        print("I don't understand.")
        travel(player, world)

def fight(player, monster, world):

    if monster['fighting'] == 'spider':

        while player['health'] > 0 and monster['spider_health'] > 0:
            use = input("What do you use?> ").lower()

            if "sword" in use or "melee" in use:
                #player['melee_weapon'] = function() {
                    #function(base_damage) {
                    #    rand(base_damage)/base_damage * 10
                hit = random.randint(1, 20) + ((player['strength'] - 10) / 2)
                if hit >= monster['spider_ac']:
                    world['roll'] = player['melee_weapon']
                    monster['spider_health'] -= random_roll(world)
                    print(f"Spiders remaining {monster['spider_health']} health")

                    if monster['spider_health'] <= 0:
                        print("You have killed a Giant Spider congrats!")
                        player['gold'] += monster['spider_gold']
                        travel(player, world)

                    else:
                        world['roll'] = monster['spider_attack']
                        player['health'] -= (random_roll(world) - player['armor'])
                        print(f"Your remaining {player['health']} health.")

                        if player['health'] <= 0:
                            print("You have died!")
                            choice = input("do you wish to restart?> ").lower()

                            if "yes" in choice:
                                new()

                            if "no" in choice:
                                exit(0)
                else:
                    print ("You missed.")

            elif "bow" in use:
                world['roll'] = player['ranged_weapon']
                monster['spider_health'] -= (random_roll(world) - monster['spider_ac'])
                print(f"Spiders remaining {monster['spider_health']} health")

                if monster['spider_health'] <= 0:
                    print("You have killed a Giant Spider congrats!")
                    player['gold'] += monster['spider_gold']
                    travel(player, world)

                else:
                    world['roll'] = monster['spider_attack']
                    player['health'] -= (random_roll(world) - player['armor'])
                    print(f"Your remaining {player['health']} health.")

                    if player['health'] <= 0:
                        print("You have died!")
                        choice = input("do you wish to restart?> ").lower()

                        if "yes" in choice:
                            new()

                        if "no" in choice:
                            exit(0)


            elif "sparks" in use:
                world['roll'] = player['attack_spell']
                monster['spider_health'] -= (random_roll(world) - monster['spider_ac'])
                print(f"Spiders remaining {monster['spider_health']} health")

                if monster['spider_health'] <= 0:
                    print("You have killed a Giant Spider congrats!")
                    player['gold'] += monster['spider_gold']
                    travel(player, world)

                else:
                    world['roll'] = monster['spider_attack']
                    player['health'] -= (random_roll(world) - player['armor'])
                    print(f"Your remaining {player['health']} health.")

                    if player['health'] <= 0:
                        print("You have died!")
                        choice = input("do you wish to restart?> ").lower()

                        if "yes" in choice:
                            new()

                        if "no" in choice:
                            exit(0)

            elif "healing" in use:
                world['roll'] = player['defense_spell']
                player['health'] += random_roll(roll)
                print(f"Your health is now{player['health']}")

            else:
                print("I don't understand what you are trying to do.")

    else:
        print("IDK")


    #monster['spider_attack'] = "2d4"

#def town():





#y = 20
#y -=  random.randint(1,6)
#print(f"here is my number {y}")
#y -= (random.randint(1,6))
#print(f"here is my number {y}")
new()
#for x in range(5):
    #print(random.randint(1,6))
