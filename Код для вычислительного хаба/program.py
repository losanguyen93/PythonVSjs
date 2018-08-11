import workmode
import save
from Tkinter import *
import trainingmode
import save
import inwork
def work_mode(username):
 print "work mode"
 workmode.interface_working(main_2, username)

def training_mode(username):
 print "training mode"
 main_2.destroy()
 trainingmode.interface_training(username)
 

def saved_mode(username):
 print "saved mode"
 # main_2.destroy()
 save.save(main_2, username)


def start(username):
 global main_2
 main_2 = Tk()
 main_2.title('Main programm')
 main_2.wm_geometry("880x680+20+40")
 main_2.resizable(False,False)
 background_image= PhotoImage(file="brain.png")
 background_label = Label(main_2, image=background_image)
 background_label.place(x=0, y=0, relwidth=1, relheight=1)


 work_btn = Button(main_2, text='Work mode', width=30, height=3, command = lambda: work_mode(username))
 work_btn.bind('a', work_mode)
 work_btn.grid(row=1, column=5)

 training_btn = Button(main_2, text='Training mode', width=30, height=3, command = lambda: training_mode(username))
 training_btn.bind('s', training_mode)
 training_btn.grid(row=2, column=5)

 save_btn = Button(main_2, text='Saved mode', width=30, height=3, command = lambda: saved_mode(username))
 # save_btn = Button(main_2, text='Saved modes', width=30, height=3, command=saved_mode)
 save_btn.bind('d', saved_mode)
 save_btn.grid(row=3, column=5) 

 main_2.mainloop()