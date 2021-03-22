lst = []
lst = [int(item) for item in input( ).split()]

c = sum(lst)

print(f'{c-max(lst)} {c-min(lst)}')




