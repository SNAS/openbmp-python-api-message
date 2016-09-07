
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

class Peer(Base):
    """
        Format class for peer parsed messages (openbmp.parsed.peer)

        Schema Version: 1.3
    """

    minimumHeaderNames = [MsgBusFields.ACTION['name'],MsgBusFields.SEQUENCE['name'],MsgBusFields.HASH['name'],MsgBusFields.ROUTER_HASH['name'],MsgBusFields.NAME['name'],
                            MsgBusFields.REMOTE_BGP_ID['name'],MsgBusFields.ROUTER_IP['name'],MsgBusFields.TIMESTAMP['name'],MsgBusFields.REMOTE_ASN['name'],
                            MsgBusFields.REMOTE_IP['name'],MsgBusFields.PEER_RD['name'],MsgBusFields.REMOTE_PORT['name'],MsgBusFields.LOCAL_ASN['name'],
                            MsgBusFields.LOCAL_IP['name'],MsgBusFields.LOCAL_PORT['name'],MsgBusFields.LOCAL_BGP_ID['name'],MsgBusFields.INFO_DATA['name'],MsgBusFields.ADV_CAP['name'],
                            MsgBusFields.RECV_CAP['name'],MsgBusFields.REMOTE_HOLDDOWN['name'],MsgBusFields.ADV_HOLDDOWN['name'],MsgBusFields.BMP_REASON['name'],
                            MsgBusFields.BGP_ERROR_CODE['name'],MsgBusFields.BGP_ERROR_SUB_CODE['name'],MsgBusFields.ERROR_TEXT['name'],MsgBusFields.IS_L3VPN['name'],
                            MsgBusFields.ISPREPOLICY['name'],MsgBusFields.IS_IPV4['name']]


    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.getContent()

        super(Peer, self).__init__()

        self.headerNames = Peer.minimumHeaderNames

        self.parse(Base.spec_version, data)

    def getProcessors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

        processors = [

            NotNull(), # action
            ParseLong(), # seq
            NotNull(), # hash
            NotNull(), # router hash
            ParseNullAsEmpty(), # name
            NotNull(), # remote_bgp_id
            NotNull(), # router_ip
            ParseTimestamp(), # Timestamp
            ParseLong(), # remote_asn
            NotNull(), # remote_ip
            ParseNullAsEmpty(), # peer_rd
            ParseLongEmptyAsZero(), # remote_port
            ParseLongEmptyAsZero(), # local_asn
            ParseNullAsEmpty(), # local_ip
            ParseLongEmptyAsZero(), # local_port
            ParseNullAsEmpty(), # local_bgp_id
            ParseNullAsEmpty(), # info_data
            ParseNullAsEmpty(), # adv_cap
            ParseNullAsEmpty(), # recv_cap
            ParseLongEmptyAsZero(), # remote_holddown
            ParseLongEmptyAsZero(), # local_holddown
            ParseLongEmptyAsZero(), # bmp_reason
            ParseLongEmptyAsZero(), # bgp_error_code
            ParseLongEmptyAsZero(), # bgp_error_sub_code
            ParseNullAsEmpty(), # error_text
            ParseLongEmptyAsZero(), # isL3VPN
            ParseLongEmptyAsZero(), # isPrePolicy
            ParseLongEmptyAsZero() # isIPv4
        ]

        return processors
