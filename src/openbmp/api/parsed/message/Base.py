
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

from abc import ABCMeta, abstractmethod
import json

class Base(object):
    """
    Base class for parsing openbmp.parsed.* messages.

    See http://openbmp.org/#!docs/MESSAGE_BUS_API.md for more details.

    Schema Version: 1.3

    The schema version is the max version supported.  Each extended class is responsible for handling
        backwards compatibility.
    """

    __metaclass__ = ABCMeta

    def __init__(self):
        """Initializes the class variables."""
        self.spec_version = float(1.3) # Default message bus specification version (max) supported
        self.headerNames = [] # Column field header names will be the MAP key for fields, order matters and must match TSV order of fields.
        self.rowMap = [] # List of records as dictionaries of records.

    @abstractmethod
    def getProcessors(self):
        """
        Processors used for each field.

        Order matters and must match the same order as defined in headerNames

        :return: array of field processor objects
        """
        pass

    def getRowMap(self):
        """
        Get rowMap as array of dictionaries.

        :return: parsed rowMap is returned as an array of dictionaries.
        """
        return self.rowMap

    def parse(self, version, data):
        """
        Parse TSV rows of data from message

        :param version: Float representation of maximum message bus specification version supported.
                            See http://openbmp.org/#!docs/MESSAGE_BUS_API.md for more details.
        :param data: TSV data (MUST not include the headers)

        :return:  True if error, False if no errors
        """
        if not data.strip(): # If "data" is not string, throws error.
            raise "Invalid data!", data

        self.spec_version = float(version)

        records = data.splitlines() # Splits data into records.

        # Splits each record into fields.
        for r in records:
            fields = r.split('\t')  # Fields of a record as array.

            fieldsMap = dict(zip(self.headerNames, fields))

            # Process and validate each field with its corresponding processor.
            for (f, p, h) in zip(fields, self.getProcessors(), self.headerNames):
                fieldsMap[h] = p.processValue(f)

            self.rowMap.append(fieldsMap)

    def toJson(self):
        """
        Get rowMap as Json

        :return: JSON String representing the parsed rowMap
        """
        return json.dumps(self.rowMap)

    def toJsonPretty(self):
        """
        Get rowMap as Pretty Json.

        :return: Pretty formatted JSON String representing the parsed rowMap.
        """
        return json.dumps(self.rowMap, indent=4, sort_keys=False)
