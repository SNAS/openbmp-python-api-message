
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

    minimumHeaderNames = [MsgBusFields.ACTION['name'], MsgBusFields.SEQUENCE['name'], MsgBusFields.HASH['name'], MsgBusFields.ROUTER_HASH['name'],
                            MsgBusFields.ROUTER_IP['name'], MsgBusFields.PEER_HASH['name'], MsgBusFields.PEER_IP['name'], MsgBusFields.PEER_ASN['name'], 
                            MsgBusFields.TIMESTAMP['name'], MsgBusFields.ORIGIN['name'], MsgBusFields.AS_PATH['name'], MsgBusFields.AS_PATH_COUNT['name'], 
                            MsgBusFields.ORIGIN_AS['name'], MsgBusFields.NEXTHOP['name'], MsgBusFields.MED['name'], MsgBusFields.LOCAL_PREF['name'], 
                            MsgBusFields.AGGREGATOR['name'], MsgBusFields.COMMUNITY_LIST['name'], MsgBusFields.EXT_COMMUNITY_LIST['name'], 
                            MsgBusFields.CLUSTER_LIST['name'], MsgBusFields.ISATOMICAGG['name'], MsgBusFields.IS_NEXTHOP_IPV4['name'], MsgBusFields.ORIGINATOR_ID['name']]

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
