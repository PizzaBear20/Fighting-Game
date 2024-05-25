import random
import tkinter as tk
from tkinter import messagebox


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
        return (
            f"Name: {self.name}\n"
            f"Health: {self.health}\n"
            f"Strength: {self.strength}\n"
            f"Speed: {self.speed}\n"
            f"Intelligence: {self.intelligence}\n"
            f"Battle IQ: {self.battleIQ}"
        )
    
    def train(self, attribute):
        if attribute == "random":
            attribute = random.choice(["health", "strength", "speed", "intelligence", "battleIQ"])

        statBoost = random.randrange(1, 21)
        if statBoost <= 5:
            increment = 0
            message = f"{self.name} trained but did not improve"
        elif statBoost <= 10:
            increment = 1
            message = f"{self.name} trained {attribute} by 1 point"
        elif statBoost <= 14:
            increment = 2
            message = f"{self.name} trained {attribute} by 2 points"
        elif statBoost <= 17:
            increment = 3
            message = f"{self.name} trained {attribute} by 3 points"
        elif statBoost <= 19:
            increment = 4
            message = f"{self.name} trained {attribute} by 4 points"
        else:
            increment = 5
            message = f"{self.name} trained {attribute} by 5 points"

        if attribute == "health":
            self.health += increment
        elif attribute == "strength":
            self.strength += increment
        elif attribute == "speed":
            self.speed += increment
        elif attribute == "intelligence":
            self.intelligence += increment
        elif attribute == "battleIQ":
            self.battleIQ += increment
        
        return message
        
# List of names
names = []

# List to store Character objects
characters = {}

#History list
history = []

# Loop through the names, create Character objects, set stats, and store in the list
for name in names:
    character = Character(name)
    character.stats()
    characters[name] = character

# train character call. attribute must be all lowercase or random
def trainCharacterCall(name, attribute):
    if name in characters:
        resultMessage = characters[name].train(attribute)
        messagebox.showinfo("Training Results", resultMessage)
        updateStats
    else:
        messagebox.showerror("Error", f"Character '{name}' not found")

# display character stats call
def displayStatsCall(name):
    if name in characters:
        stats = characters[name].displayStats()
        messagebox.showinfo("Character Stats", stats)
    else:
        messagebox.showerror("Error", f"Character '{name}' not found")

#1v1 character fight
def oneVOne(character1,character2):
    character1Name = character1
    character2Name = character2
    character1 = characters[character1]
    character2 = characters[character2]
    character1Health = character1.health
    character2Health = character2.health
    character1Speed = character1.speed
    character2Speed = character2.speed
    character1BattleIQ = character1.battleIQ
    character2BattleIQ = character2.battleIQ
    character1AttackStength = (0.25 * float(character1BattleIQ)) + float(character1.strength)
    character2AttackStength = (0.25 * float(character2BattleIQ)) + float(character2.strength)
    number = character1Speed + character2Speed
    
    maxIterations = 1000
    iteration = 0
    fighting = True
    while fighting and iteration < maxIterations:
        attackChance1 = random.randrange(1,number+1)
        attackChance2 = random.randrange(1,number+1)
        if character1Health == 0 or character2Health == 0:
            fighting = False
        else:
            if attackChance1 <= character1Speed:
                character2Health -= character1AttackStength
            if attackChance2 > character1Speed:
                character1Health -= character2AttackStength
        iteration += 1

    #comparing points
    if character1Health > character2Health:
        historyEvent = f"{character1Name} has won the fight against {character2Name}"
        messagebox.showinfo("Fight Results",historyEvent)
        documentFight(historyEvent)
    elif character2Health > character1Health:
        historyEvent = f"{character2Name} has won the fight against {character1Name}"
        messagebox.showinfo("Fight Results",historyEvent)
        documentFight(historyEvent)
    else:
        historyEvent = f"The fight between {character1Name} and {character2Name} ended in a draw"
        messagebox.showinfo("Fight Results",historyEvent)
        documentFight(historyEvent)

def updateStats():
    statsText.config(state=tk.NORMAL)
    statsText.delete('1.0',tk.END)
    for name, character in characters.items():
        statsText.insert(tk.END,character.displayStats() + "\n\n")
    statsText.config(state=tk.DISABLED)

def documentFight(historyEvent):
    history.append(historyEvent)
    historyText.config(state=tk.NORMAL)
    historyText.delete('1.0',tk.END)
    for event in history:
        historyText.insert(tk.END,event + "\n\n")
    historyText.config(state=tk.DISABLED)

def onTrainButtonClick():
    name = charNameEntry.get()
    attribute = attributeEntry.get()
    trainCharacterCall(name,attribute)
    updateStats()

def onShowStatsButtonClick():
    name = charNameEntry.get()
    displayStatsCall(name)
    updateStats()

def createCharacter(name):
    character = Character(name)
    character.stats()
    characters[name] = character
    updateStats()

def onCreateCharacterClick():
    name = createCharacterEntry.get()
    createCharacter(name)

def onFightButtonClick():
    character1 = oneVOneEntry1.get()
    character2 = oneVOneEntry2.get()
    oneVOne(character1,character2)

#GUI
root = tk.Tk()
root.title("Fighting Game")

labelCharName = tk.Label(root, text = "Character Name:")
labelCharName.grid(row=0,column=0,padx=5,pady=5)

charNameEntry = tk.Entry(root)
charNameEntry.grid(row=0,column=1,padx=5,pady=5)

labelAttribute = tk.Label(root, text = "Attribute:")
labelAttribute.grid(row=1,column=0,padx=5,pady=5)

attributeEntry = tk.Entry(root)
attributeEntry.grid(row=1,column=1,padx=5,pady=5)

createCharacterLabel = tk.Label(root, text = "Create Character")
createCharacterLabel.grid(row=3,column=0,padx=5,pady=5)

createCharacterEntry = tk.Entry(root)
createCharacterEntry.grid(row=3,column=1,padx=5,pady=5)

oneVOneLabel = tk.Label(root, text="Hold a one vs one fight")
oneVOneLabel.grid(row=0,column=3,padx=5,pady=5)

oneVOneEntry1 = tk.Entry(root)
oneVOneEntry1.grid(row=0,column=4,padx=5,pady=5)

vsLabel = tk.Label(root, text="vs")
vsLabel.grid(row=0,column=5)

oneVOneEntry2 = tk.Entry(root)
oneVOneEntry2.grid(row=0,column=6,padx=5,pady=5)

showStatsButton = tk.Button(root, text = "Show Character Stats", command=onShowStatsButtonClick)
showStatsButton.grid(row=0,column=2,padx=5,pady=5)

fightButton = tk.Button(root, text="Simulate Fight", command=onFightButtonClick)
fightButton.grid(row=0,column=7,padx=5,pady=5)

trainButton = tk.Button(root, text = "Train", command=onTrainButtonClick)
trainButton.grid(row=1,column=2,padx=5,pady=5)

createCharacterButton = tk.Button(root, text = "Create", command=onCreateCharacterClick)
createCharacterButton.grid(row=3,column=2,padx=5,pady=5)

statsText = tk.Text(root, width=40, height=15)
statsText.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
statsText.config(state=tk.DISABLED)

historyText = tk.Text(root,width=40,height=24)
historyText.grid(row=1,column=4,rowspan=4,columnspan=3,padx=5,pady=5)
historyText.config(state=tk.DISABLED)

spaceLabel = tk.Label(root)
spaceLabel.grid(row=2,column=1)

updateStats()

root.mainloop()

