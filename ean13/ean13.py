__author__ = 'xerxes'


class EAN13:
    product = manufacture = country = None
    code = checksum = None

    def __init__(self, country_code=88, manufacturer_code=12345, product_code=12345):
        self.country = self.sanitize_ean13(country_code, 'C')
        self.manufacture = self.sanitize_ean13(manufacturer_code, 'M')
        self.product = self.sanitize_ean13(product_code, 'P')


    @staticmethod
    def sanitize_ean13(number=None, s_type='C'):
        if not number:
            raise Exception('Number cannot be empty')

        cur_len = None
        if s_type == 'C':
            if not isinstance(number, int):
                raise Exception('Country code must be integer')
            if str(number).__len__() > 2:
                raise Exception('country code length must not be less than two')
            cur_len = 2
        elif s_type == 'M':
            if not isinstance(number, int):
                raise Exception('manufacturer code must be integer')
            if str(number).__len__() > 5:
                raise Exception('manufacturer code length must not be less than five')
            cur_len = 5
        else:
            if not isinstance(number, int):
                raise Exception('product code must be integer')
            if str(number).__len__() > 5:
                raise Exception('product code length must not be less than five')
            cur_len = 5

        number = str(number)
        while number.__len__() < cur_len:
            number = '0' + number
        return number

    def set_country(self, country_code=88):
        self.country = self.sanitize_ean13(country_code, 'C')

    def set_manufacturer(self, manufacturer_code=12345):
        self.manufacture = self.sanitize_ean13(manufacturer_code, 'M')

    def set_product(self, product_code=12345):
        self.product = self.sanitize_ean13(product_code, 'P')

    def merge(self):
        self.code = ''.join([self.country, self.manufacture, self.product])

    def calculate_checksum(self):
        odd_sum = 0
        evn_sum = 0
        for i in xrange(0, 12):
            if i and 1:
                odd_sum += int(self.code[i])
            else:
                evn_sum += int(self.code[i])

        self.checksum = str((10 - (((3 * odd_sum) + evn_sum) % 10)) % 10)

    def gen_ean(self, product_code=None):
        if product_code:
            self.set_product(product_code)

        self.merge()
        self.calculate_checksum()
        return ''.join([self.code, self.checksum])
