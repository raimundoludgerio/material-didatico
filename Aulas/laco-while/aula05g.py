while True:
    n = int(input("De qual número você quer ver a tabuada? "))
    if n < 0:
        break
    print("=" * 80)
    for i in range(1,11):
        print(f"{n} X {i} = {i * n}".center(40))
    print("=" * 80)
