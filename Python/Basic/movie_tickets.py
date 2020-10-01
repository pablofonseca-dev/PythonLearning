members = [

]

prompt = "Welcome to the movie tickets, buy a ticket!\n"


keyword = "exit"

active = True

while(active):
    log_intro = "Enter the following data for each member you want to add:"
    print(log_intro)
    member_name = input("Member Name: ")
    age = input("Member Age: ")
    ticket_cost = 0.0
    int_age = int(age)
    #Age validations
    if(int_age >= 3 and int_age <= 12):
        ticket_cost = 10.0
    elif(int_age > 12): 
        ticket_cost = 15.0
    
    #Generate Dictionary 
    new_member = {}

    new_member['member_name'] = member_name
    if(ticket_cost == 0.0):
        new_member['ticket_cost'] = "FREE"
    else:
        new_member['ticket_cost'] = str(ticket_cost)
    members.append(new_member)

    #Ask to add another member
    prompt = "Do you want to add another member? (Y/N) \n>>> "

    user_selection = input(prompt)
    if(user_selection.upper() == 'N'):
        active = False
    
#Print All The Information
print("These is the information that you enter: ")
for list_item in members:
    print("Name: " + list_item['member_name'])
    if(list_item['ticket_cost'] == 'FREE'):
        print("Ticket Cost: " + list_item['ticket_cost'])
    else:
        print("Ticket Cost: " + "$" + list_item['ticket_cost'])

#Print Total To Pay 

#Calc Total To Pay
total = 0.0
for list_item in members:
    if(not(list_item['ticket_cost'] == 'FREE')):
        total += float(list_item['ticket_cost'])
print("The total you need to pay is: " + "$" + str(total))



