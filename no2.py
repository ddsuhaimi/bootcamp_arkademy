import re


def is_username_valid(username):
    if re.match(r'(?=^.{5,9}$)(?=^[a-zA-Z])(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).*$', username):
        # https://regex101.com/r/Yv7L8n/1
        return True
    else:
        return False


def is_password_valid(password):
    if re.match(r'(?=^.{8,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*=).*$', password):
        return True
    else:
        return False


print(is_username_valid('Xrutaf888'))  # True
print(is_username_valid('1Diana'))  # False
print(is_password_valid('passW0rd='))  # True
print(is_password_valid('C0d3YourFuture!#'))  # False
