
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
import Base.py
from FieldProcessors import *

"""
    Format class for ls_node parsed messages (openbmp.parsed.ls_node)

    Schema Version: 1.3
"""

class LsNode(Base):

    def __init__(self, version, data):

        if version >= float(1.3):

            self.headerNames = ["action", "seq", "hash", "base_attr_hash", "router_hash", "router_ip", "peer_hash", "peer_ip",
                "peer_asn", "timestamp", "igp_router_id", "router_id", "routing_id", "ls_id", "mt_id",
                "ospf_area_id", "isis_area_id", "protocol", "flags", "as_path", "local_pref",
                "med", "nexthop", "name", "isPrePolicy", "isAdjRibIn"]

        else:

            self.headerNames = ["action", "seq", "hash", "base_attr_hash", "router_hash", "router_ip", "peer_hash", "peer_ip",
                "peer_asn", "timestamp", "igp_router_id", "router_id", "routing_id", "ls_id", "mt_id",
                "ospf_area_id", "isis_area_id", "protocol", "flags", "as_path", "local_pref",
                "med", "nexthop", "name"]

        self.parse(version, data);

    def getProcessors(self):
        processors = None

        if self._spec_version >= float(1.3):

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
                ParseNullAsEmpty(), # mt_id
                ParseNullAsEmpty(), # ospf_area_id
                ParseNullAsEmpty(), # isis_area_id
                ParseNullAsEmpty(), # protocol
                ParseNullAsEmpty(), # flags
                ParseNullAsEmpty(), # as_path
                ParseLongEmptyAsZero(), # local_pref
                ParseLongEmptyAsZero(), # med
                ParseNullAsEmpty(), # nexthop
                ParseNullAsEmpty(), # name
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
                ParseNullAsEmpty(), # mt_id
                ParseNullAsEmpty(), # ospf_area_id
                ParseNullAsEmpty(), # isis_area_id
                ParseNullAsEmpty(), # protocol
                ParseNullAsEmpty(), # flags
                ParseNullAsEmpty(), # as_path
                ParseLongEmptyAsZero(), # local_pref
                ParseLongEmptyAsZero(), # med
                ParseNullAsEmpty(), # nexthop
                ParseNullAsEmpty() # name
            ]

        return processors







