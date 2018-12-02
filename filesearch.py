from tkinter import *
import filesearch_func
import filesearch_gui


class AppWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.option_add("*font", "Helvetica 10")
        self.master.resizable(width=False, height=False)
        filesearch_func.center_window(self.master, 600, 400)
        # self.master.geometry('{}x{}'.format(600, 300))

        self.master.title('File Search Program')
        self.master.iconbitmap(self.master, default="assets/file_search.ico")
        self.master.columnconfigure(0, weight=1)

        self.var_path_name = StringVar()

        self.chkboxvars = []
        self.extlist = ['TXT', 'PDF', 'JPG', 'PNG', 'GIF', 'DOC']

        self.radiovar = IntVar()
        self.radiovar.set(5)
        self.radiovals = ["Day", "Week", "Month", "Year", "All time"]

        filesearch_gui.load_gui(self, self.master)

        # this is a tkniter protocol method to catch if user clicks the upper right "X" on windows OS
        # self.master.protocol("WM_DELETE_WINDOW", lambda: filesearch_func.ask_quit())


if __name__ == "__main__":
    root = Tk()
    App = AppWindow(root)
    root.mainloop()
