
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

class Message(object):

    """
        Constructor
            Parse the data

        @param data
    """
    def __init__(self, data):
        if not data.strip(): # If "data" is not string, throws error.
            raise "Invalid data!", data

        self.version = float()
        self.collector_hash_id = str()
        self.length = long()
        self.records = long()
        self.router_hash_id = str()
        self.content = str()
        self.content_pos = int()

        self.__parse(data)

    def __parse(self, data):
        data_end_pos = data.rfind("\n\n")
        header_data = data[:data_end_pos]

        self.content_pos = data_end_pos + 2;
        self.content = data[self.content_pos:]

        headers = header_data.split("\n");

        for header in headers:
            value = header.split(":")[1].strip();
            attr = header.split(":")[0].strip();

            """
            attribute names are from http://openbmp.org/#!docs/MESSAGE_BUS_API.md headers
            """

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
        return self.version

    def getCollector_hash_id(self):
        return self.collector_hash_id

    def getLength(self):
        return self.length

    def getRecords(self):
        return self.records

    def getRouter_hash_id(self):
        return self.router_hash_id

    def getContentPos(self):
        return self.content_pos

    def getContent(self):
        return self.content