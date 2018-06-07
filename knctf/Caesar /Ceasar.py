#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import io

def rot(c,i):
    if 'A' <= c and c <= 'Z':
        return chr((ord(c) - ord('A') + i) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        return chr((ord(c) - ord('a') + i) % 26 + ord('a'))

    return c


def rot13(s,i):
    g = (rot(c,i) for c in s)
    return ''.join(g)


if __name__ == '__main__':
    s = 'EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.'
    for i in range(1,26):
        print(rot13(s,i))