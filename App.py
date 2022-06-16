from tkinter import *
from tkinter import filedialog
from tokenize import String
from matplotlib.pyplot import text
from numpy import insert

from pyparsing import withClass
import Point_Fonction

#------Variable------#

#--Fonction permettant d'ouvrir un fichier--#
def showFrame():
    configuration_frame.place(x=180 , y=300)

def save_pts_to_csv_file():

    filetypes = (
        ('CSV files', '*.CSV'),
        ('All files', '*.*')
    )

    filenames = filedialog.asksaveasfile(
        title='Save files',
        initialdir= "/",
        filetypes=filetypes)
   ## import pdb; pdb.set_trace()
    Point_Fonction.save_csv_from_stl(file_entry.get().strip("{}"), filenames.name)

def pts_mathplot():
    pts = Point_Fonction.load_points_from_stl(file_entry.get().strip("{}"))
    Point_Fonction.plot_vert_intersection(pts, interval=10)

def pts_CSV():
    Point_Fonction.save_pts_to_csv_file()
    pts = Point_Fonction.load_points_from_stl(file_entry.get().strip("{}"))
    Point_Fonction.get_points_intersect_in_mm(pts, interval=10)

def select_files():
    filetypes = (
        ('STL files', '*.STL'),
        ('All files', '*.*')
    )

    filenames = filedialog.askopenfilenames(
        title='Open files',
        initialdir= "/",
        filetypes=filetypes)

    file_entry.delete(0, END)
    file_entry.insert(0, filenames)   

window = Tk()
window.iconbitmap('C:\\Users\\mathieu\\Documents\\project\\Utopie MFG\\SkiConverter\\logo.ico')
window.title("SkiConverter - Utopie tunnel")
window.geometry("920x600")
window.resizable(False, False)
window.config(background=('grey'))

navigation_menu = Frame(window, bg=("#2E74DA"))
navigation_menu.pack(side=TOP)

configuration_frame= Frame(window, bg=("white"))

label_Title = Label(navigation_menu, text="SkiConverter", font=("Courrier", 40), bg=("#2E74DA"), fg=("white"))
label_Title.grid(row=0, column=0)

img_bp_config = PhotoImage(file="C:\\Users\\mathieu\\Documents\\project\\Utopie MFG\\SkiConverter\\bp_config.png")
config_button = Button(navigation_menu, image=img_bp_config, bg=("#2E74DA"), bd=0, activebackground=("#2E74DA"), command=showFrame)
config_button.grid(row=0, column=1)

img_bp_upload = PhotoImage(file="C:\\Users\\mathieu\\Documents\\project\\Utopie MFG\\SkiConverter\\bp_upload.png")
upload_Button = Button(navigation_menu, image=img_bp_upload, bg=("#2E74DA"), bd=0, activebackground=("#2E74DA"), command=select_files)
upload_Button.grid(row=0, column=2)

img_bp_quit = PhotoImage(file="C:\\Users\\mathieu\\Documents\\project\\Utopie MFG\\SkiConverter\\bp_quit.png")
quit_button = Button(navigation_menu, image=img_bp_quit, bg=("#2E74DA"), bd=0, activebackground=("#2E74DA"), command=window.destroy)
quit_button.grid(row=0, column=3)

label_information = Label(window, text="Veuillez choisir votre fichier à convertir", font=("Courrier", 20), bg=("grey"), fg=("white"))
label_information.place(x=220, y=100)

str_var = StringVar(window)
file_entry = Entry(window, textvariable=str_var, bg=("#D3D7DC"), width=90)
file_entry.place(x=180, y=150)

img_bp_CSV = PhotoImage(file="C:\\Users\\mathieu\\Documents\\project\\Utopie MFG\\SkiConverter\\bp_CSV.png")
CSV_button = Button(window, image=img_bp_CSV, bg=("grey"), bd=0, activebackground=("grey"), command=save_pts_to_csv_file)
CSV_button.place(x=180, y=200)

img_bp_view = PhotoImage(file="C:\\Users\\mathieu\\Documents\\project\\Utopie MFG\\SkiConverter\\bp_view.png")
view_button = Button(window, image=img_bp_view, bg=("grey"), bd=0, activebackground=("grey"), command=pts_mathplot)
view_button.place(x=520, y=200)

label_center = Label(configuration_frame, text="Entrer la valeur entre point. Ex:10mm", font=("Courrier", 10), bg=("grey"), fg=("white"))
label_center.grid(row=0, column=0)
textbox_mm_center = Text(configuration_frame, bg=("#D3D7DC"), bd=0, width=25, height=1, fg=("grey"))
textbox_mm_center.grid(row=1, column=0)

window.mainloop()
