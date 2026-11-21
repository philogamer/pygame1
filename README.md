# LOST SOUL

A top-down action game made with pygame. Fight ghosts, slimes and bosses, level up, and build your character through passive skills. Survive as many waves as you can.
<img width="1875" height="1023" alt="image" src="https://github.com/user-attachments/assets/9b8d2898-6f06-4bfd-9b36-4d8f7e173faf" />

## HOW THIS WAS MADE
This project was made with Python and pygame and pixilart. It uses:
- Procedurally generated maps with doors and walls
- Enemy AI that wanders, chases the player and shoots or leaves slime trails
- A boss fight every 5 waves
- A reward system (health, develop, gamble) after each boss
- Pixilart to draw assets (all assets I draw with my own)

## Project structure
- `main.py`: game loop, runs every frame
- `information.py`: classes (Player, Creep, Boss, Bullet, ...) and all on-screen text
- `function.py`: game logic (map generation, enemy AI, combat, bosses, rewards)
- `dictionary.py`: maps game stages and states to the functions that handle them

## Controls
- **W A S D**: move
- **Left / Right arrow**: slash left or right
- **Mouse click**: spend level-up points, choose a reward after a boss
- **Pause button** (bottom-right corner): pause and view your passive skills (from release 2.0)
- **P**: start the game from the title screen
- **T**: skip to the test room in the tutorial
- **K**: skip the tutorial and go to the game
- **G**: go back to the tutorial from the test room
- **R**: replay after death

## How to run
1. Go to the **Releases** section and choose a release.
2. Download the zip or rar file.
3. Extract it, open the `dist` folder, and run the `.exe` file.

## Remind
Each release has its own Readme so read that

## AI DISCLOSURE
I used AI to help balance the stats and the math around them, such as how enemy first stats and increase scale with waves, player stats, mana costs, and passive skill values.
