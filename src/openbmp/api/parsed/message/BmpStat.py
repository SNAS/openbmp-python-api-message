
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""

from .Base import Base
from .FieldProcessors import NotNull, ParseTimestamp, ParseLong
from .Message import Message
from .MsgBusFields import MsgBusFields


class BmpStat(Base):
    """
    Format class for bmp_stat parsed messages (openbmp.parsed.bmp_stat)

    Schema Version: 1.4
    """

    minimum_header_names = [
        MsgBusFields.ACTION.get_name(),
        MsgBusFields.SEQUENCE.get_name(),
        MsgBusFields.ROUTER_HASH.get_name(),
        MsgBusFields.ROUTER_IP.get_name(),
        MsgBusFields.PEER_HASH.get_name(),
        MsgBusFields.PEER_IP.get_name(),
        MsgBusFields.PEER_ASN.get_name(),
        MsgBusFields.TIMESTAMP.get_name(),
        MsgBusFields.REJECTED.get_name(),
        MsgBusFields.KNOWN_DUP_UPDATES.get_name(),
        MsgBusFields.KNOWN_DUP_WITHDRAWS.get_name(),
        MsgBusFields.INVALID_CLUSTER_LIST.get_name(),
        MsgBusFields.INVALID_AS_PATH.get_name(),
        MsgBusFields.INVALID_ORIGINATOR.get_name(),
        MsgBusFields.INVALID_AS_CONFED.get_name(),
        MsgBusFields.PRE_POLICY.get_name(),
        MsgBusFields.POST_POLICY.get_name()
    ]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.get_content()

        super(BmpStat, self).__init__()
        self.header_names = BmpStat.minimum_header_names

        self.processors = self.get_processors()

        if data:
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
            NotNull(),  # hash
            NotNull(),  # router_ip
            NotNull(),  # peer_hash
            NotNull(),  # peer_ip,
            ParseLong(),  # peer_asn
            ParseTimestamp(),  # Timestamp
            NotNull(),  # rejected
            NotNull(),  # known_dup_updates
            NotNull(),  # known_dup_withdraws
            NotNull(),  # invalid_cluster_list
            NotNull(),  # invalid_as_path
            NotNull(),  # invalid_originator
            NotNull(),  # invalid_as_confed
            NotNull(),  # pre_policy
            NotNull()  # post_policy
        ]

        return processors
