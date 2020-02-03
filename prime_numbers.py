

def find_prime_numbers(n1,n2):
    prime_numbers = []
    for number in range(n1,n2+1):
        if number > 1:
          for i in range(2,number):
            if number%i == 0:
                break
          else:
            prime_numbers.append(number)
    
    #prime_numbers.append( number )
    return prime_numbers

if __name__ == '__main__':
    prime_numbers = find_prime_numbers(10,20)
    print(f'{prime_numbers}')