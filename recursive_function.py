#author__uy_thea
#section_bscpe_2-2
#date_october_1_2024


values = [] #create a list named numbers

while True:
    try:
        
        for i in range(2):
            if i == 0:
                base = int(input("Enter the value of the base ")) #get the value of the base
                values.append(base)

            elif i == 1:
                exponent = int(input("Enter the value of the exponent ")) #get the value of the exponent
                values.append(exponent)



        def power (exponent): #recursive function 
            base = values[0]
            if exponent == 0: #if the exponent is 0, the function will return 1. a variable raise to 0 will always be one
                return 1
            
            elif exponent == 1: #if the exponent is 1, the function will return its base. a variable raise to one will always result to itself
                return base
            
            elif exponent == 2: #if the exponent is 2, the function will multiply the base by itself. 
                return base*base

            return (base**(exponent-1)) * (base) 

        output = power(values[1])
        print(output)
        break

    except:
        print("Invalid Output")
        continue

        

#end_of_the_program

