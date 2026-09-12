from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key


master_pwd = input("What is your master password? ")

key = load_key()
fer = Fernet(key)


def view():
    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, encrypted_pwd = data.split("|")

                decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
                print(f"User: {user} | Password: {decrypted_pwd}")
    except FileNotFoundError:
        print("No saved passwords found.")


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("password.txt", "a") as f:

        encrypted_pwd = fer.encrypt(password.encode()).decode()
        f.write(f"{name}|{encrypted_pwd}\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view/add)? Press Q to quit: "
    ).lower().strip()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")