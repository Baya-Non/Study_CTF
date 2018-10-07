import hashlib 

ans = '1c9ed78bab3f2d33140cbce7ea223894'

# for name in hashlib.algorithms_guaranteed:
    # print(name)
i = 0
for line in open('list.txt', encoding='ascii'):
    code = bytes(line.strip(), encoding='ascii')
    hashed = hashlib.new('hmac', code).hexdigest()
    i = i+ 1
    #print(hashed)

    if hashed == ans:
        print('@@@@@@')
        print(code)
        print('@@@@@@')
        # print(hashed)

# print(hashlib.algorithms_guaranteed)