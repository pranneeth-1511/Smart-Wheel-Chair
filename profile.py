import tkinter as tk
from tkinter import PhotoImage, Label, Frame
import json
import os

def start():
    root = tk.Tk()
    root.title('User Details')
    root.geometry('925x500+300+200')
    root.configure(bg="#fff")
    root.resizable(False, False)

    #Provide the correct path to your image file
    img = PhotoImage(file=r"D:\Projects\Wheel Chair Project Orginal\images\handbrake.png")
    image_label = Label(root, image=img, bg='white')
    image_label.image = img
    image_label.place(x=50, y=50)

    frame = Frame(root, width=600, height=700, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Profile', fg='#57a1f8', bg='White', font=('Microsoft Yahei UI light', 25, 'bold'))
    heading.place(x=100, y=5)

    # Function to get user details
    def get_user_details(username, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = json.load(file)
                return existing_data.get(username, {})

        return {}  # Return an empty dictionary if the file doesn't exist

    # Specify the full path to your JSON files
    profile_file_path = r'D:\Semester - 3\VS Code\Wheel Chair Project Orginal\user_profile.json'
    data_file_path = r'D:\Semester - 3\VS Code\Wheel Chair Project Orginal\user_data.json'

    # Check if the profile file exists and load the data
    if os.path.exists(profile_file_path):
        with open(profile_file_path, 'r') as file:
            profile_data = json.load(file)

        # Iterate over the profile data and get the details
        for username, _ in profile_data.items():
            user_data = get_user_details(username, data_file_path)

            labels = ["Username:", "Name:", "Age:", "Mobile:", "Email:", "Gender:", "Password:"]
            values = [user_data.get("username", ""),
                      user_data.get("name", ""),
                      user_data.get("age", ""),
                      user_data.get("mobile", ""),
                      user_data.get("email", ""),
                      user_data.get("gender", ""),
                      user_data.get("password", "")]

            for i in range(len(labels)):
                label = Label(frame, text=labels[i], font=('Microsoft Yahei UI light', 12))
                label.place(x=30, y=100 + i * 40)

                value = Label(frame, text=values[i], font=('Microsoft Yahei UI light', 12))
                value.place(x=120, y=100 + i * 40)

    root.mainloop()


start()
