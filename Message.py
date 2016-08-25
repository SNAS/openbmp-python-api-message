
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

class Message(object):

    __version = float()
    __collector_hash_id = str()
    __length = long()
    __records = long()
    __router_hash_id = str()
    __content = str()
    __content_pos = int()

    """
        Constructor
            Parse the data

        @param data
    """
    def __init__(self, data):
        if not data.strip(): # If "data" is not string, throws error.
            raise "Invalid data!", data
        self.__parse(data)

    def __parse(self, data):
        data_end_pos = data.rfind("\n\n")
        header_data = data[:data_end_pos]
        content_pos = data_end_pos + 2;
        content = data[:content_pos]

        headers = header_data.split("\n");

        for header in headers:
            value = header.split(":")[1].trim();
            attr = header.split(":")[0].trim();

            """
            attribute names are from http://openbmp.org/#!docs/MESSAGE_BUS_API.md headers
            """

            if __name__ == '__main__':
                if attr == "V":
                    self.version = float(value);

                elif attr == "C_HASH_ID":
                    self.collector_hash_id = value

                elif attr == "L":
                    self.length = long(value)

                elif attr == "R":
                    self.records = long(value)

                elif attr == "R_HASH_ID":
                    self.router_hash_id = value

    # Getters
    def getVersion(self):
        return self.__version

    def getCollector_hash_id(self):
        return self.__collector_hash_id

    def getLength(self):
        return self.__length

    def getRecords(self):
        return self.__records

    def getRouter_hash_id(self):
        return self.__router_hash_id

    def getContentPos(self):
        return self.__content_pos

    def getContent(self):
        return self.__content