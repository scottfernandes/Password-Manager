import sqlite3


PATH_TO_DB='day29//pass.db' #Add the path to your db. If it does not exist it will be automatically created
conn = sqlite3.connect(PATH_TO_DB)



curr = conn.cursor()
table_s='''CREATE TABLE IF NOT EXISTS PASSWORDS(
             
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             website TEXT NOT NULL,
             username TEXT NOT NULL,
             password TEXT NOT NULL 
        
             
             )'''


user_table = '''CREATE TABLE IF NOT EXISTS USER(
                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                master TEXT NOT NULL,
                otp INTEGER 
                
                
                )'''

curr.execute(table_s)
curr.execute(user_table)
def add_pass_to_db(website,username,password):
    
    try:
        with conn:
            insert =f'INSERT INTO PASSWORDS (website,username,password) VALUES (?,?,?)'
            curr.execute(insert,(website,username,password))
            conn.commit()
    except Exception as e:
        print(e)

def add_user(master):
    try:
        with conn:
            insert = f'INSERT INTO USER (master) VALUES (?)'
            curr.execute(insert,(master,))
            conn.commit()
    except Exception as e:
        print(e)


def show_pass():
    try:
        select='SELECT * FROM PASSWORDS'
        data=curr.execute(select)
        pass_data=[]
        for i in data:
            pass_data.append(i)
        conn.commit()
        return pass_data
    except Exception as e:
       print(e)

def show_user():
    try:
        select='SELECT * FROM USER'
        data=curr.execute(select)
        pass_data=[]
        for i in data:
            pass_data.append(i)
        conn.commit()
        if len(pass_data)<1:
            return False
        else:
            return pass_data[0][1]
    except Exception as e:
       print(e)

def delete_pass(id):
    try:
        delete='DELETE FROM PASSWORDS WHERE id=?'
        data=curr.execute(delete,(id,))
        pass_data=[]
        for i in data:
            pass_data.append(i)
        conn.commit()
        return []
    except Exception as e:
       print(e)


def update_pass(password,id):
    try:
        update='UPDATE PASSWORDS SET password = ?  WHERE id=?'
        curr.execute(update,(password,id))
        conn.commit()
        return 
    except Exception as e:
       print(e)

show_user()
def close():
    curr.close()
    conn.close()
