while True:
    n = int(input("De qual número você quer ver a tabuada? "))
    if n < 0:
        break
    print("=" * 80)
    for i in range(1,10):
        print(f"{n} X {i} = {i * n}")
    print("=" * 80)
