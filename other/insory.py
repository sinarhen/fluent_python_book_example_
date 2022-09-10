from array import array
import random


# floats = array('d', (random.random() for i in range(10**7)))
# fp = open('bin.bin', 'wb')
# floats.tofile(fp)
# fp.close()
floats = array('d')
fp = open('../bin.bin', 'rb')
r = floats.fromfile(fp, 10**7)
fp.close()
print(r[-1])
