🇷🇺 
Консольный симулятор на Python, вдохновленный недавним событием в Fortnite «Охотники за сокровищами» (Treasure Hunters). Открывайте сундуки и испытайте удачу, чтобы получить ультра-редкие награды! Проект создан для демонстрации того, как работают вероятности и взвешенный случайный выбор в играх.

✨ Особенности
Честная вероятность: У ультра-редких предметов шанс выпадения примерно 1 к 86 000 (как в реальных играх!).

Случайные ивенты: Может внезапно начаться «Treasure Hour», который временно повышает шанс выпадения редких предметов.

Сохранение прогресса: Ваша статистика (открыто сундуков, пережито ивентов) сохраняется локально в файле stats.json.

Безопасный ввод: Игра не вылетит с ошибкой, если вы нажмете не ту клавишу. Встроена защита от случайных нажатий.

Мультиязычность: Полная поддержка русского и английского языков.

Легкий сброс: Хотите начать заново? Используйте команду сброса (с подтверждением, чтобы не нажать случайно).

🚀 Как запустить
Убедитесь, что у вас установлен Python (версия 3.8 или выше).

Склонируйте репозиторий или скачайте файлы.

Откройте терминал в папке с проектом и запустите:

bash
python main.py
🎮 Управление
Enter — Открыть сундук.

r — Сбросить прогресс (потребует подтверждения).

q — Выйти из игры с сохранением прогресса.

📁 Структура проекта
main.py — Основная логика и игровой цикл.

guard.py — Модуль защиты ввода (перехватывает неправильные клавиши).

rewards.json — Содержит все награды, их шансы (веса) и переводы на разные языки.

stats.json — Создается автоматически для хранения вашего прогресса.




 English
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