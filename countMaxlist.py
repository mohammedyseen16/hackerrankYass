n = int(input(''))

ele = list(map(int,input("").strip().split()))[:n]

print(ele.count(max(ele)))
