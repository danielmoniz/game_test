class Player:
    """Describes each player in the game. A player can be human or AI controlled."""
    
    def __init__(self, player_num, name = "N/A", human = 1):
        self.human = human
        self.name = name
        self.player_num = player_num
