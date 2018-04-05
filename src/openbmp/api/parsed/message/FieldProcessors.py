
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

from abc import ABCMeta, abstractmethod
import calendar
import datetime

# Compatible with python 2 and 3
ABC = ABCMeta('ABC', (object,), {'__slots__': ()})


class BaseFieldProcessor(ABC):
    """
    Parent class of field processors.
    """

    def __init__(self):
        pass

    @abstractmethod
    def process_value(self, field_to_process):
        """
        Parses and validates the input field.

        :param field_to_process: Data to process and validate.
        :return: Processed and validated data.
        """
        value = field_to_process
        return value


class NotNull(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def process_value(self, field_to_process):
        """
        Validates the input by checking if data is null or empty.

        :param field_to_process: Data to process and validate.
        :return: Processed and validated data.
        """
        value = field_to_process

        if field_to_process is None or field_to_process.strip() == "":
            value = ""

        return str(value)


class ParseLong(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def process_value(self, field_to_process):
        """
        Validates the input by checking if data is long and if it is not returns 0.

        :param field_to_process: Data to process and validate.
        :return: Processed and validated data.
        """
        value = None

        try:
            value = int(field_to_process)

        except ValueError:
            # Handle the exception
            value = int(0)

        return value


class ParseNullAsEmpty(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def process_value(self, field_to_process):
        """
        Validates the input by checking if data is null or empty.

        :param field_to_process: Data to process and validate.
        :return: Processed and validated data.
        """
        value = field_to_process

        if field_to_process is None or field_to_process.strip() == "":
            value = ""

        return str(value)


class ParseTimestamp(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def process_value(self, field_to_process):
        """
        Validates the input by checking if data is a timestamp and returns in timestamp format.

        :param field_to_process: Data to process and validate.
        :return: Processed and validated data.
        """
        try:
            # Date format YYYY-MM-DD HH:MM:SS.nnnnnn
            dt = datetime.datetime(
                  int(field_to_process[0:4]), # %Y
                  int(field_to_process[5:7]), # %m
                  int(field_to_process[8:10]), # %d
                  int(field_to_process[11:13]), # %H
                  int(field_to_process[14:16]), # %M
                  int(field_to_process[17:19]), # %s
                  int(field_to_process[20:26]) # %f
                  )

            # Get only ms (first 3 digits of us)
            t_us = int(field_to_process[20:23])

            t_struct = dt.timetuple()

            secs = int(calendar.timegm(t_struct)) * 1000

            return int(secs + (t_us / 1000))

        except ValueError:
            return 0
        except TypeError:
            return 0


class ParseInt(BaseFieldProcessor):
    """
    A field processor type and extends "BaseFieldProcessor".
    """

    def __init__(self):
        pass

    def process_value(self, field_to_process):
        """
        Validates the input by checking if data is an integer or not.

        :param field_to_process: Data to process and validate.
        :return: Processed and validated data.
        """

        value = None

        try:
            value = int(field_to_process)

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

    def process_value(self, field_to_process):
        """
        Validates the input by checking if data is an long or not.

        :param field_to_process: Data to process and validate.
        :return: Processed and validated data.
        """

        value = None

        try:
            value = int(field_to_process)

        except ValueError:
            # Handle the exception
            value = int(0)

        return value
