numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ordinal_numbers = []
end_with = '';
for num in numbers:
    if num == 1:
        end_with = 'st'
    elif num == 2:
        end_with = 'nd'
    else:
        end_with = 'th'
    ordinal_numbers.append(str(num) + end_with)

print(ordinal_numbers);

