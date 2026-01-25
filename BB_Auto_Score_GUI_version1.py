import tkinter as tk
from tkinter import ttk


# class Player:
#    def __init__(self, name: str, score: int):
#        self.name = name
#        self.score = int(score)  # ensure score is an integer

#    def add_score(self, value: int):
#        self.score += int(value)

#    def __str__(self):
#        return f"Player(name='{self.name}', score={self.score})"

# -----------------------------
# Configuration
# -----------------------------

START_TIME = 60  # countdown start time in seconds


P1_name = str(input("Enter Player 1 Name: "))
P2_name = str(input("Enter Player 2 Name: "))


class App(tk.Tk):
    def __init__(self, root):
        self.root = root
        super().__init__()

        self.title("Cuthbert Baines Bar Billiards Auto-Score")
        self.geometry("500x400")
        self.resizable(False, False)

        # State variables
        self.time_left = START_TIME
        self.P1Score = tk.Var(value=0)
        self.P2Score = tk.Var(value=0)

        # Build UI
        self.create_widgets()
        self.update_timer()

    # -----------------------------
    # UI Layout
    # -----------------------------
    def create_widgets(self):

        # Timer display
        self.timer_label = ttk.Label(
            self, text="Time: 60", font=("Arial", 18)
        )
        self.timer_label.pack(pady=10)

        # Score frame
        score_frame = ttk.Frame(self)
        score_frame.pack(pady=10)

        ttk.Label(score_frame, text=P1_name, font=("Arial", 12)).grid(row=0, column=0, padx=10)
        ttk.Label(score_frame, textvariable=self.P1Score, font=("Arial", 12)).grid(row=0, column=1)

        ttk.Label(score_frame, text=P2_name, font=("Arial", 12)).grid(row=0, column=2, padx=10)
        ttk.Label(score_frame, textvariable=self.P1Score, font=("Arial", 12)).grid(row=0, column=3)

        # Input frame
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=20)

        # User 1 input
        ttk.Label(input_frame, text=P1_name).grid(row=0, column=0, pady=5)
        self.entry_1 = ttk.Entry(input_frame, width=20)
        self.entry_1.grid(row=1, column=0, padx=10)

        self.button_1 = ttk.Button(
            input_frame, text="Submit 1", command=self.on_submit_1
        )
        self.button_1.grid(row=2, column=0, pady=5)

        # User 2 input
        ttk.Label(input_frame, text=P2_name).grid(row=0, column=1, pady=5)
        self.entry_2 = ttk.Entry(input_frame, width=20)
        self.entry_2.grid(row=1, column=1, padx=10)

        self.button_2 = ttk.Button(
            input_frame, text="Submit 2", command=self.on_submit_2
        )
        self.button_2.grid(row=2, column=1, pady=5)

    # -----------------------------
    # Timer Logic
    # -----------------------------
    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.time_left -= 1
            self.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's Up!")

    # -----------------------------
    # Button Callbacks
    # -----------------------------

    def on_submit_1(self):
        try:
            value = int(self.entry_1.get())   # get and convert input
            print("User 1 entered:", value)

        # add entered value to score
            self.P1Score.set(self.P1Score.get() + value)

        # clear input box
            self.entry_1.delete(0, tk.END)

        except ValueError:
            print("Invalid input: please enter an integer")
            self.entry_1.delete(0, tk.END)

    def on_submit_2(self):
        try:
            value = int(self.entry_2.get())   # get and convert input
            print("User 2 entered:", value)

        # add entered value to score
            self.P2Score.set(self.P2Score.get() + value)

        # clear input box
            self.entry_2.delete(0, tk.END)

        except ValueError:
            print("Invalid input: please enter an integer")
            self.entry_2.delete(0, tk.END)


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()
