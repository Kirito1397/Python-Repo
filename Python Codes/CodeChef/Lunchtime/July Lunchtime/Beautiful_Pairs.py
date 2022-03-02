# cook your dish here
t = int(input())
for _ in range(t):
    the_tot_count = int(input())
    my_numbers = map(int, input().split())
    secret_dictionary = {}
    for i in my_numbers:
        if i not in secret_dictionary:
            secret_dictionary[i] = 1
        else:
            secret_dictionary[i] = secret_dictionary[i] + 1
        print(secret_dictionary)
    beautiful_pairs = 0
    for i in secret_dictionary:
        beautiful_pairs += secret_dictionary[i] * (the_tot_count - secret_dictionary[i])
    print(beautiful_pairs)