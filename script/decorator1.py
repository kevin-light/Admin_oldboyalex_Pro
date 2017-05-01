import time

user,passwd = 'alex','abc123'

def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print("wrapper func args:",args,kwargs)
            username = input("Username:").strip()
            password = input("Password:").strip()
            if auth_type == "local":
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args,**kwargs)
                    print("after authenticaion")
                    return res
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("ldap...")
        return wrapper
    return outer_wrapper


def index():
    print("welcomg to index page")

@auth(auth_type = "local")
def home():
    print("welcome home")
    return "from home"

@auth(auth_type = "ldap")
def bbs():
    print("welcome bba")

index()
print(home())
bbs()

