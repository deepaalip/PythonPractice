import pytest
def swapNibbles(number):
	return ( (number & 0x0F)<<4 | (number & 0xF0)>>4 )

number = 100
print(swapNibbles(number))

