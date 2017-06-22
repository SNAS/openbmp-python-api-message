
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import Base
from FieldProcessors import ParseNullAsEmpty, ParseLongEmptyAsZero, ParseInt, NotNull, ParseTimestamp, ParseLong
from Message import Message
from MsgBusFields import MsgBusFields


class L3VpnPrefix(Base):
    """
    Format class for unicast_prefix parsed messages (openbmp.parsed.unicast_prefix)

    Schema Version: 1.4
    """

    minimum_header_names = [
        MsgBusFields.ACTION.get_name(),
        MsgBusFields.SEQUENCE.get_name(),
        MsgBusFields.HASH.get_name(),
        MsgBusFields.ROUTER_HASH.get_name(),
        MsgBusFields.ROUTER_IP.get_name(),
        MsgBusFields.BASE_ATTR_HASH.get_name(),
        MsgBusFields.PEER_HASH.get_name(),
        MsgBusFields.PEER_IP.get_name(),
        MsgBusFields.PEER_ASN.get_name(),
        MsgBusFields.TIMESTAMP.get_name(),
        MsgBusFields.PREFIX.get_name(),
        MsgBusFields.PREFIX_LEN.get_name(),
        MsgBusFields.IS_IPV4.get_name(),
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
        MsgBusFields.ORIGINATOR_ID.get_name(),
        MsgBusFields.PATH_ID.get_name(),
        MsgBusFields.LABELS.get_name(),
        MsgBusFields.ISPREPOLICY.get_name(),
        MsgBusFields.IS_ADJ_RIB_IN.get_name(),
        MsgBusFields.VPN_RD.get_name(),
        MsgBusFields.VPN_RD_TYPE.get_name()
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

        super(L3VpnPrefix, self).__init__()

        # Concatenate minimum header names and version specific header names.
        self.header_names = L3VpnPrefix.minimum_header_names

        self.spec_version = version
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
            NotNull(),  # hash
            NotNull(),  # router hash
            NotNull(),  # router_ip
            ParseNullAsEmpty(),  # base_attr_hash
            NotNull(),  # peer_hash
            NotNull(),  # peer_ip
            ParseLong(),  # peer_asn
            ParseTimestamp(),  # timestamp
            NotNull(),  # prefix
            ParseInt(),  # prefix_len
            ParseInt(),  # isIPv4
            ParseNullAsEmpty(),  # origin
            ParseNullAsEmpty(),  # as_path
            ParseLongEmptyAsZero(),  # as_path_count
            ParseLongEmptyAsZero(),  # origin_as
            ParseNullAsEmpty(),  # nexthop
            ParseLongEmptyAsZero(),  # med
            ParseLongEmptyAsZero(),  # local_pref
            ParseNullAsEmpty(),  # aggregator
            ParseNullAsEmpty(),  # community_list
            ParseNullAsEmpty(),  # ext_community_list
            ParseNullAsEmpty(),  # cluster_list
            ParseLongEmptyAsZero(),  # isAtomicAgg
            ParseLongEmptyAsZero(),  # isNexthopIPv4
            ParseNullAsEmpty(),  # originator_id
            ParseLongEmptyAsZero(),  # Path ID
            ParseNullAsEmpty(),  # Labels
            ParseLongEmptyAsZero(),  # isPrePolicy
            ParseLongEmptyAsZero(),  # isAdjRibIn
            ParseNullAsEmpty(),  # VPN RD
            ParseInt(),  # VPN RD Type
        ]

        return default_cell_processors
