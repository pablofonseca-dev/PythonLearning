current_usernames = ['alice92pm', 'john3324', 'dereck2020p']
new_users = ['Geo5642', 'Kyle123', 'ALICE92PM', 'DeReCk2020P', 'john3324']

for current_user in new_users:
    if current_user.lower() in current_usernames:
        print('Sorry but the name ' + current_user + ' is not available')
    else:
        print('The name ' + current_user + ' is available!')

