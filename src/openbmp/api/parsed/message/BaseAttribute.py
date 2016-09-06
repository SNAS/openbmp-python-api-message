
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""

from Base import *
from FieldProcessors import *

class BaseAttribute(Base):
    """
    Format class for base_attribute parsed messages (openbmp.parsed.base_attribute)

    Schema Version: 1.2
    """

    def __init__(self, data):
        """
        Handle the message by parsing it and storing the data in memory.

        :param data: Data to parse.
        """

        super(BaseAttribute, self).__init__()

        self.headerNames = ["action", "seq", "hash", "router_hash", "router_ip", "peer_hash", "peer_ip",
            "peer_asn", "timestamp", "origin", "as_path", "as_path_count", "origin_as",
            "nexthop", "med", "local_pref", "aggregator", "community_list", "ext_community_list",
            "cluster_list", "isAtomicAgg", "isNexthopIPv4", "originator_id"]

        self.parse(Base.DEFAULT_SPEC_VERSION, data);

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
            NotNull(), # router_ip
            NotNull(), # peer_hash
            NotNull(), # peer_ip
            ParseLong(), # peer_asn
            ParseTimestamp(), # timestamp
            ParseNullAsEmpty(), # origin
            ParseNullAsEmpty(), # as_path
            ParseLong(), # as_path_count
            ParseLong(), # origin_as
            ParseNullAsEmpty(), # nexthop
            ParseLong(), # med
            ParseLong(), # local_pref
            ParseNullAsEmpty(), # aggregator
            ParseNullAsEmpty(), # community_list
            ParseNullAsEmpty(), # ext_community_list
            ParseNullAsEmpty(), # cluster_list
            ParseLongEmptyAsZero(), # isAtomicAgg
            ParseLongEmptyAsZero(), # isNexthopIPv4
            ParseNullAsEmpty() # originator_id
        ]

        return processors
