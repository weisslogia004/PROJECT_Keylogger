# Real-Time Keylogger and Click Logger GUI

### Created by **Agniv Haldar**

This project includes two main components:
1. A **Real-Time Keylogger with GUI** using `tkinter` and `pynput`, with mouse click tracker.
2. A simple **Flask web application** for user registration and login.

---

## 🚀 Features

- ✅ Real-time keystroke logging
- ✅ Mouse click position tracking (with coordinates and button)
- ✅ GUI display using `tkinter`
- ✅ Auto-updates every 500ms to show latest input
- ✅ Lightweight and easy to run
- ✅ Clears buffer intelligently (e.g., on Enter)
- ✅ Handles special keys (Backspace, Arrows, Ctrl, etc.)

---

### 📂 Files

#### 🧩 Keylogger + GUI
- `keylogger_final.py` — Real-time keylogger and click logger with GUI
- `log.txt` — Automatically generated file containing keystrokes and mouse click logs

#### 🌐 Flask Web App
- `sim2.py` — Flask server with registration and login logic
- `templates/register.html` — HTML form for user registration
- `templates/login.html` — HTML form for user login

---

## 🛠️ Requirements

- Python 3.x
- Modules:
  - `pynput`
  - `tkinter` (comes built-in with Python)

