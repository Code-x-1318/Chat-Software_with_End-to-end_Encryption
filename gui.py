from Detector import main_app
from create_classifier import train_classifer
from create_dataset import start_capture
from crypt import AESCipher
import socket
import threading
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox,PhotoImage,scrolledtext
import sys
from pathlib import Path
from tkinter import *
HOST = '10.38.3.125'
PORT = 1234
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
key="opp"
object1=AESCipher(key)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
names = set()


class MainUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global names
        global Uname
        global tt
        tt=0
        with open("nameslist.txt", "r") as f:
            x = f.read()
            z = x.rstrip().split(" ")
            for i in z:
                names.add(i)
        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.title("Messenger Client")
        self.resizable(False, False)
        self.geometry("1187x678")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.active_name = None
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (LoginPage, SignUpPage, MessagePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("LoginPage")

    def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()
            if page_name == "MessagePage":
                frame.connect()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure?"):
            global names
            f =  open("nameslist.txt", "a+")
            for i in names:
                    f.write(i+" ")
            self.destroy()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(
            self,
            bg="#F9F9F9",
            height=678,
            width=1187,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.pack()
        self.canvas.create_rectangle(
            381.0,
            95.0,
            802.0,
            582.0,
            fill="#FFFFFF",
            outline="#333333"
        )

        self.canvas.create_text(
            419.0,
            280.0,
            anchor="nw",
            text="Username",
            fill="#333333",
            font=("PlusJakartaSansRoman Regular", 18 * -1)
        )

        self.canvas.create_text(
            423.0,
            149.0,
            anchor="nw",
            text="Login ",
            fill="#000000",
            font=("PlusJakartaSansRoman SemiBold", 35 * -1)
        )

        self.canvas.create_text(
            423.0,
            199.0,
            anchor="nw",
            text="to get started",
            fill="#000000",
            font=("PlusJakartaSansRoman Regular", 25 * -1)
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("new.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: controller.show_frame("SignUpPage"),
            relief="flat"
        )
        self.button_1.place(
            x=516.0,
            y=498.0,
            width=138.0,
            height=19.941810607910156
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("login.png"))
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command= self.openwebcam
        )
        self.button_2.place(
            x=419.0,
            y=420.0,
            width=333.0,
            height=50.676719665527344
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("username.png"))
        self.entry_bg_1 = self.canvas.create_image(
            585.5,
            339.33836364746094,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#8c8c8c",
            font=("Helvetica", 15),
            highlightthickness=0
        )
        self.entry_1.place(
            x=429.0,
            y=316.0,
            width=313.0,
            height=40.0
        )
    
    def openwebcam(self):
        global names
        global Uname
        self.controller.active_name = self.entry_1.get("1.0", "end-1c")
        Uname = self.entry_1.get("1.0", "end-1c")
        if(self.controller.active_name == "None"):
            messagebox.showerror("ERROR", "Please enter a valid Username!")
            return
        if(self.controller.active_name not in names):
            messagebox.showerror("ERROR", "User does not exist!")
            return
        if len(self.entry_1.get("1.0", "end-1c")) == 0:
            messagebox.showerror("Error", "Please enter a valid Username!")
            return
        if(main_app(self.controller.active_name)):
            self.controller.show_frame("MessagePage")
            # MessagePage.connect(MessagePage)
        else:
            messagebox.showerror("ERROR", "Face not recognized!") 

class SignUpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(
            self,
            bg="#F9F9F9",
            height=678,
            width=1187,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.pack()
        self.canvas.create_rectangle(
            381.0,
            95.0,
            802.0,
            582.0,
            fill="#FFFFFF",
            outline="#333333"
        )

        self.canvas.create_text(
            419.0,
            280.0,
            anchor="nw",
            text="Username",
            fill="#333333",
            font=("PlusJakartaSansRoman Regular", 18 * -1)
        )

        self.canvas.create_text(
            423.0,
            149.0,
            anchor="nw",
            text="Sign Up ",
            fill="#000000",
            font=("PlusJakartaSansRoman SemiBold", 35 * -1)
        )

        self.canvas.create_text(
            423.0,
            199.0,
            anchor="nw",
            text="to get started",
            fill="#000000",
            font=("PlusJakartaSansRoman Regular", 25 * -1)
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("bth.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("LoginPage"),
            relief="flat"
        )
        self.button_1.place(
            x=516.0,
            y=498.0,
            width=138.0,
            height=19.941810607910156
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("signup.png"))
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.capimg
        )
        self.button_2.place(
            x=419.0,
            y=420.0,
            width=333.0,
            height=50.676719665527344
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("username.png"))
        self.entry_bg_1 = self.canvas.create_image(
            585.5,
            339.33836364746094,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#8c8c8c",
            font=("Helvetica", 15),
            highlightthickness=0
        )
        self.entry_1.place(
            x=429.0,
            y=316.0,
            width=313.0,
            height=40.0
        )

    def capimg(self):
        global names
        if self.entry_1.get("1.0", "end-1c") == "None":
            messagebox.showerror("Error", "Please enter a valid Username!")
            return
        elif self.entry_1.get("1.0", "end-1c") in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif len(self.entry_1.get("1.0", "end-1c")) == 0:
            messagebox.showerror("Error", "Please enter a valid Username!")
            return
        name = self.entry_1.get("1.0", "end-1c")
        names.add(name)
        f =  open("nameslist.txt", "a+")
        f.write(name+" ")
        self.controller.active_name = name
        messagebox.showinfo("INSTRUCTIONS", "We will Capture 300 pic of your Face.")
        x = start_capture(self.controller.active_name)
        self.controller.num_of_images = x
        if self.controller.num_of_images < 300:
            messagebox.showerror("ERROR", "No enough Data, Capture at least 300 images!")
            return
        train_classifer(self.controller.active_name)
        messagebox.showinfo("SUCCESS", "Your data has been successfully captured!")
        self.controller.show_frame("LoginPage")   

class MessagePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(
            self,
            bg="#F9F9F9",
            height=678,
            width=1187,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.pack()

        self.entry_2 = Text(
            self.canvas,
            bd=0,
            font=(("Helvetica", 20)),
            bg="#b3b3cc",
            fg="white",
            highlightthickness=0
        )
        self.entry_2.place(
            x=0.0,
            y=0.0,
            width=1187.0,
            height=620.0
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("send.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.send_message,
            relief="flat"
        )
        self.button_1.place(
            x=957.0,
            y=621.0,
            width=230.0,
            height=56.676719665527344
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("chat.png"))
        self.entry_bg_1 = self.canvas.create_image(
            478.5,
            649.3383598327637,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            self.canvas,
            font=(("Helvetica", 17)),
            bd=0,
            bg="#AEAEAE",
            fg="black",
            highlightthickness=0
        )
        self.entry_1.place(
            x=10.0,
            y=621.0,
            width=937.0,
            height=54.676719665527344
        )
        
    def connect(self):
        global Uname
        # try except block
        # try:
            # Connect to the server
        client.connect((HOST, PORT))
        print("Successfully connected to server")
        self.add_message("[SERVER] Successfully connected to the server")
        # except:
        #     messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")

        username = Uname
        if username != '':
            client.sendall(username.encode())
        else:
            messagebox.showerror("Invalid username", "Username cannot be empty")

        threading.Thread(target=self.listen_for_messages_from_server, args=(client, )).start()

    def add_message(self,message):
        self.entry_2.insert(END, message + '\n')

    def send_message(self):
        message = self.entry_1.get("1.0", "end-1c")
        if message != '':
            encryptedmessage=object1.encrypt(message)
            print(encryptedmessage)
            client.sendall(encryptedmessage.encode())
            self.entry_1.delete("1.0","end")
        else:
            messagebox.showerror("Empty message", "Message cannot be empty")

    def listen_for_messages_from_server(self, client):
        while 1:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                username = message.split("~")[0]
                ciphertext = message.split('~')[1]
                if ciphertext=='':
                    self.add_message(f"[{username}]")
                else:
                    decryptedmessage=object1.decrypt(ciphertext)
                    print(decryptedmessage)
                    self.add_message(f"[{username}] {decryptedmessage}")               
            else:
                messagebox.showerror("Error", "Message recevied from client is empty")
        
app = MainUI()
app.mainloop()