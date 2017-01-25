
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import Base
from FieldProcessors import ParseTimestamp, ParseInt, ParseNullAsEmpty, NotNull, ParseLong
from Message import Message
from MsgBusFields import MsgBusFields


class Collector(Base):
    """
    Format class for collector parsed messages (openbmp.parsed.collector)

    Schema Version: 1.4
    """

    minimum_header_names = [
        MsgBusFields.ACTION.get_name(),
        MsgBusFields.SEQUENCE.get_name(),
        MsgBusFields.ADMIN_ID.get_name(),
        MsgBusFields.HASH.get_name(),
        MsgBusFields.ROUTERS.get_name(),
        MsgBusFields.ROUTER_COUNT.get_name(),
        MsgBusFields.TIMESTAMP.get_name()
    ]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.get_content()

        super(Collector, self).__init__()
        self.headerNames = Collector.minimum_header_names

        # Change below to supply version when version is required
        self.parse(self.spec_version, data)

    def get_processors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

        processors = [
            NotNull(),  # action
            ParseLong(),  # seq
            NotNull(),  # admin
            NotNull(),  # hash
            ParseNullAsEmpty(),  # routers
            ParseInt(),  # router count
            ParseTimestamp()  # Timestamp
        ]

        return processors
