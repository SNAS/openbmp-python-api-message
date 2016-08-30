
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import *
from FieldProcessors import *

"""
    Format class for ls_prefix parsed messages (openbmp.parsed.ls_prefix)

    Schema Version: 1.2
"""

class LsPrefix(Base):

    def __init__(self, version, data):

        self.spec_version = version

        if version >= float(1.3):

            self.headerNames = ["action", "seq", "hash", "base_attr_hash", "router_hash", "router_ip", "peer_hash", "peer_ip",
                "peer_asn", "timestamp", "igp_router_id", "router_id", "routing_id", "ls_id",
                "ospf_area_id", "isis_area_id", "protocol", "as_path", "local_pref", "med", "nexthop",
                "local_node_hash", "mt_id", "ospf_route_type", "igp_flags", "route_tag",
                "ext_route_tag", "ospf_fwd_addr", "igp_metric", "prefix", "prefix_len",
                "isPrePolicy", "isAdjRibIn"]

        else:

            self.headerNames = ["action", "seq", "hash", "base_attr_hash", "router_hash", "router_ip", "peer_hash", "peer_ip",
                "peer_asn", "timestamp", "igp_router_id", "router_id", "routing_id", "ls_id",
                "ospf_area_id", "isis_area_id", "protocol", "as_path", "local_pref", "med", "nexthop",
                "local_node_hash", "mt_id", "ospf_route_type", "igp_flags", "route_tag",
                "ext_route_tag", "ospf_fwd_addr", "igp_metric", "prefix", "prefix_len"]

        self.parse(version, data);

    def getProcessors(self):
        processors = None

        if self.spec_version >= float(1.3):

            processors = [

                NotNull(), # action
                ParseLong(), # seq
                NotNull(), # hash
                NotNull(), # base_hash
                NotNull(), # router_hash
                NotNull(), # router_ip
                NotNull(), # peer_hash
                NotNull(), # peer_ip
                ParseLong(), # peer_asn
                ParseTimestamp(), # timestamp
                ParseNullAsEmpty(), # igp_router_id
                ParseNullAsEmpty(), # router_id
                ParseNullAsEmpty(), # routing_id
                ParseLongEmptyAsZero(), # ls_id
                ParseNullAsEmpty(), # ospf_area_id
                ParseNullAsEmpty(), # isis_area_id
                ParseNullAsEmpty(), # protocol
                ParseNullAsEmpty(), # as_path
                ParseLongEmptyAsZero(), # local_pref
                ParseLongEmptyAsZero(), # med
                ParseNullAsEmpty(), # nexthop
                ParseNullAsEmpty(), # local_node_hash
                ParseNullAsEmpty(), # mt_id
                ParseNullAsEmpty(), # ospf_route_type
                ParseNullAsEmpty(), # igp_flags
                ParseLongEmptyAsZero(), # route_tag
                ParseLongEmptyAsZero(), # ext_route_tag
                ParseNullAsEmpty(), # ospf_fwd_addr
                ParseLongEmptyAsZero(), # igp_metric
                NotNull(), # prefix
                ParseInt(), # prefix_len
                ParseLongEmptyAsZero(), # isPrePolicy
                ParseLongEmptyAsZero() # isAdjRibIn
            ]

        else:

            processors = [

                NotNull(), # action
                ParseLong(), # seq
                NotNull(), # hash
                NotNull(), # base_hash
                NotNull(), # router_hash
                NotNull(), # router_ip
                NotNull(), # peer_hash
                NotNull(), # peer_ip
                ParseLong(), # peer_asn
                ParseTimestamp(), # timestamp
                ParseNullAsEmpty(), # igp_router_id
                ParseNullAsEmpty(), # router_id
                ParseNullAsEmpty(), # routing_id
                ParseLongEmptyAsZero(), # ls_id
                ParseNullAsEmpty(), # ospf_area_id
                ParseNullAsEmpty(), # isis_area_id
                ParseNullAsEmpty(), # protocol
                ParseNullAsEmpty(), # as_path
                ParseLongEmptyAsZero(), # local_pref
                ParseLongEmptyAsZero(), # med
                ParseNullAsEmpty(), # nexthop
                ParseNullAsEmpty(), # local_node_hash
                ParseNullAsEmpty(), # mt_id
                ParseNullAsEmpty(), # ospf_route_type
                ParseNullAsEmpty(), # igp_flags
                ParseLongEmptyAsZero(), # route_tag
                ParseLongEmptyAsZero(), # ext_route_tag
                ParseNullAsEmpty(), # ospf_fwd_addr
                ParseLongEmptyAsZero(), # igp_metric
                NotNull(), # prefix
                ParseInt() # prefix_len
            ]

        return processors







