# LOST SOUL

A dungeon game made with pygame. Fight enemy, level up, and see what will appear. Survive as much as you can and see the reward at the end.
<img width="1875" height="1023" alt="image" src="https://github.com/user-attachments/assets/9b8d2898-6f06-4bfd-9b36-4d8f7e173faf" />

## HOW THIS WAS MADE
This project was made with Python and pygame and pixilart. It has:
- Random maps with doors and walls
- Enemy that wanders, chases the player and shoots or leaves traps
- Boss fight every 5 waves with boss skills
- Reward system (health, develop, gamble) after each boss
- Pixilart to draw assets (all assets I draw with my own)

## Project structure
- `main.py`: main game loop
- `information.py`: classes (Player, Creep, Boss, Bullet, ...) and all on-screen text
- `function.py`: game logic
- `dictionary.py`: the events in game

## Controls
- **W A S D**: move
- **Left / Right arrow**: slash left or right
- **Mouse click**: press any button on screen

## How to run
1. Choose a release.
2. Download the zip or rar file.
3. Extract it, open the `dist` folder, and run the `.exe` file.

## Remind
Each release has its own Readme so read that

## AI DISCLOSURE
I used AI to help balance the stats and the math around them, such as how enemy first stats and increase scale with waves, player stats, mana costs, and passive skill values.
