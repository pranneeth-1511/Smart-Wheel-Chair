import json
import os
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
# Create a dictionary to store username and password pairs
user_data = {}
user_name = ""
def open_registration():
    reg_window = Toplevel(root)
    reg_window.title('Registration')
    reg_window.geometry('350x400+400+200')
    global name_entry, age_entry, email_entry, mobile_entry, gender_var, username_entry, password_entry

    def register_user():
        name = name_entry.get()
        age = age_entry.get()
        email = email_entry.get()
        mobile = mobile_entry.get()
        gender = gender_var.get()
        username = username_entry.get()
        password = password_entry.get()

        if not (name and age and email and mobile and gender and username and password):
            messagebox.showwarning("Warning", "Please fill all the details.")
        else:
            file_path = 'user_data.json'
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    existing_data = json.load(file)
            else:
                existing_data = {}

            if username in existing_data and existing_data[username]['name'] == name:
                messagebox.showwarning("Warning", "The Username already exists. Please change it.")

            elif username in existing_data and existing_data[username]['email'] == email:
                messagebox.showwarning("Warning", "Existing Email ID. ")

            elif username in existing_data and existing_data[username]['mobile'] == mobile:
                messagebox.showwarning("Warning", "Existing Mobile Number ID. ")

            else:
                # Update the existing data with new data instead of overwriting it

                existing_data[username] = {
                    'username': username,
                    'name': name,
                    'age': age,
                    'email': email,
                    'mobile': mobile,
                    'gender': gender,
                    'password': str(password),  # Convert password to string
                }
                with open(file_path, 'w') as file:
                    json.dump(existing_data, file, indent=4)
                messagebox.showinfo("Registration", "Registration successful")
                reg_window.destroy()


    Label(reg_window, text="Username", bg="#fff").grid(row=0, column=0, padx=10, pady=10)
    username_entry = Entry(reg_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(reg_window, text="Password", bg="#fff").grid(row=1, column=0, padx=10, pady=10)
    password_entry = Entry(reg_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(reg_window, text="Name", bg="#fff").grid(row=2, column=0, padx=10, pady=10)
    name_entry = Entry(reg_window)
    name_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(reg_window, text="Age", bg="#fff").grid(row=3, column=0, padx=10, pady=10)
    age_entry = Entry(reg_window)
    age_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(reg_window, text="Gender", bg="#fff").grid(row=4, column=0, padx=10, pady=10)
    gender_var = StringVar(reg_window)
    gender_var.set("Male")
    gender_choices = {"Male", "Female"}
    gender_dropdown = OptionMenu(reg_window, gender_var, *gender_choices)
    gender_dropdown.grid(row=4, column=1, padx=10, pady=10)

    Label(reg_window, text="Mobile Number", bg="#fff").grid(row=5, column=0, padx=10, pady=10)
    mobile_entry = Entry(reg_window)
    mobile_entry.grid(row=5, column=1, padx=10, pady=10)

    Label(reg_window, text="Email", bg="#fff").grid(row=6, column=0, padx=10, pady=10)
    email_entry = Entry(reg_window)
    email_entry.grid(row=6, column=1, padx=10, pady=10)

    # Button to submit the registration form
    submit_button = Button(reg_window, text="Submit", command=register_user)
    submit_button.grid(row=7, columnspan=2, padx=10, pady=10)


def login():
    global user, code, root, user_name  # Add user_name to the global variables
    user_name = user.get()  # Store the value in the global variable user_name
    username = user_name  # Rename the variable to username
    password = str(code.get())
    file_path = 'user_data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
            if username in existing_data and existing_data[username]['password'] == password:

                # Displaying the user details in the code entry
                user_details = existing_data[username]
                code.delete(0, END)  # Clear the code entry
                code.insert(0, user_details['password'])  # Insert the password in the code entry
                messagebox.showinfo("Login", "Login successful")

                # Store user data in user_profile.json
                user_profile_path = 'user_profile.json'
                if os.path.exists(user_profile_path):
                    with open(user_profile_path, 'r') as profile_file:
                        profile_data = json.load(profile_file)
                else:
                    profile_data = {}

                # Remove all other data from the user_profile.json file
                profile_data = {username: {
                    'username': username,
                    'password': password
                }}

                with open(user_profile_path, 'w') as profile_file:
                    json.dump(profile_data, profile_file, indent=4)

                root.destroy()  # Destroy the login window
                open_main_window()  # Open the main application window

            else:
                messagebox.showerror("Login", "Invalid username or password")
    else:
        messagebox.showerror("Login", "User data file not found")



def open_main_window():
    from menu import mainpage
    mainpage()
    # Start the main loop
    #main_window.mainloop()
def start():
    global user, code, user_name
    img = PhotoImage(file=r"images/right button.png")
    image_lable = Label(root, image=img, bg='White')
    image_lable.image = img
    image_lable.place(x=50,y=50)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Log in', fg='#57a1f8', bg='White', font=('Microsoft Yahei UI light', 25, 'bold'))
    heading.place(x=100, y=5)

    

    def on_enter_user(e):
        user.delete(0, 'end')

    def on_leave_user(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='White', font=('Microsoft Yahei UI light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter_user)
    user.bind('<FocusOut>', on_leave_user)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter_code(e):
        code.delete(0, 'end')

    def on_leave_code(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(frame, show='*', width=25, fg='black', border=0, bg='White', font=('Microsoft Yahei UI light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter_code)
    code.bind('<FocusOut>', on_leave_code)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    Button(frame, width=39, pady=7, text='Log in', bg='#57a1f8', fg='White', border=0, command=login).place(x=35, y=204)

    label = Label(frame, text="Do you Have Account?", fg='black', bg='White', font=('Microsoft Yahei UI light', 9))
    label.place(x=50, y=270)

    Register = Button(frame, width=6, text='Register', border=0, bg='White', cursor='hand2', fg='#57a1f8', command=open_registration)
    Register.place(x=215, y=270)
    print(user_name)
start()


root.mainloop()
