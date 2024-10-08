# widgets = GUI elements : Buttos, Textboxes  , Labels , image
# windows = serves as a container to hold or contain these widgets

'''

# How to create a window with python? 🔕
# Answer.........Below 👀
from tkinter import*       # import tkinter.

def click():
    print("Thank Our world")
# For create
window = Tk()              # instantiate an instance of a window 
window.geometry("420x420") # For window size # geometry() this name function


#head/Title
mujakkir_logo = PhotoImage(file="C:\\programing\\BroCode\\mujakkirphoto.png") # for import window icon or logo
window.iconphoto(True, mujakkir_logo)                                      # mujakkir_logo)
window.title("MUJAKKIR AHMAD")                                             # For window title # title() this name function

#body
photo = PhotoImage(file="C:\\programing\\BroCode\\mujakkirphoto.png")
window.config(background="#42f54e")                    # For body bg color
label = Label(window,text="HELLO! I'm Mujakkir Ahmad", # text=
              font= ("Arial", 40, "bold"),             # font(font name, font size, bold)
              fg="white",bg="black",                   # text color and text bacground color
              relief=RAISED,                           # Shape size
              bd=10,                                   # Border to text potion 
              padx=20,                                 # 
              pady=20,                                 #
              image=photo,                             # photo
              compound="bottom")                       # text and image potion            # some text for window body
# Buttons 
button = Button(window,
                text="click",
                command=click,
                font=("Aptos narrow",30),
                fg="black",
                bg="#827e91",
                activebackground="#f54242",
                activeforeground="#827e91",
                state=ACTIVE,
                )

button.pack()


label.pack()                                           # for veiw text
#label.place(x=100,y=100)                              # if need text potioin


# For output
window.mainloop()                                      # For Create a window (place window on computer sceen, listen or events)

# entry widget (input)
from tkinter import*
def submit():
    user_name = entry.get()
    print(f"Hello {user_name}")

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get()-1),END)

window = Tk()

entry = Entry(window,
              font=("Arial",50,"bold"),
              fg="#00FF00",
              bg="black",
              show="*")

entry.pack()

submit_button = Button(window,
                       text="Submit", 
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete", 
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text="Backspace", 
                       command=backspace)
backspace_button.pack(side=RIGHT)



window.mainloop()


# How To create a Checkbox 🔕
from tkinter import*
def display():
    if (x.get()==1):
        print("I am agree.")
    else:
        print("i don't agree.")
window= Tk()

x = StringVar()
emoji_photo = PhotoImage(file="C:\\Users\\USER\\Downloads\\file.png")
check_button = Checkbutton(window,
                           text="Agree with trems and condition.",
                           variable= x,
                           onvalue= 1,
                           offvalue= 0,
                           command= display,
                           font=("Aptos Narrow", 10, "bold"),
                           fg="#15d12b",
                           bg="#e3cacf",
                           activeforeground="#15d12b",
                           activebackground="#e3cacf",
                           padx=25,
                           pady=10,
                           )
check_button.pack()


window.mainloop()


'''
# How to create a RadioButton
from tkinter import*

food = ["PIZZA","ICE-CREAM","BURGER"]

window = Tk()
pizza_image =PhotoImage(file="C:\Users\USER\Downloads\fizza.png")
ice_cream_image = PhotoImage(file="C:\Users\USER\Downloads\icecream.png")
burger_image = PhotoImage(file="C:\Users\USER\Downloads\burger.png")


foodimage = [pizza_image,ice_cream_image,burger_image]

x= IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable= x,
                              value= index,
                              padx= 25,
                              font=("Impact",50,),
                              image= foodimage[index])
    radiobutton.pack(anchor= W,) # anchor use for alinment

window.mainloop()