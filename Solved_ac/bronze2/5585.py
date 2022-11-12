#5585 거스름돈

import sys

charge = 1000 - int(sys.stdin.readline())

coin = charge // 500
charge %= 500
coin += (charge // 100)
charge %= 100
coin += (charge // 50)
charge %= 50
coin += (charge // 10)
charge %= 10
coin += (charge // 5)
charge %= 5
coin += charge

print(coin)