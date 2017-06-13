
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import Base
from FieldProcessors import ParseNullAsEmpty, ParseTimestamp, ParseInt, NotNull, ParseLong
from Message import Message
from MsgBusFields import MsgBusFields


class Router(Base):
    """
    Format class for router parsed messages (openbmp.parsed.router)

    Schema Version: 1.4
    """

    minimum_header_names = [
        MsgBusFields.ACTION.get_name(),
        MsgBusFields.SEQUENCE.get_name(),
        MsgBusFields.NAME.get_name(),
        MsgBusFields.HASH.get_name(),
        MsgBusFields.IP_ADDRESS.get_name(),
        MsgBusFields.DESCRIPTION.get_name(),
        MsgBusFields.TERM_CODE.get_name(),
        MsgBusFields.TERM_REASON.get_name(),
        MsgBusFields.INIT_DATA.get_name(),
        MsgBusFields.TERM_DATA.get_name(),
        MsgBusFields.TIMESTAMP.get_name()
    ]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        version = message.get_version()
        data = message.get_content()

        super(Router, self).__init__()
        self.spec_version = version

        if version >= float(1.2):
            version_specific_headers = [MsgBusFields.BGP_ID.get_name()]
        else:
            version_specific_headers = []

        # Concatenate minimum header names and version specific header names.
        self.header_names = Router.minimum_header_names + version_specific_headers

        self.processors = self.get_processors()

        if data:
            self.parse(version, data)


    def get_processors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

        default_cell_processors = [
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
            version_specific_processors = [
                ParseNullAsEmpty()  # Global BGP - ID for router
            ]
        else:
            version_specific_processors = []

        return default_cell_processors + version_specific_processors
