class Game:
    """The main game class. Holds information about the current game state."""

    def __init__(self):
        """Initialize an empty gamestate."""
        self.players = []
        self.round_number = 0
        self.active_player = 0


# Define a set of functions for modifying and retrieving the game state.
    def end_game(self):
        """End the current game."""
        pass

    def is_game_over(self):
        """Return whether or not the game is over."""
        pass

    def set_player_list(self, player_list):
        """Set the list of players. Input a list of Player objects."""
        pass:

    def get_player_list(self, player_list):
        """Return the list of players in the current game."""
        pass:
    
    def end_turn(self):
        """End the current player's turn."""
        self.turn++
        self.active_player


