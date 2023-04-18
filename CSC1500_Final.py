import random
import pickle
employeeData = [] #dictionary stored in a list
def add(): #function to add new employees to data base
    q1 = int(input("Enter number of entries to add: ")) #input to allow multiple entries
    i=0
    while True:
        employee =  {'Name':input("Enter Name: "), #dictionary for each employee
                     'Email':input("Enter gmail: "),
                     'SSN':input("Enter SSN: "),
                     'Position':input("Enter position: "),
                     'Address':input("Enter address: "),
                     'Phone':input("Enter phone number: "),
                     'Skills':input("Enter skills: "),
                     'Identifier':random.random()}
        print('\n')
        for i1 in employee: #loops to check email format is correct
            if ("@gmail.com" not in employee.get('Email')):
                print("error must include @gmail.com")
                employee.update(Email = input("Enter email: "))
                print('\n')
        for i2 in employee: #loop to check ssn format is correct
            if ("-" not in employee.get('SSN')):
                print("error must include - in SSN")
                employee.update(SSN = input("Enter SSN: "))
                print('\n')
        for i3 in employee: #loop to check phone format is correct
            if (")" not in employee.get('Phone')):
                print("error must include () in number")
                employee.update(Phone = input("Enter phone number: "))
                print('\n')
        for i4 in employee: #loop to check their are no symbols in names
            if ("&"in employee.get('Name') or "%"in employee.get('Name') or "$"in employee.get('Name') or "#"in employee.get('Name')  ):
                print("error cant have symbols in name")
                employee.update(Name = input("Enter Name: "))
                print('\n')


        employeeData.append(employee)
        i= i+1
        if(i == (q1)):
            break
    print(employeeData) #pickle the data into file
    with open('ProjectData.txt','wb') as x:
        pickle.dump(employeeData,x)
    


def query(): #function to search by employee name
    q1 = input("Enter Name to query: ")
    item = next((item for item in employeeData if item.get('Name') == q1), None)
    print(item)

def Remove(): 
    q1 = input("Enter name of employee to remove: ") 
    for  i in range(len(employeeData)): 
        if employeeData[i]['Name'] == q1: 
            q2 = input("Please confirm name of employee: ") 
            if employeeData[i]['Name'] == q2: 
                del employeeData[i] 

def import1(): #function to import data into the database
    q1 = input("Enter name of file: ")
    y = open(q1,"r")
    with open(q1,'r') as y1:
        employeeData.append([line.strip() for line in y1])
    print(employeeData)
    with open('ProjectData.txt','wb') as x:
        pickle.dump(employeeData,x)


import tkinter as tk #tkinter to create gui
from PIL import ImageTk,Image  
import tkinter.font as font 

def Main(): #function to create the main program screen with all the previous
    home_root.destroy()#functions as individual buttons
    windows = tk.Tk(className = 'Employee Database')
    windows.geometry('600x700')
    windows.configure(background='deep sky blue') 
    aFont = font.Font(family='Helvetica', weight='bold' )

    button1 = tk.Button(text = "Import Data",
    fg = "black",
    bg = "yellow",
    width = 25,
    height = 5,
    command = import1)
    button1['font'] = aFont
    button1.pack(pady=10)

    button2 = tk.Button(text = "Add Data",
    fg = "black",
    bg = "yellow",
    width = 25,
    height = 5,
    command = add)
    button2['font'] = aFont
    button2.pack(pady=15)

    button3 = tk.Button(text = "Query Data",
    fg = "black",
    bg = "yellow",
    width = 25,
    height = 5,
    command = query)
    button3['font'] = aFont
    button3.pack(pady=20)

    button4 = tk.Button(text = "Cloud backup - coming soon",
    fg = "black",
    bg = "yellow",
    width = 25,
    height = 5)
    button4['font'] = aFont
    button4.pack(pady=25)

    button5 = tk.Button(text = "Remove", 
    fg = "black",
    bg = "yellow",
    width = 25,
    height = 5, 
    command = Remove)
    button5['font'] = aFont
    button5.pack(pady=20)


    button6 = tk.Button(windows,text = "Quit",
    fg = "black",
    bg = "yellow",
    width = 25,
    height = 5,
    command = windows.destroy)
    button6['font'] = aFont
    button6.pack(pady=30)

    windows.mainloop()

    

home_root = tk.Tk(className = 'Agreement') #splash screen to get user to agree to terms
home_root.geometry("800x600")
home_root.configure(background='deep sky blue')
logo = Image.open('Forestviewlogo.jpeg')  #Forestview logo on splash screen
resize_logo = logo.resize((400,300))
log = ImageTk.PhotoImage(resize_logo)
logo_label = tk.Label(image=log)
logo_label.grid(row = 0, column=0, columnspan=5)


img = tk.Image("photo", file="icon.ico")#application icon with Forestview logo
home_root.iconphoto(True, img) 
home_root.tk.call('wm','iconphoto', home_root._w, img)
home_label = tk.Label(home_root, text = "By agreeing to the form the user agrees to not sell, share, or distribute data without the consent of FrostView", font=("Helvetica",12)) 
home_label.grid(row = 1, column = 0)
home_label2 = tk.Label(home_root, text = "Frostview is not legally responsible for any data breaches such as, zero-day attacks, database worms, or SQL injections", font=("Helvetica",12)) 
home_label2.grid(row = 2, column = 0)
home_label3 = tk.Label(home_root, text = "Frostview will conduct periodic vulnerability assessments against the employee database system and similar actions are taken by our key vendors", font=("Helvetica",12))
home_label3.grid(row = 3, column = 0)
home_label4 = tk.Label(home_root, text = "The requirments will change over time as technology changes and the security landscape changes", font=("Helvetica",12))
home_label4.grid(row = 4, column = 0)

button1 = tk.Button(text = "Agree",
fg = "blue",
bg = "yellow",
width = 25,
height = 5,
command = Main)
button1.grid(row = 5, column = 0)



       
                
