
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""

from .Base import Base
from .FieldProcessors import ParseNullAsEmpty, ParseLongEmptyAsZero, ParseLong, ParseTimestamp, NotNull
from .Message import Message
from .MsgBusFields import MsgBusFields


class BaseAttribute(Base):
    """
    Format class for base_attribute parsed messages (openbmp.parsed.base_attribute)

    Schema Version: 1.7
    """

    minimum_header_names = [
        MsgBusFields.ACTION.get_name(),
        MsgBusFields.SEQUENCE.get_name(),
        MsgBusFields.HASH.get_name(),
        MsgBusFields.ROUTER_HASH.get_name(),
        MsgBusFields.ROUTER_IP.get_name(),
        MsgBusFields.PEER_HASH.get_name(),
        MsgBusFields.PEER_IP.get_name(),
        MsgBusFields.PEER_ASN.get_name(),
        MsgBusFields.TIMESTAMP.get_name(),
        MsgBusFields.ORIGIN.get_name(),
        MsgBusFields.AS_PATH.get_name(),
        MsgBusFields.AS_PATH_COUNT.get_name(),
        MsgBusFields.ORIGIN_AS.get_name(),
        MsgBusFields.NEXTHOP.get_name(),
        MsgBusFields.MED.get_name(),
        MsgBusFields.LOCAL_PREF.get_name(),
        MsgBusFields.AGGREGATOR.get_name(),
        MsgBusFields.COMMUNITY_LIST.get_name(),
        MsgBusFields.EXT_COMMUNITY_LIST.get_name(),
        MsgBusFields.CLUSTER_LIST.get_name(),
        MsgBusFields.ISATOMICAGG.get_name(),
        MsgBusFields.IS_NEXTHOP_IPV4.get_name(),
        MsgBusFields.ORIGINATOR_ID.get_name()
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

        super(BaseAttribute, self).__init__()

        if version >= float(1.7):
            version_specific_headers = [
                MsgBusFields.LARGE_COMMUNITY_LIST.get_name()
            ]
        else:
            version_specific_headers = []

        self.header_names = self.minimum_header_names + version_specific_headers
        self.spec_version = version
        self.processors = self.get_processors()

        if data:
            self.parse(self.spec_version, data)

    def get_processors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

        default_processors = [
            NotNull(),  # action
            ParseLong(),  # seq
            NotNull(),  # hash
            NotNull(),  # router hash
            NotNull(),  # router_ip
            NotNull(),  # peer_hash
            NotNull(),  # peer_ip
            ParseLong(),  # peer_asn
            ParseTimestamp(),  # timestamp
            ParseNullAsEmpty(),  # origin
            ParseNullAsEmpty(),  # as_path
            ParseLong(),  # as_path_count
            ParseLong(),  # origin_as
            ParseNullAsEmpty(),  # nexthop
            ParseLong(),  # med
            ParseLong(),  # local_pref
            ParseNullAsEmpty(),  # aggregator
            ParseNullAsEmpty(),  # community_list
            ParseNullAsEmpty(),  # ext_community_list
            ParseNullAsEmpty(),  # cluster_list
            ParseLongEmptyAsZero(),  # isAtomicAgg
            ParseLongEmptyAsZero(),  # isNexthopIPv4
            ParseNullAsEmpty()  # originator_id
        ]

        if self.spec_version >= float(1.7):
            version_specific_processors = [
                ParseNullAsEmpty()  # large communities
            ]
        else:
            version_specific_processors = []

        return default_processors + version_specific_processors
