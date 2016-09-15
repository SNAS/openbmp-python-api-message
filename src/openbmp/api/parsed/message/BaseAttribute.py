
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""

from Base import *
from FieldProcessors import *
from Message import *
from MsgBusFields import MsgBusFields

class BaseAttribute(Base):
    """
    Format class for base_attribute parsed messages (openbmp.parsed.base_attribute)

    Schema Version: 1.2
    """

    minimumHeaderNames = [MsgBusFields.ACTION.getName(), MsgBusFields.SEQUENCE.getName(), MsgBusFields.HASH.getName(), MsgBusFields.ROUTER_HASH.getName(),
                            MsgBusFields.ROUTER_IP.getName(), MsgBusFields.PEER_HASH.getName(), MsgBusFields.PEER_IP.getName(), MsgBusFields.PEER_ASN.getName(), 
                            MsgBusFields.TIMESTAMP.getName(), MsgBusFields.ORIGIN.getName(), MsgBusFields.AS_PATH.getName(), MsgBusFields.AS_PATH_COUNT.getName(), 
                            MsgBusFields.ORIGIN_AS.getName(), MsgBusFields.NEXTHOP.getName(), MsgBusFields.MED.getName(), MsgBusFields.LOCAL_PREF.getName(), 
                            MsgBusFields.AGGREGATOR.getName(), MsgBusFields.COMMUNITY_LIST.getName(), MsgBusFields.EXT_COMMUNITY_LIST.getName(), 
                            MsgBusFields.CLUSTER_LIST.getName(), MsgBusFields.ISATOMICAGG.getName(), MsgBusFields.IS_NEXTHOP_IPV4.getName(), MsgBusFields.ORIGINATOR_ID.getName()]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.getContent()

        super(BaseAttribute, self).__init__()

        self.headerNames = BaseAttribute.minimumHeaderNames

        self.parse(self.spec_version, data);

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
