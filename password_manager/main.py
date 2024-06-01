from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []
    letter = [password_list.append(random.choice(letters)) for _ in range(1,4)]
    number = [password_list.append(random.choice(numbers)) for _ in range(1,3)] 
    sym = [password_list.append(random.choice(symbols)) for _ in range (1, 5)]
    
    random.shuffle(password_list)
    result = "".join(password_list)
    pyperclip.copy(result)
    password_input.insert(END,result)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_input.get()
    sec = password_input.get()
    email = email_username_input.get()
    new_data = {web:{
        "password":sec,
        "email":email,
    }
                }
    if web == "" or sec == "":
        messagebox.showinfo(title="info", message="password or email field is empty")

    else:    
        is_ok = messagebox.askokcancel(title="is ohk",message=f"{web}\npassword:{sec}")
        if is_ok:
            try:
                with open("password.json", "r") as data_file:
                    data = json.load(data_file)
                    
            except FileNotFoundError:
                with open("password.json" ,"w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("password.json" ,"w") as data_file:
                    json.dump(data,data_file,indent=4)
            website_input.delete(0,END)
            password_input.delete(0,END)
                #email_username_input.delete(0,END)


def find():
    with open("password.json",'r') as p:
        data = json.load(p)
        passes , email = data[website_input.get()]
        passe = data[website_input.get()][passes]
        emails = data[website_input.get()][email]
        messagebox.showinfo(message= f'password: {passe} \n email: {emails}')
        pyperclip.copy(passe)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password-manager")
window.config(padx=20,pady=20)
canvas =Canvas(width=200,height=224,highlightthickness=0)

photo = PhotoImage(file="logo.png")
canvas.create_image(111,114,image=photo)

canvas.grid(column=3,row=3)

website = Label(text="Website: ")
website.grid(column=1,row=4)

email_username = Label(text="  Email/Username: ")
email_username.grid(column=1,row=5)

email_username_input = Entry(width=35)
email_username_input.grid(row=5, column=3)

website_input = Entry(width=35)
website_input.grid(column=3,row=4)
website_input.focus()

password = Label(text="Password: ")
password.grid(column=1,row=6)

password_input = Entry(width=35)
password_input.grid(row=6, column=3)

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=3,row=7)

generate_password = Button(text="GeneratePassword",command=generate_passwords)
generate_password.grid(column=4,row=6)

search = Button(text="search",command=find)
search.grid(row=4, column=4)

window.mainloop()