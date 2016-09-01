
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import *
from FieldProcessors import *

class Peer(Base):
    """
        Format class for peer parsed messages (openbmp.parsed.peer)

        Schema Version: 1.3
    """

    def __init__(self, data):
        """
        Handle the message by parsing it and storing the data in memory.

        :param data: Data to parse.
        """

        self.headerNames = ["action", "seq", "hash", "router_hash", "name", "remote_bgp_id", "router_ip",
            "timestamp", "remote_asn", "remote_ip", "peer_rd", "remote_port", "local_asn",
            "local_ip", "local_port", "local_bgp_id", "info_data", "adv_cap", "recv_cap",
            "remote_holddown", "adv_holddown", "bmp_reason", "bgp_error_code",
            "bgp_error_sub_code", "error_text", "isL3VPN", "isPrePolicy", "isIPv4"]

        self.parse(Base.DEFAULT_SPEC_VERSION, data)

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
