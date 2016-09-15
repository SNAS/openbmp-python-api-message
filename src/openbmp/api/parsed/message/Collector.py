
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import *
from FieldProcessors import *
from Message import *
from MsgBusFields import MsgBusFields

class Collector(Base):
    """
        Format class for collector parsed messages (openbmp.parsed.collector)

        Schema Version: 1.2
    """

    minimumHeaderNames = [MsgBusFields.ACTION.getName(),MsgBusFields.SEQUENCE.getName(),MsgBusFields.ADMIN_ID.getName(),
                          MsgBusFields.HASH.getName(),MsgBusFields.ROUTERS.getName(),MsgBusFields.ROUTER_COUNT.getName(),
                          MsgBusFields.TIMESTAMP.getName()]


    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.getContent()

        super(Collector, self).__init__()
        self.headerNames = Collector.minimumHeaderNames

        # Change below to supply version when version is required
        self.parse(self.spec_version, data)

    def getProcessors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

        processors = [

            NotNull(), # action
            ParseLong(), # seq
            NotNull(), # admin
            NotNull(), # hash
            ParseNullAsEmpty(), # routers
            ParseInt(), # router count
            ParseTimestamp() # Timestamp
        ]

        return processors
