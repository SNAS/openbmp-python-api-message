
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import *
from FieldProcessors import *

class Router(Base):
    """
        Format class for router parsed messages (openbmp.parsed.router)

        Schema Version: 1.2
    """

    def __init__(self, version, data):
        """
        Handle the message by parsing it and storing the data in memory.

        :param version: Schema version of the message.
        :param data: Data to parse.
        """

        super(Router, self).__init__()
        self.spec_version = version

        if version >= float(1.2):

            self.headerNames = ["action", "seq", "name", "hash", "ip_address", "description", "term_code",
                "term_reason", "init_data", "term_data", "timestamp", "bgp_id"]

        else:

            self.headerNames = ["action", "seq", "name", "hash", "ip_address", "description", "term_code",
                "term_reason", "init_data", "term_data", "timestamp"]

        self.parse(version, data)

    def getProcessors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

        processors = None

        if self.spec_version >= float(1.2):

            processors = [

                NotNull(), # action
                ParseLong(), # seq
                ParseNullAsEmpty(), # name
                NotNull(), # hash
                NotNull(), # IP Address
                ParseNullAsEmpty(), # Description
                ParseInt(), # Term code
                ParseNullAsEmpty(), # Term reason
                ParseNullAsEmpty(), # Init data
                ParseNullAsEmpty(), # Term data
                ParseTimestamp(), # Timestamp
                ParseNullAsEmpty() # Global BGP - ID for router
            ]

        else:

            processors = [

                NotNull(), # action
                ParseLong(), # seq
                ParseNullAsEmpty(), # name
                NotNull(), # hash
                NotNull(), # IP Address
                ParseNullAsEmpty(), # Description
                ParseInt(), # Term code
                ParseNullAsEmpty(), # Term reason
                ParseNullAsEmpty(), # Init data
                ParseNullAsEmpty(), # Term data
                ParseTimestamp() # Timestamp
            ]

        return processors
