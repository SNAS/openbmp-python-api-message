
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""

from Base import *
from FieldProcessors import *

class BmpStat(Base):
    """
        Format class for bmp_stat parsed messages (openbmp.parsed.bmp_stat)

        Schema Version: 1.2
    """

    def __init__(self, data):
        """
        Handle the message by parsing it and storing the data in memory.

        :param data: Data to parse.
        """

        self.headerNames = ["action", "seq", "router_hash", "router_ip", "peer_hash", "peer_ip",
            "peer_asn", "timestamp", "rejected", "known_dup_updates", "known_dup_withdraws",
            "invalid_cluster_list", "invalid_as_path", "invalid_originator",
            "invalid_as_confed", "pre_policy", "post_policy"]

        self.parse(data);

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
            NotNull(), # router_ip
            NotNull(), # peer_hash
            NotNull(), # peer_ip,
            ParseLong(), # peer_asn
            ParseTimestamp(), # Timestamp
            NotNull(), # rejected
            NotNull(), # known_dup_updates
            NotNull(), # known_dup_withdraws
            NotNull(), # invalid_cluster_list
            NotNull(), # invalid_as_path
            NotNull(), # invalid_originator
            NotNull(), # invalid_as_confed
            NotNull(), # pre_policy
            NotNull() # post_policy
        ]

        return processors
