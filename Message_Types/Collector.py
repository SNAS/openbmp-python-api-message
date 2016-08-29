
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http:#www.eclipse.org/legal/epl-v10.html
"""
import Base.py
from FieldProcessors import *

"""
    Format class for collector parsed messages (openbmp.parsed.collector)

    Schema Version: 1.2
"""

class Collector(Base):

    def __init__(self, data):

        self.headerNames = ["action", "seq", "admin_id", "hash", "routers", "router_count", "timestamp"]

        # Change below to supply version when version is required
        self.parse(data);

    def getProcessors(self):
        processors = None

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
