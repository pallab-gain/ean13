Yet Another EAN13 code generator
    How to use:
    
        class name:
            EAN13
        parameters:
            country_code ( default = 88 ) : type integer
            manufacturer_code ( default = 12345 ): type integer
            product_code ( default = 12345 ) : type integer

        return:
            thirteen digit ean13 number: type string

        available methods:
            1. sanitize_ean13:
                    parameters:
                        number ( mandatory ) : type integer
                        s_type ( default = 'C' ) : type char
                            available s_type:
                                'C' for country
                                'M' for manufacturer
                                anything else for product
                    return:
                        sanitized country, manufacturer, or product code : type string



            2. set_country:
                    parameters:
                        //takes two digit country code
                        country_code ( default = 88 ): type integer
                    return:
                        none
            3. set_manufacturer:
                    parameters:
                        //takes five digit manufacturer code
                        manufacturer_code( default = 12345): type integer
                    return:
                        none
            4. set_product:
                    parameters:
                        //takes five digit product code
                        product_code( default = 12345): type integer
                    return:
                        none

            5. merge:
                    parameters:
                        //merge country, manufacture and product code in order to get 12 digit ean number
                        none
                    return:
                        none

            6. calculate_checksum
                    parameters:
                        //calculate checksum of 12 digit ean number
                        none
                    return:
                        none
            7. gen_ean:
                    parameters:
                        //generate 13 digit ean13 number
                        product_code ( default = 12345 ): type integer
                    return:
                        13 digit ean13 number: type string

Example Use:
        example 1:

        ean = EAN13() #country code will set to default 88
                    #manufacturer code will set to default 12345
                    #product code will set to default 12345


        tmp_ean = ean.gen_ean()   #will generate 13 digit ean13 number and return it
        print tmp_ean

     example 2:
        ean = EAN13(22,33333,44444) #take customer country, manufacturer and product code
        tmp_ean = ean.gen_ean()   #will generate 13 digit ean13 number and return it
        tmp_ean = ean.get(55555)  #will generate 13 digit ean13 number for new product ( new product with given product code as 55555 ) and return it

        print tmp_ean

