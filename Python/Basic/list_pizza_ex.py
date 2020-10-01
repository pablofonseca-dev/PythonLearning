available_toppins  = ['mooshrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese'];

requested_toppins = ['pineapple', 'onion', 'pepperoni', 'apple', 'extra cheese'];

if(len(requested_toppins) >= 1):
    for requested_toppin in requested_toppins:
        if(requested_toppin not in available_toppins):
            print(requested_toppin.title() + " is not available");
        else:
            print("Adding " + requested_toppin.title() + " to your pizza!");
else:
    print('Are you sure you want a plain pizza?');

print('\nFinishing making your pizza!')