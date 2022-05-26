def fizzBuzz(n):
    for i in range(1,100):
       
        if n % 3 == 0:    
            print("Fizz\n")                                        
            continue
     
        elif n % 5 == 0:        
            print("Buzz\n")                                    
            continue
        
        # Print numbers
        print(n + "\n" )

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)