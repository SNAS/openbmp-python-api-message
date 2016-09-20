
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

    minimumHeaderNames = [MsgBusFields.ACTION.getName(),MsgBusFields.SEQUENCE.getName(),MsgBusFields.HASH.getName(),MsgBusFields.ROUTER_HASH.getName(),MsgBusFields.ROUTER_IP.getName(),
                            MsgBusFields.BASE_ATTR_HASH.getName(),MsgBusFields.PEER_HASH.getName(),MsgBusFields.PEER_IP.getName(),MsgBusFields.PEER_ASN.getName(),MsgBusFields.TIMESTAMP.getName(),
                            MsgBusFields.PREFIX.getName(),MsgBusFields.PREFIX_LEN.getName(),MsgBusFields.IS_IPV4.getName(),MsgBusFields.ORIGIN.getName(),MsgBusFields.AS_PATH.getName(),
                            MsgBusFields.AS_PATH_COUNT.getName(),MsgBusFields.ORIGIN_AS.getName(),MsgBusFields.NEXTHOP.getName(),MsgBusFields.MED.getName(),MsgBusFields.LOCAL_PREF.getName(),
                            MsgBusFields.AGGREGATOR.getName(),MsgBusFields.COMMUNITY_LIST.getName(),MsgBusFields.EXT_COMMUNITY_LIST.getName(),MsgBusFields.CLUSTER_LIST.getName(),MsgBusFields.ISATOMICAGG.getName(),
                            MsgBusFields.IS_NEXTHOP_IPV4.getName(),MsgBusFields.ORIGINATOR_ID.getName()]

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

            versionSpecificHeaders = [MsgBusFields.PATH_ID.getName(),MsgBusFields.LABELS.getName(),MsgBusFields.ISPREPOLICY.getName(),MsgBusFields.IS_ADJ_RIB_IN.getName()]

        elif version >= float(1.1):

            versionSpecificHeaders = [MsgBusFields.PATH_ID.getName(),MsgBusFields.LABELS.getName()]

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
