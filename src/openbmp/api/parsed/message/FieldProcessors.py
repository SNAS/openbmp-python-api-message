
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

from abc import ABCMeta, abstractmethod
import time

class BaseFieldProcessor(object):
    """
    Parent class of field processors.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def processValue(self, fieldToProcess):
        """
        Parses and validates the input field.

        :param fieldToProcess: Data to process and validate.
        :return: Processed and validated data.
        """
        value = fieldToProcess
        return value

class NotNull(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        """
        Validates the input by checking if data is null or empty.

        :param fieldToProcess: Data to process and validate.
        :return: Processed and validated data.
        """
        value = fieldToProcess

        if fieldToProcess is None or fieldToProcess.strip() == "":
            value = ""

        return str(value)

class ParseLong(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        """
        Validates the input by checking if data is long and if it is not returns 0.

        :param fieldToProcess: Data to process and validate.
        :return: Processed and validated data.
        """
        value = None

        try:
            value = long(fieldToProcess)

        except ValueError:
            # Handle the exception
            value = long(0)

        return value

class ParseNullAsEmpty(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        """
        Validates the input by checking if data is null or empty.

        :param fieldToProcess: Data to process and validate.
        :return: Processed and validated data.
        """
        value = fieldToProcess

        if fieldToProcess is None or fieldToProcess.strip() == "":
            value = ""

        return str(value)

class ParseTimestamp(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        """
        Validates the input by checking if data is a timestamp and returns in timestamp format.

        :param fieldToProcess: Data to process and validate.
        :return: Processed and validated data.
        """

        return int(time.mktime(time.strptime(fieldToProcess, '%Y-%m-%d %H:%M:%S.%f')) * 1000)

class ParseInt(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        """
        Validates the input by checking if data is an integer or not.

        :param fieldToProcess: Data to process and validate.
        :return: Processed and validated data.
        """

        value = None

        try:
            value = int(fieldToProcess)

        except ValueError:
            # Handle the exception
            value = int(0)

        return value

class ParseLongEmptyAsZero(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        """
        Validates the input by checking if data is an long or not.

        :param fieldToProcess: Data to process and validate.
        :return: Processed and validated data.
        """

        value = None

        try:
            value = long(fieldToProcess)

        except ValueError:
            # Handle the exception
            value = long(0)

        return value