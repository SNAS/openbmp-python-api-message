
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

from abc import ABCMeta, abstractmethod
import json

class Base(object):
    __metaclass__ = ABCMeta

    __DEFAULT_SPEC_VERSION = float(1.3)  # Default message bus specification version (max) supported

    def __init__(self):
        self.spec_version = float(0.0) # Configured message bus specification version (max) supported
        self.headerNames = []
        self.rowMap = [] # List of records as dictionaries of records.

    @abstractmethod
    def getProcessors(self):
        #return self.processors
        pass

    def getRowMap(self):
        return self.rowMap

    def parse(self, data):
        if not data.strip(): # If "data" is not string, throws error.
            raise "Invalid data!", data

        return self.parse(self.__DEFAULT_SPEC_VERSION, data)

    def parse(self, version, data):
        self.spec_version = float(version)

        #print self.headerNames
        #print self.getProcessors()

        # Splits data into records.
        records = data.splitlines()

        # Splits each record into fields.
        for r in records:
            fields = r.split('\t')  # Fields of a record as array.

            fieldsMap = dict(zip(self.headerNames, fields))

            # Process and validate each field with its corresponding processor.
            for (f, p, h) in zip(fields, self.getProcessors(), self.headerNames):
                fieldsMap[h] = p.processValue(f)

            self.rowMap.append(fieldsMap)
            #print fieldsMap

    def toJson(self):
        return json.dumps(self.rowMap)

    def toJsonPretty(self):
        return json.dumps(self.rowMap, indent=4, sort_keys=False)




