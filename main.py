from UserModule import User
from LoggingApiModule import LoggingApi


def run():
    if __name__ == '__main__': run()


def begin():
    newapi = createNewLoggingApi()

    print("Witaj")
    while True:
        option = int(input("Zaloguj albo zarejestruj się: 1 lub 2 "))
        if option in ['1', '2']:
            break
        if option == 1:
            newapi.login()
        else:
            newuser = createNewUser()
            newapi.login(newuser)
        newapi.options()


def createNewLoggingApi():
    newapi = LoggingApi()
    return newapi


def createNewUser():
    username = input("Utwórz konto użytkownika, podaj swój login / username: ")
    password = input("Podaj swoje nowe hasło: ")
    newuser = User(username=username, password=password)
    return newuser


begin()
