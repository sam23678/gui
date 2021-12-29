from __future__ import unicode_literals
import youtube_dl
video = input ("Please Enter your youtube link: ")
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video])
    from tkinter import*
    from tkinter import filedialog
    window =Tk()
    Path = Entry(root, width=20, textvariable=Path).place(x=20, y=10)
    def openFile():
        filepath=filedialog.askopenfilename(initialdir="C:\\HP\\PycharmProjects\\ad")
        file=open(filepath,'r')
        print(file.read())
        file.close()
    button=Button(text="open", command=openFile)
    button.pack()

    window.mainloop()

