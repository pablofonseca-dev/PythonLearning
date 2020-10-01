
guests = ['Camila', 'Tatiana', 'Julia', 'Felipe', 'Emmanuel', 'Danny', 'Mariella', 'Daniel'];

invite_message = "Diana and I want to invite you to a dinner at our house, I hope you come, we are waiting for you!";

print("Hello " + guests[0] + " " + invite_message);
print("Hello " + guests[1] + " " + invite_message);
print("Hello " + guests[2] + " " + invite_message);
print("Hello " + guests[3] + " " + invite_message);
print("Hello " + guests[4] + " " + invite_message);
print("Hello " + guests[5] + " " + invite_message);
print("Hello " + guests[6] + " " + invite_message);
print("Hello " + guests[7] + " " + invite_message);


# Changing Guest List
print(guests[4]);

guests.remove('Emmanuel');
guests.insert(4, 'Jose');

print(guests);

new_invite_message = 'dinner has not been canceled, we are still waiting for you at our house';

print("Hello " + guests[0] + " " + new_invite_message);
print("Hello " + guests[1] + " " + new_invite_message);
print("Hello " + guests[2] + " " + new_invite_message);
print("Hello " + guests[3] + " " + new_invite_message);
print("Hello " + guests[4] + " " + new_invite_message);
print("Hello " + guests[5] + " " + new_invite_message);
print("Hello " + guests[6] + " " + new_invite_message);
print("Hello " + guests[7] + " " + new_invite_message);


bigger_table_message = 'we found a bigger table!';

print("Hello " + guests[0] + " " + bigger_table_message);
print("Hello " + guests[1] + " " + bigger_table_message);
print("Hello " + guests[2] + " " + bigger_table_message);
print("Hello " + guests[3] + " " + bigger_table_message);
print("Hello " + guests[4] + " " + bigger_table_message);
print("Hello " + guests[5] + " " + bigger_table_message);
print("Hello " + guests[6] + " " + bigger_table_message);
print("Hello " + guests[7] + " " + bigger_table_message);


#Use insert() to add one new guest to the beggining of your list 
guests.insert(0, 'Charles');

#Use insert() to add one new guest to the middle of your list
guests.insert(int(len(guests) / 2), 'Johnathan');

#Use insert() to add one new guest to the end of your list
guests.append('Ken');
print(guests);
