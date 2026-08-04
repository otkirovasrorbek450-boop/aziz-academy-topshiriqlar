try:
    n = int(input())
    if 10 <= n <= 99:
        tens = n // 10
        ones = n % 10
        print(f"Tens: {tens}")
        print(f"Ones: {ones}")
    else:
        print("BAD")
except:
    print("BAD")