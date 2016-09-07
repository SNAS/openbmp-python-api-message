
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""

class MsgBusFields:
    """
    Class to look up the default values for each field.
    'name' is the name of corresponding field.
    'defaultValue' is the default value of corresponding field.
    """

    ACTION = {"name": "action", "defaultValue": ""}
    SEQUENCE = {"name": "seq", "defaultValue": 0}
    HASH = {"name": "hash", "defaultValue": ""}
    BASE_ATTR_HASH = {"name": "base_attr_hash", "defaultValue": ""}
    ROUTER_HASH = {"name": "router_hash", "defaultValue": ""}
    ROUTER_IP = {"name": "router_ip", "defaultValue": ""}
    PEER_HASH = {"name": "peer_hash", "defaultValue": ""}
    PEER_IP = {"name": "peer_ip", "defaultValue": ""}
    PEER_ASN = {"name": "peer_asn", "defaultValue": 0}
    TIMESTAMP = {"name": "timestamp", "defaultValue": ""}
    IGP_ROUTER_ID = {"name": "igp_router_id", "defaultValue": ""}
    ROUTER_ID = {"name": "router_id", "defaultValue": ""}
    ROUTING_ID = {"name": "routing_id", "defaultValue": 0}
    LS_ID = {"name": "ls_id", "defaultValue": 0}
    MT_ID = {"name": "mt_id" ""}
    OSPF_AREA_ID = {"name": "ospf_area_id", "defaultValue": ""}
    ISIS_AREA_ID = {"name": "isis_area_id", "defaultValue": ""}
    PROTOCOL = {"name": "protocol", "defaultValue": ""}
    FLAGS = {"name": "flags", "defaultValue": ""}
    AS_PATH = {"name": "as_path", "defaultValue": ""}
    LOCAL_PREF = {"name": "local_pref", "defaultValue": 0}
    MED = {"name": "med", "defaultValue": 0}
    NEXTHOP = {"name": "nexthop", "defaultValue": ""}
    NAME = {"name": "name", "defaultValue": ""}
    ISPREPOLICY = {"name": "isPrePolicy", "defaultValue": 1}
    IS_ADJ_RIB_IN = {"name": "isAdjRibIn", "defaultValue": 1}
    ORIGIN = {"name": "origin", "defaultValue": ""}
    AS_PATH_COUNT = {"name": "as_path_count", "defaultValue": 0}
    ORIGIN_AS = {"name": "origin_as", "defaultValue": 0}
    AGGREGATOR = {"name": "aggregator", "defaultValue": ""}
    COMMUNITY_LIST = {"name": "community_list", "defaultValue": ""}
    EXT_COMMUNITY_LIST = {"name": "ext_community_list", "defaultValue": ""}
    CLUSTER_LIST = {"name": "cluster_list", "defaultValue": ""}
    ISATOMICAGG = {"name": "isAtomicAgg", "defaultValue": 1}
    IS_NEXTHOP_IPV4 = {"name": "isNexthopIPv4", "defaultValue": 1}
    ORIGINATOR_ID = {"name": "originator_id", "defaultValue": ""}
    LOCAL_LINK_ID = {"name": "local_link_id", "defaultValue": 0}
    REMOTE_LINK_ID = {"name": "remote_link_id", "defaultValue": 0}
    INTF_IP = {"name": "intf_ip", "defaultValue": ""}
    NEI_IP = {"name": "nei_ip", "defaultValue": ""}
    IGP_METRIC = {"name": "igp_metric", "defaultValue": 0}
    ADMIN_GROUP = {"name": "admin_group", "defaultValue": 0}
    MAX_LINK_BW = {"name": "max_link_bw", "defaultValue": 0}
    MAX_RESV_BW = {"name": "max_resv_bw", "defaultValue": 0}
    UNRESV_BW = {"name": "unresv_bw", "defaultValue": ""}
    TE_DEFAULT_METRIC = {"name": "te_default_metric", "defaultValue": 0}
    LINK_PROTECTION = {"name": "link_protection", "defaultValue": ""}
    MPLS_PROTO_MASK = {"name": "mpls_proto_mask", "defaultValue": ""}
    SRLG = {"name": "srlg", "defaultValue": ""}
    LINK_NAME = {"name": "link_name", "defaultValue": ""}
    REMOTE_NODE_HASH = {"name": "remote_node_hash", "defaultValue": ""}
    LOCAL_NODE_HASH = {"name": "local_node_hash", "defaultValue": ""}
    REMOTE_IGP_ROUTER_ID = {"name": "remote_igp_router_id", "defaultValue": ""}
    REMOTE_ROUTER_ID = {"name": "remote_router_id", "defaultValue": ""}
    LOCAL_NODE_ASN = {"name": "local_node_asn", "defaultValue": 0}
    REMOTE_NODE_ASN = {"name": "remote_node_asn", "defaultValue": 0}
    PEER_NODE_SID = {"name": "peer_node_sid", "defaultValue": ""}
    REJECTED = {"name": "rejected", "defaultValue": 0}
    KNOWN_DUP_UPDATES = {"name": "known_dup_updates", "defaultValue": 0}
    KNOWN_DUP_WITHDRAWS = {"name": "known_dup_withdraws", "defaultValue": 0}
    INVALID_CLUSTER_LIST = {"name": "invalid_cluster_list", "defaultValue": 0}
    INVALID_AS_PATH = {"name": "invalid_as_path", "defaultValue": 0}
    INVALID_ORIGINATOR = {"name": "invalid_originator", "defaultValue": 0}
    INVALID_AS_CONFED = {"name": "invalid_as_confed", "defaultValue": 0}
    PRE_POLICY = {"name": "pre_policy", "defaultValue": 0}
    POST_POLICY = {"name": "post_policy", "defaultValue": 0}
    ADMIN_ID = {"name": "admin_id", "defaultValue": ""}
    ROUTERS = {"name": "routers", "defaultValue": ""}
    ROUTER_COUNT = {"name": "router_count", "defaultValue": 0}
    OSPF_ROUTE_TYPE = {"name": "ospf_route_type", "defaultValue": ""}
    IGP_FLAGS = {"name": "igp_flags", "defaultValue": ""}
    ROUTE_TAG = {"name": "route_tag", "defaultValue": 0}
    EXT_ROUTE_TAG = {"name": "ext_route_tag", "defaultValue": 0}
    OSPF_FWD_ADDR = {"name": "ospf_fwd_addr", "defaultValue": ""}
    PREFIX = {"name": "prefix", "defaultValue": ""}
    PREFIX_LEN = {"name": "prefix_len", "defaultValue": 0}
    REMOTE_BGP_ID = {"name": "remote_bgp_id", "defaultValue": ""}
    REMOTE_ASN = {"name": "remote_asn", "defaultValue": 0}
    REMOTE_IP = {"name": "remote_ip", "defaultValue": ""}
    PEER_RD = {"name": "peer_rd", "defaultValue": ""}
    REMOTE_PORT = {"name": "remote_port", "defaultValue": 0}
    LOCAL_ASN = {"name": "local_asn", "defaultValue": 0}
    LOCAL_IP = {"name": "local_ip", "defaultValue": ""}
    LOCAL_PORT = {"name": "local_port", "defaultValue": 0}
    LOCAL_BGP_ID = {"name": "local_bgp_id", "defaultValue": ""}
    INFO_DATA = {"name": "info_data", "defaultValue": ""}
    ADV_CAP = {"name": "adv_cap", "defaultValue": ""}
    RECV_CAP = {"name": "recv_cap", "defaultValue": ""}
    REMOTE_HOLDDOWN = {"name": "remote_holddown", "defaultValue": 0}
    ADV_HOLDDOWN = {"name": "adv_holddown", "defaultValue": 0}
    BMP_REASON = {"name": "bmp_reason", "defaultValue": 0}
    BGP_ERROR_CODE = {"name": "bgp_error_code", "defaultValue": 0}
    BGP_ERROR_SUB_CODE = {"name": "bgp_error_sub_code", "defaultValue": 0}
    ERROR_TEXT = {"name": "error_text", "defaultValue": ""}
    IS_L3VPN = {"name": "isL3VPN", "defaultValue": 1}
    IS_IPV4 = {"name": "isIPv4", "defaultValue": 1}
    IP_ADDRESS = {"name": "ip_address", "defaultValue": ""}
    DESCRIPTION = {"name": "description", "defaultValue": ""}
    TERM_CODE = {"name": "term_code", "defaultValue": 0}
    TERM_REASON = {"name": "term_reason", "defaultValue": ""}
    INIT_DATA = {"name": "init_data", "defaultValue": ""}
    TERM_DATA = {"name": "term_data", "defaultValue": ""}
    BGP_ID = {"name": "bgp_id", "defaultValue": ""}
    PATH_ID = {"name": "path_id", "defaultValue": 0}
    LABELS = {"name": "labels", "defaultValue": ""}
