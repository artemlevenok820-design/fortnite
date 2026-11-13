
A console-based Python simulator inspired by the recent Fortnite "Treasure Hunters" event. Open chests and try your luck to get ultra-rare rewards! This project was created to demonstrate how probability and random weighted choices work in games.

✨ Features
Weighted Randomness: Ultra-rare items have a 1-in-86,000 chance (just like in real games!).

Random Events: A "Treasure Hour" can trigger randomly, temporarily boosting the drop rate of rare items.

Progress Saving: Your stats (chests opened, events survived) are saved locally in stats.json.

Safe Input: The game won't crash if you press the wrong keys. Built-in anti-frustration protection.

Multi-language: Fully playable in both English and Russian.

Easy Reset: Want to start over? Use the reset command with a confirmation prompt.

🚀 How to Run
Make sure you have Python installed (version 3.8 or higher).

Clone this repository or download the files.

Open a terminal in the project folder and run:

bash
python main.py
🎮 Controls
Enter — Open a chest.

r — Reset your progress (requires confirmation).

q — Quit the game and save progress.

📁 Project Structure
main.py — The core game logic and loop.

guard.py — Input protection module (catches invalid keys).

rewards.json — Contains all chest rewards, drop weights, and language translations.

stats.json — Automatically created to store your progress.
