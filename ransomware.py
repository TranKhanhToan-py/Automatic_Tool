import tkinter as tk
import time
import keyboard
import threading
from time import sleep

def ma():
    remaining = 24 * 3600
    timer_after_id = None
    blink_after_id = None

    def update_timer():
        nonlocal remaining, timer_after_id, timer_label
        if remaining > 0:
            remaining -= 1
            hrs, rem = divmod(remaining, 3600)
            mins, secs = divmod(rem, 60)
            timer_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
            timer_after_id = root.after(1000, update_timer)
        else:
            timer_label.config(text="00:00:00")

    def blink_title():
        nonlocal blink_after_id, title
        current_color = title.cget("fg")
        new_color = "black" if current_color == "red" else "red"
        title.config(fg=new_color)
        blink_after_id = root.after(500, blink_title)

    def hotkey_listener():
        keyboard.wait("windows+space")
        print(f"\n\033[33mĐã đóng cửa sổ\033[0m")
        try:
            root.after(0, safe_destroy)
        except Exception:
            pass

    def safe_destroy():
        nonlocal timer_after_id, blink_after_id
        try:
            if timer_after_id is not None:
                root.after_cancel(timer_after_id)
                timer_after_id = None
        except Exception:
            pass
        try:
            if blink_after_id is not None:
                root.after_cancel(blink_after_id)
                blink_after_id = None
        except Exception:
            pass
        try:
            root.destroy()
        except Exception:
            pass

    def disable_event():
        pass

    sleep(2)
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.bind("<Alt-F4>", lambda e: "break")
    root.title("Ransomware Simulation")
    root.configure(bg="black")
    root.attributes('-fullscreen', True)
    title = tk.Label(root, text="WARNING: YOUR FILES ARE ENCRYPTED",
                     fg="red", bg="black", font=("Arial", 28, "bold"))
    title.pack(pady=40)
    subtitle = tk.Label(root, text="All your important files have been locked by advanced encryption.",
                        fg="red", bg="black", font=("Arial", 14))
    subtitle.pack(pady=10)
    frame_timer = tk.Frame(root, bg="black")
    frame_timer.pack(pady=20)
    label_text = tk.Label(frame_timer, text="YOU HAVE", fg="red", bg="black", font=("Arial", 14, "bold"))
    label_text.grid(row=0, column=0, padx=10)
    timer_label = tk.Label(frame_timer, text="24:00:00", fg="red", bg="black", font=("Arial", 26, "bold"))
    timer_label.grid(row=0, column=1, padx=10)
    label_text2 = tk.Label(frame_timer, text="TO COMPLY!", fg="red", bg="black", font=("Arial", 14, "bold"))
    label_text2.grid(row=0, column=2, padx=10)
    warn = tk.Label(root, text="Failure to follow instructions will result in permanent data loss.",
                    fg="red", bg="black", font=("Arial", 12))
    warn.pack(pady=20)
    frame_box = tk.Frame(root, bg="black")
    frame_box.pack(pady=10)
    btc_box = tk.Label(frame_box, text="Send 0.5 BTC to the address below to receive the decryption key:\n"
                                       "1XxY1234567890AbCdEfGh7kLmN\n"
                                       "After payment, your files will be decrypted.",
                       fg="red", bg="black", font=("Arial", 12), justify="center", bd=2, relief="solid", padx=10, pady=10)
    btc_box.pack()
    btn = tk.Button(root, text="FOLLOW INSTRUCTIONS", bg="red", fg="white", font=("Arial", 14, "bold"))
    btn.pack(pady=40)
    update_timer()
    blink_title()
    threading.Thread(target=hotkey_listener, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    ma()