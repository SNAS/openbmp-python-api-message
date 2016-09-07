
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

class UnicastPrefix(Base):
    """
        Format class for unicast_prefix parsed messages (openbmp.parsed.unicast_prefix)

        Schema Version: 1.3
    """

    minimumHeaderNames = [MsgBusFields.ACTION["name"],MsgBusFields.SEQUENCE["name"],MsgBusFields.HASH["name"],MsgBusFields.ROUTER_HASH["name"],MsgBusFields.ROUTER_IP["name"],
                            MsgBusFields.BASE_ATTR_HASH["name"],MsgBusFields.PEER_HASH["name"],MsgBusFields.PEER_IP["name"],MsgBusFields.PEER_ASN["name"],MsgBusFields.TIMESTAMP["name"],
                            MsgBusFields.PREFIX["name"],MsgBusFields.PREFIX_LEN["name"],MsgBusFields.IS_IPV4["name"],MsgBusFields.ORIGIN["name"],MsgBusFields.AS_PATH["name"],
                            MsgBusFields.AS_PATH_COUNT["name"],MsgBusFields.ORIGIN_AS["name"],MsgBusFields.NEXTHOP["name"],MsgBusFields.MED["name"],MsgBusFields.LOCAL_PREF["name"],
                            MsgBusFields.AGGREGATOR["name"],MsgBusFields.COMMUNITY_LIST["name"],MsgBusFields.EXT_COMMUNITY_LIST["name"],MsgBusFields.CLUSTER_LIST["name"],MsgBusFields.ISATOMICAGG["name"],
                            MsgBusFields.IS_NEXTHOP_IPV4["name"],MsgBusFields.ORIGINATOR_ID["name"]]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        version = message.getVersion()
        data = message.getContent()

        super(UnicastPrefix, self).__init__()
        self.spec_version = version

        if version >= float(1.3):

            versionSpecificHeaders = [MsgBusFields.PATH_ID["name"],MsgBusFields.LABELS["name"],MsgBusFields.ISPREPOLICY["name"],MsgBusFields.IS_ADJ_RIB_IN["name"]]

        elif version >= float(1.1):

            versionSpecificHeaders = [MsgBusFields.PATH_ID["name"],MsgBusFields.LABELS["name"]]

        else:

            versionSpecificHeaders = []

        # Concatenate minimum header names and version specific header names.
        self.headerNames = UnicastPrefix.minimumHeaderNames + versionSpecificHeaders
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
        ]

        if self.spec_version >= float(1.3):

            versionSpecificProcessors = [

                ParseLongEmptyAsZero(), # Path ID
                ParseNullAsEmpty(), # Labels
                ParseLongEmptyAsZero(), # isPrePolicy
                ParseLongEmptyAsZero() # isAdjRibIn
            ]

        elif self.spec_version >= float(1.1):

            versionSpecificProcessors = [

                ParseLongEmptyAsZero(),  # Path ID
                ParseNullAsEmpty(),  # Labels
            ]

        else:

            versionSpecificProcessors = []

        return defaultCellProcessors + versionSpecificProcessors
