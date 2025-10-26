#All imported libraries:
import random #number generator
import sys #for the clear function 
import time #for the  speed
import os

#all global variables:
chest_code = 539 # used for secret chest
fish_cooked = False
player_health = 100
player_inventory = [ "EMPTY",]
player_damage = 10
deer_health = 100
bear_health = 500
bear_damage = 50
deer_eaten = False
forest = "incomplete"
river= "incomplete"
lake = "incomplete"
woodland = "incomplete"
ans = False # used for simple decisions
ans2 = False # used for further decision
clearing = "incomplete"
clearing_completion = 0 # used to track how many places have been visited
chest_is_open = False
visit_chest = "incomplete"
visit_sign = "incomplete"
visit_tree = "incomplete"
empty_chest_visit_num = 0 # used when the player pointlessly visits the chest
apples = 3 # monitors the number of uncollected apples available on the apple trees
def type_text(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    player_name = input(str("Before we begin, please Enter Your Name: \n")).capitalize()
    clear_screen()
    if player_name.isalpha():
        type_text(f"Welcome Player '{player_name}' to the 'Survivor In The Wilderness' Game\n")
        time.sleep(2)
        clear_screen()
        break
    else:
        print("Please only use letters\n")
type_text("In this python text-based game, you will go and explore different situations in a wildlife survival story\n")
type_text("You'll collect items, hunt, eat, and fight animals\n")
type_text("Tip: Depending on the items you collect, you can also improve your own stats to help you in different scenarios\n")
type_text("The way that you will engage with the game is by typing your responses according to what is presented.\n")
time.sleep(2)
clear_screen()
while True:
    start_game = input(f"{player_name}, Would you like to start the game? (Yes or No):\n").lower()
    clear_screen()
    if start_game == "yes":
        type_text("Dropping you in to the game now...\n")
        type_text("...\n",0.5)
        type_text("..\n",0.5)
        type_text(".\n",0.5)
        time.sleep(2)
        clear_screen()
        type_text("You've just woke up from a nice nap, it's currently 5AM in the morning - a little breezy\n")
        type_text("You need to get going for the day as you've got a long day ahead.\n")
        time.sleep(2)
        clear_screen()
        break
    elif start_game == "no":
        type_text(f"{player_name}, maybe next time...\n")
        exit()
    else:
        type_text("Please either type 'yes' or 'no':\n")
type_text("As with every morning, you need to gather some food and freshen up...\n")
while forest == "incomplete" or river == "incomplete": #on my first go I used "and", this didn't create a loop and kept finishing this condition, so after looking at my code with AI, I found that the OR function must be used.
    explore1 = input(f"{player_name} You can visit the Forest or the River, which way do you go? :\n").lower()
    clear_screen()
    if explore1 == "river" and river == "incomplete":
        type_text("You've decided to go to the river to freshen up.\n")
        player_health += 10
        type_text(f"{player_name}'s health increased to: {player_health}\n")
        type_text("You wash and clean yourself there and feel refreshed.\n")
        type_text("Now you start getting a little hungry\n")
        type_text("So you head back towards your camping spot\n")
        time.sleep(3)
        clear_screen()
        while True:
            explore2 = input(f"{player_name}, You find a bow and some arrows on the way back, looks repairable... Do you take them? (Yes or No):\n")
            clear_screen()
            if explore2 == "yes":
                river = "complete"
                player_inventory.pop()
                player_inventory.append("Bow and Arrow (+40 damage)")
                player_damage += 40
                type_text("Great, now we have something to use, should help with catching an animal later\n")
                type_text(f"Your new damage: {player_damage}\n")
                time.sleep(3)
                clear_screen()
                break
            elif explore2 == "no":
                river = "complete"
                type_text("You decided not to take the items, maybe you'll find something later\n")
                time.sleep(3)
                clear_screen()
                break
            else:
             clear_screen()
             type_text("Please type either yes or no :\n")
    elif explore1 == "forest" and forest == "incomplete":
        type_text("You start making your way through the dense bushes to reach the forest\n")
        type_text("You find a bag that looks almost new, someone else must be here...\n")
        type_text("You check its contents and find a sling shot, with some fresh fruit\n")
        type_text("You see what looks like a fireplace that's been stoked out, there are more items there\n")
        time.sleep(2)
        clear_screen()
        type_text("Items: Fire Starter, Sling Shot, Fire Wood and some Fruits\n")
        while True:
            explore3 = input("Do you take the items? (Yes or No):\n")
            if explore3 == "yes":
                clear_screen()
                forest = "complete"
                player_inventory.pop()
                player_inventory.append("fruit",)
                player_inventory.append("fruit",)
                player_inventory.append("fruit",)
                player_inventory.append("fruit",)
                player_inventory.append("fruit",)
                player_inventory.append("fire wood",)
                player_inventory.append("fire starter",)
                player_inventory.append("sling shot (+20 Damage)",)
                player_damage = + 20
                type_text("Perfect, you have some items to starts a fire.\n")
                type_text(f"Your inventory: ['Fruits x 5'], ['Fire Starter'], ['Sling Shot + 20 Damage'], ['Fire Wood']\n")
                type_text(f"Your new damage: {player_damage}\n")
                time.sleep(2)
                clear_screen()
                break
            elif explore3 == "no":
                clear_screen()
                forest = "complete"
                type_text("You decided not to take the items, maybe you'll find something at the lake\n")
                type_text(f"Your new damage: {player_damage}\n")
                time.sleep(2)
                clear_screen()
                break
            else: 
                type_text("Please type either yes or no :\n")
    elif explore1 == "river" and river == "complete":
        type_text("You've already been down the river bed, there's not much to do here now.\n")
    elif explore1 == "forest" and forest == "complete":
        type_text("You've cleared this section of the forest already, nothing useful around here.\n")
    else: 
        type_text("Please type either Forest or River.\n")
type_text("It's now 10AM and you know you need to prepare some lunch for yourself. Nothing sounds better than having a deer!\n")
type_text("You notice some footprints that look like a deer's hoof, thinking of the potential, you follow the lead...\n")
type_text("After scoping around, following the trail, through some trees and down a slope you see a deer grazing.\n")
while deer_eaten == False:
    if deer_health > 0:
        catch_deer = input(f"{player_name} what do you do? ('catch' or 'let it go') :\n").lower()
        clear_screen()
        if catch_deer == "catch" :
            player_damage = round(random.uniform(player_damage - 1, player_damage + 1), 1) 
            deer_health -= player_damage
            deer_health = max(deer_health, 0)
            type_text(f"You hit the deer for {player_damage} damage. deer health is now {deer_health}.\n")
            time.sleep(1)
            clear_screen()
        elif catch_deer == "let it go":
            player_health -= 30
            type_text(f"{player_name}, you let the deer go and you let yourself go hungry\n")
            type_text(f"Your health is now {player_health}\n")
            break
        else:
            print("Please enter Catch or Let Go :\n")
    elif deer_health <=0 and deer_eaten == False:
            type_text(f"Congratulations {player_name}! You've captured the deer, and can now have a nice lunch 🍖!\n")
            type_text("You can choose to take the whole deer with you back to camp or just take the meat...\n")
            type_text("Full Deer or Meat Only?\n")
            while True:
                clear_screen()
                caught_deer = input(f"{player_name}, What do you do? (Full deer or Meat only?):\n").lower()
                if caught_deer == "full deer" and deer_health <=0:
                    clear_screen()
                    type_text(f"while going back over to the deer to collect it, you see a piece of paper and can barely make out what it says\n")
                    player_inventory.append("paper with the number 5 on it")
                    player_health += 50
                    type_text(f"{player_name}'s New Health: {player_health}\n")
                    type_text(f"The item: [{player_inventory[-1]}]\n")
                    deer_eaten = True
                    break
                elif caught_deer == "meat only" and deer_health <=0:
                    clear_screen()
                    player_health += 50
                    type_text("You decide to only take the meat with you to eat\n")
                    type_text("After finishing up cooking that food and eating it, your fire starts to diminish itself\n")
                    print(f"Your new health: {player_health}")
                    deer_eaten = True
                    break
                else:
                    print("Please type either 'meat only' or 'full deer':\n")
                    time.sleep(1)
deer_eaten = False
type_text("The sun's bright and high above you, right now it's 2pm and you've still got work to do.\n")
type_text("You decide to take yourself over to the lake...\n")
time.sleep(2)
while True:
    if "EMPTY" in player_inventory:
        player_inventory.remove("EMPTY")
        print(f"{player_inventory}")
        time.sleep(1)
        break
    else: 
        print(f"{player_inventory}")
        time.sleep(1)
        break
clear_screen()
type_text("Welcome to the Lake\n")
type_text("As you look around at the lake you notice it is filled with different types of fish.\n")
type_text("Maybe catching and eating the fish will give you more energy for the journey...\n")
time.sleep(2)
clear_screen()
while lake == "incomplete" or woodland =="incomplete":
    opening_option1 = input(f"{player_name}, would you like to visit the Lake or return to the Woodland?:\n").lower()
    if opening_option1 == "lake":
        clear_screen()
        type_text("You walk towards the lake where you can fish, but we need to check if you have fishing items...\n")
        if "fishing line" in player_inventory:
            type_text("You have a fishing line in your inventory, so you make a quick fishing rod and cast it out in the lake\n")
            clear_screen()
            time.sleep(2)
            type_text("You caught a small Cod, a medium Haddock, and a large Salmon:\n")
            while True:
                keep_fish = input("Do you keep the fish? (Yes or No):\n").lower()
                if keep_fish == "yes":
                    clear_screen()
                    player_inventory.append("cod")
                    player_inventory.append("haddock")
                    player_inventory.append("salmon")
                    player_inventory.remove("fishing line")
                    player_health += 50
                    type_text(f"You added to your inventory now: [Cod, Haddock, Salmon]\n")
                    lake = "complete"
                    break
                elif keep_fish == "no":
                    clear_screen()
                    type_text("I hope you have enough energy to survive the journey...\n")
                    lake = "complete"
                    break
                else:
                    clear_screen()
                    type_text("Please only type from the given options.\n")
        elif "fishing line" not in player_inventory:
            clear_screen()
            type_text("You don't have a fishing line right now, try visiting the woodlands and see if you can find something there and come back\n")
        else:
            clear_screen()
            print("Please only type from the given options.\n")
    elif opening_option1 == "woodland" and "fishing line" not in player_inventory:
        clear_screen()
        type_text("So you go down to the woodlands to see if you can find something useful...\n")
        type_text("You stumble across a rock and you find a fishing line under it and put them in your bag\n")
        player_inventory.append("fishing line")
        print("'Fishing Line' added to inventory:\n")
        woodland = "complete"
        type_text("Now you finally have your Fishing Line but the view of the Woodlands are amazing!\n")
        while True:
            stay_woodland = input("Do you want to stay in the Woodlands a bit longer? (Yes or No):\n").lower()
            if stay_woodland == "yes":
                    clear_screen()
                    type_text("While enjoying the view of the Woodlands a massive eagle lands nearby...\n")
                    type_text("As you approach the eagle it drops a piece of paper from its claws...\n")
                    type_text("Hmmm it's strange for an eagle to have a piece of paper... maybe you should hold on to that...\n")
                    player_inventory.append("paper with number 3 on it")
                    type_text("'Paper with number 3 on it' added to inventory\n")
                    woodland = "complete"
                    break
            elif stay_woodland == "no":
                clear_screen()
                type_text("Let's hurry back to the lake!\n")
                woodland = "complete"
                break
            else:
                clear_screen()
                type_text("Please only type from the given options.\n")
    elif opening_option1 == "woodland" and "fishing line" in player_inventory:
        clear_screen()
        type_text("You already have a Fishing Line, no need to enter the Woodland.\n")
    else:
        clear_screen()
        type_text("Please only type from the given options.\n")
type_text("You've now completed the midday scene. Time to continue your journey...\n")
time.sleep(2)
clear_screen()
type_text("Now it's 5PM in the afternoon and it's going to start getting dark soon\n")
type_text("We need to prepare some food for the night if we can, we need to check the inventory...\n")
while fish_cooked == False:
    check_inventory_cooking = input("Do you want to open your inventory or skip cooking? \n").lower()
    if check_inventory_cooking == "open inventory":
        type_text(f"{player_inventory}")
        time.sleep(3)
        clear_screen()
        while True:
            if "cod" in player_inventory and "fire starter" in player_inventory:
                type_text("You have some fish and a fire starter from before so you get cooking\n")
                type_text("Item added to inventory [Cooked Fish]\n")
                player_inventory.remove("cod",)
                player_inventory.remove("haddock",)
                player_inventory.remove("salmon",)
                player_inventory.append("cooked haddock",)
                player_inventory.append("cooked cod",)
                player_inventory.append("cooked salmon",)
                fish_cooked = True
                time.sleep(2)
                break
            elif fish_cooked == True and "cooked salmon" in player_inventory:
                type_text("You have already cooked everything for tonight, let's move on...\n")
                fish_cooked = True
                time.sleep(2)
                break
            elif "fire starter" in player_inventory and "cod" not in player_inventory:
                type_text("Aw dang it! You have a fire starter but nothing to cook!\n")
                fish_cooked = True
                time.sleep(2)
                break
            elif "fire starter" not in player_inventory and "cod" in player_inventory:
                type_text("You have some food that you can cook, but nothing to start a fire! Let's go take a stroll instead...\n")
                fish_cooked = True
                time.sleep(2)
                break
            elif "fire starter" not in player_inventory and "cod" not in player_inventory:
                type_text("You have nothing to start a fire or anything to cook... Let's just get on with the evening.\n")
                fish_cooked = True
                time.sleep(2)
                break
    elif check_inventory_cooking == "skip":
        type_text("You decide not to cook anything and move on with your evening...\n")
        break
    else: 
        clear_screen()
        type_text("please type either Skip or Open Inventory\n")
time.sleep(2)
clear_screen()
type_text("You've been strolling around for hours now and you've got a lot done\n")
type_text("While you stop to take a leak near some bushes, you see something under your feet...\n")
type_text("Paper with number '9' on it\n")
while True:
    collect_paper = input("Could be nothing, do you take it with you? (Yes or No)\n").lower()
    if collect_paper == "yes":
        clear_screen()
        type_text("You've put it in your inventory\n")
        player_inventory.append("paper with number 9 on it")
        break
    elif collect_paper == "no":
        clear_screen()
        type_text("it was wet anyway...\n")
        time.sleep(2)
        break
    else:
        clear_screen()
        print("Please type either yes or no\n")
clear_screen()
type_text("It's looking all good so far, you've explored the river beds, woodlands, forest, and the lakes.\n")
time.sleep(2)
clear_screen()
type_text("The time is 8PM.\n")
type_text("Running away from the sounds of wolves, you enter a dense, misty forest.\n")
type_text("As nightfall begins to set, you come across a fallen tree. Looks like a great place set up camp for the night.\n")
time.sleep(5)
clear_screen()
while ans == False:
    start_fire = input("Start fire here?\n").lower().strip()
    print("\n")
    if start_fire == "yes":
        if "fire starter" in player_inventory:
            fire_outcome = "success"
        else:
            type_text("You don't have the resources to start a fire.\n")
            input("Press enter to continue.\n")
            fire_outcome = "missing_item"
        ans = True
    elif start_fire == "no":
        fire_outcome = "declined"
        ans = True
    else:
        print("Please answer with 'Yes' or 'No'.\n")
ans = False
if fire_outcome == "missing_item":
    type_text("You continue earnest. A passing cold breeze sends shivers down your spine.\n")
elif fire_outcome == "declined":
    type_text("You decide to embrace the cold night.\n")
    type_text("As you continue through the dense forest, a passing cold breeze reminds you of your mortality.\n")
else:
    type_text("You start the fire using the fire starter. The warm glow slowly reveals the subtle beauty in the surrounding nature.\n")
    type_text("Kneeling down beside the fire, you are calm, at peace. For a moment, you are reminded of home.\n")
    print("\n")
    player_health += 50
    print(f"{player_name}'s health increased to: {player_health}.\n")
time.sleep(3)
input("Press Enter to continue...\n")
clear_screen()
type_text("The time is 10PM.\n")
if fire_outcome != "success":
    type_text("After wandering for some time, you admit yourself completely lost. Upon finding a small clearing, you attempt to look around and get your bearings.\n")
else:
    type_text("After resting at the fire for a short time, you begin to search the immediate area to get your bearings.\n")
type_text("The area is unrecognizable in the darkness of the night and a deep fog obscures the horizon.\n")
if fire_outcome != "success":
    type_text("You are cold and shivering. The silence is uncanny.\n")
else:
    type_text("The silence is uncanny.\n")
time.sleep(5)
type_text("At that moment, you hear the distinct sound of leaves crunching in the distance. Maybe another deer?", 0.07)
print("\n")
while ans == False:
    investigate = input("Investigate?\n").lower().strip()
    print("\n")
    if investigate == "yes":
        type_text("You peer around the trees, attempting to get a good look at what's out there. You can't get a good view through the fog.\n")
        type_text("Attempting to follow the sound, you find yourself in a small clearing.\n")
        ans = True
    elif investigate == "no" and fire_outcome == "success":
        type_text("You decide to abandon the fire and quickly leave.\n")
        ans = True
    elif investigate == "no" and fire_outcome != "success":
        type_text("You decide to stay quiet and ignore the animal until it leaves.\n")
        type_text("The cold air thickens. You are extremely cold.\n")
        print("\n")
        player_health -= 10
        print(f"{player_name}'s health decreased by 10.\n")
        ans = True
    else:
        print("Please answer with 'Yes' or 'No'.\n")
ans = False
time.sleep(3)
type_text("After a short while, the sound dissipates. Whatever it was, it's gone now.\n")
time.sleep(3)
input("Press Enter to continue...\n")
clear_screen()
while clearing == "incomplete":
    ans = False
    ans2 = False
    clear_screen()
    if visit_chest == "complete" and visit_sign == "complete" and visit_tree == "complete":
        type_text("You have fully explored this area. You can now type 'Leave' if you wish to leave, or continue exploring.\n")
    type_text("You are in a small clearing.\n") 
    type_text("To your left is an open cave. Straight ahead, there seems to be a broken wooden object laying on the ground. To your right are a few apple trees.\n")
    print("\n")
    direction_choice = input("Which direction would you like to go?\n").lower().strip()
    if direction_choice == "left":
        clear_screen()
        if visit_chest == "complete":
            type_text("You climb back into the nearby cave, and find your way to the chest.\n")
        else:
            type_text("You clamber your way into the nearby cave. As you explore deeper, darker passageways, you faintly hear the heavy wind echo throughout the small cave.\n") 
            type_text("Shrouded in dust and darkness, you discover a large chest at the bottom.\n")
        print("\n")
        while ans == False:
            if chest_is_open == False:
                type_text("The chest is secured with a 3-digit combination padlock.\n")
                if "paper with number 5 on it" or "paper with number 3 on it" or "paper with number 9 on it" in player_inventory:
                    print(f"{player_inventory}")
                chest_code_attempt = input("Enter a combination to try, or leave the chest be.\n").strip()
            else:
                chest_code_attempt = chest_code
            if str(chest_code_attempt).isdigit() == True and len(str(chest_code_attempt)) == 3:
                if int(chest_code_attempt) == chest_code:
                    if chest_is_open == False:
                        type_text("The lock clicks and falls to the ground. The chest swings open, revealing a sturdy hatchet. It has illegible inscriptions down the handle, looks a bit used.\n")
                    while ans2 == False:
                        if "lost hatchet" not in player_inventory:
                            if chest_is_open == True:
                                type_text("The mysterious hatchet remains in the chest.\n")
                            hatchet_obtain = input("Take the hatchet?\n").lower().strip()
                            if hatchet_obtain == "yes":
                                type_text("You firmly grasp the hatchet. It is extremely sharp and heavy.\n")
                                type_text("Feeling accomplished, you head back to the surface.\n")
                                time.sleep(3)
                                player_inventory.append("lost hatchet",)
                                player_damage += 50
                                clear_screen()
                                visit_chest = "complete"
                                chest_is_open = True
                                ans = True 
                                ans2 = True
                            elif hatchet_obtain == "no":
                                type_text("You leave the hatchet where it is, quickly leaving the way you came.\n")
                                time.sleep(3)
                                clear_screen()
                                visit_chest = "complete"
                                chest_is_open = True
                                ans = True
                                ans2 = True
                            else:
                                print("Please answer with 'Yes' or 'No'.\n")
                        else:
                            if empty_chest_visit_num < 1:
                                type_text("The chest is empty. Who would've guessed? After twiddling your thumbs for a while, you head back to the surface.\n")
                                empty_chest_visit_num += 1
                                time.sleep(5 * empty_chest_visit_num)
                                clear_screen()
                            else:
                                type_text("Astonishingly, the chest is still empty! So, after twiddling your thumbs for twice as long as before, you head back to the surface.\n")
                                time.sleep(5 * empty_chest_visit_num)
                                clear_screen()
                            empty_chest_visit_num = 2 * empty_chest_visit_num
                            ans = True
                            ans2 = True
                else:
                    type_text("The lock doesn't budge.\n")
                    time.sleep(3)
                    clear_screen()
            elif str(chest_code_attempt).lower() == "leave":
                clear_screen()
                visit_chest = "complete"
                ans = True
            else:
                clear_screen()
                print("Please enter a 3 digit number or type 'Leave'.\n")
    elif direction_choice == "straight" or direction_choice == "forward":
        clear_screen()
        type_text("You walk over to the object and pick it up.\n")
        print("\n")
        type_text("The sign reads:\n")
        print(" [ CAUTION  ] \n |   BEARS  | \n [NEXT 10 km]\n")
        visit_sign = "complete"
        time.sleep(3)
        input("Press Enter to continue...\n")
        clear_screen()
    elif direction_choice == "right":
        clear_screen()
        if visit_tree == "complete":
            type_text("You walk back over to the apple trees.\n")
        else:            
            type_text("You walk over to inspect the apple trees. Most of the apples have yet to ripen; some look edible.\n")
        print("\n")
        while ans == False:
            if apples == 0:
                type_text("There are no more fresh apples to pick. You leave the rest to ripen.\n")
                take_apple = ""
                time.sleep(3)
                ans = True
            elif apples == 3:
                take_apple = input("Take an apple?\n").lower().strip()
            else:
                take_apple = input("Take another apple?\n")
            if take_apple == "yes":
                type_text("You pick a fresh apple from the tree.\n")
                print("\n")
                apples -= 1
                player_inventory.append("apple")
                visit_tree = "complete"
            elif take_apple == "no":
                type_text("You leave the apples and walk away.\n")
                time.sleep(3)
                visit_tree = "complete"
                ans = True
            else:
                clear_screen()
                print("Please answer with 'Yes' or 'No'.\n")
    elif direction_choice == "leave":
        if visit_chest == "complete" and visit_sign == "complete" and visit_tree == "complete":
            clear_screen()
            type_text("As thick clouds begin to overtake the red hue of the night sky, you decide it best to leave.\n")
            type_text("Slowly making your way back, you make a mental note to never stray this far from home again.\n")
            type_text("The harsh winds are excruciating.\n")
            clearing = "complete"
            time.sleep(5)
            input("Press Enter to continue...\n")
    else:
        clear_screen()
        print("Please answer with 'Left', 'Straight' or 'Right'.\n")
clear_screen()
type_text("It's now close to midnight\n")
if fire_outcome == "success":
    type_text("Arriving back to your campfire, you find it trampled and destroyed.\n", 0.07)
    type_text("You kneel down to get a closer look at the footprints.\n", 0.07)
else:
    type_text("Wandering the unlit forest, you are unable to find any clues to your whereabouts.\n")
    type_text("After a while, the area feels liminal. The trees are seemingly endless through the dense fog.\n")
    type_text("Eventually, you come across a trail of large footprints. Hoping they may lead to the river, you kneel down to get a closer look.\n", 0.07)
time.sleep(3)
type_text("As you do, you quickly recognize the familiar sound of leaves crunching behind you... It can't be!\n", 0.07)
time.sleep(5)
clear_screen()
type_text("As soon as you turn around, you are face-to-face with a wild grizzly bear!\n", 0.02)
time.sleep(3)
#boss
while True:
    if bear_health <= 0:
        clear_screen()
        type_text(f"Congratulations {player_name}! You defeated the Wild Bear and live another day. 💪\n")
        time.sleep(5)
        break    
    if player_health <= 0:
        clear_screen() 
        type_text(f"Oh No! {player_name}, the bear overpowered you, you're now ☠️!\n")
        type_text("What a way to end the game 😢\n")
        time.sleep(5)
        exit()
    fight_bear = input(f"{player_name} what do you do? ('hit' or 'heal'):\n").lower()
    if fight_bear == "hit":
        clear_screen()
        player_damage = round(random.uniform(player_damage - 1, player_damage + 1), 1)
        bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
        bear_health -= player_damage
        player_health -= bear_damage
        bear_health = max(bear_health, 0)
        player_health = max(player_health, 0)
        type_text(f"You hit the bear for {player_damage} damage. Bear health is now {bear_health}. ", speed=0.02)
        type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name}'s health is now {player_health}. ", speed=0.02)
    elif fight_bear == "heal":
        clear_screen()
        if "apple" in player_inventory:
            player_health += 30
            player_inventory.remove("apple")
            type_text(f"Player eats Apple health increased to: {player_health}\n")
            bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
            player_health -= bear_damage
            type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name} health is now {player_health}. ", speed=0.02)
        elif "cooked salmon" in player_inventory:
            player_health += 125
            player_inventory.remove("cooked salmon")
            type_text(f"Player eats cooked Salmon health increased to: {player_health}.\n")
            bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
            player_health -= bear_damage
            type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name} health is now {player_health}. ", speed=0.02)
        elif "cooked cod" in player_inventory:
            player_health += 150
            player_inventory.remove("cooked cod")
            type_text(f"Player eats cooked Cod health increased to: {player_health}.\n")
            bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
            player_health -= bear_damage
            type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name} health is now {player_health}. ", speed=0.02)
        elif "cooked haddock" in player_inventory:
            player_health += 100
            player_inventory.remove("cooked haddock")
            type_text(f"Player eats cooked Haddock health increased to: {player_health}.\n")
            bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
            player_health -= bear_damage
            type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name} health is now {player_health}. ", speed=0.02)
        elif "haddock" in player_inventory:
            player_health += 50
            player_inventory.remove("haddock")
            type_text(f"Player eats raw Haddock health increased to: {player_health}.\n")
            bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
            player_health -= bear_damage
            type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name} health is now {player_health}. ", speed=0.02)
        elif "salmon" in player_inventory:
            player_health += 60
            player_inventory.remove("salmon")
            type_text(f"health increased to: {player_health}.\n")
            type_text(f"Player eats raw Salmon health increased to: {player_health}.\n")
            bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
            player_health -= bear_damage
            type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name} health is now {player_health}. ", speed=0.02)
        elif "cod" in player_inventory:
            player_health += 75
            player_inventory.remove("cod")
            type_text(f"Player eats raw Cod health increased to: {player_health}.\n")
            bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
            player_health -= bear_damage
            type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name} health is now {player_health}. ", speed=0.02)
        elif "fruit" in player_inventory:
            player_health += 50
            player_inventory.remove("fruit")
            type_text(f"player eats 1 fruit health increased to: {player_health}.\n")
            bear_damage = round(random.uniform(bear_damage - 20, bear_damage + 20), 1)
            player_health -= bear_damage
            type_text(f"The bear hit back and dealt {bear_damage} damage. {player_name} health is now {player_health}. ", speed=0.02)
        else:
            type_text("You have no healing items.\n")
    else:
       type_text("Please type 'Hit' or 'Heal'.\n")
type_text("You completed the game!🎊🎉\n")
type_text("Now it's time for you to put your feet up, eat some bear meat by the fire next to your camp and wear the bears skin as a cloak\n")
type_text("There was a nice drink you picked up earlier so you pop open the bottle.\n")
type_text("As you take your sip you hear the bushes bustling behind you, you turn around to see what it could be...\n")
type_text("You go closer to take a look...\n")
type_text("Something jumps out at you and starts beating at you\n")
type_text("You push it off you and give it a kick and it stopped moving.\n")
type_text("you go closer to remove the cloak over them and you see its another survivor...\n")
time.sleep(5)
exit()

