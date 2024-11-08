import bcrypt

def hash_pass(password):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode(),salt)
    return hashed_pass

def verify(plain,hashed):
    return bcrypt.checkpw(plain.encode(),hashed)

