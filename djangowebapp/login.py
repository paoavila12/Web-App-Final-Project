from tkinter import *
from tkinter import messagebox
from adminWindow import *
import sqlite3  

# -------------------------------
# Database Functions
# -------------------------------
def get_db_connection():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    #conn = sqlite3.connect('assignments.db')
    return conn

def initialize_db():
    # Create the assignments table if it doesn't exist
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            user_type TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to handle login
def login():
    username = login_username.get()
    password = login_password.get()

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        user_type = result[3]  
        messagebox.showinfo("Login Successful", f"Welcome, {username}!\nRole: {user_type}")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        
# Function to open signup window
def open_signup():
    login_window.destroy()  # Close login window
    signup_window()

# Function to handle signup
def signup():
    username = signup_username.get()
    password = signup_password.get()
    user_type = user_type_var.get()  # Get selected user type

    conn = get_db_connection()
    c = conn.cursor()

    # Check if username already exists
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = c.fetchone()

    if existing_user:
        messagebox.showerror("Signup Failed", "Username already exists!")
    else:
        # Insert new user into the database
        c.execute("INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)",
                  (username, password, user_type))
        conn.commit()
        messagebox.showinfo("Signup Successful", f"Account created successfully!\nRole: {user_type}")
        signup_win.destroy()  # Close signup window
        login_gui()  # Reopen login window

    conn.close()

# Login Window
def login_gui():
    global login_window, login_username, login_password

    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("500x500")

    Label(login_window, text="Username").pack()
    login_username = Entry(login_window)
    login_username.pack()

    Label(login_window, text="Password").pack()
    login_password = Entry(login_window, show="*")
    login_password.pack()

    Button(login_window, text="Login", command=login).pack()
    Button(login_window, text="Sign Up", command=open_signup).pack()

    login_window.mainloop()

# Signup Window
def signup_window():
    global signup_win, signup_username, signup_password, user_type_var

    signup_win = Tk()
    signup_win.title("Sign Up")
    signup_win.geometry("500x500")

    Label(signup_win, text="Username:").pack()
    signup_username = Entry(signup_win)
    signup_username.pack()

    Label(signup_win, text="Password:").pack()
    signup_password = Entry(signup_win, show="*")
    signup_password.pack()

    Label(signup_win, text="Select User Type: ").pack()
    user_type_var = StringVar(value="Regular")  # Default to Regular user
    Radiobutton(signup_win, text="Regular User", variable=user_type_var, value="Regular").pack()
    Radiobutton(signup_win, text="Admin", variable=user_type_var, value="Admin").pack()

    Button(signup_win, text="Sign Up", command=signup).pack()
    
    signup_win.mainloop()

# Start the application
initialize_db()
login_gui()
