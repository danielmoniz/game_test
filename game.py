import player as playerClass

class Game:
    """The main game class."""
# define commonly used strings and constants
    quit_confirm = """Are you sure you want to quit? y, [n]
"""

    def __init__(self):
        pass

    def get_confirm_input(self, question = "yes (y) or no (n)? ", confirm_answers = ["yes", "y"], decline_answers = ["no", "n"]):
        """Loop until the person puts in an acceptable value. An empty list of acceptable answers indicates that any answer is okay."""
        while 1:
            try:
                user_input = raw_input(question)
                if confirm_answers == []:
                    return user_input
                elif user_input in str(confirm_answers):
                    return 1;
                elif user_input in str(decline_answers):
                    return 0;
                else:
                    print user_input
                    raise ValueError;
            except ValueError:
                print "Bad input!"
                continue



    def get_players(self):
        question = "How many players?\n" 
        num_players = self.get_confirm_input(question, range(1, 4), [])
        players = []
        for i in range(1, num_players + 1):
            print i
            question = "Is player human? "
            is_human = self.get_confirm_input(question)
            if is_human:
                question = "Enter player {0} name: ".format(i)
                name = self.get_confirm_input(question, [], [])
            else:
                name = "Player {0}".format(i)
            player = playerClass.Player(i, name, is_human)
            players.append(player)
                
        return num_players, players
        
    def end_game(self):
        print "Game over!"

    def main(self):
        """The primary game loop."""

# get initial game setup information
        num_players, players = self.get_players()
        print players
        
        while 1:
            cmd = raw_input("Enter a command: ")
            if cmd == "exit" or cmd == "quit" or cmd == "q":
                confirm = raw_input(self.quit_confirm)
                if confirm == "yes" or confirm == "y" or confirm == "q":
                    self.end_game()
                    break
                else:
                    continue
            elif cmd == "q!" or cmd == "qq":
                self.end_game()
                break

            print "Not a command\n"

