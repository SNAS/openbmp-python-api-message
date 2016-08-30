
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

from abc import ABCMeta, abstractmethod
import time

class BaseFieldProcessor(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def processValue(self, fieldToProcess):
        value = fieldToProcess
        return value

class NotNull(BaseFieldProcessor):

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        value = fieldToProcess

        if fieldToProcess is None or fieldToProcess.strip() == "":
            value = ""

        return str(value)

class ParseLong(BaseFieldProcessor):

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        value = None

        try:
            value = long(fieldToProcess)

        except ValueError:
            # Handle the exception
            value = long(0)

        return value

class ParseNullAsEmpty(BaseFieldProcessor):

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        value = fieldToProcess

        if fieldToProcess is None or fieldToProcess.strip() == "":
            value = ""

        return str(value)

class ParseTimestamp(BaseFieldProcessor):

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):

        return int(time.mktime(time.strptime(fieldToProcess, '%Y-%m-%d %H:%M:%S.%f')) * 1000)

class ParseInt(BaseFieldProcessor):

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        value = None

        try:
            value = int(fieldToProcess)

        except ValueError:
            # Handle the exception
            value = int(0)

        return value

class ParseLongEmptyAsZero(BaseFieldProcessor):

    def __init__(self):
        pass

    def processValue(self, fieldToProcess):
        value = None

        try:
            value = long(fieldToProcess)

        except ValueError:
            # Handle the exception
            value = long(0)

        return value