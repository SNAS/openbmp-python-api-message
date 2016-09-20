
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

class Router(Base):
    """
        Format class for router parsed messages (openbmp.parsed.router)

        Schema Version: 1.2
    """

    minimumHeaderNames = [MsgBusFields.ACTION.getName(),MsgBusFields.SEQUENCE.getName(),MsgBusFields.NAME.getName(),MsgBusFields.HASH.getName(),MsgBusFields.IP_ADDRESS.getName(),
                            MsgBusFields.DESCRIPTION.getName(),MsgBusFields.TERM_CODE.getName(),MsgBusFields.TERM_REASON.getName(),MsgBusFields.INIT_DATA.getName(),MsgBusFields.TERM_DATA.getName(),
                            MsgBusFields.TIMESTAMP.getName()]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        version = message.getVersion()
        data = message.getContent()

        super(Router, self).__init__()
        self.spec_version = version

        if version >= float(1.2):

            versionSpecificHeaders = [MsgBusFields.BGP_ID.getName()]

        else:

            versionSpecificHeaders = []

        # Concatenate minimum header names and version specific header names.
        self.headerNames = Router.minimumHeaderNames + versionSpecificHeaders
        self.parse(version, data)

    def getProcessors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

        defaultCellProcessors = [

            NotNull(),  # action
            ParseLong(),  # seq
            ParseNullAsEmpty(),  # name
            NotNull(),  # hash
            NotNull(),  # IP Address
            ParseNullAsEmpty(),  # Description
            ParseInt(),  # Term code
            ParseNullAsEmpty(),  # Term reason
            ParseNullAsEmpty(),  # Init data
            ParseNullAsEmpty(),  # Term data
            ParseTimestamp()  # Timestamp
        ]

        if self.spec_version >= float(1.2):

            versionSpecificProcessors = [

                ParseNullAsEmpty()  # Global BGP - ID for router
            ]

        else:

            versionSpecificProcessors = []

        return defaultCellProcessors + versionSpecificProcessors
