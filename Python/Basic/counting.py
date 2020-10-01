prompt = "Type a number\n>>> "
iterations_num = int(input(prompt).lstrip())
counter = 0
while(counter < iterations_num):
    counter += 1
    if(counter % 2 == 0):
        continue
    else:
        print(counter)
