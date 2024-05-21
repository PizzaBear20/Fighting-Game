import random
import tkinter as tk


class Character:
    def __init__(self, name):
        self.name = name

    def stats(self):
        self.points = random.randrange(1, 21)
        self.health = 1
        self.strength = 1
        self.speed = 1
        self.intelligence = 1
        self.battleIQ = 1
        count = 1
        while count <= self.points:
            randomNum = random.randrange(1, 6)
            if randomNum == 1:
                self.health += 1
            elif randomNum == 2:
                self.strength += 1
            elif randomNum == 3:
                self.speed += 1
            elif randomNum == 4:
                self.intelligence += 1
            else:
                self.battleIQ += 1
            count += 1  # Increment count to avoid infinite loop

    def displayStats(self):
        # Printing the results
        print()
        print("------------------------------------")
        print("Name: ", self.name)
        print("Health: ", self.health)
        print("Strength: ", self.strength)
        print("Speed: ", self.speed)
        print("Intelligence: ", self.intelligence)
        print("Battle IQ: ", self.battleIQ)
        print("------------------------------------")
        print()
    
    def train(self, attribute):
        if attribute == "random":
            randomAttribute = random.randrange(1, 6)
            if randomAttribute == 1:
                attribute = "health"
            elif randomAttribute == 2:
                attribute = "strength"
            elif randomAttribute == 3:
                attribute = "speed"
            elif randomAttribute == 4:
                attribute = "intelligence"
            else:
                attribute = "battleIQ"
        
        statBoost = random.randrange(1, 21)
        if statBoost <= 5:
            increment = 0
            print(self.name, " trained but did not improve")
        elif statBoost <= 10:
            increment = 1
        elif statBoost <= 14:
            increment = 2
        elif statBoost <= 17:
            increment = 3
        elif statBoost <= 19:
            increment = 4
        else:
            increment = 5
        if increment > 0:
            if attribute == "health":
                self.health += increment
                print(self.name, " trained Health by ", increment, " points")
            elif attribute == "strength":
                self.strength += increment
                print(self.name, " trained Strength by ", increment, " points")
            elif attribute == "speed":
                self.speed += increment
                print(self.name, " trained Speed by ", increment, " points")
            elif attribute == "intelligence":
                self.intelligence += increment
                print(self.name, " trained Intelligence by ", increment, " points")
            elif attribute == "battleIQ":
                self.battleIQ += increment
                print(self.name, " trained Battle IQ by ", increment, " points")
        


# List of names
names = [
    "Chris", "Abby", "Tom", "Jake", "Leland", "Cassius"
]

# List to store Character objects
characters = {}

# Loop through the names, create Character objects, set stats, and store in the list
for name in names:
    character = Character(name)
    character.stats()
    characters[name] = character

# Display stats for each character
def displayAllStats():
    for name, character in characters.items():
        character.displayStats()

# train character call. attribute must be all lowercase or random
def trainCharacterCall(name, attribute):
    if name in characters:
        characters[name].train(attribute)
    else:
        print("Character '", name, "' not found")

# display character stats call
def displayStatsCall(name):
    if name in characters:
        characters[name].displayStats()
    else:
        print("Character '", name, "' not found")

#1v1 character fight
def oneVOne(character1,character2):
    character1Name = character1
    character2Name = character2
    character1 = characters[character1]
    character2 = characters[character2]
    character1Points = 0
    character2Points = 0
    #Health
    if character1.health > character2.health:
        character1Points += 1
    elif character2.health > character1.health:
        character2Points += 1
    #Strength
    if character1.strength > character2.strength:
        character1Points += 1
    elif character2.strength > character1.strength:
        character2Points += 1
    #Speed
    if character1.speed > character2.speed:
        character1Points += 1
    elif character2.speed > character1.speed:
        character2Points += 1
    #Intelligence
    if character1.intelligence > character2.intelligence:
        character1Points += 1
    elif character2.intelligence > character1.intelligence:
        character2Points += 1
    #Battle IQ
    if character1.battleIQ > character2.battleIQ:
        character1Points += 1
    elif character2.battleIQ > character1.battleIQ:
        character2Points += 1
    #comparing points
    if character1Points > character2Points:
        print("Here are the fight results...")
        displayStatsCall(character1Name)
        displayStatsCall(character2Name)
        print(character1Name, " has won the fight")
    elif character2Points > character1Points:
        print("Here are the fight results...")
        displayStatsCall(character1Name)
        displayStatsCall(character2Name)
        print(character2Name, " has won the fight")
    else:
        print("Here are the fight results...")
        displayStatsCall(character1Name)
        displayStatsCall(character2Name)
        print("The fight has ended in a draw")


def main():
    while True:
        menu = input("Type menu to access the menu: ")
    
        if menu:

            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print("****************************")
            print("1. Display Stats")
            print("2. Display all stats")
            print("3. Train Character")
            print("4. Hold 1v1 Battle")
            print("5. Exit")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid Input. Please enter a number")
                continue #restarts the loop

            if choice == 1:
                name = input("Enter character name: ")
                displayStatsCall(name)
            elif choice == 2:
                displayAllStats()
            elif choice == 3:
                name = input("Enter character name: ")
                attribute = input("Enter attribute to train or write randon (must be all lowercase)")
                trainCharacterCall(name,attribute)
            elif choice == 4:
                characterOne = input("Enter the name of the first fighter: ")
                characterTwo = input("Enter the name of the second fighter: ")
                oneVOne(characterOne,characterTwo)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again")
if __name__ == "__main__":
    main()
