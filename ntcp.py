#!/usr/bin/env python3
# import
from tkinter import *
from tkinter.simpledialog import askstring, askinteger, askfloat
from tkinter.messagebox import showerror, showinfo
from tkinter import filedialog

root = Tk()
root.title("EUD based NTCP calculator")


# defining manual entry
def ab_value():
    global alphabeta
    alphabeta = float(alpha.get())


def s_value():
    global s
    s = 0


def clear():
    global abi, gp, tdf, no, dosep, alpha
    abi.delete(0, END)
    gp.delete(0, END)
    tdf.delete(0, END)
    no.delete(0, END)
    alpha.delete(0, END)
    dosep.delete(0, END)


def a_value():
    global a
    a = float(abi.get())


def g_value():
    global g
    g = float(gp.get())


def td_value():
    global td
    td = float(tdf.get())


def nofraction():
    global nof
    nof = float(no.get())


def doseperfraction():
    global dosepf
    dosepf = float(dosep.get())


# parameter emami et al
def brain():
    global a, g, td, s
    a = 5
    g = 3
    td = 60
    s = 1


def brainstem():
    global a, g, td, s
    s = 1
    a = 7
    g = 3
    td = 65


def optic():
    global a, g, td, s
    s = 1
    a = 25
    g = 3
    td = 65


def colon():
    global a, g, td, s
    s = 1
    a = 6
    g = 4
    td = 55


def ear1():
    global a, g, td, s
    s = 1
    a = 31
    g = 3
    td = 40


def ear2():
    global a, g, td, s
    s = 1
    a = 31
    g = 4
    td = 65


def esophagus():
    global a, g, td, s
    s = 1
    a = 19
    g = 4
    td = 68


def heart():
    global a, g, td, s
    s = 1
    a = 3
    g = 3
    td = 50


def kidney():
    global a, g, td, s
    s = 1
    a = 1
    g = 3
    td = 28


def lens():
    global a, g, td, s
    s = 1
    a = 3
    g = 1
    td = 18


def liver():
    global a, g, td, s
    s = 1
    a = 3
    g = 3
    td = 40


def lung():
    global a, g, td, s
    s = 1
    a = 1
    g = 2
    td = 24.5


def nerve():
    global a, g, td, s
    s = 1
    a = 25
    g = 3
    td = 65


def retina():
    global a, g, td, s
    s = 1
    a = 15
    g = 2
    td = 65


def bladder():
    global a, g, td, s
    s = 1
    a = 6
    g = 3.63
    td = 80


def rectum():
    global a, g, td, s
    s = 1
    a = 6
    g = 2.66
    td = 80


# parameter nimierko et al
def nbrain():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 2.9
    nof = 30
    dosepf = 2
    a = 5
    g = 3
    td = 60


def nbrainstem():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 2.5
    nof = 30
    dosepf = 2
    a = 7
    g = 3
    td = 65


def nheart():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 2.5
    nof = 30
    dosepf = 2
    a = 3
    g = 3
    td = 50


def nkidney():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 2
    nof = 30
    dosepf = 2
    a = 1
    g = 3
    td = 28


def nliver():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 2.5
    nof = 30
    dosepf = 2
    a = 3
    g = 3
    td = 40


def nlung():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 4
    nof = 30
    dosepf = 2
    a = 1
    g = 2
    td = 24.5


def noesophagus():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 10
    nof = 30
    dosepf = 2
    a = 19
    g = 4
    td = 68


def nopticchiasm():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 2
    nof = 30
    dosepf = 2
    a = 25
    g = 3
    td = 65


def nopticnerve():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 1.6
    nof = 30
    dosepf = 2
    a = 25
    g = 3
    td = 65


def nparotids():
    global alphabeta, nof, dosepf, a, g, td, s
    s = 0
    alphabeta = 3
    nof = 30
    dosepf = 2
    a = 1
    g = 2
    td = 31.4


# ask file name
def file_name():
    global fn
    fn = filedialog.askopenfilename()


# calculate
def calculate_eud():
    import pandas as pd
    import os

    test = pd.read_excel(fn)
    dose = (test.loc[:, "dose"])
    volume = (test.loc[:, "volume"])

    totalnumber = dose.count()
    global eud, q, ntcp
    eud = float(0)
    if s == 0:
        for i in range(0, totalnumber):
            bed = dose[i] * (alphabeta + (dose[i]) / nof) / (alphabeta + dosepf)
            eud = eud + (volume[i] / 100) * (bed ** a)
    elif s == 1:
        for i in range(0, totalnumber):
            eud = eud + (volume[i] / 100) * (dose[i] ** a)
    q = eud ** (1 / a)
    ntcp = (td / q)
    ntcp = ntcp ** g
    ntcp = 1.0 + ntcp
    ntcp = (1.0 / ntcp) * 100
    showinfo('Normal tissue complication probability (percentage)', 'NTCP Percentage %s\nEUD is %s Gy' % (ntcp, q))


# display reference
def open1():
    new_frame = Toplevel(root)
    new_frame.title("Reference Values")
    scro = Scrollbar(new_frame)
    tex = Text(new_frame, height=30, width=70)
    scro.pack(side=RIGHT, fill=Y)
    tex.pack(side=LEFT, fill=Y)
    scro.config(command=tex.yview)
    tex.config(yscrollcommand=scro.set)
    ent = '''Gay and Niemierko                                                     '''
    tex.insert(END, ent)
    from prettytable import PrettyTable
    x = PrettyTable()
    x.field_names = ['NTCP', 'fx', 'alpha/beta', 'dose/fx', 'a', 'gamma50', 'TD50']
    x.add_row(['Brain', 30, 2.9, 2, 5, 3, 60])
    x.add_row(['Brainstem', 30, 2.5, 2, 7, 3, 65])
    x.add_row(['Heart', 30, 2.5, 2, 3, 3, 50])
    x.add_row(['Kidney', 30, 2, 2, 1, 3, 28])
    x.add_row(['Liver', 30, 2.5, 2, 3, 3, 40])
    x.add_row(['Lung', 30, 4, 2, 1, 2, 24.5])
    x.add_row(['Oesophagus', 30, 10, 2, 19, 4, 68])
    x.add_row(['Optic Chiasm', 30, 2, 2, 25, 3, 65])
    x.add_row(['Optic Nerve', 30, 1.6, 2, 25, 3, 65])
    x.add_row(['Parotids', 30, 3, 2, 1, 2, 31.4])
    tex.insert(END, x)
    emami = '''
    In emami data while calculating BED the dose per fraction is 
    considered as 1.8-2 Gy, 5 days a week                             '''
    tex.insert(END, emami)
    y = PrettyTable()
    y.field_names = ['Structure', 'End point', 'a', 'gamma50', 'TD50']
    y.add_row(['Brain', 'Necrosis', 5, 3, 60])
    y.add_row(['Brainstem', 'Necrosis', 7, 3, 65])
    y.add_row(['Optic chiasm', 'Blindness', 25, 3, 65])
    y.add_row(['Colon', 'Obstruction', 6, 4, 55])
    y.add_row(['Ear', 'Acute serous otitis', 31, 3, 40])
    y.add_row(['Ear', 'Chronic serous otitis', 31, 4, 65])
    y.add_row(['Esophagus', 'Perforation', 19, 4, 68])
    y.add_row(['Heart', 'Pericarditis', 3, 3, 50])
    y.add_row(['Kidney', 'Nephritis', 1, 3, 28])
    y.add_row(['Lens', 'Cataract', 3, 1, 18])
    y.add_row(['Liver', 'Liver failure', 3, 3, 40])
    y.add_row(["Lung", 'Pneumonitis', 1, 2, 24.5])
    y.add_row(['Optic nerve', 'Blindness', 25, 3, 65])
    y.add_row(['Retina', 'Blindness', 15, 2, 65])
    tex.insert(END, y)


# display License
def open2():
    new_frame2 = Toplevel(root)
    new_frame2.title('License')
    scr = Scrollbar(new_frame2)
    tex1 = Text(new_frame2, height=30, width=70)
    scr.pack(side=RIGHT, fill=Y)
    tex1.pack(side=LEFT, fill=Y)
    scr.config(command=tex1.yview)
    tex1.config(yscrollcommand=scr.set)
    lic = '''<EUD based NTCP calculator.>
    \nCopyright (C) <2020>  <Thirumurugan Elango>

    \nThis program is free software: you can redistribute it and/or modify
    \nit under the terms of the GNU General Public License as published by
    \nthe Free Software Foundation, either version 3 of the License, or
    \n(at your option) any later version.

    \nThis program is distributed in the hope that it will be useful,
    \nbut WITHOUT ANY WARRANTY; without even the implied warranty of
    \nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    \nGNU General Public License for more details.

    \nYou should have received a copy of the GNU General Public License
    \nalong with this program.  If not, see <https://www.gnu.org/licenses/>.'''
    tex1.insert(END, lic)


# Entry widgets for manual inputs
abi = Entry(root, width=25, borderwidth=5)
abi.grid(row=0, column=1)
gp = Entry(root, width=25, borderwidth=5)
gp.grid(row=0, column=3)
tdf = Entry(root, width=25, borderwidth=5)
tdf.grid(row=1, column=1)
no = Entry(root, width=25, borderwidth=5)
no.grid(row=1, column=3)
dosep = Entry(root, width=25, borderwidth=5)
dosep.grid(row=2, column=1)
alpha = Entry(root, width=25, borderwidth=5)
alpha.grid(row=2, column=3)

# Create Buttons
btn_1 = Button(root, text="import", command=file_name).grid(row=5, column=0)
btn_2 = Button(root, text="calculate", command=calculate_eud).grid(row=5, column=1)
btn_3 = Button(root, text="manual value entry",
               command=lambda: [ab_value(), g_value(), td_value(), s_value(), doseperfraction(), nofraction(),
                                a_value()])
btn_3.grid(row=5, column=3)
btn_4 = Button(root, text="Clear", command=clear).grid(row=5, column=2)
# create Label for manual entry
l1 = Label(root, text="a value").grid(row=0, column=0)
l2 = Label(root, text="Gamma 50 value").grid(row=0, column=2)
l3 = Label(root, text='Tolerance Dose in Gy').grid(row=1, column=0)
l4 = Label(root, text="Number of Fractions").grid(row=1, column=2)
l5 = Label(root, text="Dose per faction in Gy").grid(row=2, column=0)
l6 = Label(root, text="Alpha/Beta Value").grid(row=2, column=2)
# create menubar
menubar = Menu(root)
root.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="emami et al", menu=submenu)
submenu.add_command(label="Brain Necrosis", command=brain)
submenu.add_command(label="Brainstem Necrosis", command=brainstem)
submenu.add_command(label="optic chiasm blindness", command=optic)
submenu.add_command(label="colon Obstruction", command=colon)
submenu.add_command(label="Ear Acute serous otitis", command=ear1)
submenu.add_command(label="Ear Chronic serous otitis", command=ear2)
submenu.add_command(label="Esophagus perforation", command=esophagus)
submenu.add_command(label="Heart Pericarditis", command=heart)
submenu.add_command(label="Kidney Nephritis", command=kidney)
submenu.add_command(label="Lens Cataract", command=lens)
submenu.add_command(label="Liver failure", command=liver)
submenu.add_command(label="Lung Pneumonitis", command=lung)
submenu.add_command(label="optic nerve blindness", command=nerve)
submenu.add_command(label="Retina Blindness", command=retina)
submenu.add_command(label='Bladder', command=bladder)
submenu.add_command(label='Rectum', command=rectum)

nmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Gay & Niemierko", menu=nmenu)
nmenu.add_command(label="Brain", command=nbrain)
nmenu.add_command(label="Brainstem", command=nbrainstem)
nmenu.add_command(label="Heart", command=nheart)
nmenu.add_command(label="Kidney", command=nkidney)
nmenu.add_command(label="Liver", command=nliver)
nmenu.add_command(label="Lung", command=nlung)
nmenu.add_command(label="Oesophagus", command=noesophagus)
nmenu.add_command(label="Optic Chiasm", command=nopticchiasm)
nmenu.add_command(label="Optic nerve", command=nopticnerve)
nmenu.add_command(label="Parotids", command=nparotids)

rmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Reference", menu=rmenu)
rmenu.add_command(label='Reference value', command=open1)

amenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About', menu=amenu)
amenu.add_command(label='about', command=open2)

root.mainloop()

