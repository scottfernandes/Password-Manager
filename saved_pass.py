from customtkinter import *
from CTkMessagebox import CTkMessagebox
from store_pass import show_pass, delete_pass,update_pass
from password_manipulation import hash_pass
class SavedPasswords:
    def __init__(self, parent):
        self.main_frame = CTkFrame(parent, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=40, pady=20)

        self.title = CTkLabel(self.main_frame, text='Your Saved Passwords', font=('Arial', 25, 'bold'))
        self.title.grid(row=0, column=0, columnspan=5, pady=(10, 20))

        self.populate_table()

        

    def populate_table(self):
        for widget in self.main_frame.winfo_children():
            if widget != self.title:
                widget.destroy()

        headers = ["ID", "Website", "Username", "Password", "Actions"]
        for col_index, header in enumerate(headers):
            label = CTkLabel(self.main_frame, text=header, font=('Arial', 14, 'bold'))
            label.grid(row=1, column=col_index, padx=5, pady=5, sticky="nsew")

        
        self.data = show_pass()
        for row_index, entry in enumerate(self.data, start=2):
            for col_index, value in enumerate(entry):
                label = CTkLabel(self.main_frame, text=value, anchor='center',font=('Arial', 12))
                label.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

            delete_button = CTkButton(
                self.main_frame,
                text='Delete',
                fg_color='red',
                hover_color='black',
                font=('Arial', 12),
                command=lambda id=entry[0]: self.delete_entry(id)
            )
            delete_button.grid(row=row_index, column=len(entry), padx=5, pady=5, sticky="nsew")
            update_button = CTkButton(
                self.main_frame,
                text='Update',
                fg_color='Blue',
                hover_color='black',
                font=('Arial', 12),
                command=lambda id=entry[0]: self.update_entry(id)
            )
            update_button.grid(row=row_index, column=len(entry)+1, padx=5, pady=5, sticky="nsew")

    def delete_entry(self, id):
        confirmation = CTkMessagebox(
            title='Confirm Delete',
            message=f'Are you sure you want to delete this entry ?'
        )
        if confirmation.get()=='OK':  
            delete_pass(id) 
            self.populate_table()  
    
    def update_entry(self,id):
        prompt_new_pass = CTkInputDialog(title='Update Password',text='Enter the new password')
        new_pass = prompt_new_pass.get_input()
        if new_pass is not None:
            update_pass(hash_pass(new_pass),id=id)
            self.populate_table()
    

    def show(self):
        self.main_frame.tkraise()
