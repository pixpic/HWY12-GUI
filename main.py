from tkinter import *
import sqlite3
from tkcalendar import *
import datetime
import babel.numbers

root = Tk()
root.geometry("1080x720")
root.title("HWY12 DOCS")
today = datetime.date.today()
current = ""
#root.filename = filedialog.askopenfilename(initialdir="/C/GUI/imgs", title="Select A File", filetypes=())

#Create Function to Delete A Record
def delete():
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    if not current in "":
        #Delete a record
        c.execute("DELETE from info WHERE oid = " + current)

    print(current)
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

def submit():
    # Create databases
    conn = sqlite3.connect("titles.db")

    # Create cursor
    c = conn.cursor()

    #Insert Into Table
    c.execute("INSERT INTO info VALUES (:c_vin, :c_make, :c_model, :c_year, :c_color, :c_status , :c_date)",
        {
            "c_vin": c_vin.get(),
            "c_make": c_make.get(),
            "c_model": c_model.get(),
            "c_year": c_year.get(),
            "c_color": c_color.get(),
            "c_status": c_status.get(),
            "c_date":  cal.get_date()
        })

    c.execute("SELECT *, oid FROM info")
    records = c.fetchall()
    # print(records)

    print_records = ""
    i = 0
    j = 3
    for record in records:
        i = 0
        j += 1
        while i < len(record):
            print_records = (str(record[i])) + "\n"
            query_label = Label(root, text=print_records, font=(12, 12))
            query_label.grid(row=j, column=i)
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

    top = Toplevel()
    #vMake = StringVar()
    #vMake.set("Make")
    #make_dd = OptionMenu(top, vMake, *makes)
    # make_dd.pack()

    #Creating Calendar
    cal = Calendar(top, selectmode="day", year=today.year, month=today.month, day=today.day)
    cal.grid(row=4, column=0, columnspan=5)

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

    # Commit Changes
    conn.commit()

    conn.close()

    submitButton = Button(top, text="Submit", command=submit)
    submitButton.grid(row=5, column=0, columnspan=5, pady=10, padx=10, ipadx=100)

def show(event):
    global current
    current = (event.widget.cget("text"))
    print(current)

# Code to add widgets will go here...
myLabel = Label(root, text="HWY 12 Titles", font=(30,30))
myLabel.grid(row=0, column=0, columnspan=10, padx=400)
myLabel.bind("<Button-1>", show)
newCar = Button(root, text="Add new Vehicle", command=newVehicle)


side = Scale(root, from_=0, to=100)
#side.grid(row=2, column=7, rowspan= 3)
newCar.grid(row=1, column=1, columnspan=10, sticky=E)

#Create databases
conn = sqlite3.connect("titles.db")

#Create cursor
c = conn.cursor()

#Create table
#c.execute("""CREATE TABLE info(
 #   car_VIN text,
  #  car_make text,
   # car_model text,
    #car_year integer,
    #car_color text,
    #car_status text,
    #c_date text
     # )""")

#Table Headers Label
head1 = Label(root, text="VIN", font=(16,16))
head1.grid(column=0, row=3, pady=40, padx=40)
head2 = Label(root, text="Make", font=(16,16))
head2.grid(column=1, row=3, padx=30)
head3 = Label(root, text="Model", font=(16,16))
head3.grid(column=2, row=3, padx=30)
head4 = Label(root, text="Year", font=(16,16))
head4.grid(column=3, row=3, padx=30)
head5 = Label(root, text="Color", font=(16,16))
head5.grid(column=4, row=3, padx=30)
head5 = Label(root, text="Title Status", font=(16,16))
head5.grid(column=5, row=3, padx=30)
head6 = Label(root, text="Date In", font=(16,16))
head6.grid(column=6, row=3, padx=30)

# Query the database
c.execute("SELECT *, oid FROM info")
records = c.fetchall()
# print(records)

print_records = ""
i=0
j=3
for record in records:
    i=0
    j+=1
    while i < len(record):
        print_records = (str(record[i])) + "\n"

        query_label = Label(root, text=print_records, font=(12,12))
        query_label.grid(row=j, column=i)
        query_label.bind("<Button-1>", show)
        i+=1

delete_btn = Button(root, text="Delete Profile", command=delete)
delete_btn.grid(row=2, column=0, columnspan=10, pady=(5,0), sticky=E)


#Commit Changes
conn.commit()
#Close Connection
conn.close()

root.mainloop()
