
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""
import Base.py

"""
    Format class for unicast_prefix parsed messages (openbmp.parsed.unicast_prefix)

    Schema Version: 1.3
"""

class UnicastPrefix(Base):

    def __init__(self, version, data):
        self.version = version
        self.data = data

        if self.version == float(1.3) >= 0:

            self.headerNames = ["action", "seq", "hash", "router_hash", "router_ip", "base_attr_hash", "peer_hash",
            "peer_ip", "peer_asn", "timestamp", "prefix", "prefix_len", "isIPv4",
            "origin", "as_path", "as_path_count", "origin_as",
            "nexthop", "med", "local_pref", "aggregator", "community_list", "ext_community_list",
            "cluster_list", "isAtomicAgg", "isNexthopIPv4", "originator_id",
            "path_id", "labels", "isPrePolicy", "isAdjRibIn"]

        elif float(1.1) == self.version >= 0:

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



