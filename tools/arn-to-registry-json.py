import xml.etree.ElementTree as ET
import uuid
import os
import time
import logging
import logging.handlers
import uuid

class ScriptLogger():
    def __init__(self):
        self.log_file_name = 'logs/latest.log'
        self.path = os.getcwd()
        self.logpath = os.path.join(self.path, 'logs')
        if not os.path.exists(self.logpath):
            os.mkdir(self.logpath)
        self.logging_level = logging.INFO
        # set TimedRotatingFileHandler for root
        self.formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
        # use very short interval for this example, typical 'when' would be 'midnight' and no explicit interval
        self.handler = logging.handlers.TimedRotatingFileHandler(self.log_file_name, when="S", interval=30, backupCount=10)
        self.handler.setFormatter(self.formatter)
        self.logger = logging.getLogger() # or pass string to give it a name
        self.logger.addHandler(self.handler)
        self.logger.setLevel(self.logging_level)
    def getLogger(self):
        return self.logger

class DataFixtureCreator():
    def create_operator(self):
        id = str(uuid.uuid4())
        return {"model":"registry.operator", "pk":id, "fields":{"company_name":"", "website":"", "email":"", "phone_number":"", "operator_type":"", "address":"", "operational_authorizations":"", "authorized_activities":"", "vat_number":"", "insurance_number":"", "company_number":"", "country":""}}

    def create_owner(self):
        id = str(uuid.uuid4())
        return {"model":"registry.person", "pk":id, "fields":{}}

    def create_contact(self):
        id = str(uuid.uuid4())
        return {"model":"registry.contact", "pk":id, "fields":{"first_name":"", "middle_name":"", "last_name":"", "email":"", "phone_number":"", "identification_number":""}}

    def create_address(self):
        id = str(uuid.uuid4())
        return {"model":"registry.address", "pk":id, "fields":{"address_line_1":"", "address_line_2":"", "address_line_3":"", "postcode":"", "city":"", "country":""}}

    def create_manufacturer(self):
        id = str(uuid.uuid4())
        return {"model":"registry.address", "pk":id, "fields":{"full_name":"", "common_name":"", "address":"","acronym":"", "role":"", "country":""}}


    def create_type_certificate(self):
        id = str(uuid.uuid4())
        return {"model":"registry.typecertificate", "pk":id, "fields":{"type_certificate_id":"", "type_certificate_issuing_country":"", "type_certificate_holder":"", "type_certificate_holder_country":""}}


    def create_aircraft(self):
        id = str(uuid.uuid4())
        return {"model":"registry.aircraft", "pk":id, "fields":{"operator":"","mass":0,"is_airworthy":1, "make":"", "model":"","master_series":"","series":"","popular_name":"", "manufacturer":"", "category":"","registration_mark":"", "sub_category":"", "icao_aircraft_type_designator":"", "max_certified_takeoff_weight":0,"esn":0, "maci_number":"" , "status":1 }}



if __name__ == "__main__":    
    myLogger = ScriptLogger()
    logger = myLogger.getLogger()
    myDataFixtureCreator = DataFixtureCreator()
    output_data = []

    # Global lookup for Aircraft
    TAG_DICT = {'IRCA_ID':"", "REGISTRATION_MARK":"registration_mark", "MANUFACTURER":"" ,"MAKE":"make", "MODEL":"model","SERIES1":"master_series", "SERIES2":"series","BAPTISM":"popular_name", "SER_NUM":"","OWNER_NAME":"", "OWNER_ADD_1":"address_line_1", "OWNER_ADD_2":"address_line_2", "OWNER_ADD_3":"address_line_3","OWNER_STATE":"", "OPERATOR_NAME":"", "OPERATOR_ADD_1":"address_line_1", "OPERATOR_ADD_2":"address_line_2", "OPERATOR_ADD_3":"address_line_3","OPERATOR_STATE":"", "AUTHORITY":"", "CONTACT":"", "NAT_REG":"", "REGISTRATION_DATE":"", "UPDATE_DATE":""}

    IGNORE_TAG_LIST = ['OWNER_ADD','OPERATOR_ADD']

    # root = ET.parse('icao.xml').getroot()
    root = ET.parse('ICAO.xml').getroot()
    
    search_keys = TAG_DICT.keys();
    for t in root.findall('.//AIRCRAFT/*'):
        address_tree = t.getchildren()

        if address_tree:
            address = myDataFixtureCreator.create_address()
            for child in address_tree:
                if child.tag not in search_keys and \
                    child.tag not in IGNORE_TAG_LIST:
                        logger.info("%s tag not in Tag Dict and IGNORE LIST" % child.tag)
                else:
                    # create JSON
                    second_level_children = child.getchildren()
                    if second_level_children: 
                        # address entities 
                        for cur_second_level_children in second_level_children: 
                            # print(TAG_DICT[cur_second_level_children.tag], cur_second_level_children.text)
                            address['fields'][TAG_DICT[cur_second_level_children.tag]] = cur_second_level_children.text
                    else:
                        pass
            output_data.append(address)

        else:
            if not t.tag in search_keys:
                logger.info("%s tag not in Tag Dict" % t.tag)
                
            else:
                # pass
                print(t.tag, t.text)
                aircraft = myDataFixtureCreator.create_aircraft()
                # check if the keys exist

                # create JSON

    # print(output_data)
