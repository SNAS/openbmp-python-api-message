
"""
    Copyright (c) 2015-2016 Cisco Systems, Inc. and others.  All rights reserved.
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License v1.0 which accompanies this distribution,
    and is available at http://www.eclipse.org/legal/epl-v10.html
"""

from abc import ABCMeta, abstractmethod

class BaseFieldProcessor(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def parse(value):
        pass

class NotNull(BaseFieldProcessor):

    def __init__(self):
        pass

    def parse(value):
        super(value)

class ParseLong(BaseFieldProcessor):

    def __init__(self):
        pass

    def parse(value):
        super(value)

class ParseNullAsEmpty(BaseFieldProcessor):

    def __init__(self):
        pass

    def parse(value):
        super(value)

class ParseTimestamp(BaseFieldProcessor):

    def __init__(self):
        pass

    def parse(value):
        super(value)

class ParseInt(BaseFieldProcessor):

    def __init__(self):
        pass

    def parse(value):
        super(value)

class ParseLongEmptyAsZero(BaseFieldProcessor):

    def __init__(self):
        pass

    def parse(value):
        super(value)