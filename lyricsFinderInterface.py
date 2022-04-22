#Made by Reef Rosenblat
from tkinter import *
from PIL import Image,ImageTk
from automated_lyrics import LyricsFinder

def submit():#function to initiate the lyrics finder object. it is invoked by entering to correct info and clicking submit
    finder = LyricsFinder(spotify_client_id=e1.get(),
                          spotify_secret=e2.get(),
                          genius_access_token=e3.get())
    checker = finder.initProgram()
    if checker is None or finder is None: #If the initProgram method return None or findr object is None,pop a message
        error = Tk()
        errorLabel = Label(error,
                           text="Program initialization has failed... check if the information you have entered is correct",
                           font=("Arial",14))
        errorLabel.pack()
        error.eval('tk::PlaceWindow . center')


info = Tk()
infoLabel = Label(info,text="please read README file before using the system")
info.eval('tk::PlaceWindow . center')
okButton = Button(info,text="ok",command=info.destroy)
infoLabel.pack()
okButton.pack()
info.mainloop()


#Create a main window to hold 3 frames
mainWindow = Tk() #instantiate an instance of a window
mainWindow.geometry("430x200")
mainWindow.title("Spotify Lyrics Finder")
icon = PhotoImage(file="logo.png")
mainWindow.iconphoto(True,icon)
mainWindow.resizable(False,False)
mainWindow.eval('tk::PlaceWindow . center')

#Initialize the 3 frames to hold the text entry area,photo area and button area
bottomFrame = Frame(mainWindow)
leftFrame = Frame(mainWindow)
rightFrame = Frame(mainWindow)
bottomFrame.grid(row=1,columnspan=2)
leftFrame.grid(row=0,column=0)
rightFrame.grid(row=0,column=1)


img = Image.open("spoti.jpg")
resized = img.resize((150,150),Image.ANTIALIAS)
dancer = ImageTk.PhotoImage(resized)
picLabel = Label(rightFrame,image=dancer)
picLabel.grid()

#Initialize 3 labels for the 3 entry boxes
l1 = Label(leftFrame, text="spotify ID",font="Arial,16")
l2 = Label(leftFrame, text="spotify SECRET",font="Arial,16")
l3 = Label(leftFrame,text="genius TOKEN",font="Arial,16")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=0, column=0, sticky=W, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)
l3.grid(row=2, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e1 = Entry(leftFrame)
e2 = Entry(leftFrame)
e3 = Entry(leftFrame)

# this will arrange entry widgets
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
submit_button = Button(bottomFrame,text="submit",command=submit)
submit_button.grid(columnspan=2)

mainWindow.mainloop() # place window on computer screen,listen for events



