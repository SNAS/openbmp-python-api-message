
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

from abc import ABCMeta, abstractmethod

class Base(object):
    __metaclass__ = ABCMeta

    __DEFAULT_SPEC_VERSION = float(1.3) # Default message bus specification version (max) supported
    _spec_version = float(1.0) # Configured message bus specification version (max) supported
    _headerNames = []
    _rowMap = 0

    def parse(self, data):
        if not data.strip(): # If "data" is not string, throws error.
            raise "Invalid data!", data

        return self.parse(self.__DEFAULT_SPEC_VERSION, data)

    def parse(self, version, data):
        self._spec_version = float(version)

        # Read tab deliminated data.
        values = data.split("\t")
        print values