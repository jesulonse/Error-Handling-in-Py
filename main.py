# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    if len(userInput) == 2:
        try:
            number = userInput
        #if len(number) == 2:#Ensure the length of inputs is 2
            number = int(number)
        
            user_list.append(number) 
            if number % 2 == 0:#Ensure that input is divisible by 2
                list_sum += number      
        except ValueError:
            print("Incorrect value. That's not an int!")
        except Exception as e:
            print("Wrong length of number: {}".format(e))
    else:
        print("Wrong length of input")
   
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    """
    try:
        number = userInput
        if len(number) == 2:#Ensure the length of inputs is 2
            number = int(number)
        
            user_list.append(number) 
            if number % 2 == 0:#Ensure that input is divisible by 2
                list_sum += number      
    except ValueError:
        print("Incorrect value. That's not an int!")
    except Exception as e:
        print("Wrong length of number: {}".format(e))
        """
        

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))