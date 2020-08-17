import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("bus management")

connection = sqlite3.connect('management')

BUS_ID = "bus_id"
BUS_NAME = "bus_NAME"
BUS_SEAT = "bus_SEAT"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + BUS_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   BUS_NAME + " TEXT, " + BUS_SEAT + " INTEGER);")

appLabel = tk.Label(root, text="Bus management System", fg="#06a099", width=25)
appLabel.config(font=("times", 20))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(20, 0))

class people:
    Totalpeople = StringVar()
    PeopleName = "people name"
    # Seat number= "seatnumber"
    def __init__ (self, BUS_ID, BUS_SEAT):
            self.__busid = busid
            self._busseat = busseat
        

    nameLabel = tk.Label(root, text="Enter your bus name", width=25, anchor='w',
                        font=("times", 20)).grid(row=1, column=0, padx=(10,0),
                                                    pady=(30, 0))
    seatLabel = tk.Label(root, text="Enter seat number ", width=15, anchor='w',
                            font=("times", 10)).grid(row=1, column=0, padx=(10,0))

    name = tk.name(root, width =25 )
    seat = tk.number(root, width = 15)

    name = Entry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
    number_of_people=Entry.grid(row=2, column=1, padx=(0,10), pady = 20)

    
    
    def takeNameInput():
        sajhayatayat nameEntry, seatnumber
        # Sajhayatayat Nameentry, seatnumber 
        Sajhayatayat list
        sajhayatayat = BUS_NAME, PEOPLE_NAME, SEAT_NUMBER
        Peoplename = nameEntry.get()
        nameEntry.delete(0, tk.END)
        seatnumber = seatnumber.get()
        seatnumber.delete(0, tk.END)



        connection.execute("INSERT INTO " + BUS_NAME + " ( "  + PEOPLE_NAME + ", " + SEAT_NUMBER + ") VALUES ('"+ BUSName + "', "+ str(rollNo) +");")
        connection.commit()
        messagebox.showinfo("Success", "Data Saved Successfully.")


    def destroyRootWindow():
        root.destroy()
        secondWindow = tk.Tk()

        secondWindow.title("Display results")

        appLabel = tk.Label(secondWindow, text="Bus Management System",
                            fg="#06a099", width=50)
        appLabel.config(font=("times", 25))
        appLabel.pack()

        tree = ttk.Treeview(secondWindow)
        tree["columns"] = ("one", "two")

        tree.heading("one", text="people Name")
        tree.heading("two", text="Seat No")
    

        cursor = connection.execute("SELECT * FROM " + BUS_NAME + " ;")
        i = 0

        for row in cursor:
            tree.insert('', i, text="people " + str(row[0]),
                        values=(row[1], row[2]))
            i = i + 1

        tree.pack()
        secondWindow.mainloop()


    # def printDetails():
    #     for singleItem in list:
    #         print("bus name is: sajayatayat name is:%40 total number of people is:%1 to 40 seat number is: 
    #               (singleItem.busName, singleItem.seatnumber, singleItem.peoplename,.))
    #         print("****************************************")

    button = tk.Button(root, text="Save", command=lambda :takeNameInput())
    button.grid(row=5, column=0, pady=30)

    displayButton = tk.Button(root, text="Display bus management", command=lambda :destroyRootWindow())
    displayButton.grid(row=5, column=1)

    root.mainloop()