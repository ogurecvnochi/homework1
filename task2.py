s = input('Введите список чисел через пробел: ')
nums = list(map(int, s.split()))
if len(set(nums)) == 1:
    print("Второго по величине элемента нет")
else:
    nums_set = sorted(set(nums))
    print(nums_set[-2])