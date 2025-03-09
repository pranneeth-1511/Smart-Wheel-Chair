import tkinter as tk

class WheelChairController(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.move_flag = False
        self.create_widgets()

    def create_widgets(self):
        self.pack()
        self.up_button = tk.Button(self, text="Up", command=lambda: self.start_move('Up'))
        self.up_button.pack(side="top")

        self.down_button = tk.Button(self, text="Down", command=lambda: self.start_move('Down'))
        self.down_button.pack(side="top")

        self.left_button = tk.Button(self, text="Left", command=lambda: self.start_move('Left'))
        self.left_button.pack(side="left")

        self.right_button = tk.Button(self, text="Right", command=lambda: self.start_move('Right'))
        self.right_button.pack(side="right")

        self.stop_button = tk.Button(self, text="Stop", command=lambda: self.start_move('Stop'))
        self.stop_button.pack(side="bottom")

    def start_move(self, direction):
        if not self.move_flag:
            self.move_flag = True
            print(f"Moving {direction}")
            self.move_object(direction)

    def stop_move(self, event):
        print("Stopping movement")
        self.move_flag = False

    def move_object(self, direction):
        # Implement your logic to move the object or perform actions based on the direction
        if direction == 'Up':
            print("Moving up")
        elif direction == 'Down':
            print("Moving down")
        elif direction == 'Left':
            print("Moving left")
        elif direction == 'Right':
            print("Moving right")
        elif direction == 'Stop':
            print("Stopping object's movement")
        elif direction == 'Handbrake':
            print("Applying handbrake")

        if self.move_flag:
            # Schedule the next move after 0.1 seconds (100 milliseconds)
            self.after(100, lambda: self.move_object(direction))


root = tk.Tk()
app = WheelChairController(master=root)
app.mainloop()
