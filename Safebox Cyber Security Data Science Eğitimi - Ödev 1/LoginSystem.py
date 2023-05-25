import time

def enter():
    user_name= input("Enter the User Name: ")
    passwd= input("Enter the Password: ")

    with open("list.txt", "r") as file:
        for i in file:
            time.sleep(1)
            name, password = i.strip().split(",")
            if name == user_name and password == passwd:
                print("Entered Successfully!")
                return  # Giriş başarılıysa fonksiyondan çık
        print("User name or password is wrong!")  # Döngü tamamlandı, hatalı giriş

enter()
