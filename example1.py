__author__ = 'xerxes'

from ean13.ean13 import EAN13

ean_object = EAN13()
tmp_ean = ean_object.gen_ean()
print tmp_ean
