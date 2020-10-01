users = ['erick', 'john', 'admin', 'luke', 'warner', 'josh']

if len(users) >= 1:
    for user in users:
        if user.lower() == 'admin':
            print('Hello ' + user.title() + ', would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', thank you for logging again')
else:
    print('We need to find some users!')