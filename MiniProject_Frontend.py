from tkinter import *
import tkinter.messagebox
import MiniProject_Backend

class Movie:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Movie Ticket Booking System")
        self.root.geometry("1340x750+0+0")
        self.root.config(bg="#333")
        
        FONT = ('Arial', 18, 'bold')
        BUTTON_COLOR = "#FF5722"
        LABEL_COLOR = "orange"

        # Variables
        Movie_Name = StringVar()
        Movie_ID = StringVar()
        Release_Date = StringVar()
        Director = StringVar()
        Cast = StringVar()
        Budget = StringVar()
        Duration = StringVar()
        Rating = StringVar()

        # Functions
        def iExit():
            iExit = tkinter.messagebox.askyesno("Online Movie Ticket Booking System", "Are you sure???")
            if iExit > 0:
                root.destroy()
            return

        def clcdata():
            self.txtMovie_ID.delete(0, END)
            self.txtMovie_Name.delete(0, END)
            self.txtRelease_Date.delete(0, END)
            self.txtDirector.delete(0, END)
            self.txtCast.delete(0, END)
            self.txtBudget.delete(0, END)
            self.txtRating.delete(0, END)
            self.txtDuration.delete(0, END)

        def adddata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.AddMovieRec(
                    Movie_ID.get(), Movie_Name.get(), Release_Date.get(),
                    Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get()
                )
                MovieList.delete(0, END)
                MovieList.insert(END, (
                    Movie_ID.get(), Movie_Name.get(), Release_Date.get(),
                    Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get()
                ))

        def disdata():
            MovieList.delete(0, END)
            for row in MiniProject_Backend.ViewMovieData():
                MovieList.insert(END, row)

        def movierec(event):
            global sd
            searchmovie = MovieList.curselection()[0]
            sd = MovieList.get(searchmovie)

            self.txtMovie_ID.delete(0, END)
            self.txtMovie_ID.insert(END, sd[1])
            self.txtMovie_Name.delete(0, END)
            self.txtMovie_Name.insert(END, sd[2])
            self.txtRelease_Date.delete(0, END)
            self.txtRelease_Date.insert(END, sd[3])
            self.txtDirector.delete(0, END)
            self.txtDirector.insert(END, sd[4])
            self.txtCast.delete(0, END)
            self.txtCast.insert(END, sd[5])
            self.txtBudget.delete(0, END)
            self.txtBudget.insert(END, sd[6])
            self.txtDuration.delete(0, END)
            self.txtDuration.insert(END, sd[7])
            self.txtRating.delete(0, END)
            self.txtRating.insert(END, sd[8])

        def deldata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.DeleteMovieRec(sd[0])
                clcdata()
                disdata()

        def searchdb():
            MovieList.delete(0, END)
            for row in MiniProject_Backend.SearchMovieData(
                Movie_ID.get(), Movie_Name.get(), Release_Date.get(),
                Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get()
            ):
                MovieList.insert(END, row)

        def updata():
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.DeleteMovieRec(sd[0])
            if len(Movie_ID.get()) != 0:
                MiniProject_Backend.AddMovieRec(
                    Movie_ID.get(), Movie_Name.get(), Release_Date.get(),
                    Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get()
                )
                MovieList.delete(0, END)
                MovieList.insert(END, (
                    Movie_ID.get(), Movie_Name.get(), Release_Date.get(),
                    Director.get(), Cast.get(), Budget.get(), Duration.get(), Rating.get()
                ))

        MainFrame = Frame(self.root, bg="#333")
        MainFrame.grid()

        TFrame = Frame(MainFrame, bd=5, padx=54, pady=8, bg="#333", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame = Label(TFrame, font=('Arial', 40, 'bold'), text="ONLINE MOVIE TICKET BOOKING SYSTEM", bg="#333", fg="orange")
        self.TFrame.grid()

        BFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="#333", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame = Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="#333", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL = LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="#333", relief=RIDGE, font=FONT, text="Movie Info_\n", fg=LABEL_COLOR)
        DFrameL.pack(side=LEFT)

        DFrameR = LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="#333", relief=RIDGE, font=FONT, text="Movie Details_\n", fg=LABEL_COLOR)
        DFrameR.pack(side=RIGHT)

        # Labels & Entry Box

        self.lblMovie_ID = Label(DFrameL, font=FONT, text="Movie ID:", padx=2, pady=2, bg="#333", fg=LABEL_COLOR, anchor="e")
        self.lblMovie_ID.grid(row=0, column=0, sticky=W)

        self.txtMovie_ID = Entry(DFrameL, font=FONT, textvariable=Movie_ID, width=39, bg="#333", fg="white")
        self.txtMovie_ID.grid(row=0, column=1)

        self.lblMovie_Name = Label(DFrameL, font=FONT, text="Movie Name:", padx=2, pady=2, bg="#333", fg=LABEL_COLOR, anchor="e")
        self.lblMovie_Name.grid(row=1, column=0, sticky=W)

        self.txtMovie_Name = Entry(DFrameL, font=FONT, textvariable=Movie_Name, width=39, bg="#333", fg="white")
        self.txtMovie_Name.grid(row=1, column=1)

        self.lblRelease_Date = Label(DFrameL, font=FONT, text="Release Date:", padx=2, pady=2, bg="#333", fg=LABEL_COLOR, anchor="e")
        self.lblRelease_Date.grid(row=2, column=0, sticky=W)

        self.txtRelease_Date = Entry(DFrameL, font=FONT, textvariable=Release_Date, width=39, bg="#333", fg="white")
        self.txtRelease_Date.grid(row=2, column=1)

        self.lblDirector = Label(DFrameL, font=FONT, text="Director:", padx=2, pady=2, bg="#333", fg=LABEL_COLOR, anchor="e")
        self.lblDirector.grid(row=3, column=0, sticky=W)

        self.txtDirector = Entry(DFrameL, font=FONT, textvariable=Director, width=39, bg="#333", fg="white")
        self.txtDirector.grid(row=3, column=1)

        self.lblCast = Label(DFrameL, font=FONT, text="Cast:", padx=2, pady=2, bg="#333", fg=LABEL_COLOR, anchor="e")
        self.lblCast.grid(row=4, column=0, sticky=W)

        self.txtCast = Entry(DFrameL, font=FONT, textvariable=Cast, width=39, bg="#333", fg="white")
        self.txtCast.grid(row=4, column=1)

        self.lblBudget = Label(DFrameL, font=FONT, text="Budget (Crores INR):", padx=2, pady=2, bg="#333", fg=LABEL_COLOR, anchor="e")
        self.lblBudget.grid(row=5, column=0, sticky=W)

        self.txtBudget = Entry(DFrameL, font=FONT, textvariable=Budget, width=39, bg="#333", fg="white")
        self.txtBudget.grid(row=5, column=1)

        self.lblDuration = Label(DFrameL, font=FONT, text="Duration (Hrs):", padx=2, pady=2, bg="#333", fg=LABEL_COLOR, anchor="e")
        self.lblDuration.grid(row=6, column=0, sticky=W)

        self.txtDuration = Entry(DFrameL, font=FONT, textvariable=Duration, width=39, bg="#333", fg="white")
        self.txtDuration.grid(row=6, column=1)

        self.lblRating = Label(DFrameL, font=FONT, text="Rating (Out of 5):", padx=2, pady=2, bg="#333", fg=LABEL_COLOR, anchor="e")
        self.lblRating.grid(row=7, column=0, sticky=W)

        self.txtRating = Entry(DFrameL, font=FONT, textvariable=Rating, width=39, bg="#333", fg="white")
        self.txtRating.grid(row=7, column=1)

        # ListBox & ScrollBar
        sb = Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        MovieList = Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="#333", fg="white", yscrollcommand=sb.set)
        MovieList.bind('<<ListboxSelect>>', movierec)
        MovieList.grid(row=0, column=0, padx=8)
        sb.config(command=MovieList.yview)

        # Buttons
        self.btnadd = Button(BFrame, text="Add New", font=FONT, width=10, height=1, bd=4, bg=BUTTON_COLOR, command=adddata)
        self.btnadd.grid(row=0, column=0, padx=5, pady=5)

        self.btndis = Button(BFrame, text="Display", font=FONT, width=10, height=1, bd=4, bg=BUTTON_COLOR, command=disdata)
        self.btndis.grid(row=0, column=1, padx=5, pady=5)

        self.btnclc = Button(BFrame, text="Clear", font=FONT, width=10, height=1, bd=4, bg=BUTTON_COLOR, command=clcdata)
        self.btnclc.grid(row=0, column=2, padx=5, pady=5)

        self.btnse = Button(BFrame, text="Search", font=FONT, width=10, height=1, bd=4, bg=BUTTON_COLOR, command=searchdb)
        self.btnse.grid(row=0, column=3, padx=5, pady=5)

        self.btndel = Button(BFrame, text="Delete", font=FONT, width=10, height=1, bd=4, bg=BUTTON_COLOR, command=deldata)
        self.btndel.grid(row=0, column=4, padx=5, pady=5)

        self.btnup = Button(BFrame, text="Update", font=FONT, width=10, height=1, bd=4, bg=BUTTON_COLOR, command=updata)
        self.btnup.grid(row=0, column=5, padx=5, pady=5)

        self.btnx = Button(BFrame, text="Exit", font=FONT, width=10, height=1, bd=4, bg=BUTTON_COLOR, command=iExit)
        self.btnx.grid(row=0, column=6, padx=5, pady=5)


if __name__ == '__main__':
    root = Tk()
    MiniProject_Backend.MovieData()
    datbase = Movie(root)
    root.mainloop()
