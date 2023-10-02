import requests
import jwt
import random
import string

# Replace these with your server details
BASE_URL = 'http://127.0.0.1:8080'
REGISTER_URL = BASE_URL + '/register'
LOGIN_URL = BASE_URL + '/login'


def random_string(length):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# User credentials
username = random_string(10)
password = random_string(15)

# Register a new user
register_data = {'username': username, 'password': password}
response = requests.post(REGISTER_URL, json=register_data)

if response.status_code == 201:
    print('Step 1: User registration successful.')
else:
    print('Step 1: User registration failed.')

# Attempt to log in with the registered username and password
login_data = {'username': username, 'password': password}
response = requests.post(LOGIN_URL, json=login_data)

if response.status_code == 200:
    token = response.json().get('token')
    print('Step 2: Login successful.')
    print('JWT Token:', token)
else:
    print('Step 2: Login failed.')

# Attempt to log in with the wrong password
wrong_password = 'wrongpassword'
login_data['password'] = wrong_password
response = requests.post(LOGIN_URL, json=login_data)

if response.status_code == 401:
    print('Step 3: Login with wrong password failed (as expected).')
else:
    print('Step 3: Login with wrong password succeeded (unexpected).')

# Log in using the obtained JWT
if token:
    headers = {'Authorization': 'Bearer ' + token}
    response = requests.post(LOGIN_URL, headers=headers, json={})

    if response.status_code == 200:
        print('Step 4: Login with JWT successful.')
    else:
        print('Step 4: Login with JWT failed.')
        print('Response:', response.json())


secret = "08e0626e1fae5b9c5c247edb605a385df961754f6c780007911a72a2a979f48b"
# Decode and verify the JWT
if token:
    try:
        decoded_payload = jwt.decode(token, secret, algorithms=['HS256'])
        print('Decoded JWT Payload:', decoded_payload)
    except jwt.ExpiredSignatureError:
        print('JWT has expired.')
    except jwt.InvalidTokenError:
        print('Invalid JWT token.')
    except Exception as e:
        print('JWT decoding error:', e)
else:
    print('JWT token not available for decoding.')

