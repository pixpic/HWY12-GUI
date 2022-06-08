from tkinter import *
import sqlite3
from tkcalendar import *
import datetime
from tkinter_custom_button import TkinterCustomButton
import json
import babel.numbers

root = Tk()
w = 1280
l = 700
root.geometry(("%dx%d" % (w,l)))
root.title("HWY12")
today = datetime.date.today()
current = ""
vin_order = 1
make_order = 1
model_order = 1
year_order = 1
color_order = 1
status_order = 1
from_order = 1
date_order = 1
id_order = 1
root.update()

#response = requests.get("https://vpic.nhtsa.dot.gov/api/")

#root.filename = filedialog.askopenfilename(initialdir="/C/GUI/imgs", title="Select A File", filetypes=())
def sortVin():
    global vin_order
    # Create databases
    conn = sqlite3.connect("titles.db")

    #Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if vin_order == 1:
        vin_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY car_VIN")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY car_VIN DESC")
        vin_order = 1

    records = c.fetchall()
    print_records = ""
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"

            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def sortMake():
    global make_order

    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if make_order == 1:
        make_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY car_make")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY car_make DESC")
        make_order = 1

    records = c.fetchall()
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"
            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    #Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def sortModel():
    global model_order
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if model_order == 1:
        model_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY car_model")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY car_model DESC")
        model_order = 1


    records = c.fetchall()
    print_records = ""
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"
            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def sortYear():
    global year_order
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if year_order == 1:
        year_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY car_year")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY car_year DESC")
        year_order = 1


    records = c.fetchall()
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"

            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def sortColor():
    global color_order
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if color_order == 1:
        color_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY car_color")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY car_color DESC")
        color_order = 1


    records = c.fetchall()
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"

            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def sortStatus():
    global status_order
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if status_order == 1:
        status_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY car_status")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY car_status DESC")
        status_order = 1

    records = c.fetchall()
    print_records = ""
    i = 0
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"

            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def sortFrom():
    global from_order
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if from_order == 1:
        from_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY c_from")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY c_from DESC")
        from_order = 1

    records = c.fetchall()
    print_records = ""
    i = 0
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"

            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def sortDate():
    global date_order
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if date_order == 1:
        date_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY c_date")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY c_date DESC")
        date_order = 1

    records = c.fetchall()
    print_records = ""
    i = 0
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"

            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

def sortId():
    global id_order
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    if id_order == 1:
        id_order = 0
        c.execute("SELECT *, oid FROM info ORDER BY oid")
    else:
        c.execute("SELECT *, oid FROM info ORDER BY oid DESC")
        id_order = 1

    records = c.fetchall()
    print_records = ""
    i = 0
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"

            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

#Re-prints Table Headers
def update():
    # Re-add Table Headers Label
    head1 = Label(frame, text="VIN", font=(16, 16), cursor="hand2")
    head1.grid(column=0, row=3, pady=(0, 15), padx=30)
    head1.bind("<Button-1>", show)

    head2 = Label(frame, text="Make", font=(16, 16), cursor="hand2")
    head2.grid(column=1, row=3, pady=(0, 15), padx=20)
    head2.bind("<Button-1>", show)

    head3 = Label(frame, text="Model", font=(16, 16), cursor="hand2")
    head3.grid(column=2, row=3, pady=(0, 15), padx=20)
    head3.bind("<Button-1>", show)

    head4 = Label(frame, text="Year", font=(16, 16), cursor="hand2")
    head4.grid(column=3, row=3, pady=(0, 15), padx=20)
    head4.bind("<Button-1>", show)

    head6 = Label(frame, text="Title Status", font=(16, 16), cursor="hand2")
    head6.grid(column=4, row=3, pady=(0, 15), padx=20)
    head6.bind("<Button-1>", show)

    head7 = Label(frame, text="From", font=(16, 16), cursor="hand2")
    head7.grid(column=5, row=3, pady=(0, 15), padx=20)
    head7.bind("<Button-1>", show)

    head8 = Label(frame, text="Date In", font=(16, 16), cursor="hand2")
    head8.grid(column=6, row=3, pady=(0, 15), padx=20)
    head8.bind("<Button-1>", show)

    head9 = Label(frame, text="ID", font=(16, 16), cursor="hand2")
    head9.grid(column=7, row=3, pady=(0, 15), padx=20)
    head9.bind("<Button-1>", show)

def print_titles():
    c.execute("SELECT car_vin, car_make, car_model, car_year, car_status, c_from, c_date, oid FROM info")
    records = c.fetchall()
    print_records = ""
    j = 3
    for record in records:
        i = 0
        j += 1
        if i == 5:
            i += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"
            if (i == 0):
                if (j % 2 == 0):
                    query_label = Label(frame, text=print_records, font=(12, 12), bg="lightblue", width=18, height=2,
                                        anchor=CENTER, cursor="hand2")
                    query_label.grid(row=j, column=i)
                    query_label.bind("<Button-1>", show)
                    i += 1
                else:
                    query_label = Label(frame, text=print_records, font=(12, 12), bg="lightskyblue", width=18, height=2,
                                        anchor=CENTER, cursor="hand2")
                    query_label.grid(row=j, column=i)
                    query_label.bind("<Button-1>", show)
                    i += 1
            else:
                if (j % 2 == 0):
                    query_label = Label(frame, text=print_records, font=(12, 12), bg="lightblue", width=15, height=2,
                                        anchor=CENTER, cursor="hand2")
                    query_label.grid(row=j, column=i)
                    query_label.bind("<Button-1>", show)
                    i += 1
                else:
                    query_label = Label(frame, text=print_records, font=(12, 12), bg="lightskyblue", width=15, height=2,
                                        anchor=CENTER, cursor="hand2")
                    query_label.grid(row=j, column=i)
                    query_label.bind("<Button-1>", show)
                    i += 1

#Create Function to Delete A Record
def delete():
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    if not current in "":

        #Delete a record and widgets
        for widget in frame.winfo_children():
            widget.destroy()
        c.execute("DELETE from info WHERE oid = " + current)
        c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME='info'")

        update()
        # Add Widgets/Update
        c.execute("SELECT *, oid FROM info")
        records = c.fetchall()
        j = 3
        for record in records:
            i = 0
            j += 1
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=15)
                query_label.bind("<Button-1>", show)
                i += 1

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

def edit():
    global mid
    global c_vin
    global c_make
    global c_model
    global c_year
    global c_color
    global c_status
    global c_date
    global cal
    global c_from
    global current

    mid = Toplevel()
    mid.title("Edit Entry")
    print(int(current))

    #Creating Calendar
    cal = Calendar(mid, selectmode="day", year=today.year, month=today.month, day=today.day)
    cal.grid(row=5, column=0, columnspan=5)

    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    # Create Text Boxes
    c.execute("SELECT *, oid FROM info")
    records = c.fetchall()
    c_vin = Entry(mid, width=30)
    c_vin.insert(0,(str(records[int(current)][0])))
    c_vin.grid(row=1, column=1, pady=10)

    c_make = Entry(mid, width=30)
    c_make.grid(row=1, column=3, pady=10, padx=10)

    c_model = Entry(mid, width=30)
    c_model.grid(row=2, column=1, pady=10)

    c_year = Entry(mid, width=30)
    c_year.grid(row=2, column=3, pady=10)

    c_color = Entry(mid, width=30)
    c_color.grid(row=3, column=1, pady=10)

    c_status = Entry(mid, width=30)
    c_status.grid(row=3, column=3, pady=10)

    c_from = Entry(mid, width=30)
    c_from.grid(row=4, column=1, pady=10)

    # Create Text Boxes Labels
    c_vin_label = Label(mid, text="VIN")
    c_vin_label.grid(row=1, column=0)

    c_make_label = Label(mid, text="Vehicle Make")
    c_make_label.grid(row=1, column=2, padx=20)

    c_model_label = Label(mid, text="Vehicle Model")
    c_model_label.grid(row=2, column=0, padx=20)

    c_year_label = Label(mid, text="Vehicle Year")
    c_year_label.grid(row=2, column=2)

    c_color_label = Label(mid, text="Vehicle Color")
    c_color_label.grid(row=3, column=0)

    c_status_label = Label(mid, text="Title Status")
    c_status_label.grid(row=3, column=2)

    c_status_label = Label(mid, text="Bought From")
    c_status_label.grid(row=4, column=0)


    # Commit Changes
    conn.commit()

    conn.close()

    submitButton = Button(mid, text="Submit", cursor="hand2", command=submit2)
    submitButton.grid(row=6, column=0, columnspan=5, pady=10, padx=10, ipadx=100)

#Submit New Record
def submit():
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    #Insert Into Table
    c.execute("INSERT INTO info VALUES (:c_vin, :c_make, :c_model, :c_year, :c_color, :c_status , :c_from, :c_date)",
        {
            "c_vin": c_vin.get(),
            "c_make": c_make.get(),
            "c_model": c_model.get(),
            "c_year": c_year.get(),
            "c_color": c_color.get(),
            "c_status": c_status.get(),
            "c_from": c_from.get(),
            "c_date":  cal.get_date()
        })

    c.execute("SELECT *, oid FROM info")

    for widget in frame.winfo_children():
        widget.destroy()

    update()

    records = c.fetchall()

    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"
            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1



    # Commit Changes
    conn.commit()

   #Close Connection
    conn.close()

     #Clear Text Box
    c_vin.delete(0, END)
    c_make.delete(0, END)
    c_model.delete(0, END)
    c_year.delete(0, END)
    c_color.delete(0, END)
    c_status.delete(0, END)

    top.destroy()

def submit2():
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    # Insert Into Table
    conn.execute(
        """UPDATE info SET car_VIN=?, 
        car_make=?, 
        car_model=?, 
        car_year=?, 
        car_color=?, 
        car_status=?, 
        c_from=?, 
        c_date=?
        WHERE ROWID = ?""",
        (c_vin.get(), c_make.get(), c_model.get(), c_year.get(), c_color.get(), c_status.get(), c_from.get(),
         cal.get_date(), int(current)))

    c.execute("SELECT *, oid FROM info")

    for widget in frame.winfo_children():
        widget.destroy()

    update()

    records = c.fetchall()

    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"
            query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
            query_label.grid(row=j, column=i, pady=20, padx=15)
            query_label.bind("<Button-1>", show)
            i += 1

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    # Clear Text Box
    c_vin.delete(0, END)
    c_make.delete(0, END)
    c_model.delete(0, END)
    c_year.delete(0, END)
    c_color.delete(0, END)
    c_status.delete(0, END)

    mid.destroy()


#Creates New Window with New Data
def newVehicle():
    global top
    global c_vin
    global c_make
    global c_model
    global c_year
    global c_color
    global c_status
    global c_date
    global cal
    global c_from

    top = Toplevel()
    top.title("New Entry")

    #Creating Calendar
    cal = Calendar(top, selectmode="day", year=today.year, month=today.month, day=today.day)
    cal.grid(row=5, column=0, columnspan=5)

    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    # Create Text Boxes
    c_vin = Entry(top, width=30)
    c_vin.grid(row=1, column=1, pady=10)

    c_make = Entry(top, width=30)
    c_make.grid(row=1, column=3, pady=10, padx=10)

    c_model = Entry(top, width=30)
    c_model.grid(row=2, column=1, pady=10)

    c_year = Entry(top, width=30)
    c_year.grid(row=2, column=3, pady=10)

    c_color = Entry(top, width=30)
    c_color.grid(row=3, column=1, pady=10)

    c_status = Entry(top, width=30)
    c_status.grid(row=3, column=3, pady=10)

    c_from = Entry(top, width=30)
    c_from.grid(row=4, column=1, pady=10)

    # Create Text Boxes Labels
    c_vin_label = Label(top, text="VIN")
    c_vin_label.grid(row=1, column=0)

    c_make_label = Label(top, text="Vehicle Make")
    c_make_label.grid(row=1, column=2, padx=20)

    c_model_label = Label(top, text="Vehicle Model")
    c_model_label.grid(row=2, column=0, padx=20)

    c_year_label = Label(top, text="Vehicle Year")
    c_year_label.grid(row=2, column=2)

    c_color_label = Label(top, text="Vehicle Color")
    c_color_label.grid(row=3, column=0)

    c_status_label = Label(top, text="Title Status")
    c_status_label.grid(row=3, column=2)

    c_status_label = Label(top, text="Bought From")
    c_status_label.grid(row=4, column=0)

    # Commit Changes
    conn.commit()

    conn.close()

    submitButton = Button(top, text="Submit", cursor="hand2", command=submit)
    submitButton.grid(row=6, column=0, columnspan=5, pady=10, padx=10, ipadx=100)

#For Mouse Clicks
def show(event):
    global current
    current = (event.widget.cget("text"))
    if "VIN" in current:
        sortVin()
    elif "Make" in current:
        sortMake()
    elif "Model" in current:
        sortModel()
    elif "Year" in current:
        sortYear()
    elif "Color" in current:
        sortColor()
    elif "Title Status" in current:
        sortStatus()
    elif "From" in current:
        sortFrom()
    elif "Date In" in current:
        sortDate()
    elif "ID" in current:
        sortId()

def forCar():
    rn = carSearch.get().lower()
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    for widget in frame.winfo_children():
        widget.destroy()

    update()
    c.execute("SELECT *, oid from info")
    records = c.fetchall()

    j = 3
    for record in records:
        i = 0
        j += 1
        if rn in record[0]:
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=15)
                query_label.bind("<Button-1>", show)
                i += 1
        if rn in record[1].lower():
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=30)
                query_label.bind("<Button-1>", show)
                i += 1
        if rn in record[2].lower():
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=30)
                query_label.bind("<Button-1>", show)
                i += 1
        if rn in str(record[3]):
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=30)
                query_label.bind("<Button-1>", show)
                i += 1
        if rn in record[4].lower():
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=30)
                query_label.bind("<Button-1>", show)
                i += 1
        if rn in record[5].lower():
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=30)
                query_label.bind("<Button-1>", show)
                i += 1
        if rn in record[6].lower():
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=30)
                query_label.bind("<Button-1>", show)
                i += 1
        if rn in record[7].lower():
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=30)
                query_label.bind("<Button-1>", show)
                i += 1
        if rn in str(record[8]):
            while i < len(record):
                print_records = (str(record[i])) + "\n"
                query_label = Label(frame, text=print_records, font=(12, 12), cursor="hand2")
                query_label.grid(row=j, column=i, pady=20, padx=30)
                query_label.bind("<Button-1>", show)
                i += 1

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

#For Scrollbar
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=root.winfo_width()*.98, height=root.winfo_height()*.74)

# Code to add widgets will go here...
myLabel = Label(root, text="HWY 12 Titles", font=(30,30))
myLabel.place(x=w/2, y=20, anchor=CENTER)
newCar_btn = TkinterCustomButton(text="Add New Vehicle", corner_radius=0, cursor="hand2", command=newVehicle, border_width=1, border_color="black")
newCar_btn.place(x=w-(w/5), y=30, anchor=N)
carSearch = Entry(root)
carSearch.insert(0,"Please type here")
carSearch.place(x=w-(w/4), y=110, height=30)
carSearch_button =  TkinterCustomButton(text="Enter", corner_radius=0, width=50, cursor="hand2", command=forCar, border_width=1, border_color="black")
carSearch_button.place(x=w-(w/8), y=110)

myframe = Frame(root,relief=GROOVE,width=w,height=l,bd=1)
myframe.place(x=0, y=155)

canvas = Canvas(myframe)
frame = Frame(canvas)
myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0,0), window=frame, anchor='nw')
frame.bind("<Configure>", myfunction)

#Create databases
conn = sqlite3.connect("titles.db")
#Create cursor
c = conn.cursor()

#Create table
c.execute("""CREATE TABLE IF NOT EXISTS info(
    car_VIN text,
    car_make text,
    car_model text,
    car_year integer,
    car_color text,
    car_status text,
    c_from text,
    c_date text
    )""")

update()

# Add Widgets/Update
print_titles()

delete_btn = TkinterCustomButton(text="Delete Vehicle", corner_radius=0, cursor="hand2", command=delete, border_width=1, border_color="black")
delete_btn.place(x=w-(w/5), y=70, anchor=N)

edit_btn = TkinterCustomButton(text="Edit Entry", corner_radius=0, cursor="hand2", command=edit, border_width=1, border_color="black")
edit_btn.place(x=w-(w/10), y=70, anchor=N)

#Commit Changes
conn.commit()
#Close Connection
conn.close()

root.mainloop()
