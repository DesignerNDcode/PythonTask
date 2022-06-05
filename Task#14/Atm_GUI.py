import tkinter as tk
from tkinter import ttk

import mysql.connector as sq
from tkinter import messagebox
import time as dt

screen1 = tk.Tk()
screen1.config(background="white")
screen1.resizable(False, False)

# screen1 centering
screen_width = screen1.winfo_screenwidth()
screen_height = screen1.winfo_screenheight()

w_width = 300
w_height = 500

center_x = int(screen_width / 2 - w_width / 2)
center_y = int(screen_height / 2 - w_height / 2)

screen1.geometry(f'{w_width}x{w_height}+{center_x}+{center_y}')

# screen1 centering

# Header
photo = tk.PhotoImage(file=r'Image.png')

screen1.iconphoto(False, photo)
image_label = ttk.Label(
    screen1,
    image=photo,
    padding=5,
    background="white"
)

image_label.pack()

Label = ttk.Label(screen1,
                  text="PTM (Transfer Cash with ease)",
                  font=("MS Sans Serif", 15), background="white", padding=15)
Label.pack()


# Header

def log():
    global screen2
    db = sq.connect(host="localhost", user="root", password="samosamo", database="muhaimin")
    cursor = db.cursor()

    cursor.execute("Select * From dp ")
    dp_am = cursor.fetchall()
    print(dp_am)

    cursor.execute("Select * From wd ")
    wd_am = cursor.fetchall()
    print(wd_am)

    account = int(ac1.get())
    pin = int(mpin1.get())

    # acc match
    cursor.execute("Select acn From ac ")
    a = cursor.fetchall()
    print(a)

    for i in a[0]:
        print(i)
        print(account)

        # acc match

        # mpin match

        cursor.execute("Select mpin From ac ")
        b = cursor.fetchall()
        print(b)

        for j in b[0]:
            print(j)
            print(pin)

            # mpin match

            if account == i and pin == j:
                messagebox.showinfo("showinfo", "LoggedIn")
                screen1.destroy()
                screen2 = tk.Tk()
                screen2.config(background="white")
                screen2.resizable(False, False)
                # screen1 centering
                screen_width1 = screen2.winfo_screenwidth()
                screen_height1 = screen2.winfo_screenheight()

                w_width1 = 300
                w_height1 = 500

                center_x1 = int(screen_width1 / 2 - w_width1 / 2)
                center_y1 = int(screen_height1 / 2 - w_height1 / 2)

                screen2.geometry(f'{w_width1}x{w_height1}+{center_x1}+{center_y1}')

                screen2.title("PTM (Transfer Cash with ease)")

                # screen1 centering

                # Header

                Label1 = ttk.Label(screen2,
                                   text="PTM (Transfer Cash with ease)",
                                   font=("MS Sans Serif", 15), background="white", padding=25)
                Label1.pack()

                # Header

                # amount
                am = ttk.Label(screen2, text="Enter Your Amount", background="white")
                am.pack()

                am1 = tk.Entry(screen2, width=40)
                am1.pack(padx=8, pady=8)
                am1.insert(0, "Enter Your Amount")
                am1.config(state="disabled")

                def p_holder3(event):
                    am1.config(state="normal")
                    am1.delete(0, 'end')

                am1.bind('<Button-1>', p_holder3)

                # amount

                # button
                ex = tk.Button(screen2, text="Exit", borderwidth=0 , cursor="hand2", background="white", command=lambda: quit())
                img = tk.PhotoImage(file="ex_btn.png")
                ex.config(image=img)
                ex.pack(padx=15, pady=15)  # Displaying the button

                # button

                def deposit():
                    # bal
                    cursor.execute("Select c_am From ac ")
                    cbl = cursor.fetchall()

                    for bal in cbl[0]:
                        amount = int(am1.get())
                        n_bal = bal + amount
                        print(n_bal)

                        sql = "UPDATE ac SET c_am = %s WHERE c_am = %s"
                        val = (n_bal, bal)

                        cursor.execute(sql, val)

                        db.commit()
                        print(cursor.rowcount, "record(s) affected")

                        dp_am = ttk.Label(screen2, text=f"your new balance is {n_bal}", padding=8, background="white")
                        dp_am.pack()

                        now = dt.strftime('%Y-%m-%d %H:%M:%S')
                        sql = "INSERT INTO dp (dp_am, date) VALUES (%s, %s)"
                        val = (amount, now)
                        cursor.execute(sql, val)

                        db.commit()

                        print(cursor.rowcount, "record inserted.")

                # button
                DP_button = tk.Button(screen2, borderwidth=0 , cursor="hand2", background="white",  text="Deposit Amount", command=deposit)
                img1 = tk.PhotoImage(file="dp_btn.png")
                DP_button.config(image=img1)
                DP_button.pack(padx=15, pady=15)  # Displaying the button

                # button

                def withdraw():
                    # bal
                    cursor.execute("Select c_am From ac ")
                    cbl = cursor.fetchall()

                    for bal in cbl[0]:
                        amount = int(am1.get())
                        n_bal = bal - amount
                        print(n_bal)

                        sql = "UPDATE ac SET c_am = %s WHERE c_am = %s"
                        val = (n_bal, bal)

                        cursor.execute(sql, val)

                        db.commit()
                        print(cursor.rowcount, "record(s) affected")

                        wd_am = tk.Label(screen2, text=f"your new balance is {n_bal}",pady=8,padx=8, borderwidth=0 , cursor="hand2", background="white",)
                        wd_am.pack()

                        now = dt.strftime('%Y-%m-%d %H:%M:%S')
                        sql = "INSERT INTO wd (date, wd_am) VALUES (%s, %s)"
                        val = (now, amount)
                        cursor.execute(sql, val)

                        db.commit()

                        print(cursor.rowcount, "record inserted.")

                # button
                WD_button = tk.Button(screen2,  borderwidth=0 , cursor="hand2", background="white", text="Withdraw Amount", command=withdraw)
                img2 = tk.PhotoImage(file="wd_btn.png")
                WD_button.config(image=img2)
                WD_button.pack(padx=15, pady=15)  # Displaying the button

                # button

                # bal
                def c_bal():
                    # bal
                    cursor.execute("Select c_am From ac ")
                    cbl = cursor.fetchall()

                    for bal in cbl[0]:
                        am_c = ttk.Label(screen2, text=f"your balance is {bal}", padding=8, background="white")
                        am_c.pack()

                # button
                CB_button = tk.Button(screen2 , borderwidth=0, cursor="hand2", background="white", text="Check balance Amount", command=c_bal)
                img3 = tk.PhotoImage(file="cb_btn.png")
                CB_button .config(image=img3)
                CB_button .pack(padx=15, pady=15)  # Displaying the button
                # button




            else:
                messagebox.showwarning("showwarning", "Wrong credentials")

    screen2.mainloop()


# Email
ac = ttk.Label(screen1, text="Enter Your Account Number", background="white")
ac.pack()

ac1 = tk.Entry(screen1, width=40)
ac1.pack(padx=8, pady=8)
ac1.insert(0, "Enter Your Account Number")
ac1.config(state="disabled")


def p_holder(event):
    ac1.config(state="normal")
    ac1.delete(0, 'end')


ac1.bind('<Button-1>', p_holder)

# Email

mpin = ttk.Label(screen1, text="Enter Your PIN", background="white")
mpin.pack()

mpin1 = tk.Entry(screen1, width=40, show='*')
mpin1.pack(padx=8, pady=8)

mpin1.insert(0, "Enter Your PIN")
mpin1.config(state="disabled")


def p_holder1(event):
    mpin1.config(state="normal")
    mpin1.delete(0, 'end')


mpin1.bind('<Button-1>', p_holder1)

# button
button = ttk.Button(screen1, text="Click me!", command=log)
img = tk.PhotoImage(file="btn1.png")
button.config(image=img)
button.pack()  # Displaying the button
# button

screen1.title("PTM (Transfer Cash with ease)")
screen1.mainloop()
