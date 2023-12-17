import time
import tkinter as tk

WINDOW = (200, 100)


class App(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initUI()
        self.timer_update()

    def initUI(self):
        self.root.geometry(f"{WINDOW[0]}x{WINDOW[1]}")
        self.root.title("Stop Watch")

        self.timer = None
        self.start = None
        self.end = None
        self.run = False

        self.time_display = tk.Label(self.root, text="Ready?")
        self.time_display.pack()

        self.but = tk.Button(
            self.root, text="Start", command=self.switch, width=50, height=25
        )
        self.but.pack()

    def timer_update(self):
        if self.timer is None:
            self.timer = time.time()
        if self.run:
            self.timer = time.time() - self.start
            self.time_display.config(
                text=str(time.strftime("%H:%M:%S", time.gmtime(self.timer)))
            )
            but_text = "Stop"
        else:
            but_text = "Start"

        self.but.config(text=but_text)
        self.root.after(100, self.timer_update)

    def switch(self):
        self.start = time.time()
        self.run = False if self.run else True
        if not self.run:
            self.timer = None


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
