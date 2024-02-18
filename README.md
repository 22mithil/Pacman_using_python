
# Pac-Man Game
This Python script implements a simple version of the classic Pac-Man game using the Pygame library. Players control Pac-Man and navigate through the game window to eat pellets while avoiding ghosts. The game includes features such as power-ups, vulnerable ghosts, scoring, and a restart option.




## How to Play

Run the Game: Execute the script to start the game window.

Game Start: Click within the window to begin the game.

Controls:
 Use the arrow keys to navigate Pac-Man (right, up, left, down).
Eat yellow pellets to score points.
Avoid ghosts, or consume power-ups to make ghosts vulnerable temporarily.

Game Over:
The game ends when Pac-Man collides with a ghost without a power-up.
Alternatively, the game concludes when all pellets are eaten or all ghosts are defeated.

Restart:
After a game over, click within the window to restart the game.



## Features
- Pac-Man is controlled using arrow keys.
- Ghosts move randomly and can become vulnerable after consuming a power-up.
- Power-ups appear randomly on the screen.
- Scoring system tracks points earned by consuming pellets and defeating ghosts.



## Installation
Pygame library: Ensure Pygame is installed (pip install pygame) before running the script.

```bash
  pip install pygame
```
    
## Game Elements

- Pac-Man: Controlled by the player, eats pellets, and avoids ghosts.
- Ghosts: Move randomly, become vulnerable after power-up consumption.
- Pellets: Yellow dots that Pac-Man consumes for points.
- Power-ups: Cyan circles that make ghosts vulnerable when consumed by Pac-Man.


## Code Structure

- The code uses Pygame to handle game initialization, events, and drawing.
- The game loop continuously updates the game state, handles player input, and manages collisions.
- Ghosts, pellets, and power-ups are represented as dictionaries, each with their specific properties.
## Contributing

Feel free to explore and modify the code to enhance the game or add new features!



