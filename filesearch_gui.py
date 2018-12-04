import tkinter as tk
from tkinter import *
import filesearch_func


def load_gui(app, window):
    # creating grid frames for each row of content,
    # then items will be packed into each grid to align everything left

    window.inputframe = tk.Frame(window)  # create new frame for input field row
    window.extframe = tk.Frame(window)  # create new frame for extension options
    window.dateframe = tk.Frame(window)  # create new frame for date range options
    window.resultframe = tk.Frame(window)  # create new frame for result area
    window.lbl_error = tk.Label(window.resultframe)  # define a label for error messages (goes in result frame)
    window.tvframe = tk.Frame(window.resultframe)  # define treeview result (goes in result frame)

    tk.Label(window, text="File Search Program", justify=LEFT, font='Helvetica 10 bold') \
        .grid(row=0, column=0, sticky=W, padx=20, pady=15)

    tk.Label(window, text="Choose the directory to search and parameters below.",
             justify=LEFT, font=("Helvetica", 10)) \
        .grid(row=1, column=0, sticky=W, padx=30, pady=(0, 10))

    tk.Label(window.inputframe, text='Directory:').pack(side=LEFT)

    # use the lambda operator to prevent browse function from running on start-up
    tk.Button(window.inputframe, text="Browse", command=lambda: filesearch_func.browse_button(app), font='Helvetica 9',
              relief=GROOVE, bg='#dcdcdc') \
        .pack(side=LEFT, padx=(10, 5))
    tk.Entry(window.inputframe, text=app.var_path_name, width=55) \
        .pack(side=LEFT, ipady=2, ipadx=2)

    window.inputframe.grid(row=2, column=0, sticky=W, padx=30)

    tk.Label(window.extframe, text='Extension: ').pack(side=LEFT)

    filesearch_func.check_bar(window.extframe, app)
    window.extframe.grid(row=3, column=0, sticky=W, padx=30, pady=10)

    tk.Label(window, text='Search for files modified within the last:') \
        .grid(row=4, column=0, sticky=W, padx=30)

    filesearch_func.search_range(window.dateframe, app)
    window.dateframe.grid(row=5, column=0, sticky=W, padx=30)

    tk.Button(window, text="Search Files", width=10, height=1, command=lambda: filesearch_func.search_files(window, app), bg='#dcdcdc') \
        .grid(row=6, column=0, padx=30, pady=10)

    window.resultframe.grid(row=7, column=0, padx=30)
