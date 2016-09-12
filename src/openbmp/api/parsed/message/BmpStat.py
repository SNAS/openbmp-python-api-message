
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

class BmpStat(Base):
    """
        Format class for bmp_stat parsed messages (openbmp.parsed.bmp_stat)

        Schema Version: 1.2
    """

    minimumHeaderNames = [MsgBusFields.ACTION['name'],MsgBusFields.SEQUENCE['name'],MsgBusFields.ROUTER_HASH['name'],
                          MsgBusFields.ROUTER_IP['name'], MsgBusFields.PEER_HASH['name'],MsgBusFields.PEER_IP['name'],
                          MsgBusFields.PEER_ASN['name'],MsgBusFields.TIMESTAMP['name'],MsgBusFields.REJECTED['name'],
                          MsgBusFields.KNOWN_DUP_UPDATES['name'],MsgBusFields.KNOWN_DUP_WITHDRAWS['name'],
                          MsgBusFields.INVALID_CLUSTER_LIST['name'],MsgBusFields.INVALID_AS_PATH['name'],
                          MsgBusFields.INVALID_ORIGINATOR['name'],MsgBusFields.INVALID_AS_CONFED['name'],
                          MsgBusFields.PRE_POLICY['name'],MsgBusFields.POST_POLICY['name']]

    def __init__(self, message):
        """
        Handle the message by parsing it and storing the data in memory.

        :param message: 'Message' object.
        """
        if not isinstance(message, Message):
            raise TypeError("Expected Message object instead of type " + type(message))

        data = message.getContent()

        super(BmpStat, self).__init__()
        self.headerNames = BmpStat.minimumHeaderNames

        self.parse(self.spec_version, data)

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
            NotNull(), # router_ip
            NotNull(), # peer_hash
            NotNull(), # peer_ip,
            ParseLong(), # peer_asn
            ParseTimestamp(), # Timestamp
            NotNull(), # rejected
            NotNull(), # known_dup_updates
            NotNull(), # known_dup_withdraws
            NotNull(), # invalid_cluster_list
            NotNull(), # invalid_as_path
            NotNull(), # invalid_originator
            NotNull(), # invalid_as_confed
            NotNull(), # pre_policy
            NotNull() # post_policy
        ]

        return processors
