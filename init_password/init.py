from notebook.auth import passwd
from getpass import getpass
for i in range(3):
    my_password = getpass('set password: ')
    my_password_confirm = getpass('type password again: ')
    if my_password == my_password_confirm:
        hashed_password = passwd(passphrase=my_password, algorithm='sha256')
        with open("work/jupyter-config.yml", "w")as f:
            f.write(f"password: {hashed_password}")
        print("password encryption finished")
        break
    else:
        print("please type consistent password")
