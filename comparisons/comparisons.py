the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

biggest = the_list[0]
for number in the_list:
    if number > biggest:
        biggest = number

print(biggest)