import re
import socket

host = '2018shell2.picoctf.com'
port = 50430

def recv_via(sock):
    resp = sock.recv(2048).decode('utf-8')
    print('[+] {0}'.format(resp))
    return resp

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    res = recv_via(s)
    res = recv_via(s)
    q = int(re.search(r'q : (\d+)', res).group(1))
    p = int(re.search(r'p : (\d+)', res).group(1))

    res = s.send(b'Y\n')
    res = recv_via(s)
    res = recv_via(s)

    n = p * q
    msg = (str(n) + '\n').encode('utf-8')
    s.send(msg)
    print('>> {0}'.format(msg))

    res = recv_via(s)
    res = recv_via(s)
    p = int(re.search(r'p : (\d+)', res).group(1))
    n = int(re.search(r'n : (\d+)', res).group(1))
    q = n // p

    res = s.send(b'Y\n')
    res = recv_via(s)
    msg = (str(q) + '\n').encode('utf-8')
    s.send(msg)
    print('>> {0}'.format(msg))

    res = recv_via(s)
    res = recv_via(s)
    res = s.send(b'Y\n')
    res = recv_via(s)
    res = recv_via(s)

    # s.send((str(n) + '\n').encode('utf-8'))
    # print(n)