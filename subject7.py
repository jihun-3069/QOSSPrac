def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor += 1    # divisor를 줄을 두번째 while이랑 같이 맞추고 
    return factors    #s추가 하고 

number = int(input("소인수분해할 수를 입력하세요: "))         ## 이걸 float말고 int로 해야함.
print(f"{number}의 소인수분해 결과:", prime_factors(number))  # 