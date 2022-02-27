print('--------Task 1--------')
email = input('Enter your email address: ')
print(email.endswith('.com'))

print('===========Task 2===========')
name = input('Please tell me your name: ')
print('Hello ', name.title(), ', I hope you are fine. please let me know how can u help you?')
user = input(' Do you need any help? ')
print('okay, Get in touch')

print('==============task 3=============')

url = input('Enter your url: ')
print(url.startswith('https://www.'))

print(url.replace('https://www.', name))
