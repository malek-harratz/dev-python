def boucle():

    for m in range (0,101) :
        if m % 3 == 0 and m % 5 == 0 :
            print ("fizzbuzz")
        elif m % 3 == 0 :
            print ("fizz")
        elif m % 5 ==0 : 
            print ("buzz")
        else :
            print (m)
boucle()

