from customtkinter import *
import random
from CTkMessagebox import CTkMessagebox
from store_pass import close  
from add_pass_screen import AddPassword
from saved_pass import SavedPasswords
import smtplib
from password_manipulation import hash_pass,verify
from store_pass import add_user,show_user

set_appearance_mode('dark')
set_default_color_theme('dark-blue')
class SecureHomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureHome")
        self.root.geometry('1980x1280')
        if show_user():
            self.mst = show_user()
            self.enter_master_pass()
        else:
            self.register()
        
       

        self.setup_sidebar()
        self.setup_content_frame()
        self.show_add_password_screen()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_sidebar(self):
        self.sidebar_frame = CTkFrame(master=self.root, width=200, height=600, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky='nsew')
        self.root.grid_rowconfigure(0, weight=1)

        sidebar_label = CTkLabel(self.sidebar_frame, text="SecureHome", font=('Arial', 20, 'bold'))
        sidebar_label.grid(row=0, column=0, pady=(20, 10), padx=10)

     
        add_pass_button = CTkButton(
            master=self.sidebar_frame, text="Add Passwords", fg_color='transparent',
            font=('Arial', 14), hover_color='black', 
            command=self.show_add_password_screen
        )
        add_pass_button.grid(row=1, column=0, pady=(30, 10), padx=10, sticky="ew")

        add_pass_button = CTkButton(
            master=self.sidebar_frame, text="Show Passwords", fg_color='transparent',
            font=('Arial', 14), hover_color='black', 
            command=self.show_saved
        )
        add_pass_button.grid(row=2, column=0, pady=(30, 10), padx=10, sticky="ew")

    def setup_content_frame(self):
        self.content_frame = CTkFrame(master=self.root, fg_color='transparent')
        self.content_frame.grid(row=0, column=1, rowspan=5, sticky="nsew", pady=20, padx=50)
        self.password_txt = StringVar()
        
        self.conf = CTkLabel(self.content_frame, text='', font=('Arial', 25, 'bold'))
        self.conf.grid(row=5, column=1, columnspan=3, pady=(30, 0), padx=(80, 0))

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_add_password_screen(self):
        self.clear_content_frame()  
        AddPassword(self.content_frame).show()

    def show_saved(self):
        self.clear_content_frame()
        SavedPasswords(self.content_frame).show()

    def register(self):
        master_pass = CTkInputDialog(
            title='Master Password Creation',
            text='Create your Master Password',
            button_fg_color='#4B0082',
            button_hover_color='black',
           font=('Arial',12)
        )
        val  = master_pass.get_input()
        if val is not None:
            add_user(hash_pass(val))
            return True
        else:
            self.root.destroy()
            return False

    def enter_master_pass(self):
        inp =CTkInputDialog(
            title='Enter Master Password',
            text='Enter the Master Password and gain access:',
            button_fg_color='#4B0082',
            button_hover_color='black',
           font=('Arial',12))
        user_input = inp.get_input()
        if user_input is None:
            self.root.destroy()
            return False
        elif verify(user_input,self.mst):
            return True
        else:
            errormsg=CTkMessagebox(title='Error',icon='warning', message='Wrong Password.',button_color='#4B0082', button_hover_color='black',font=('Arial',15))
            if errormsg.get()=='OK':
                self.root.destroy()
                return False

    def on_closing(self):
        close()
        self.root.destroy()

if __name__ == "__main__":
    root = CTk()
    app = SecureHomeApp(root)
    root.mainloop()
