
from tkinter import messagebox
from Orders import OrderScreenClass
from CensusManagement import DisplayCensusClass
import tkinter as tk
from tkinter import font as tkfont
from PatientClass import PatientClass
from PatientClass import ProviderClass
from PatientClass import ProviderFrame
from PresetOrders import PresetOrderClass
import sys

NAME = 0
ROOM = 1
DOB = 2


#  #####   This is the base frame of the program
#   #####   Frame Name is base frame
#   ###    All the utility type stuff can eventually be done from here
def buildthebaseframe():
    times24 = tkfont.Font(family="Times", size=24)
    buttonfont = tkfont.Font(family="Times", size=14)

    this_frame = window.nametowidget("base_frame")

    def preset_order_pressed(which):
        # window.nametowidget(which).setreturnframe(
        #     window.nametowidget("base_frame"))
        window.nametowidget(which).tkraise()

    # def radbuttonpressed():
    #     #theradiologyobj.setreturnframe(window.nametowidget("base_frame"))
    #     radiologyframe.setreturnframe(window.nametowidget("base_frame"))
    #     window.nametowidget("radiology_frame").tkraise()

    # def otherordersbuttonpressed():
    #     otherorderframe.setreturnframe(window.nametowidget("base_frame"))
    #     #theotherodersobj.setreturnframe(window.nametowidget("base_frame"))
    #     window.nametowidget("other_order_frame").tkraise()

    # def labbuttonpressed():
    #     labframe.setreturnframe(window.nametowidget("base_frame"))
    #     #thelabObj.setreturnframe(window.nametowidget("base_frame"))
    #     window.nametowidget("lab_frame").tkraise()

    def open_provider_frame():
        window.nametowidget("provider_frame").tkraise()

    def open_new_census():
        if patients_object.arethereorders():
            msg = 'The are orders on the current patient list.  Make sure you''ve printed them before loading a new census'
            messagebox.showinfo('Warning', msg)

        census_frame = window.nametowidget("create_census_frame")
        census_frame.tkraise()

    def currentpatientlist():
        window.nametowidget("display_census").tkraise()

    def exitprogram():
        if patients_object.arethereorders():
            confirmation = messagebox.askquestion("Exit", "The are orders on the current patient list.  Do you need to print them still?")
            if not(confirmation == 'yes'):
                sys.exit()
        else:
            sys.exit()

    thisrow = 0

    this_frame.rowconfigure(thisrow, weight=1)
    this_frame.columnconfigure(0, weight=1)
    this_frame.columnconfigure(4, weight=1)

    title_txt = program_name + " - The Program for Writing Orders"

    #is it right to have a variable for each of these?
    tk.Label(this_frame, text=title_txt, font=times24).grid(row=thisrow, column=1, columnspan=3)
    # labeltitlebaseframe.config()
    # labeltitlebaseframe

    thisrow = thisrow + 1
    
    tk.Button(this_frame, font=buttonfont,
              text="Add Labs", command=lambda: preset_order_pressed('labs')).grid(row=thisrow, column=3, sticky='news')
    tk.Button(this_frame, text="Load Patient List", height=1,
              font=buttonfont, command=loadpatientlistframe).grid(row=thisrow, column=1, sticky='news')

    thisrow = thisrow + 1


    tk.Button(this_frame, text="Current Patient List", height=1,
              font=buttonfont, command=currentpatientlist).grid(row=thisrow, column=1, sticky='news')
    tk.Button(this_frame, text="Add Radiology", height=1,
              font=buttonfont,  command=lambda: preset_order_pressed('radiology')).grid(row=thisrow, column=3, sticky='news')

    thisrow = thisrow + 1


    tk.Button(this_frame, text="Provider Data", height=1,
              font=buttonfont, command=open_provider_frame).grid(row=thisrow, column=1, sticky='news')


    tk.Button(this_frame, text="Add Other Orders", height=1,
              font=buttonfont, command=lambda: preset_order_pressed('other orders')).grid(row=thisrow, column=3, sticky='news')

    thisrow = thisrow + 1



    tk.Button(this_frame, text="Create New Census", height=1,
              font=buttonfont, command=open_new_census).grid(row=thisrow, column=1, sticky='news')
    tk.Button(this_frame, text="Exit", height=1,
              font=buttonfont, command=exitprogram).grid(row=thisrow, column=3, sticky='news')

    thisrow = thisrow + 1
    this_frame.rowconfigure(thisrow, weight=1)

    # labbutton = tk.Button(this_frame, font=buttonfont, text="Add Labs", command=labbuttonpressed)
    # labbutton = tk.Button(this_frame, font=buttonfont,
    #                       text="Add Labs", command=lambda: preset_order_pressed('labs'))
    # labbutton.grid(row=thisrow, column=3, sticky='news')

    # buttonpatientlist = tk.Button(this_frame, text="Load Patient List", height=1)
    # buttonpatientlist.config(command=loadpatientlistframe)
    # buttonpatientlist.config(font=buttonfont)
    # buttonpatientlist.grid(row=thisrow, column=1, sticky='news')
    # buttondisplaycensus = tk.Button(this_frame, text="Current Patient List", height=1)
    # buttondisplaycensus.config(command=currentpatientlist)
    # buttondisplaycensus.config(font=buttonfont)
    # buttondisplaycensus.grid(row=thisrow, column=1, sticky='news')
    # radbutton = tk.Button(this_frame, font=buttonfont, text="Add Radiology", command=radbuttonpressed)
    # radbutton = tk.Button(this_frame, font=buttonfont,
    #                       text="Add Radiology", command=lambda: preset_order_pressed('radiology'))
    # radbutton.grid(row=thisrow, column=3, sticky='news')
    # buttonprovider = tk.Button(this_frame, text="Provider Data",  height=1, command=open_provider_frame)
    # buttonprovider.config(font=buttonfont)
    # buttonprovider.grid(row=thisrow, column=1, sticky='news')
#    otherordersbutton = tk.Button(this_frame, text="Add Other Orders", command=otherordersbuttonpressed)
    # otherordersbutton = tk.Button(this_frame, text="Add Other Orders", command=lambda: preset_order_pressed('other orders'))

    # otherordersbutton.config(font=buttonfont)
    # otherordersbutton.grid(row=thisrow, column=3, sticky='news')
    # buttoncreatecensus = tk.Button(this_frame, text="Create New Census", height=1, command=open_new_census)
    # buttoncreatecensus.config(font=buttonfont)
    # buttoncreatecensus.grid(row=thisrow, column=1, sticky='news')
    # exitprogram = tk.Button(this_frame, text="Exit Program", font=buttonfont, command=exitprogram)
    # exitprogram.grid(row=thisrow, column=3, sticky='news')

def loadpatientlistframe():

    if patients_object.arethereorders():
        msg = 'The are orders on the current patient list.  Make sure you''ve printed them before loading a new census'
        messagebox.showinfo('Warning', msg)

    if census_object.loadcensus_file_names() == 0:
        window.nametowidget("patient_census_frame_empty").tkraise()
    else:
        window.nametowidget("patient_census_frame_not_empty").tkraise()


def initialize_frames():
    global window

    baseframe = tk.Frame(window, name="base_frame")
    baseframe.grid(row=0, column=0, sticky='nsew')

    # patientcensusframe = tk.Frame(window, name="patient_census_frame_not_empty")
    # patientcensusframe.grid(row=0, column=0, sticky='nsew')


    tk.Frame(window, name="patient_census_frame_empty")
    tk.Frame(window, name="patient_census_frame_not_empty")

    changepatientdata = tk.Frame(window, name="change_patient_data")
    changepatientdata.grid(row=0, column=0, sticky='nsew')

    deletecensusframe = tk.Frame(window, name="delete_census_frame")
    deletecensusframe.grid(row=0, column=0, sticky='nsew')

    # labframe = tk.Frame(window, name="lab_frame")
    # labframe.grid(row=0, column=0, sticky='nsew')

    # radiologyframe = tk.Frame(window, name="radiology_frame")
    # radiologyframe.grid(row=0, column=0, sticky='nsew')

    # otherorderframe = tk.Frame(window, name="other_order_frame")
    # otherorderframe.grid(row=0, column=0, sticky='nsew')

    addorderframe = tk.Frame(window, name="add_order_frame")
    addorderframe.grid(row=0, column=0, sticky='nsew')

    displaycensus = tk.Frame(window, name="display_census")
    displaycensus.grid(row=0, column=0, sticky='nsew')

    # providerframe = tk.Frame(window, name="provider_frame")
    # providerframe.grid(row=0, column=0, sticky='nsew')
    providerframe = ProviderFrame(this_provider, window, name="provider_frame")

    createcensusframe = tk.Frame(window, name="create_census_frame")
    createcensusframe.grid(row=0, column=0, sticky='nsew')


program_name = "Popcorn"

window = tk.Tk()


window.geometry('800x500')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.title(program_name)
window.resizable(0, 0)

this_provider = ProviderClass()
patients_object = PatientClass(this_provider)

initialize_frames()

labframe = PresetOrderClass(window, name="labs")
radiologyframe = PresetOrderClass(window, name="radiology")
otherorderframe = PresetOrderClass(window, name="other orders")




# thelabObj = PresetOrderClass(window.nametowidget("lab_frame"), "Labs")

# theradiologyobj = PresetOrderClass(window.nametowidget("radiology_frame"), "Radiology")
# theotherodersobj = PresetOrderClass(window.nametowidget("other_order_frame"), "Other Orders")

addorders_object = OrderScreenClass(window,
                                    patients_object, labframe,
                                    radiologyframe,
                                    otherorderframe)
# addorders_object = OrderScreenClass(window,
#                                     patients_object, thelabObj,
#                                     theradiologyobj,
#                                     theotherodersobj)
census_object = DisplayCensusClass(window,
                                   patients_object,
                                   addorders_object,
                                   this_provider)


buildthebaseframe()
census_object.buildeverything()

addorders_object.buildorderframe()
labframe.buildframe()
radiologyframe.buildframe()
otherorderframe.buildframe()
# thelabObj.buildframe()
# theradiologyobj.buildframe()
# theotherodersobj.buildframe()
window.nametowidget("base_frame").tkraise()

window.mainloop()
