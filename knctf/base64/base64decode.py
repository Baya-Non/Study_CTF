import os
import sys
import base64
import uu
from io import StringIO
from codecs import decode

if __name__ == '__main__':
	f = open('base64.txt')
	data1 = f.read()  # ファイル終端まで全て読んだデータを返す
	f.close()
	for x in range(0,2):
		data1 = base64.b64decode(data1)
	print(data1)

