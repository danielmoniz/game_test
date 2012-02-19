import player

class Game:
    """The main game class."""
# define commonly used strings and constants
    quit_confirm = """Are you sure you want to quit? y, [n]
"""

    def __init__(self):
        pass

    def get_confirm_input(question = "yes (y) or no (n)? ", confirm_answers = ["yes", "y"], decline_answers = ["no", "n"]):
        """Loop until the person puts in a frigging integer"""
        while 1:
            try:
                user_input = int(raw_input(question))
                if user_input in confirm_answers:
                    return 1;
                elif user_input in decline_answers:
                    return 0;
                else:
                    raise ValueError;
            except ValueError:
                print "Bad input!"
                continue



    def get_players(self):
        question = "How many players?\n" 
        num_players = self.get_confirm_input(question, range(1, 4), [])
        players = []
        for i in range(1, num_players + 1):
            question = "Is player human?"
            is_human = self.get_confirm_input(question)
            if is_human:
                name = self.get_confirm_input("Enter player name: ")
                player = player.Player()
                players.append(player)
                
                


        return num_players, players
        
    def end_game(self):
        print "Game over!"

    def main(self):
        """The primary game loop."""

# get initial game setup information
        num_players, players = self.get_players()
        
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

