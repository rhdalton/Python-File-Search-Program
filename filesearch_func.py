import os
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime, timedelta


def check_bar(window, app):
    for box in app.extlist:
        var = IntVar()
        chk = tk.Checkbutton(window, text=box, variable=var)
        if box == 'TXT':
            chk.select()
        chk.pack(side=LEFT)
        app.chkboxvars.append(var)


def search_range(window, app):
    for val, txt in enumerate(app.radiovals, start=1):
        chk = tk.Radiobutton(window, text=txt, variable=app.radiovar, value=val)
        chk.pack(side=LEFT)


def browse_button(app):
    filepath = filedialog.askdirectory()
    app.var_path_name.set(filepath)
    # print(filename)


def search_files(window, app):
    try:
        # get extensions to search for, if none are selected return error
        validext = []
        for i in range(len(app.extlist)):
            if app.chkboxvars[i].get() == 1:
                validext.append("." + app.extlist[i])
                # if JPG is selected, add 'JPEG' to search extension as well
                if app.extlist[i] == 'JPG':
                    validext.append(".JPEG")
                elif app.extlist[i] == 'DOC':
                    validext.append(".DOCX")
        if not validext:
            error_message(window, 'No extensions selected.')
            return

        dirlist = os.listdir(app.var_path_name.get())

        valid_file_list = []
        expire_time = {
            1: 1,  # 1 day
            2: 7,  # 1 week
            3: 30,  # 1 month
            4: 365,  # 1 year
            5: 0  # all time
        }

        # set the expired time limit based on user input
        expire_limit = datetime.today() - timedelta(days=expire_time.get(app.radiovar.get()))

        for i in dirlist:
            extension = os.path.splitext(i)
            # if extension is in valid extension list
            if extension[1].upper() in validext:
                mod = os.path.getmtime(os.path.join(app.var_path_name.get(), i))
                # if datetime of modified file is greater than expired time limit
                if (datetime.fromtimestamp(mod) > expire_limit) or (app.radiovar.get() == 5):
                    valid_file_list.append(i)

        if len(valid_file_list) > 0:
            # create new treeview for results
            CreateTreeView(window, len(valid_file_list))

            for j in valid_file_list:
                mod = os.path.getmtime(os.path.join(app.var_path_name.get(), j))
                mod = time.strftime("%m-%d-%Y", time.localtime(mod))
                LoadTreeViewItem(window, j, mod)

        else:
            error_message(window, 'No files with the selected extensions and time frame were found in:\n'
                                  '"' + app.var_path_name.get() + '"')

    except FileNotFoundError:
        error_message(window, 'Invalid directory! Please try again.')

    except Exception as e:
        print(str(e))


def error_message(window, m):
    ClearResultFrame(window)
    window.lbl_error = tk.Label(window.resultframe, text=m, fg='red')
    window.lbl_error.pack()


def center_window(window, w, h):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - w / 2)
    y = int((screen_height / 2) - h / 2) - 100
    centerGeo = window.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo


def CreateTreeView(window, file_count):
    ClearResultFrame(window)

    window.tvframe = tk.Frame(window.resultframe)
    tv = ttk.Treeview(window.tvframe, height=5)

    vsb = tk.Scrollbar(window.tvframe, orient='vertical', command=tv.yview)
    tv.pack(side=LEFT, fill=Y)
    vsb.pack(side=RIGHT, fill=Y)
    tv.config(yscrollcommand=vsb.set)

    tv['columns'] = 'modified'
    tv.heading("#0", text='File Name (' + str(file_count) + ' files found)', anchor=W)
    tv.column("#0", anchor=W, width=400)
    tv.heading('modified', text='Last Modified')
    tv.column('modified', anchor='center', width=120)
    window.treeview = tv
    window.tvframe.pack()


def LoadTreeViewItem(window, f, m):
    window.treeview.insert('', 'end', text=f, values=m)


def ClearResultFrame(window):
    window.tvframe.destroy()  # remove any previous treeview
    window.lbl_error.destroy()  # remove any previous error message


def ask_quit(window):
    if messagebox.askokcancel("Exit Program", "Okay to exit application?"):
        window.master.destroy()
        os._exit(0)
