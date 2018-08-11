import program
import MySQLdb
import database
import string
import re
import hashlib
from Tkinter import *
 
# creates the main window object, defines its name, and default size
main = Tk()
main.title('Go read your brain')
main.wm_geometry("1000x650+20+40")
main.resizable(False,False)
background_image = PhotoImage(file="brain.png")
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def clear_widget(event):
 
    # will clear out any entry boxes defined below when the user shifts
    # focus to the widgets defined below
    if username_box == main.focus_get() and username_box.get() == 'Enter Username':
        username_box.delete(0, END)
    elif password_box == password_box.focus_get() and password_box.get() == '     ':
        password_box.delete(0, END)
 
def repopulate_defaults(event):
 
    # will repopulate the default text previously inside the entry boxes defined below if
    # the user does not put anything in while focused and changes focus to another widget
    if username_box != main.focus_get() and username_box.get() == '':
        username_box.insert(0, 'Enter Username')
    elif password_box != main.focus_get() and password_box.get() == '':
        password_box.insert(0, '     ')

def quit_signup():
    email_regex = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    em = email_box.get()
    is_valid = email_regex.match(em)
    passw1 = passwords1_box.get()
    passw2 = passwords2_box.get()
    check_email = database.get_profile(em)
    print check_email
    if is_valid and passw1 == passw2 and len(check_email) == 0:
        lname = lastname_box.get() 
        fname = firstname_box.get() 
        add = address_box.get()
        em = email_box.get()
        h = hashlib.md5(passw1)
        p = h.hexdigest()
        # print lname, " ", fname, " ", add, " ", em, " ", passw1
        # connect with SQL database
        db = MySQLdb.connect(host="eu-cdbr-sl-lhr-01.cleardb.net", user="bd51db6b9db508", passwd="1561ab78", db="ibmx_29e62892a53c4f3")
        cursor = db.cursor()
        cursor.execute("INSERT INTO persons (LastName, FirstName, Address, Mail, Passwords) VALUES (%s, %s, %s, %s, %s);", (lname, fname, add, em, p))
        db.commit()
        cursor.close()
        db.close()
        main.window.destroy()
    else:
        if len(check_email) != 0:
            error = Label(main.window, text='This mail was in system', fg='red').grid(row=8, column=2, sticky='NESW')
        if passw1 != passw2:
            error = Label(main.window, text='the repeated password \n does not match', fg='red').grid(row=8, column=2, sticky='NESW')
        if not is_valid:
            error = Label(main.window, text='not correct Email', fg='red').grid(row=8, column=2, sticky='NESW')

def login(*event):
    username = username_box.get()
    email_regex = re.compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = email_regex.match(username)
    if is_valid:
        print username
        db = MySQLdb.connect(host="eu-cdbr-sl-lhr-01.cleardb.net", user="bd51db6b9db508", passwd="1561ab78", db="ibmx_29e62892a53c4f3")
        cursor = db.cursor()
        cursor.execute("SELECT Passwords FROM ibmx_29e62892a53c4f3.persons WHERE Mail = %s;", (username))
        datafromdb =  cursor.fetchall()
        cursor.close()
        db.close()
        passwords = password_box.get()
        h2 = hashlib.md5(passwords)
        print passwords
        print 'ok'
        if len(datafromdb) == 1 and datafromdb[0][0] == h2.hexdigest():
            print passwords
            main.destroy()
            program.start(username)
            
        else:
            error = Label(main, text='No data in base', fg='red').grid(row=7, column=5, sticky='NESW')

        
    else:
        error = Label(main, text='Not correct data!!!', fg='red').grid(row=7, column=5, sticky='NESW')
        
    # main.destroy()
    # If I wanted I could also pass the username and password I got above to another 
    # function from here.

def new_window(*event):
    main.window = Toplevel(main)
    main.window.wm_geometry("250x180+40+40")
    main.window.title('New user')
    main.window.resizable(False,False)

    global lastname_box
    global firstname_box
    global address_box
    global email_box
    global passwords1_box
    global passwords2_box

    lastname = Label(main.window, text='Last name: ').grid(row=1, column=1)
    lastname_box = Entry(main.window)
    lastname_box.bind("<FocusIn>", clear_widget)
    lastname_box.bind('<FocusOut>', repopulate_defaults)
    lastname_box.grid(row=1, column=2)

    firstname = Label(main.window, text='First name: ').grid(row=2, column=1)
    firstname_box = Entry(main.window)
    firstname_box.bind("<FocusIn>", clear_widget)
    firstname_box.bind('<FocusOut>', repopulate_defaults)
    firstname_box.grid(row=2, column=2)

    address = Label(main.window, text='Address: ').grid(row=3, column=1)
    address_box = Entry(main.window)
    address_box.bind("<FocusIn>", clear_widget)
    address_box.bind('<FocusOut>', repopulate_defaults)
    address_box.grid(row=3, column=2)


    email = Label(main.window, text='Email: ').grid(row=4, column=1)
    email_box = Entry(main.window)
    email_box.bind("<FocusIn>", clear_widget)
    email_box.bind('<FocusOut>', repopulate_defaults)
    email_box.grid(row=4, column=2)

    passwords = Label(main.window, text='Passwords: ').grid(row=5, column=1)
    passwords1_box = Entry(main.window, show='*')
    passwords1_box.bind("<FocusIn>", clear_widget)
    passwords1_box.bind('<FocusOut>', repopulate_defaults)
    passwords1_box.grid(row=5, column=2)

    passwords2_box = Entry(main.window, show='*')
    passwords2_box.bind("<FocusIn>", clear_widget)
    passwords2_box.bind('<FocusOut>', repopulate_defaults)
    passwords2_box.grid(row=6, column=2)

        
    Apply_btn = Button(main.window, text='Apply', command=quit_signup )
    Apply_btn.bind('z', quit_signup)
    Apply_btn.grid(row=7, column=2, sticky='NESW')

 
# adds username entry widget and defines its properties
username_box = Entry(main)
username_box.insert(0, 'Enter Username')
username_box.bind("<FocusIn>", clear_widget)
username_box.bind('<FocusOut>', repopulate_defaults)
username_box.grid(row=1, column=5, sticky='NS')
 
 
# adds password entry widget and defines its properties
password_box = Entry(main, show='*')
password_box.insert(0, '     ')
password_box.bind("<FocusIn>", clear_widget)
password_box.bind('<FocusOut>', repopulate_defaults)
password_box.bind('<Return>', login)
password_box.grid(row=2, column=5, sticky='NS')
 
 
# adds login button and defines its properties
login_btn = Button(main, text='Login', command=login)
login_btn.bind('<Return>', login)
login_btn.grid(row=5, column=5, sticky='NESW')

signup_btn = Button(main, text='Sign up', command= new_window)
signup_btn.bind('z', new_window)
signup_btn.grid(row=6, column=5, sticky='NESW')
 
main.mainloop()







   
