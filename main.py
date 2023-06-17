from typing import List
from urllib import parse
import random
import re


# 社会主义核心价值观加密

def enc(inp: str) -> str:
    def step3(inp: List[int]) -> str:
        VALUE = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'
        return ''.join(list(map(lambda v: VALUE[v << 1] + VALUE[v << 1 | 1], inp)))

    def step2(inp: str) -> List[int]:
        ans = []
        for c in inp:
            v = int(c, 16)
            if v < 10:
                ans.append(v)
            elif random.random() < 0.5:
                ans.append(11)
                ans.append(v - 6)
            else:
                ans.append(10)
                ans.append(v - 10)
        return ans

    def step1(inp: str) -> str:
        reg = re.compile(r'[A-Za-z0-9\-\_\.\!\~\*\'\(\)]')
        tmp = reg.sub(lambda g: hex(ord(g.group(0)))[2:], inp)
        return parse.quote(tmp).replace('%', '').upper()

    return step3(step2(step1(inp)))


# 社会主义核心价值观解密
def dec(enc: str) -> str:
    def step3(enc: str) -> List[int]:
        assert len(enc) % 2 == 0
        VALUE = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'
        ans = []
        for i in range(0, len(enc), 2):
            ans.append(VALUE.index(enc[i:i + 2]) >> 1)
        return ans

    def step2(enc: List[int]) -> str:
        ans = ''
        i = 0
        while i < len(enc):
            if enc[i] < 10:
                ans += str(enc[i])
                i += 1
            elif enc[i] == 10:
                ans += hex(enc[i + 1] + 10)[2:]
                i += 2
            elif enc[i] == 11:
                ans += hex(enc[i + 1] + 6)[2:]
                i += 2
            else:
                raise f'step2 failed. 不合法数据{enc}'
        return ans

    def step1(enc: str) -> str:
        tmp = ''
        for i in range(len(enc)):
            if not i % 2:
                tmp += '%'
            tmp += enc[i]
        return parse.unquote(tmp)

    return step1(step2(step3(enc)))

