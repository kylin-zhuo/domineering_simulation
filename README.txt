================================= README =================================

Background

Domineering is a game invented by Goran Andersson in 1974 under the name of Crosscram but now more known as Domineering since the tile of dominoes are used in the game. The rules are simple and straightforward:  

a) 	Set up a grid of any size. Normally the board is square. In this analysis we may start from simple size and evolve to a more complex one, i.e start from  5x5 board and expand even until 10x10. 

b) Both players place a 2×1 block on their turn. Player 1 must place his horizontally and Player 2 places hers vertically.

c) The last player to be able to place a block wins the game.


Solution

The basic knowledge of game playing, or adversarial game search, can be applied to the fundamental analysis of the procedure of small board game of Domineering, such as Minimax algorithms and sub-game perfect theorem.

Since it is an old problem, the solution has been promoted by other researchers especially for the basic cases. For example, the 5x5 board is know to be a second-player win(Conway, 1976). Nevertheless, there is still space for analysis when the board is large enough. 


This code tries to play around with the low-dimensional cases. Still writing and modifying. Keep update. Run “python domineering.py” can play a 4x4 demo. 
