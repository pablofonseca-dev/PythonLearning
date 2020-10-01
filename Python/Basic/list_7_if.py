#Para averiguar si un elemento está en una lista
requested_toppins = ['mushrooms', 'onions', 'pineapple']

validate_toppins = ['mushrooms', 'onions', 'watermelon'];

for toppin in validate_toppins:
	if(toppin in requested_toppins):
		print(str(toppin) + ' is in the list');
	else:
		print(str(toppin) + ' is NOT in the list');

#Para averiguar si un elemento NO está en una listat

banned_users = ['andrew', 'carolina', 'david'];

want_to_comment = ['alex', 'aurelio', 'victor', 'steve', 'andrew', 'carolina', 'kenneth'];

for user in want_to_comment:
	if(user.lower() not in banned_users):
		print(user.title() + ", you can post if you wish.");
	else:
		print('Sorry ' + user.title() + ", you are banned and can't post in this app");

