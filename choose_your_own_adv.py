import random

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.inventory = []
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
    
    def display_inventory(self):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(item)
    
    def __str__(self):
        return f"{self.name} the {self.role}"

class Game:
    def __init__(self):
        self.player = None
    
    def start(self):
        print('''
              

:::'###::::'########::'##::::'##:'########:'##::: ##:'########:'##::::'##:'########::'########:::::'######::::::'###::::'##::::'##:'########:
::'## ##::: ##.... ##: ##:::: ##: ##.....:: ###:: ##:... ##..:: ##:::: ##: ##.... ##: ##.....:::::'##... ##::::'## ##::: ###::'###: ##.....::
:'##:. ##:: ##:::: ##: ##:::: ##: ##::::::: ####: ##:::: ##:::: ##:::: ##: ##:::: ##: ##:::::::::: ##:::..::::'##:. ##:: ####'####: ##:::::::
'##:::. ##: ##:::: ##: ##:::: ##: ######::: ## ## ##:::: ##:::: ##:::: ##: ########:: ######:::::: ##::'####:'##:::. ##: ## ### ##: ######:::
 #########: ##:::: ##:. ##:: ##:: ##...:::: ##. ####:::: ##:::: ##:::: ##: ##.. ##::: ##...::::::: ##::: ##:: #########: ##. #: ##: ##...::::
 ##.... ##: ##:::: ##::. ## ##::: ##::::::: ##:. ###:::: ##:::: ##:::: ##: ##::. ##:: ##:::::::::: ##::: ##:: ##.... ##: ##:.:: ##: ##:::::::
 ##:::: ##: ########::::. ###:::: ########: ##::. ##:::: ##::::. #######:: ##:::. ##: ########::::. ######::: ##:::: ##: ##:::: ##: ########:
..:::::..::........::::::...:::::........::..::::..:::::..::::::.......:::..:::::..::........::::::......::::..:::::..::..:::::..::........::

          
 
                                                                                 
                                                                                  ''')
           
        print("Welcome to the Text Adventure Game!")
        print("----------------------------------")
        self.create_character()
        self.intro_story()
        self.play_game()
    
    def create_character(self):
        name = input("Enter your name: ")
        print("Choose your role:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        role_choice = input("Enter the number corresponding to your choice: ")
        roles = {
            '1': 'Warrior',
            '2': 'Mage',
            '3': 'Rogue'
        }
        if role_choice in roles:
            self.player = Player(name, roles[role_choice])
            print(f"Welcome, {self.player}!")
        else:
            print("Invalid choice. Defaulting to Warrior.")
            self.player = Player(name, 'Warrior')
            print(f"Welcome, {self.player}!")
    
    def intro_story(self):
        print("You find yourself standing at the entrance of a dark cave...")
        print("You hear strange noises coming from inside.")
        print("What do you do?")
        input("Press Enter to continue...")
    
    def play_game(self):
        while True:
            print("\nWhat would you like to do?")
            print("1. Enter the cave")
            print("2. Check inventory")
            print("3. Quit game")
            choice = input("Enter the number corresponding to your choice: ")
            
            if choice == '1':
                self.explore_cave()
            elif choice == '2':
                self.player.display_inventory()
            elif choice == '3':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def explore_cave(self):
        print("You cautiously enter the cave...")
        print("As you move deeper, you see a fork in the path.")
        print("What do you do?")
        input("Press Enter to continue...")
        
        print("1. Go left")
        print("2. Go right")
        choice = input("Enter the number corresponding to your choice: ")
        
        if choice == '1':
            self.go_left()
        elif choice == '2':
            self.go_right()
        else:
            print("Invalid choice. You stand still and think again.")
    
    def go_left(self):
        print("You decide to go left...")
        print("You encounter a small chest hidden in the shadows.")
        print("What do you do?")
        input("Press Enter to continue...")
        
        print("1. Open the chest")
        print("2. Leave it alone")
        choice = input("Enter the number corresponding to your choice: ")
        
        if choice == '1':
            self.open_chest()
        elif choice == '2':
            print("You decide to leave the chest alone and continue your journey.")
        else:
            print("Invalid choice. You move on.")
    
    def go_right(self):
        print("You decide to go right...")
        print("You encounter a fierce monster blocking your path!")
        print("What do you do?")
        input("Press Enter to continue...")
        
        print("1. Fight the monster")
        print("2. Run away")
        choice = input("Enter the number corresponding to your choice: ")
        
        if choice == '1':
            self.fight_monster()
        elif choice == '2':
            print("You turn around and run back to the cave entrance.")
        else:
            print("Invalid choice. The monster approaches...")
            self.fight_monster()  # Default to fighting the monster
    
    def open_chest(self):
        print("You cautiously open the chest...")
        loot = random.choice(['Gold coins', 'Health potion', 'Magical sword'])
        print(f"You found: {loot}!")
        self.player.add_to_inventory(loot)
    
    def fight_monster(self):
        # Simulated combat scenario (very basic)
        monster_health = 10
        player_health = 10
        
        while monster_health > 0 and player_health > 0:
            print(f"Player Health: {player_health}  Monster Health: {monster_health}")
            print("1. Attack")
            print("2. Defend")
            choice = input("Enter the number corresponding to your choice: ")
            
            if choice == '1':
                player_attack = random.randint(1, 6)
                monster_health -= player_attack
                print(f"You attack the monster and deal {player_attack} damage!")
                
                if monster_health <= 0:
                    print("You defeated the monster!")
                    print("You continue deeper into the cave.")
                    self.open_chest()
            elif choice == '2':
                print("You defend against the monster's attack.")
                monster_attack = random.randint(1, 4)
                player_health -= monster_attack
                print(f"The monster attacks you and deals {monster_attack} damage!")
                
                if player_health <= 0:
                    print("You have been defeated...")
                    print("Game over.")
                    break
            else:
                print("Invalid choice. You hesitate and miss your chance to act.")

# Start the game
if __name__ == "__main__":
    game = Game()
    game.start()
