
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import *
from FieldProcessors import *

class LsLink(Base):
    """
        Format class for ls_link parsed messages (openbmp.parsed.ls_link)

        Schema Version: 1.3
    """

    def __init__(self, version, data):
        """
        Handle the message by parsing it and storing the data in memory.

        :param version: Schema version of the message.
        :param data: Data to parse.
        """

        self.spec_version = version

        if version >= float(1.3):

            self.headerNames = ["action", "seq", "hash", "base_attr_hash", "router_hash", "router_ip", "peer_hash", "peer_ip",
                "peer_asn", "timestamp", "igp_router_id", "router_id", "routing_id", "ls_id",
                "ospf_area_id", "isis_area_id", "protocol", "as_path", "local_pref", "med", "nexthop",
                "mt_id", "local_link_id", "remote_link_id", "intf_ip", "nei_ip", "igp_metric",
                "admin_group", "max_link_bw", "max_resv_bw", "unresv_bw", "te_default_metric",
                "link_protection", "mpls_proto_mask", "srlg", "link_name", "remote_node_hash",
                "local_node_hash", "remote_igp_router_id", "remote_router_id", "local_node_asn",
                "remote_node_asn", "peer_node_sid", "isPrePolicy", "isAdjRibIn"]

        elif version >= float(1.2):

            self.headerNames = ["action", "seq", "hash", "base_attr_hash", "router_hash", "router_ip", "peer_hash", "peer_ip",
                "peer_asn", "timestamp", "igp_router_id", "router_id", "routing_id", "ls_id",
                "ospf_area_id", "isis_area_id", "protocol", "as_path", "local_pref", "med", "nexthop",
                "mt_id", "local_link_id", "remote_link_id", "intf_ip", "nei_ip", "igp_metric",
                "admin_group", "max_link_bw", "max_resv_bw", "unresv_bw", "te_default_metric",
                "link_protection", "mpls_proto_mask", "srlg", "link_name", "remote_node_hash",
                "local_node_hash", "remote_igp_router_id", "remote_router_id", "local_node_asn",
                "remote_node_asn", "peer_node_sid"]

        else:

            self.headerNames = ["action", "seq", "hash", "base_attr_hash", "router_hash", "router_ip", "peer_hash", "peer_ip",
                "peer_asn", "timestamp", "igp_router_id", "router_id", "routing_id", "ls_id",
                "ospf_area_id", "isis_area_id", "protocol", "as_path", "local_pref", "med", "nexthop",
                "mt_id", "local_link_id", "remote_link_id", "intf_ip", "nei_ip", "igp_metric",
                "admin_group", "max_link_bw", "max_resv_bw", "unresv_bw", "te_default_metric",
                "link_protection", "mpls_proto_mask", "srlg", "link_name", "remote_node_hash",
                "local_node_hash"]

        self.parse(version, data);

    def getProcessors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

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
                ParseNullAsEmpty(), # mt_id
                ParseLongEmptyAsZero(), # local_link_id
                ParseLongEmptyAsZero(), # remote_link_id
                ParseNullAsEmpty(), # intf_ip
                ParseNullAsEmpty(), # nei_ip
                ParseLongEmptyAsZero(), # igp_metric
                ParseLongEmptyAsZero(), # admin_group
                ParseNullAsEmpty(), # max_link_bw
                ParseNullAsEmpty(), # max_resv_bw
                ParseNullAsEmpty(), # unresv_bw
                ParseLongEmptyAsZero(), # te_default_metric
                ParseNullAsEmpty(), # link_protection
                ParseNullAsEmpty(), # mpls_proto_mask
                ParseNullAsEmpty(), # srlg
                ParseNullAsEmpty(), # link_name
                ParseNullAsEmpty(), # remote_node_hash
                ParseNullAsEmpty(), # local_node_hash
                ParseNullAsEmpty(), # remote_igp_router_id
                ParseNullAsEmpty(), # remote_router_id
                ParseLongEmptyAsZero(), # local_node_asn
                ParseLongEmptyAsZero(), # remote_node_asn
                ParseNullAsEmpty(), # Peer node SID
                ParseLongEmptyAsZero(), # isPrePolicy
                ParseLongEmptyAsZero() # isAdjRibIn
            ]

        elif self.spec_version >= float(1.2):

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
                ParseNullAsEmpty(), # mt_id
                ParseLongEmptyAsZero(), # local_link_id
                ParseLongEmptyAsZero(), # remote_link_id
                ParseNullAsEmpty(), # intf_ip
                ParseNullAsEmpty(), # nei_ip
                ParseLongEmptyAsZero(), # igp_metric
                ParseLongEmptyAsZero(), # admin_group
                ParseNullAsEmpty(), # max_link_bw
                ParseNullAsEmpty(), # max_resv_bw
                ParseNullAsEmpty(), # unresv_bw
                ParseLongEmptyAsZero(), # te_default_metric
                ParseNullAsEmpty(), # link_protection
                ParseNullAsEmpty(), # mpls_proto_mask
                ParseNullAsEmpty(), # srlg
                ParseNullAsEmpty(), # link_name
                ParseNullAsEmpty(), # remote_node_hash
                ParseNullAsEmpty(), # local_node_hash
                ParseNullAsEmpty(), # remote_igp_router_id
                ParseNullAsEmpty(), # remote_router_id
                ParseLongEmptyAsZero(), # local_node_asn
                ParseLongEmptyAsZero(), # remote_node_asn
                ParseNullAsEmpty() # Peer node SID
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
                ParseNullAsEmpty(), # mt_id
                ParseLongEmptyAsZero(), # local_link_id
                ParseLongEmptyAsZero(), # remote_link_id
                ParseNullAsEmpty(), # intf_ip
                ParseNullAsEmpty(), # nei_ip
                ParseLongEmptyAsZero(), # igp_metric
                ParseLongEmptyAsZero(), # admin_group
                ParseNullAsEmpty(), # max_link_bw
                ParseNullAsEmpty(), # max_resv_bw
                ParseNullAsEmpty(), # unresv_bw
                ParseLongEmptyAsZero(), # te_default_metric
                ParseNullAsEmpty(), # link_protection
                ParseNullAsEmpty(), # mpls_proto_mask
                ParseNullAsEmpty(), # srlg
                ParseNullAsEmpty(), # link_name
                ParseNullAsEmpty(), # remote_node_hash
                ParseNullAsEmpty() # local_node_hash
            ]

        return processors
