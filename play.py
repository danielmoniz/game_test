#!/usr/bin/env python

import game as Game

game = Game.Game()

def game_loop():
    """The primary loop for the game. Should go as follows:
        a) If the game is over, end the game.
        b) If not, get the current game state.
        c1) Tell the game object to perform its next action.
        c2) Send the current game state to the interface module.
        d) """
    while !game.is_game_over():
        game_state = game.get_game_state()

