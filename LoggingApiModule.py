class LoggingApi:

    def __init__(self):
        self = self

    def login(self):
        self.username = input("Podaj swój login: ")
        self.password = input("Podaj swoje hasło: ")
        with open('users.csv', 'r') as csvfile:
            if self.username == self.username and self.password == self.password:
                print("Zalogowałeś się")
            else:
                print("Logowanie nie powiodło się ")

    def register(self):
        self.username = input("Podaj swój login, celem rejestracji: ")
        self.password = input("Podaj hasło, aby dokończyć rrjestrację: ")
        self.passwordcheck = input("Podaj ponownie hasło, celem weryfikacji: ")
        with open("users.csv", 'a', newline='') as csvfile:
            csvfile.write("Użytkownik:", self.username + ",", "Hasło:", self.password + ",")
        if self.password == self.passwordcheck:
            print("Hasła pasują do siebie, zaloguj się ")
        else:
            print("Hasła się różnią")
