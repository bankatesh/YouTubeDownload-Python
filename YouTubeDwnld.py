from tkinter import *
from tkinter import ttk
from  tkinter import filedialog
from pytube import YouTube




def openlocation():
    global Folder
    Folder = filedialog.askdirectory()

    if (len(Folder)>1):
        YtdPathError.config(text=Folder,fg='green')
    else:
        YtdPathError.config(text='Please select Folder', fg='red')


def download():
    global select
    choice = YtdChoices.get()
    url =YtdEntry.get()

    if len(url)>1:
        YtdError.config(text='')
        yt = YouTube(url)

        if(choice == Choices[0]):
            select = yt.streams.filter(progressive=True,resolution='480p').first()


        elif(choice == Choices[1]):
            select = yt.streams.filter(progressive=True,resolution='360p').first()

        elif(choice == Choices[2]):
            select = yt.streams.filter(progressive=True,resolution='144p').first()

        elif(choice == Choices[3]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            YtdError.config(text="Paste Link again!!",fg="red")

    select.download(Folder)
    YtdError.config(text="Download Completed!!")






# Making object of tkinter (creating box for video download)
Ytd = Tk()
Ytd.title('Your YTD')
Ytd.geometry('350x350')
Ytd.columnconfigure(0,weight=1)

# Label for url on top most part for video download
YtdLabel = Label(Ytd, text='Enter the URL of your video', font=('jost',15))
YtdLabel.grid(pady=(10,0))

#Designing the entry box

YtdEntryVariable = StringVar()
YtdEntry = Entry(Ytd,width=60,textvariable = YtdEntryVariable)
YtdEntry.grid()

#Error message(if url is wrong)

YtdError = Label(Ytd, text ='', fg= 'red')
YtdError.grid()

#Saving file

Ytdsave = Label(Ytd, text= 'save your file', font= ('jost',15, 'bold'))
Ytdsave.grid(pady=(20,0))

#Button to save

Ytdpath = Button(Ytd, width=10, bg='red', fg='white', text='choose path', command = openlocation)
Ytdpath.grid()

#Location pth error

YtdPathError = Label(Ytd, text='', fg='red')
YtdPathError.grid()

#Download quality
YtdQuality = Label(Ytd, text='Select quality', font=('jost',15))
YtdQuality.grid(pady=(20,0))

#Dropboxes for choices
Choices = ['Best Quality','Medium quality','Worst quality','Audio']
YtdChoices =ttk.Combobox(Ytd,value=Choices)
YtdChoices.grid()

#Download button

YtdDownload = Button(Ytd,text='Downoad', width=10, bg='red',fg='white', command=download)
YtdDownload.grid()


Ytd.mainloop()





