# Pipso Digital Pet 🐾

A fun, interactive terminal-based digital pet game built with Python! Adopt Pipso and take care of them by managing their hunger, energy, and boredom levels.

## Features ✨

- **Interactive Gameplay**: Feed and play with your digital pet in real-time
- **Dynamic Emotions**: Pipso's mood changes based on their needs (Happy, Sad, Angry, Bored, Glorp)
- **Cute Expressions**: Each emotion has a unique ASCII face expression
- **Stat Management**: 
  - Hunger: Increases over time; feed your pet to satisfy them
  - Energy: Decreases with activity and time; increases when fed
  - Boredom: Increases over time; playing reduces boredom
- **Spell-Checking**: Uses the enchant library to validate food items are real words

## Requirements 📋

- Python 3.x
- `enchant` library (for spell-checking)

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/gabrielworgul-prog/Pipso-Digital-Pet.git
cd Pipso-Digital-Pet
```

2. Install required dependencies:
```bash
pip install enchant
```

## How to Play 🎮

Run the game:
```bash
python main.py
```

### Commands

- **feed** - Feed your Pipso a food item (must be a valid English word)
- **play** - Play with your Pipso to reduce boredom (costs 10 energy)
- **none** - Do nothing this turn

### Game Loop

- Every 5 seconds, your Pipso's stats update
- Hunger increases, boredom increases, and energy decreases naturally
- Monitor your pet's emotional state by their facial expression
- Keep your pet happy by balancing food, play, and rest!

## Emotion States 😊

| Emotion | Expression | Cause |
|---------|-----------|-------|
| Happy | °ω° | Good balance of stats |
| Sad | °̆ ︿ °̆ | Very low energy (≤20) |
| Angry | ಠ╭╮ಠ | Low energy (<50) |
| Bored | -_- | High boredom (≥30) |
| Glorp | ◉_◉ | Extremely hungry (≥100) |

## Project Structure 📁

```
Pipso-Digital-Pet/
├── main.py           # Main game file with Pipso class
├── README.md         # This file
└── LICENSE           # GNU General Public License v3.0
```

## License 📜

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**. 

In simple terms:
- ✅ You can **use, modify, and distribute** this project freely
- ✅ You can **use it commercially**
- ⚠️ If you distribute or modify this project, you must also release your changes under GPLv3
- ⚠️ You must include a copy of the license and state what changes you made
- ⚠️ You must provide access to the source code

For the full legal details, see the LICENSE file.

---

Have fun with your Pipso! 🎉
