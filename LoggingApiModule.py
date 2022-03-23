import csv
from UserModule import User


class LoggingApi:
    user = User

    def __init__(self):
        self = self

    def login(self):
        self.username = input("Podaj swój login: ")
        self.password = input("Podaj swoje hasło: ")
        with open('users.csv', 'r') as csvfile:
            if self.username == self.username and self.password == self.password:
                print("Zalogowałeś się do newapi")
            else:
                print("Logowanie nie powiodło się ")

    def register(self):
        self.username = input("Podaj swój login, celem rejestracji: ")
        self.password = input("Podaj hasło, aby dokończyć rejestrację: ")
        self.passwordcheck = input("Podaj ponownie hasło, celem weryfikacji: ")
        with open("users.csv", 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([self.username, self.password])
            csvfile.close()
        while self.password != self.passwordcheck:
            self.passwordcheck = input("Hasła się różnią, podaj ponownie hasło celem weryfikacji: ")

    def listAll(self):
        data = []
        with open("users.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        print(data)

    def searchByLogin(self):
        login = input("Podaj login do wyszukania: \n")
        csv_file = csv.reader(open("users.csv", "r"))
        for row in csv_file:
            if login == row[0]:
                print(row)
            else:
                print("--------------------------")
                break

    def deleteEntry(self):
        name = input("Podaj login do usunięcia: ")

        with open('users.csv', 'r+') as in_file:
            reader = csv.reader(in_file)
            rows = [row for row in csv.reader(in_file) if name not in row]
            in_file.seek(0)
            writer = csv.writer(in_file)
            writer.writerows(rows)

    def options(self):
        print("Witamy w programie logowania\n")
        islogged = True
        while islogged:
            print("Wybierz opcję menu lista: 1/szukaj: 2/usun: 3/zakoncz: 4\n")
            menu = int(input("podaj wybór: "))
            if menu == 1:
                self.listAll()
            elif menu == 2:
                self.searchByLogin()
            elif menu == 3:
                self.deleteEntry()
            else:
                exit()
