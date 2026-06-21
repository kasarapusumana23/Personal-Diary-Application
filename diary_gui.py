from tkinter import *
from tkinter import messagebox
from datetime import datetime

PASSWORD = "Diary@2026"

# ---------------- LOGIN ----------------
def login():
    if password_entry.get() == PASSWORD:
        login_window.destroy()
        open_diary()
    else:
        messagebox.showerror("Error", "Incorrect Password!")

# ---------------- SAVE ENTRY ----------------
def save_entry():
    entry = text_area.get("1.0", END).strip()

    if entry == "":
        messagebox.showwarning("Warning", "Please write something!")
        return

    with open("diary.txt", "a") as file:
        file.write("\n")
        file.write(
            "Date: "
            + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            + "\n"
        )
        file.write(entry + "\n")
        file.write("-" * 40 + "\n")

    messagebox.showinfo("Success", "Entry Saved Successfully!")
    text_area.delete("1.0", END)

# ---------------- VIEW ENTRIES ----------------
def view_entries():
    try:
        with open("diary.txt", "r") as file:
            content = file.read()

        view_window = Toplevel()
        view_window.title("My Diary Entries")
        view_window.geometry("700x500")

        text = Text(view_window, wrap=WORD)
        text.pack(fill=BOTH, expand=True)

        text.insert(END, content)
        text.config(state=DISABLED)

    except FileNotFoundError:
        messagebox.showinfo("Info", "No diary entries found.")

# ---------------- DELETE ENTRIES ----------------
def delete_entries():
    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete all diary entries?"
    )

    if confirm:
        with open("diary.txt", "w") as file:
            pass

        messagebox.showinfo(
            "Success",
            "All diary entries deleted successfully!"
        )

# ---------------- MAIN DIARY WINDOW ----------------
def open_diary():
    global text_area

    diary_window = Tk()
    diary_window.title("Personal Diary Application")
    diary_window.geometry("800x600")

    heading = Label(
        diary_window,
        text="📖 Personal Diary Application",
        font=("Arial", 20, "bold")
    )
    heading.pack(pady=15)

    text_area = Text(
        diary_window,
        height=15,
        width=80,
        font=("Arial", 12)
    )
    text_area.pack(pady=10)

    Button(
        diary_window,
        text="Save Entry",
        command=save_entry,
        width=25,
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    Button(
        diary_window,
        text="View Entries",
        command=view_entries,
        width=25,
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    Button(
        diary_window,
        text="Delete All Entries",
        command=delete_entries,
        width=25,
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    Button(
        diary_window,
        text="Exit",
        command=diary_window.destroy,
        width=25,
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    diary_window.mainloop()

# ---------------- LOGIN WINDOW ----------------
login_window = Tk()
login_window.title("Diary Login")
login_window.geometry("400x250")

Label(
    login_window,
    text="🔒 Personal Diary Login",
    font=("Arial", 16, "bold")
).pack(pady=20)

Label(
    login_window,
    text="Enter Password:",
    font=("Arial", 11)
).pack()

password_entry = Entry(
    login_window,
    show="*",
    width=30
)
password_entry.pack(pady=10)

Button(
    login_window,
    text="Login",
    command=login,
    width=20,
    font=("Arial", 10, "bold")
).pack(pady=10)

login_window.mainloop()