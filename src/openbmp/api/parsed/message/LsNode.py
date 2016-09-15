
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

class LsNode(Base):
    """
        Format class for ls_node parsed messages (openbmp.parsed.ls_node)

        Schema Version: 1.3
    """

    minimumHeaderNames = [MsgBusFields.ACTION.getName(),MsgBusFields.SEQUENCE.getName(),MsgBusFields.HASH.getName(),MsgBusFields.BASE_ATTR_HASH.getName(),MsgBusFields.ROUTER_HASH.getName(),
                            MsgBusFields.ROUTER_IP.getName(),MsgBusFields.PEER_HASH.getName(),MsgBusFields.PEER_IP.getName(),MsgBusFields.PEER_ASN.getName(),MsgBusFields.TIMESTAMP.getName(),
                            MsgBusFields.IGP_ROUTER_ID.getName(),MsgBusFields.ROUTER_ID.getName(),MsgBusFields.ROUTING_ID.getName(),MsgBusFields.LS_ID.getName(),MsgBusFields.MT_ID.getName(),
                            MsgBusFields.OSPF_AREA_ID.getName(),MsgBusFields.ISIS_AREA_ID.getName(),MsgBusFields.PROTOCOL.getName(),MsgBusFields.FLAGS.getName(),MsgBusFields.AS_PATH.getName(),
                            MsgBusFields.LOCAL_PREF.getName(),MsgBusFields.MED.getName(),MsgBusFields.NEXTHOP.getName(),MsgBusFields.NAME.getName()]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.getContent()
        version = message.getVersion()

        super(LsNode, self).__init__()
        self.spec_version = version

        if version >= float(1.3):

            versionSpecificHeaders = [MsgBusFields.ISPREPOLICY.getName(),MsgBusFields.IS_ADJ_RIB_IN.getName()]

        else:

            versionSpecificHeaders = []

        # Concatenate minimum header names and version specific header names.
        self.headerNames = LsNode.minimumHeaderNames + versionSpecificHeaders
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
            NotNull(),  # base_hash
            NotNull(),  # router_hash
            NotNull(),  # router_ip
            NotNull(),  # peer_hash
            NotNull(),  # peer_ip
            ParseLong(),  # peer_asn
            ParseTimestamp(),  # timestamp
            ParseNullAsEmpty(),  # igp_router_id
            ParseNullAsEmpty(),  # router_id
            ParseNullAsEmpty(),  # routing_id
            ParseLongEmptyAsZero(),  # ls_id
            ParseNullAsEmpty(),  # mt_id
            ParseNullAsEmpty(),  # ospf_area_id
            ParseNullAsEmpty(),  # isis_area_id
            ParseNullAsEmpty(),  # protocol
            ParseNullAsEmpty(),  # flags
            ParseNullAsEmpty(),  # as_path
            ParseLongEmptyAsZero(),  # local_pref
            ParseLongEmptyAsZero(),  # med
            ParseNullAsEmpty(),  # nexthop
            ParseNullAsEmpty(),  # name
        ]

        if self.spec_version >= float(1.3):

            versionSpecificProcessors = [

                ParseLongEmptyAsZero(),  # isPrePolicy
                ParseLongEmptyAsZero()  # isAdjRibIn
            ]

        else:

            versionSpecificProcessors = []

        return defaultCellProcessors + versionSpecificProcessors
