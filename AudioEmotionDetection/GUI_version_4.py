#     t k P h o n e . p y
#
from tkinter import *
#from phones  import *

"""def whichSelected () :
    print("At %s of %d" % (select.curselection(), len(emotionlist))
    #return int(select.curselection()[0])
        pass"""

def addEntry () :
    emotionList.append ([userVar.get(), userVar.get()])
    setSelect ()

def updateEntry() :
    emotionlist[whichSelected()] = [nameVar.get(), userVar.get()]
    setSelect ()

def deleteEntry() :
    del emotionlist[whichSelected()]
    setSelect ()

def loadEntry  () :
    name, user = emotionlist[whichSelected()]
    userVar.set(name)
    emotionVar.set(phone)

def makeWindow () :
    global nameVar, userVar, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="User Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Emotion").grid(row=1, column=0, sticky=W)
    phoneVar= StringVar()
    phone= Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Record  ",command=addEntry)
    b2 = Button(frame2,text="Play Recorded Audio",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Train ",command=loadEntry)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    return win

    frame4 = Frame(win)
    frame4.pack()
    scroll = Scrollbar(frame4, orient = VERTICAL)
    select = Listbox(Frame4, yscrollcommand=scroll.set,height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT,fill=Y)
    select.pack(side =LEFT, fill=BOTH, expand=1)
    return win

def setSelect () :
    emotionlist.sort()
    select.delete(0,END)
    for name,emotion in emotionlist :
        select.insert (END, name)

win = makeWindow()
setSelect ()
win.mainloop()
