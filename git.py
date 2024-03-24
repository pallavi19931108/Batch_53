#print the even number from list using list function
def even(lis):
    for i in lis:
        if i % 2 ==0:
            print(i)
    lis = [1,2,3,4,5,6,7,8,9,10]
    even(lis)
