import tkinter as tk
import sys

def mainpage():
    root = tk.Tk()
    root.geometry('300x500')
    root.title('Aqua Clear')

    def show_profile_details():
        try:
            from profile import start
            start()

        except Exception as e:
            print(f"Error in profile page: {e}")

    def show_settings():
        settings_frame = tk.Frame(root, bg="#ffffff")
        settings_frame.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.4)

        settings_label = tk.Label(settings_frame, text="Settings Page", font=('Arial', 12))
        settings_label.pack(padx=10, pady=5, anchor='w')

        back_button = tk.Button(settings_frame, text='Back', command=settings_frame.destroy)
        back_button.pack(pady=10)

    def show_controls():
            try:
                from motor_working_code_orginal import controll
                controll()
            except Exception as e:
                print(f"Error in controls: {e}")

    def logout():
        root.destroy()
        sys.exit(0)

    head_frame = tk.Frame(root, bg='#158aff', highlightbackground='white', highlightthickness=1)

    title_lb = tk.Label(head_frame, text='Aqua Clear', bg='#158aff', fg='white', font=('Bold', 20))
    title_lb.pack(side=tk.LEFT)

    head_frame.pack(side=tk.TOP, fill=tk.X)
    head_frame.pack_propagate(False)
    head_frame.configure(height=50)

    profile_btn = tk.Button(root, text='Profile', font=('Bold', 20), bd=0, bg='#158aff', fg='white',
                            activebackground='#158aff', activeforeground='white', command=show_profile_details)
    profile_btn.place(relx=0.05, rely=0.3)

    settings_btn = tk.Button(root, text='Settings', font=('Bold', 20), bd=0, bg='#158aff', fg='white',
                             activebackground='#158aff', activeforeground='white', command=show_settings)
    settings_btn.place(relx=0.05, rely=0.45)

    controls_btn = tk.Button(root, text='Controls', font=('Bold', 20), bd=0, bg='#158aff', fg='white',
                             activebackground='#158aff', activeforeground='white', command=show_controls)
    controls_btn.place(relx=0.05, rely=0.15)

    logout_btn = tk.Button(root, text='Logout', font=('Bold', 20), bd=0, bg='#158aff', fg='white',
                           activebackground='#158aff', activeforeground='white', command=logout)
    logout_btn.place(relx=0.05, rely=0.6)

    root.mainloop()


if __name__ == "__main__":
    mainpage()
