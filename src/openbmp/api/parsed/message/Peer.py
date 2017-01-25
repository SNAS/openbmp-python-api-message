
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import Base
from FieldProcessors import ParseLongEmptyAsZero, ParseNullAsEmpty, NotNull, ParseLong, ParseTimestamp
from Message import Message
from MsgBusFields import MsgBusFields


class Peer(Base):
    """
    Format class for peer parsed messages (openbmp.parsed.peer)

    Schema Version: 1.4
    """

    minimum_header_names = [
        MsgBusFields.ACTION.get_name(),
        MsgBusFields.SEQUENCE.get_name(),
        MsgBusFields.HASH.get_name(),
        MsgBusFields.ROUTER_HASH.get_name(),
        MsgBusFields.NAME.get_name(),
        MsgBusFields.REMOTE_BGP_ID.get_name(),
        MsgBusFields.ROUTER_IP.get_name(),
        MsgBusFields.TIMESTAMP.get_name(),
        MsgBusFields.REMOTE_ASN.get_name(),
        MsgBusFields.REMOTE_IP.get_name(),
        MsgBusFields.PEER_RD.get_name(),
        MsgBusFields.REMOTE_PORT.get_name(),
        MsgBusFields.LOCAL_ASN.get_name(),
        MsgBusFields.LOCAL_IP.get_name(),
        MsgBusFields.LOCAL_PORT.get_name(),
        MsgBusFields.LOCAL_BGP_ID.get_name(),
        MsgBusFields.INFO_DATA.get_name(),
        MsgBusFields.ADV_CAP.get_name(),
        MsgBusFields.RECV_CAP.get_name(),
        MsgBusFields.REMOTE_HOLDDOWN.get_name(),
        MsgBusFields.ADV_HOLDDOWN.get_name(),
        MsgBusFields.BMP_REASON.get_name(),
        MsgBusFields.BGP_ERROR_CODE.get_name(),
        MsgBusFields.BGP_ERROR_SUB_CODE.get_name(),
        MsgBusFields.ERROR_TEXT.get_name(),
        MsgBusFields.IS_L3VPN.get_name(),
        MsgBusFields.ISPREPOLICY.get_name(),
        MsgBusFields.IS_IPV4.get_name()
    ]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.get_content()

        super(Peer, self).__init__()

        self.headerNames = Peer.minimum_header_names

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
            NotNull(),  # router hash
            ParseNullAsEmpty(),  # name
            NotNull(),  # remote_bgp_id
            NotNull(),  # router_ip
            ParseTimestamp(),  # Timestamp
            ParseLong(),  # remote_asn
            NotNull(),  # remote_ip
            ParseNullAsEmpty(),  # peer_rd
            ParseLongEmptyAsZero(),  # remote_port
            ParseLongEmptyAsZero(),  # local_asn
            ParseNullAsEmpty(),  # local_ip
            ParseLongEmptyAsZero(),  # local_port
            ParseNullAsEmpty(),  # local_bgp_id
            ParseNullAsEmpty(),  # info_data
            ParseNullAsEmpty(),  # adv_cap
            ParseNullAsEmpty(),  # recv_cap
            ParseLongEmptyAsZero(),  # remote_holddown
            ParseLongEmptyAsZero(),  # local_holddown
            ParseLongEmptyAsZero(),  # bmp_reason
            ParseLongEmptyAsZero(),  # bgp_error_code
            ParseLongEmptyAsZero(),  # bgp_error_sub_code
            ParseNullAsEmpty(),  # error_text
            ParseLongEmptyAsZero(),  # isL3VPN
            ParseLongEmptyAsZero(),  # isPrePolicy
            ParseLongEmptyAsZero()  # isIPv4
        ]

        return processors
