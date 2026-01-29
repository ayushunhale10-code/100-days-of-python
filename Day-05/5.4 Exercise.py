print("lets start with fizz buzz game")
i=range(1,101)
for m in i:
    if m%3==0 and m%5 == 0:
        print("fizzbuzz")
    elif m%3==0:
        print("fizz")
    elif m%5==0:
        print("buzz")
    else:
        print(m)
