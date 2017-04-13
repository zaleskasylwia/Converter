


def converter_binary(number): #z dziesietnego na binarny
    a = []
    #print(number)
    while number > 0:
        a.append(number % 2)
        number = int(number / 2)
    print_backward(a)
    print (" 2")


def converter_decimal(number): # z binarnego na dziesietny
    decimal = 0
    for digit in str(number):
        decimal = decimal*2 + int(digit)
    print (decimal, "10")
    #print (" 10")



def print_backward(table): #funkcja aby napisać wynik od tylu
    length = len(table) - 1
    while length >= 0:
        print(table[length], end='')
        length -= 1

        
    

while True: 
    def main():
        print (""" Hello in binary and decimal converter
        First number which you'll write is a number to convert, after that the sesond number is responsible for the system
        '2' is for decimal, '10' is for binary """)

        input_read = input()
        try: 
            input_read = input_read.split()
            number = int(input_read[0])
            system = int(input_read[1])
            if system == 10:
                converter_binary(number)
            elif system == 2:
                converter_decimal(number)
        except ValueError:
            print("Game over")
  


    main()
    ask = ""
    while not (ask == 'YES' or ask== 'NO'):                                     #ask about game again
        ask = input("Do you want to try again? (YES/NO) ").upper()
    if ask == 'NO':
        break

    
    




