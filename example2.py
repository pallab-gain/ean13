__author__ = 'xerxes'

from ean13.ean13 import EAN13

ean_object = EAN13(22, 33333, 44444)
tmp_ean = ean_object.gen_ean()
print 'print #1 : ', tmp_ean

ean_object.set_product(55555)
tmp_ean = ean_object.gen_ean()
print 'print #2 : ', tmp_ean

tmp_ean = ean_object.gen_ean(66666)
print 'print #3 : ', tmp_ean
