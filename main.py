USER = 'Admin'
PASS = 'pass@123'

username = input('Username: ')

if username != USER:
    print('Usuário inexistente.')
else:
    password = input('Password: ')
    if password == PASS:
        print('Acesso autorizado.')
    else:
        print('A senha não confere.')
