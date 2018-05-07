def to_roman(data):

    cyph={1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

    result = ""


    while data > 0:    

        list_sort = sorted([i for i in cyph if i<=data], reverse = True)

        result += cyph[list_sort[0]]

        data -= list_sort[0]

    return result

    
data = int(input("Enter the number: "))
print(to_roman(data))
