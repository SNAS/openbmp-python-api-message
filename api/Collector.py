
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
from Base import *
from FieldProcessors import *

class Collector(Base):
    """
        Format class for collector parsed messages (openbmp.parsed.collector)

        Schema Version: 1.2
    """

    def __init__(self, data):
        """
        Handle the message by parsing it and storing the data in memory.

        :param data: Data to parse.
        """

        super(Collector, self).__init__()
        self.headerNames = ["action", "seq", "admin_id", "hash", "routers", "router_count", "timestamp"]

        # Change below to supply version when version is required
        self.parse(Base.DEFAULT_SPEC_VERSION, data)

    def getProcessors(self):
        """
        Processors used for each field.
        Order matters and must match the same order as defined in headerNames

        :return: array of cell processors.
        """

        processors = [

            NotNull(), # action
            ParseLong(), # seq
            NotNull(), # admin
            NotNull(), # hash
            ParseNullAsEmpty(), # routers
            ParseInt(), # router count
            ParseTimestamp() # Timestamp
        ]

        return processors
