
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

from abc import ABCMeta, abstractmethod
import json

# Compatible with python 2 and 3
ABC = ABCMeta('ABC', (object,), {'__slots__': ()})


class Base(ABC):
    """
    Base class for parsing openbmp.parsed.* messages.

    See http://openbmp.org/#!docs/MESSAGE_BUS_API.md for more details.

    Schema Version: 1.7

    The schema version is the max version supported.  Each extended class is responsible for handling
    backwards compatibility.
    """

    def __init__(self):
        """Initializes the class variables."""
        # Default message bus specification version (max) supported
        self.spec_version = float(1.7)
        # Column field header names will be the MAP key for fields, order matters and must match TSV order of fields.
        self.header_names = []
        # List of records as dictionaries of records.
        self.row_map = []

        # List of cell processors
        self.processors = []

    @abstractmethod
    def get_processors(self):
        """
        Processors used for each field.

        Order matters and must match the same order as defined in headerNames

        :return: array of field processor objects
        """
        pass

    def get_row_map(self):
        """
        Get rowMap as array of dictionaries.

        :return: parsed rowMap is returned as an array of dictionaries.
        """
        return self.row_map

    def parse(self, version, data):
        """
        Parse TSV rows of data from message

        :param version: Float representation of maximum message bus specification version supported.
                            See http://openbmp.org/#!docs/MESSAGE_BUS_API.md for more details.
        :param data: TSV data (MUST not include the headers)

        :return:  True if error, False if no errors
        """
        if not data:
            return False

        if not data.strip():  # If "data" is not string, throws error.
            raise ValueError("Invalid data!", data)

        self.spec_version = float(version)

        if len(self.header_names) == 0:
            raise Exception("header_names should be overriden.")

        records = data.splitlines()

        # # Splits each record into fields.
        for r in records:
            fields = r.split('\t')  # Fields of a record as array.

            # # # Process and validate each field with its corresponding processor.
            if len(fields) >= len(self.processors):
                for i,processor in enumerate(self.processors):
                    fields[i] = processor.process_value(fields[i])

            fields_dict = dict(list(zip(self.header_names, fields)))

            self.row_map.append(fields_dict)

    def to_json(self):
        """
        Get rowMap as Json

        :return: JSON String representing the parsed rowMap
        """
        return json.dumps(self.row_map)

    def to_json_pretty(self):
        """
        Get rowMap as Pretty Json.

        :return: Pretty formatted JSON String representing the parsed rowMap.
        """
        return json.dumps(self.row_map, indent=4, sort_keys=False)
