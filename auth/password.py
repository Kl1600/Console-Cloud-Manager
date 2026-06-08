import bcrypt

def hash_password(password):
    password_hasher=bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
    return(password_hasher.decode())
