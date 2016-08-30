
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import *
from FieldProcessors import *

"""
    Format class for unicast_prefix parsed messages (openbmp.parsed.unicast_prefix)

    Schema Version: 1.3
"""

class UnicastPrefix(Base):

    def __init__(self, version, data):
        super(UnicastPrefix, self).__init__()
        self.spec_version = version

        if version >= float(1.3):

            self.headerNames = ["action", "seq", "hash", "router_hash", "router_ip", "base_attr_hash", "peer_hash",
                "peer_ip", "peer_asn", "timestamp", "prefix", "prefix_len", "isIPv4",
                "origin", "as_path", "as_path_count", "origin_as",
                "nexthop", "med", "local_pref", "aggregator", "community_list", "ext_community_list",
                "cluster_list", "isAtomicAgg", "isNexthopIPv4", "originator_id",
                "path_id", "labels", "isPrePolicy", "isAdjRibIn"]

        elif version >= float(1.1):

            self.headerNames = ["action", "seq", "hash", "router_hash", "router_ip", "base_attr_hash", "peer_hash",
                "peer_ip", "peer_asn", "timestamp", "prefix", "prefix_len", "isIPv4",
                "origin", "as_path", "as_path_count", "origin_as",
                "nexthop", "med", "local_pref", "aggregator", "community_list", "ext_community_list",
                "cluster_list", "isAtomicAgg", "isNexthopIPv4", "originator_id",
                "path_id", "labels"]

        else:

            self.headerNames = ["action", "seq", "hash", "router_hash", "router_ip", "base_attr_hash", "peer_hash",
                "peer_ip", "peer_asn", "timestamp", "prefix", "prefix_len", "isIPv4",
                "origin", "as_path", "as_path_count", "origin_as",
                "nexthop", "med", "local_pref", "aggregator", "community_list", "ext_community_list",
                "cluster_list", "isAtomicAgg", "isNexthopIPv4", "originator_id"]

        #self.processors = self.getProcessors()
        self.parse(version, data);

    def getProcessors(self):
        processors = None

        if self.spec_version >= float(1.3):

            processors = [

                NotNull(), # action
                ParseLong(), # seq
                NotNull(), # hash
                NotNull(), # router hash
                NotNull(), # router_ip
                ParseNullAsEmpty(), # base_attr_hash
                NotNull(), # peer_hash
                NotNull(), # peer_ip
                ParseLong(), # peer_asn
                ParseTimestamp(), # timestamp
                NotNull(), # prefix
                ParseInt(), # prefix_len
                ParseInt(), # isIPv4
                ParseNullAsEmpty(), # origin
                ParseNullAsEmpty(), # as_path
                ParseLongEmptyAsZero(), # as_path_count
                ParseLongEmptyAsZero(), # origin_as
                ParseNullAsEmpty(), # nexthop
                ParseLongEmptyAsZero(), # med
                ParseLongEmptyAsZero(), # local_pref
                ParseNullAsEmpty(), # aggregator
                ParseNullAsEmpty(), # community_list
                ParseNullAsEmpty(), # ext_community_list
                ParseNullAsEmpty(), # cluster_list
                ParseLongEmptyAsZero(), # isAtomicAgg
                ParseLongEmptyAsZero(), # isNexthopIPv4
                ParseNullAsEmpty(), # originator_id
                ParseLongEmptyAsZero(), # Path ID
                ParseNullAsEmpty(), # Labels
                ParseLongEmptyAsZero(), # isPrePolicy
                ParseLongEmptyAsZero() # isAdjRibIn
            ]

        elif self.spec_version >= float(1.1):

            processors = [

                NotNull(), # action
                ParseLong(), # seq
                NotNull(), # hash
                NotNull(), # router hash
                NotNull(), # router_ip
                ParseNullAsEmpty(), # base_attr_hash
                NotNull(), # peer_hash
                NotNull(), # peer_ip
                ParseLong(), # peer_asn
                ParseTimestamp(), # timestamp
                NotNull(), # prefix
                ParseInt(), # prefix_len
                ParseInt(), # isIPv4
                ParseNullAsEmpty(), # origin
                ParseNullAsEmpty(), # as_path
                ParseLongEmptyAsZero(), # as_path_count
                ParseLongEmptyAsZero(), # origin_as
                ParseNullAsEmpty(), # nexthop
                ParseLongEmptyAsZero(), # med
                ParseLongEmptyAsZero(), # local_pref
                ParseNullAsEmpty(), # aggregator
                ParseNullAsEmpty(), # community_list
                ParseNullAsEmpty(), # ext_community_list
                ParseNullAsEmpty(), # cluster_list
                ParseLongEmptyAsZero(), # isAtomicAgg
                ParseLongEmptyAsZero(), # isNexthopIPv4
                ParseNullAsEmpty(), # originator_id
                ParseLongEmptyAsZero(), # Path ID
                ParseNullAsEmpty() # Labels
            ]

        else:

            processors = [

                NotNull(), # action
                ParseLong(), # seq
                NotNull(), # hash
                NotNull(), # router hash
                NotNull(), # router_ip
                ParseNullAsEmpty(), # base_attr_hash
                NotNull(), # peer_hash
                NotNull(), # peer_ip
                ParseLong(), # peer_asn
                ParseTimestamp(), # timestamp
                NotNull(), # prefix
                ParseInt(), # prefix_len
                ParseInt(), # isIPv4
                ParseNullAsEmpty(), # origin
                ParseNullAsEmpty(), # as_path
                ParseLongEmptyAsZero(), # as_path_count
                ParseLongEmptyAsZero(), # origin_as
                ParseNullAsEmpty(), # nexthop
                ParseLongEmptyAsZero(), # med
                ParseLongEmptyAsZero(), # local_pref
                ParseNullAsEmpty(), # aggregator
                ParseNullAsEmpty(), # community_list
                ParseNullAsEmpty(), # ext_community_list
                ParseNullAsEmpty(), # cluster_list
                ParseLongEmptyAsZero(), # isAtomicAgg
                ParseLongEmptyAsZero(), # isNexthopIPv4
                ParseNullAsEmpty() # originator_id
            ]

        return processors
