## Not so secret password
username = input('Username: ')
password = input('Password: ')

## Correct method to do it
from getpass import getpass

new_username = input('Username: ')
new_password = getpass('Password: ')
