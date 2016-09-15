
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

    minimumHeaderNames = [MsgBusFields.ACTION.getName(),MsgBusFields.SEQUENCE.getName(),MsgBusFields.HASH.getName(),MsgBusFields.ROUTER_HASH.getName(),MsgBusFields.NAME.getName(),
                            MsgBusFields.REMOTE_BGP_ID.getName(),MsgBusFields.ROUTER_IP.getName(),MsgBusFields.TIMESTAMP.getName(),MsgBusFields.REMOTE_ASN.getName(),
                            MsgBusFields.REMOTE_IP.getName(),MsgBusFields.PEER_RD.getName(),MsgBusFields.REMOTE_PORT.getName(),MsgBusFields.LOCAL_ASN.getName(),
                            MsgBusFields.LOCAL_IP.getName(),MsgBusFields.LOCAL_PORT.getName(),MsgBusFields.LOCAL_BGP_ID.getName(),MsgBusFields.INFO_DATA.getName(),MsgBusFields.ADV_CAP.getName(),
                            MsgBusFields.RECV_CAP.getName(),MsgBusFields.REMOTE_HOLDDOWN.getName(),MsgBusFields.ADV_HOLDDOWN.getName(),MsgBusFields.BMP_REASON.getName(),
                            MsgBusFields.BGP_ERROR_CODE.getName(),MsgBusFields.BGP_ERROR_SUB_CODE.getName(),MsgBusFields.ERROR_TEXT.getName(),MsgBusFields.IS_L3VPN.getName(),
                            MsgBusFields.ISPREPOLICY.getName(),MsgBusFields.IS_IPV4.getName()]


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

        self.parse(self.spec_version, data)

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
