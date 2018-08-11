import database
from Tkinter import *
import Tkinter as tk
from tkintertable.Tables import TableCanvas
class createTable(tk.Frame): 
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.place(x=0, y=100, relwidth=1, relheight=1)
        # self.grid()
        self.F = tk.Frame(self)
        self.F.grid(sticky=tk.N+tk.S+tk.W)
        # self.F.place(x=10,y=10)
        self.createWidgets()
    def createWidgets(self):
        self.table = TableCanvas(self.F,rows=0,cols=0,width=350,height=150,editable=False,cellwidth=175)
        self.table.createTableFrame()
        data = database.get_data_file(username1)
        print data
        if len(data) != 0:
	        for i in range(len(data)):
	          for j in range(2):
	            if j == 0:
	               data_1 = data[i][j]
	            if j == 1:
	               data_2 = data[i][j]     
	          keyname = "rec" + str(i)
	          self.table.addRow(keyname, **{'Name of File': data_2, 'Date of created': data_1})    
	        self.table.redrawTable()
        else:
	        keyname = "1" 
	        data_2 = "no file in storage"
	        self.table.addRow(keyname, **{'Name of File': data_2, 'Date of created': data_2})   
	        self.table.redrawTable()


def save(root, username):
  global username1
  username1 = username
  # global root
  # root = Tk()
  window = Toplevel(root)
  window.title('View profile')
  window.geometry("380x320")
  window.resizable(False,False)

  data_profile = database.get_profile(username1)
  value_lastname = StringVar()
  value_firstname = StringVar()
  value_address = StringVar()
  value_mail = StringVar()


  lastname = Label(window, text='Last name: ', width=10).grid(row=1, column=1)
  lastnameVarible = Label(window, textvariable = value_lastname, width=30).grid(row=1, column=2)

  firstname = Label(window, text='First name: ', width=10).grid(row=2, column=1)
  firstnameVarible = Label(window, textvariable = value_firstname, width=30).grid(row=2, column=2)

  address = Label(window, text='Address: ', width=10).grid(row=3, column=1)
  addressVarible = Label(window, textvariable = value_address, width=30).grid(row=3, column=2)


  mail = Label(window, text='Mail: ', width=10).grid(row=4, column=1)
  mailVarible = Label(window, textvariable = value_mail, width=30).grid(row=4, column=2)

 
  value_lastname.set(data_profile[0][1])
  value_firstname.set(data_profile[0][2])
  value_address.set(data_profile[0][3])
  value_mail.set(data_profile[0][4])

 
  window = createTable(window) 
  window.mainloop()