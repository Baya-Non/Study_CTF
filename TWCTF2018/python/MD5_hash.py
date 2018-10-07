import hashlib
import sys

def decryptMD5(testHash):
        s = []
        while True:
                m = hashlib.md5()
                for c in s:
                        m.update(chr(c))
                hash = m.hexdigest()
                #(hash)
                if hash == testHash:
                        return ''.join([chr(c) for c in s])
                wrapped = True
                for i in range(0, len(s)):
                        s[i] = (s[i] + 1) % 126
                        if s[i] != 0:
                                wrapped = False
                                break
                if wrapped:
                        s.append(0)

hashstring="c019f6e5cd8aa0bbbcc6e994a54c757e"
print(decryptMD5(hashstring))

