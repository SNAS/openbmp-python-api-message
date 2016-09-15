
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""

class MsgBusField:
    """
    Class to look up the default values for a single field.
    'name' is the name of corresponding field.
    'defaultValue' is the default value of corresponding field.
    """
    def __init__(self, fieldDict):
        self.name = fieldDict['name']
        self.defaultValue = fieldDict['defaultValue']

    def getName(self):
        return self.name

    def getDefaultValue(self):
        return self.defaultValue

class MsgBusFields:
    """
    Class to look up the default values for all fields.
    'name' is the name of corresponding field.
    'defaultValue' is the default value of corresponding field.
    """

    ACTION = MsgBusField({"name": "action", "defaultValue": ""})
    SEQUENCE = MsgBusField({"name": "seq", "defaultValue": 0})
    HASH = MsgBusField({"name": "hash", "defaultValue": ""})
    BASE_ATTR_HASH = MsgBusField({"name": "base_attr_hash", "defaultValue": ""})
    ROUTER_HASH = MsgBusField({"name": "router_hash", "defaultValue": ""})
    ROUTER_IP = MsgBusField({"name": "router_ip", "defaultValue": ""})
    PEER_HASH = MsgBusField({"name": "peer_hash", "defaultValue": ""})
    PEER_IP = MsgBusField({"name": "peer_ip", "defaultValue": ""})
    PEER_ASN = MsgBusField({"name": "peer_asn", "defaultValue": 0})
    TIMESTAMP = MsgBusField({"name": "timestamp", "defaultValue": ""})
    IGP_ROUTER_ID = MsgBusField({"name": "igp_router_id", "defaultValue": ""})
    ROUTER_ID = MsgBusField({"name": "router_id", "defaultValue": ""})
    ROUTING_ID = MsgBusField({"name": "routing_id", "defaultValue": 0})
    LS_ID = MsgBusField({"name": "ls_id", "defaultValue": 0})
    MT_ID = MsgBusField({"name": "mt_id", "defaultValue": ""})
    OSPF_AREA_ID = MsgBusField({"name": "ospf_area_id", "defaultValue": ""})
    ISIS_AREA_ID = MsgBusField({"name": "isis_area_id", "defaultValue": ""})
    PROTOCOL = MsgBusField({"name": "protocol", "defaultValue": ""})
    FLAGS = MsgBusField({"name": "flags", "defaultValue": ""})
    AS_PATH = MsgBusField({"name": "as_path", "defaultValue": ""})
    LOCAL_PREF = MsgBusField({"name": "local_pref", "defaultValue": 0})
    MED = MsgBusField({"name": "med", "defaultValue": 0})
    NEXTHOP = MsgBusField({"name": "nexthop", "defaultValue": ""})
    NAME = MsgBusField({"name": "name", "defaultValue": ""})
    ISPREPOLICY = MsgBusField({"name": "isPrePolicy", "defaultValue": 1})
    IS_ADJ_RIB_IN = MsgBusField({"name": "isAdjRibIn", "defaultValue": 1})
    ORIGIN = MsgBusField({"name": "origin", "defaultValue": ""})
    AS_PATH_COUNT = MsgBusField({"name": "as_path_count", "defaultValue": 0})
    ORIGIN_AS = MsgBusField({"name": "origin_as", "defaultValue": 0})
    AGGREGATOR = MsgBusField({"name": "aggregator", "defaultValue": ""})
    COMMUNITY_LIST = MsgBusField({"name": "community_list", "defaultValue": ""})
    EXT_COMMUNITY_LIST = MsgBusField({"name": "ext_community_list", "defaultValue": ""})
    CLUSTER_LIST = MsgBusField({"name": "cluster_list", "defaultValue": ""})
    ISATOMICAGG = MsgBusField({"name": "isAtomicAgg", "defaultValue": 1})
    IS_NEXTHOP_IPV4 = MsgBusField({"name": "isNexthopIPv4", "defaultValue": 1})
    ORIGINATOR_ID = MsgBusField({"name": "originator_id", "defaultValue": ""})
    LOCAL_LINK_ID = MsgBusField({"name": "local_link_id", "defaultValue": 0})
    REMOTE_LINK_ID = MsgBusField({"name": "remote_link_id", "defaultValue": 0})
    INTF_IP = MsgBusField({"name": "intf_ip", "defaultValue": ""})
    NEI_IP = MsgBusField({"name": "nei_ip", "defaultValue": ""})
    IGP_METRIC = MsgBusField({"name": "igp_metric", "defaultValue": 0})
    ADMIN_GROUP = MsgBusField({"name": "admin_group", "defaultValue": 0})
    MAX_LINK_BW = MsgBusField({"name": "max_link_bw", "defaultValue": 0})
    MAX_RESV_BW = MsgBusField({"name": "max_resv_bw", "defaultValue": 0})
    UNRESV_BW = MsgBusField({"name": "unresv_bw", "defaultValue": ""})
    TE_DEFAULT_METRIC = MsgBusField({"name": "te_default_metric", "defaultValue": 0})
    LINK_PROTECTION = MsgBusField({"name": "link_protection", "defaultValue": ""})
    MPLS_PROTO_MASK = MsgBusField({"name": "mpls_proto_mask", "defaultValue": ""})
    SRLG = MsgBusField({"name": "srlg", "defaultValue": ""})
    LINK_NAME = MsgBusField({"name": "link_name", "defaultValue": ""})
    REMOTE_NODE_HASH = MsgBusField({"name": "remote_node_hash", "defaultValue": ""})
    LOCAL_NODE_HASH = MsgBusField({"name": "local_node_hash", "defaultValue": ""})
    REMOTE_IGP_ROUTER_ID = MsgBusField({"name": "remote_igp_router_id", "defaultValue": ""})
    REMOTE_ROUTER_ID = MsgBusField({"name": "remote_router_id", "defaultValue": ""})
    LOCAL_NODE_ASN = MsgBusField({"name": "local_node_asn", "defaultValue": 0})
    REMOTE_NODE_ASN = MsgBusField({"name": "remote_node_asn", "defaultValue": 0})
    PEER_NODE_SID = MsgBusField({"name": "peer_node_sid", "defaultValue": ""})
    REJECTED = MsgBusField({"name": "rejected", "defaultValue": 0})
    KNOWN_DUP_UPDATES = MsgBusField({"name": "known_dup_updates", "defaultValue": 0})
    KNOWN_DUP_WITHDRAWS = MsgBusField({"name": "known_dup_withdraws", "defaultValue": 0})
    INVALID_CLUSTER_LIST = MsgBusField({"name": "invalid_cluster_list", "defaultValue": 0})
    INVALID_AS_PATH = MsgBusField({"name": "invalid_as_path", "defaultValue": 0})
    INVALID_ORIGINATOR = MsgBusField({"name": "invalid_originator", "defaultValue": 0})
    INVALID_AS_CONFED = MsgBusField({"name": "invalid_as_confed", "defaultValue": 0})
    PRE_POLICY = MsgBusField({"name": "pre_policy", "defaultValue": 0})
    POST_POLICY = MsgBusField({"name": "post_policy", "defaultValue": 0})
    ADMIN_ID = MsgBusField({"name": "admin_id", "defaultValue": ""})
    ROUTERS = MsgBusField({"name": "routers", "defaultValue": ""})
    ROUTER_COUNT = MsgBusField({"name": "router_count", "defaultValue": 0})
    OSPF_ROUTE_TYPE = MsgBusField({"name": "ospf_route_type", "defaultValue": ""})
    IGP_FLAGS = MsgBusField({"name": "igp_flags", "defaultValue": ""})
    ROUTE_TAG = MsgBusField({"name": "route_tag", "defaultValue": 0})
    EXT_ROUTE_TAG = MsgBusField({"name": "ext_route_tag", "defaultValue": 0})
    OSPF_FWD_ADDR = MsgBusField({"name": "ospf_fwd_addr", "defaultValue": ""})
    PREFIX = MsgBusField({"name": "prefix", "defaultValue": ""})
    PREFIX_LEN = MsgBusField({"name": "prefix_len", "defaultValue": 0})
    REMOTE_BGP_ID = MsgBusField({"name": "remote_bgp_id", "defaultValue": ""})
    REMOTE_ASN = MsgBusField({"name": "remote_asn", "defaultValue": 0})
    REMOTE_IP = MsgBusField({"name": "remote_ip", "defaultValue": ""})
    PEER_RD = MsgBusField({"name": "peer_rd", "defaultValue": ""})
    REMOTE_PORT = MsgBusField({"name": "remote_port", "defaultValue": 0})
    LOCAL_ASN = MsgBusField({"name": "local_asn", "defaultValue": 0})
    LOCAL_IP = MsgBusField({"name": "local_ip", "defaultValue": ""})
    LOCAL_PORT = MsgBusField({"name": "local_port", "defaultValue": 0})
    LOCAL_BGP_ID = MsgBusField({"name": "local_bgp_id", "defaultValue": ""})
    INFO_DATA = MsgBusField({"name": "info_data", "defaultValue": ""})
    ADV_CAP = MsgBusField({"name": "adv_cap", "defaultValue": ""})
    RECV_CAP = MsgBusField({"name": "recv_cap", "defaultValue": ""})
    REMOTE_HOLDDOWN = MsgBusField({"name": "remote_holddown", "defaultValue": 0})
    ADV_HOLDDOWN = MsgBusField({"name": "adv_holddown", "defaultValue": 0})
    BMP_REASON = MsgBusField({"name": "bmp_reason", "defaultValue": 0})
    BGP_ERROR_CODE = MsgBusField({"name": "bgp_error_code", "defaultValue": 0})
    BGP_ERROR_SUB_CODE = MsgBusField({"name": "bgp_error_sub_code", "defaultValue": 0})
    ERROR_TEXT = MsgBusField({"name": "error_text", "defaultValue": ""})
    IS_L3VPN = MsgBusField({"name": "isL3VPN", "defaultValue": 1})
    IS_IPV4 = MsgBusField({"name": "isIPv4", "defaultValue": 1})
    IP_ADDRESS = MsgBusField({"name": "ip_address", "defaultValue": ""})
    DESCRIPTION = MsgBusField({"name": "description", "defaultValue": ""})
    TERM_CODE = MsgBusField({"name": "term_code", "defaultValue": 0})
    TERM_REASON = MsgBusField({"name": "term_reason", "defaultValue": ""})
    INIT_DATA = MsgBusField({"name": "init_data", "defaultValue": ""})
    TERM_DATA = MsgBusField({"name": "term_data", "defaultValue": ""})
    BGP_ID = MsgBusField({"name": "bgp_id", "defaultValue": ""})
    PATH_ID = MsgBusField({"name": "path_id", "defaultValue": 0})
    LABELS = MsgBusField({"name": "labels", "defaultValue": ""})
