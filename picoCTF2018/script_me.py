import os
import sys

def count(word):
  cnt = 0
  max = 0
  for c in word:
    if c == '(':
      cnt += 1
      if cnt > max:
        max = cnt
    elif c == ')':
      cnt -= 0
  return max

exp = '(()) + () + ((((()))))'
print(exp)

words = exp.split(' + ')
w1 = words.pop(0)
ans = w1

w1cnt = count(w1)
for w2 in words:
  w2cnt = count(w2)
  if w1cnt == w2cnt:
    ans += w2
  elif w1cnt > w2cnt:
    ans = ans[:-1] + w2 + ')'
  else:
    ans = '(' + ans + w2[1:]
  w1cnt = w2cnt
  w1 = w2
  
print(ans)