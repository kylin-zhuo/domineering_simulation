README

Background
Domineering is a game invented by Goran Andersson in 1974 under the name of Crosscram but now more known as Domineering since the tile of dominoes are used in the game. The rules are simple and straightforward:  
	a)	Set up a grid of any size. Normally the board is square. In this analysis we may start from simple size and evolve to a more complex one, i.e start from  5x5 board and expand even until 10x10. 
	b)	Both players place a 2×1 block on their turn. Player 1 must place his horizontally and Player 2 places hers vertically.
	c)	The last player to be able to place a block wins the game.

Primary Analysis
Consider the game in two phases: 
	a)	Starting phase 
Because the space is sufficient at the beginning, it appears that we cannot distinguish the performances of the settlements of tiles. As the figure below, the strategy in this phase for both players is to preserve a hole-like space for future move. 

	a)	Middle-to-end phase
Soma fatal mistakes can happen in this phase because the space available becomes complex (normally in the middle) and one fatal mistake may lead to the failure. The most tricky part of calculation should be applied during this phase. 

Solution
The basic knowledge of game playing, or adversarial game search, can be applied to the fundamental analysis of the procedure of small board game of Domineering, such as Minimax algorithms and sub-game perfect theorem.

Since it is an old problem, the solution has been promoted by other researchers especially for the basic cases. For example, the 5x5 board is know to be a second-player win(Conway, 1976). Nevertheless, there is still space for analysis when the board is large enough. 

This code tries to play around with the low-dimensional cases.

Still writing and modifying. Keep update.
