from customtkinter import *
import random
from CTkMessagebox import CTkMessagebox
from store_pass import *
from password_manipulation import hash_pass,verify
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'


class AddPassword:
    def __init__(self,parent):
        self.main_frame = CTkFrame(master=parent,fg_color='transparent')
        self.main_frame.grid(row=0,column=1)
        
        self.title = CTkLabel(self.main_frame, text='SecureHome Password Manager', font=('Arial', 25, 'bold'))
        self.title.grid(row=1, column=1, columnspan=3, pady=(0, 0),padx=(80,0))
        
        website_label = CTkLabel(self.main_frame, text='Website:', font=('Arial', 13))
        website_label.grid(row=2, column=1, pady=(100, 0), sticky="e")
        
      
        self.web_txt = CTkEntry(self.main_frame, width=400, height=35)
        self.web_txt.grid(row=2, column=2, pady=(100, 0), padx=10, sticky="w", columnspan=2)
        self.web_txt.focus()
    
        email_label = CTkLabel(self.main_frame, text='Email/Username:', font=('Arial', 13))
        email_label.grid(row=3, column=1, pady=(20,0), sticky="e")

        self.email_txt = CTkEntry(self.main_frame, width=400, height=35)
        self.email_txt.grid(row=3, column=2, pady=(20,0), padx=10, sticky="w", columnspan=2)
        self.email_txt.insert(0, 'scottfernandes3586@gmail.com')
    
        password_label = CTkLabel(self.main_frame, text='Password:', font=('Arial', 13))
        password_label.grid(row=4, column=1, pady=20, sticky="e")

        self.password_txt= StringVar()
        self.pass_inp = CTkEntry(self.main_frame, show='*', textvariable=self.password_txt, width=400, height=35)
        self.pass_inp.grid(row=4, column=2, pady=20, padx=10, sticky="w", columnspan=2)
    
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_columnconfigure(2, weight=2)
        self.main_frame.grid_columnconfigure(3, weight=1)
    
        gen_pass_button = CTkButton(self.main_frame, text='Generate Password', font=('Arial', 14), hover_color='black', fg_color='#4B0082', command=self.generate_pass, width=200, height=40)
        gen_pass_button.grid(row=5, column=2, pady=10, padx=(10, 20), sticky="e")
    
        save_pass_button = CTkButton(self.main_frame, text='Save Password', font=('Arial', 14), hover_color='black', command=self.save_password, height=40, fg_color='#4B0082')
        save_pass_button.grid(row=5, column=3, pady=10, padx=(20, 10), sticky="w")
        
        self.conf = CTkLabel(self.main_frame,text='',font=('Arial', 19))
        self.conf.grid(row=6,column=1,columnspan=3)
        
    def generate_pass(self):
        password = [random.choice(letters) for _ in range(5)] + \
               [random.choice(numbers) for _ in range(5)] + \
               [random.choice(symbols) for _ in range(5)]
        random.shuffle(password)
        final_pass = ''.join(password)
        self.password_txt.set(final_pass)

    def save_password(self):
        website = self.web_txt.get()
        email = self.email_txt.get()
        password = self.pass_inp.get()

        if not website or not email or not password:
            CTkMessagebox(title='Error',icon='warning', message='Please enter all details.',button_color='#4B0082',button_hover_color='black',font=('Arial',15))
        else:
            save_conf =CTkMessagebox(
            title='Confirmation',
            message=f'The details are:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nSave this?',
            option_1='OK',
            option_2='Cancel',
            button_width=50,
            button_color='#4B0082',button_hover_color='black',font=('Arial',15)
        )
            if save_conf.get()=='OK':
                add_pass_to_db(website=website,username=email,password=hash_pass(password))
                self.conf.configure(text='Password Saved Successfully!')


    def show(self):
        self.main_frame.tkraise()