# 2048 — A 2048 simulator with a GUI

A lightweight 2048 game simulator with a graphical user interface, implemented in Python. Play the classic 2048 puzzle, experiment with AI/automation, or use the simulator for research and teaching.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Configuration](#configuration)
- [Credits](#credits)
- [Contact](#contact)

## Features
- Classic 4x4 2048 gameplay (configurable grid support)
- Clean, minimal GUI for playing and observing moves
- Keyboard controls and optional automated play mode
- Option to log games for analysis or training agents
- Lightweight and easy to extend for experiments

## Requirements
- Python 3.8+ (recommended)
- pip
- tkinter (bundled with Python)
- random (also bundled with Python)

## Installation
Clone the repository:
```bash
git clone https://github.com/TurtleManPurple/2048.git
cd 2048
```

Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

## Usage
Start the GUI (adjust the command to the actual entrypoint, e.g. `main.py` or a module):
```bash
python main.py
# or
python -m 2048
```

Optional command-line flags (examples — update to match your implementation):
```bash
# start with a specific board size
python main.py --size 4

# run in automated mode (AI plays)
python main.py --auto --episodes 100
```

## Controls
- Arrow keys or WASD: move tiles (Up, Down, Left, Right)
- R: restart game
- U: undo last move (if implemented)
- Q or Esc: quit

(Adjust controls to your implementation.)

## Configuration
If your simulator supports configuration (grid size, seed, AI settings), place examples or a sample config file here, e.g. `config.yaml` or command-line examples.

## Credits
- Inspired by the original 2048 game by Gabriele Cirulli.
- Forked from @mattbatwings's 2048 simulator
- UI ideas and gameplay mechanics adapted for Python.

## Contact
Maintainer: TurtleManPurple  
Repository: https://github.com/TurtleManPurple/2048
