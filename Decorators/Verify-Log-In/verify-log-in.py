import json

with open('users.json','r') as json_file:
    users = json.load(json_file)

def verify_log_in(func):
    def wrapper(username, password):
        if username in users and password == users[username]['password']:
            print(f"Successful login for the user '{username}'.")
            return func(users[username])
        else:
            print("Login failed. Verify your username and password.")
    
    return wrapper

@verify_log_in
def user_information(user):
    print("User personal information:")
    print(f"Full name: {user['full_name']}")
    print(f"Email adress: {user['email']}")

user_information('user1', 'password123')
