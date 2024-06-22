from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        # variables
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()

        # Establish database connection
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='aldokunaldo123',
            database='crime'
        )
        self.cursor = self.conn.cursor()

        lbl_title = Label(self.root, text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE', font=('times new roman', 40, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0, width=1530, height=70)

        #Logo unila
        img_logo = Image.open('images/Logo UNILA.jpg')
        img_logo = img_logo.resize((60, 60), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=60, y=5, width=60, height=60)

        #img_frame kiri
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=70, width=1530, height=150)

        img1 = Image.open('images/pemuda 1.jpeg')
        img1 = img1.resize((540, 200), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=200)

        #img_frame kanan
        img2 = Image.open('images/pemuda 2.jpeg')
        img2 = img2.resize((540, 160), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=1080, y=0, width=540, height=160)

        #img_frame tengah
        img3 = Image.open('images/pemuda 3.jpeg')
        img3 = img3.resize((540, 160), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=540, y=0, width=540, height=160)

        #Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=0, y=220, width=1530, height=800)

        #Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information', font=('times new roman', 15, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=270)

        #Label Entry

        #Case ID
        caseid = Label(upper_frame, text='Case ID:', font=('arial', 11, 'bold'), bg='white')
        caseid.grid(row=0, column=0, padx=2, sticky=W)

        caseentry = ttk.Entry(upper_frame, textvariable=self.var_case_id, width=22, font=('arial', 11, 'bold'))
        caseentry.grid(row=0, column=1, padx=2, sticky=W)

        #Criminal NO
        lbl_criminal_no = Label(upper_frame, font=('arial', 12, 'bold'), text="Criminal NO:", bg="white")
        lbl_criminal_no.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_criminal_no = ttk.Entry(upper_frame, textvariable=self.var_criminal_no, width=22, font=('arial', 11, 'bold'))
        txt_criminal_no.grid(row=0, column=3, padx=2, pady=7)

        #Criminal Name
        lbl_Name = Label(upper_frame, font=('arial', 12, 'bold'), text="Criminal Name:", bg="white")
        lbl_Name.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=('arial', 11, 'bold'))
        txt_name.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        #Criminal Nickname
        lbl_nickname = Label(upper_frame, font=('arial', 12, 'bold'), text="Nickname:", bg="white")
        lbl_nickname.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_nickname = ttk.Entry(upper_frame, textvariable=self.var_nickname, width=22, font=('arial', 11, 'bold'))
        txt_nickname.grid(row=1, column=3, padx=2, pady=7)

        #Arrest Date
        lbl_arrestDate = Label(upper_frame, font=('arial', 12, 'bold'), text="Arrest Date:", bg="white")
        lbl_arrestDate.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_arrestDate = ttk.Entry(upper_frame, textvariable=self.var_arrest_date, width=22, font=('arial', 11, 'bold'))
        txt_arrestDate.grid(row=2, column=1, padx=2, pady=7)

        #Date Crime
        lbl_dateOfCrime = Label(upper_frame, font=('arial', 12, 'bold'), text="Date Of Crime:", bg="white")
        lbl_dateOfCrime.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_dateOfCrime = ttk.Entry(upper_frame, textvariable=self.var_date_of_crime, width=22, font=('arial', 11, 'bold'))
        txt_dateOfCrime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        #Address
        lbl_address = Label(upper_frame, font=('arial', 12, 'bold'), text="Address:", bg="white")
        lbl_address.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=('arial', 11, 'bold'))
        txt_address.grid(row=3, column=1, padx=2, pady=7)

        #Age
        lbl_age = Label(upper_frame, font=('arial', 12, 'bold'), text="Age:", bg="white")
        lbl_age.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_age = ttk.Entry(upper_frame, textvariable=self.var_age, width=22, font=('arial', 11, 'bold'))
        txt_age.grid(row=3, column=3, padx=2, pady=7)

        #Occupation
        lbl_occupation = Label(upper_frame, font=('arial', 12, 'bold'), text="Occupation:", bg="white")
        lbl_occupation.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_occupation = ttk.Entry(upper_frame, textvariable=self.var_occupation, width=22, font=('arial', 11, 'bold'))
        txt_occupation.grid(row=4, column=1, padx=2, pady=7)

        #Birthmark
        lbl_birthmark = Label(upper_frame, font=('arial', 12, 'bold'), text="Birth Mark:", bg="white")
        lbl_birthmark.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_birthmark = ttk.Entry(upper_frame, textvariable=self.var_birthMark, width=22, font=('arial', 11, 'bold'))
        txt_birthmark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        #Crime Type
        lbl_crimetype = Label(upper_frame, font=('arial', 12, 'bold'), text="Crime Type:", bg="white")
        lbl_crimetype.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_crimetype = ttk.Entry(upper_frame, textvariable=self.var_crime_type, width=22, font=('arial', 11, 'bold'))
        txt_crimetype.grid(row=0, column=5, padx=2, pady=7)

        #Father Name
        lbl_fathername = Label(upper_frame, font=('arial', 12, 'bold'), text="Father Name:", bg="white")
        lbl_fathername.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_fathername = ttk.Entry(upper_frame, textvariable=self.var_father_name, width=22, font=('arial', 11, 'bold'))
        txt_fathername.grid(row=1, column=5, padx=2, pady=7)

        #Gender
        lbl_gender = Label(upper_frame, font=('arial', 12, 'bold'), text="Gender:", bg="white")
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        # Combobox Gender
        combo_gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=("arial", 12, "bold"), width=20, state="readonly")
        combo_gender["value"] = ("Select Option", "Male", "Female")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=5, padx=2, pady=7)

        #Most Wanted
        lbl_wanted = Label(upper_frame, font=('arial', 12, 'bold'), text="Most Wanted:", bg="white")
        lbl_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        # Combobox wanted
        combo_wanted = ttk.Combobox(upper_frame, textvariable=self.var_wanted, font=("arial", 12, "bold"), width=20, state="readonly")
        combo_wanted["value"] = ("Select Option", "Yes", "No")
        combo_wanted.current(0)
        combo_wanted.grid(row=3, column=5, padx=2, pady=7)

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=200, width=1470, height=40)

        # Buttons
        btn_add = Button(button_frame, text="Record Save", command=self.add_data, font=("arial", 13, "bold"), width=14, bg="red", fg="white")
        btn_add.grid(row=0, column=0, padx=3, pady=5)

        btn_update = Button(button_frame, text="Update", command=self.update_data, font=("arial", 13, "bold"), width=14, bg="red", fg="white")
        btn_update.grid(row=0, column=1, padx=3, pady=5)

        btn_delete = Button(button_frame, text="Delete", command=self.delete_data, font=("arial", 13, "bold"), width=14, bg="red", fg="white")
        btn_delete.grid(row=0, column=2, padx=3, pady=5)

        btn_clear = Button(button_frame, text="Clear", command=self.clear_data, font=("arial", 13, "bold"), width=14, bg="red", fg="white")
        btn_clear.grid(row=0, column=3, padx=3, pady=5)

        # Down frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text="Criminal Information Table", font=("times new roman", 11, "bold"), fg="red", bg="white")
        down_frame.place(x=10, y=280, width=1500, height=270)

        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text="Search Criminal Record", font=("times new roman", 11, "bold"), fg="red", bg="white")
        search_frame.place(x=0, y=0, width=1470, height=60)

        # Search by
        search_by = Label(search_frame, font=("arial", 11, "bold"), text="Search By:", bg="red", fg="white")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        self.var_com_search = StringVar()
        combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=("arial", 12, "bold"), width=18, state="readonly")
        combo_search_box["value"] = ("Select Option", "Case_id", "Criminal_no")
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        search_txt = ttk.Entry(search_frame, textvariable=self.var_search, width=18, font=("arial", 13, "bold"))
        search_txt.grid(row=0, column=2, sticky=W, padx=5)

        search_btn = Button(search_frame, text="Search", command=self.search_data, font=("arial", 13, "bold"), width=14, bg="red", fg="white")
        search_btn.grid(row=0, column=3, padx=5)

        showAll_btn = Button(search_frame, text="Show All", command=self.fetch_data, font=("arial", 13, "bold"), width=14, bg="red", fg="white")
        showAll_btn.grid(row=0, column=4, padx=5)

        # Table Frame
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1", text="CaseId")
        self.criminal_table.heading("2", text="CrimeNo")
        self.criminal_table.heading("3", text="CrimeName")
        self.criminal_table.heading("4", text="Nickname")
        self.criminal_table.heading("5", text="ArrestDate")
        self.criminal_table.heading("6", text="DateOfCrime")
        self.criminal_table.heading("7", text="Address")
        self.criminal_table.heading("8", text="Age")
        self.criminal_table.heading("9", text="Occupation")
        self.criminal_table.heading("10", text="BirthMark")
        self.criminal_table.heading("11", text="CrimeType")
        self.criminal_table.heading("12", text="FatherName")
        self.criminal_table.heading("13", text="Gender")
        self.criminal_table.heading("14", text="Wanted")
        self.criminal_table.heading("15", text="ID")

        self.criminal_table["show"] = "headings"

        self.criminal_table.column("1", width=100)
        self.criminal_table.column("2", width=100)
        self.criminal_table.column("3", width=100)
        self.criminal_table.column("4", width=100)
        self.criminal_table.column("5", width=100)
        self.criminal_table.column("6", width=100)
        self.criminal_table.column("7", width=100)
        self.criminal_table.column("8", width=100)
        self.criminal_table.column("9", width=100)
        self.criminal_table.column("10", width=100)
        self.criminal_table.column("11", width=100)
        self.criminal_table.column("12", width=100)
        self.criminal_table.column("13", width=100)
        self.criminal_table.column("14", width=100)
        self.criminal_table.column("15", width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if self.var_case_id.get() == "" or self.var_criminal_no.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                self.cursor.execute("INSERT INTO criminal (Case_id, Criminal_no, name, nickname, arrest_date, date_of_crime, address, age, occupation, birthMark, crime_type, father_name, gender, wanted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (
                                        self.var_case_id.get(),
                                        self.var_criminal_no.get(),
                                        self.var_name.get(),
                                        self.var_nickname.get(),
                                        self.var_arrest_date.get(),
                                        self.var_date_of_crime.get(),
                                        self.var_address.get(),
                                        self.var_age.get(),
                                        self.var_occupation.get(),
                                        self.var_birthMark.get(),
                                        self.var_crime_type.get(),
                                        self.var_father_name.get(),
                                        self.var_gender.get(),
                                        self.var_wanted.get()
                                    ))
                self.conn.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo("Success", "Record has been inserted")
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}")

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM criminal")
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for row in rows:
                self.criminal_table.insert("", END, values=row)
            self.conn.commit()

    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        row = content["values"]
        self.var_case_id.set(row[0])
        self.var_criminal_no.set(row[1])
        self.var_name.set(row[2])
        self.var_nickname.set(row[3])
        self.var_arrest_date.set(row[4])
        self.var_date_of_crime.set(row[5])
        self.var_address.set(row[6])
        self.var_age.set(row[7])
        self.var_occupation.set(row[8])
        self.var_birthMark.set(row[9])
        self.var_crime_type.set(row[10])
        self.var_father_name.set(row[11])
        self.var_gender.set(row[12])
        self.var_wanted.set(row[13])

    def update_data(self):
        if self.var_case_id.get() == "" or self.var_criminal_no.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                self.cursor.execute("UPDATE criminal SET criminal_no=%s, name=%s, nickname=%s, arrest_date=%s, date_of_crime=%s, address=%s, age=%s, occupation=%s, birthMark=%s, crime_type=%s, father_name=%s, gender=%s, wanted=%s WHERE case_id=%s",
                                    (
                                        self.var_criminal_no.get(),
                                        self.var_name.get(),
                                        self.var_nickname.get(),
                                        self.var_arrest_date.get(),
                                        self.var_date_of_crime.get(),
                                        self.var_address.get(),
                                        self.var_age.get(),
                                        self.var_occupation.get(),
                                        self.var_birthMark.get(),
                                        self.var_crime_type.get(),
                                        self.var_father_name.get(),
                                        self.var_gender.get(),
                                        self.var_wanted.get(),
                                        self.var_case_id.get()
                                    ))
                self.conn.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo("Success", "Record has been updated")
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}")

    def delete_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                delete = messagebox.askyesno("Delete Record", "Are you sure you want to delete this record?")
                if delete > 0:
                    self.cursor.execute("DELETE FROM criminal WHERE Case_id=%s", (self.var_case_id.get(),))
                    self.conn.commit()
                    self.fetch_data()
                    self.clear_data()
                else:
                    if not delete:
                        return
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}")

    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select a search option")
        else:
            try:
                self.cursor.execute("SELECT * FROM criminal WHERE " + str(self.var_com_search.get()) + " LIKE '%" + str(self.var_search.get()) + "%'")
                rows = self.cursor.fetchall()
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for row in rows:
                        self.criminal_table.insert("", END, values=row)
                    self.conn.commit()
                else:
                    messagebox.showerror("Error", "No record found")
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
