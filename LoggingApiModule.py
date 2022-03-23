from UserModule import User
class LoggingApi:

    user = User

    def __init__(self):
        self = self

    def login(self, user):
        self.username = input("Podaj swój login: ")
        self.password = input("Podaj swoje hasło: ")
        with open('users.csv', 'r') as csvfile:
            if self.username == self.username and self.password == self.password:
                print("Zalogowałeś się do newapi")
            else:
                print("Logowanie nie powiodło się ")

    def register(self, user):
        self.username = input("Podaj swój login, celem rejestracji: ")
        self.password = input("Podaj hasło, aby dokończyć rejestrację: ")
        self.passwordcheck = input("Podaj ponownie hasło, celem weryfikacji: ")
        with open("users.csv", 'a', newline='') as csvfile:
            csvfile.write("Użytkownik:", self.username + ",", "Hasło:", self.password + ",")
        if self.password == self.passwordcheck:
            print("Hasła pasują do siebie, zaloguj się ")
        else:
            print("Hasła się różnią")

    def options(self):
            print("Witamy w programie logowania\n")
            success = True
            while success:
                print("Wybierz opcję menu lista: 1/szukaj: 2/usun: 3/zakoncz: 4\n")
                menu = int(input("podaj wybór: "))
                if menu == 1:
                    print("tu 1")
                elif menu == 2:
                    print("tu 2")
                elif menu == 3:
                    print("tu 3")
                else:
                    exit()
