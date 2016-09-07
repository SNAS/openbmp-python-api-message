
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

class LsLink(Base):
    """
        Format class for ls_link parsed messages (openbmp.parsed.ls_link)

        Schema Version: 1.3
    """

    minimumHeaderNames = [MsgBusFields.ACTION['name'],MsgBusFields.SEQUENCE['name'],MsgBusFields.HASH['name'],MsgBusFields.BASE_ATTR_HASH['name'],MsgBusFields.ROUTER_HASH['name'],
                            MsgBusFields.ROUTER_IP['name'],MsgBusFields.PEER_HASH['name'],MsgBusFields.PEER_IP['name'],MsgBusFields.PEER_ASN['name'],MsgBusFields.TIMESTAMP['name'],
                            MsgBusFields.IGP_ROUTER_ID['name'],MsgBusFields.ROUTER_ID['name'],MsgBusFields.ROUTING_ID['name'],MsgBusFields.LS_ID['name'],MsgBusFields.OSPF_AREA_ID['name'],
                            MsgBusFields.ISIS_AREA_ID['name'],MsgBusFields.PROTOCOL['name'],MsgBusFields.AS_PATH['name'],MsgBusFields.LOCAL_PREF['name'],MsgBusFields.MED['name'],
                            MsgBusFields.NEXTHOP['name'],MsgBusFields.MT_ID['name'],MsgBusFields.LOCAL_LINK_ID['name'],MsgBusFields.REMOTE_LINK_ID['name'],MsgBusFields.INTF_IP['name'],
                            MsgBusFields.NEI_IP['name'],MsgBusFields.IGP_METRIC['name'],MsgBusFields.ADMIN_GROUP['name'],MsgBusFields.MAX_LINK_BW['name'],MsgBusFields.MAX_RESV_BW['name'],
                            MsgBusFields.UNRESV_BW['name'],MsgBusFields.TE_DEFAULT_METRIC['name'],MsgBusFields.LINK_PROTECTION['name'],MsgBusFields.MPLS_PROTO_MASK['name'],
                            MsgBusFields.SRLG['name'],MsgBusFields.LINK_NAME['name'],MsgBusFields.REMOTE_NODE_HASH['name'],MsgBusFields.LOCAL_NODE_HASH['name']]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.getContent()
        version = message.getVersion()

        super(LsLink, self).__init__()
        self.spec_version = version

        if version >= float(1.3):
            versionSpecificHeaders = [MsgBusFields.REMOTE_IGP_ROUTER_ID['name'],MsgBusFields.REMOTE_ROUTER_ID['name'],MsgBusFields.LOCAL_NODE_ASN['name'],MsgBusFields.REMOTE_NODE_ASN['name'],
                                      MsgBusFields.PEER_NODE_SID['name'],MsgBusFields.ISPREPOLICY['name'],MsgBusFields.IS_ADJ_RIB_IN['name']]

        elif version >= float(1.2):
            versionSpecificHeaders = [MsgBusFields.REMOTE_IGP_ROUTER_ID['name'],MsgBusFields.REMOTE_ROUTER_ID['name'],MsgBusFields.LOCAL_NODE_ASN['name'],
                                      MsgBusFields.REMOTE_NODE_ASN['name'],MsgBusFields.PEER_NODE_SID['name']]

        else:
            versionSpecificHeaders = []

        # Concatenate minimum header names and version specific header names.
        self.headerNames = LsLink.minimumHeaderNames + versionSpecificHeaders
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
            ParseNullAsEmpty(),  # ospf_area_id
            ParseNullAsEmpty(),  # isis_area_id
            ParseNullAsEmpty(),  # protocol
            ParseNullAsEmpty(),  # as_path
            ParseLongEmptyAsZero(),  # local_pref
            ParseLongEmptyAsZero(),  # med
            ParseNullAsEmpty(),  # nexthop
            ParseNullAsEmpty(),  # mt_id
            ParseLongEmptyAsZero(),  # local_link_id
            ParseLongEmptyAsZero(),  # remote_link_id
            ParseNullAsEmpty(),  # intf_ip
            ParseNullAsEmpty(),  # nei_ip
            ParseLongEmptyAsZero(),  # igp_metric
            ParseLongEmptyAsZero(),  # admin_group
            ParseNullAsEmpty(),  # max_link_bw
            ParseNullAsEmpty(),  # max_resv_bw
            ParseNullAsEmpty(),  # unresv_bw
            ParseLongEmptyAsZero(),  # te_default_metric
            ParseNullAsEmpty(),  # link_protection
            ParseNullAsEmpty(),  # mpls_proto_mask
            ParseNullAsEmpty(),  # srlg
            ParseNullAsEmpty(),  # link_name
            ParseNullAsEmpty(),  # remote_node_hash
            ParseNullAsEmpty(),  # local_node_hash
        ]

        if self.spec_version >= float(1.3):

            versionSpecificProcessors = [

                ParseNullAsEmpty(),  # remote_igp_router_id
                ParseNullAsEmpty(),  # remote_router_id
                ParseLongEmptyAsZero(),  # local_node_asn
                ParseLongEmptyAsZero(),  # remote_node_asn
                ParseNullAsEmpty(),  # Peer node SID
                ParseLongEmptyAsZero(),  # isPrePolicy
                ParseLongEmptyAsZero()  # isAdjRibIn
            ]

        elif self.spec_version >= float(1.2):

            versionSpecificProcessors = [

                ParseNullAsEmpty(),  # remote_igp_router_id
                ParseNullAsEmpty(),  # remote_router_id
                ParseLongEmptyAsZero(),  # local_node_asn
                ParseLongEmptyAsZero(),  # remote_node_asn
                ParseNullAsEmpty()  # Peer node SID
            ]

        else:

            versionSpecificProcessors = []

        return defaultCellProcessors + versionSpecificProcessors
