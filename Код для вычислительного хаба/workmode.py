#! /usr/bin/env python
# coding: utf-8
from Tkinter import *
import Tkinter as tk
from tkintertable.Tables import TableCanvas
import database
import pickle
import download
import inwork
def select_ok(*event):
        ds = listbox1.get(ACTIVE)
        print ds
        bucketname = database.get_bucket_name(username1)
        print bucketname
        download.download_ds(bucketname,ds)
        window.destroy()
        inwork.in_working()
        

def interface_working(root, username):
    # Стартуем потоки
    global username1
    global listbox1
    global window
    global root_for_send
    username1 = username
    root_for_send = root
    list1=[]
    window = Toplevel(root_for_send)
    window.title('Выбор файл загрузки')
    window.wm_geometry("380x260")
    window.resizable(False,False)
    data = database.get_data_file(username1)
    for i in range(len(data)):
      data_1 = data[i][0]
      list1.append(data_1)   
    listbox1=Listbox(window,height=15,width=48,selectmode=SINGLE)
    for i in list1:
      listbox1.insert(END,i)
    listbox1.grid(row=1, column=1, sticky='NESW')
    select_btn = Button(window, text='Select', command=select_ok)
    select_btn.bind('z', select_ok)
    select_btn.grid(row=2, column=1, sticky='NESW')
    window.mainloop()

















    