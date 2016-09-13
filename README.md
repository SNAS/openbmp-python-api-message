# OpenBMP API Message Python Library

This library implements the OpenBMP message bus specification as defined at [MESSAGE_BUS_API.md](http://openbmp.org/#!docs/MESSAGE_BUS_API.md).
 
Messages from kafka (headers and content) are parsed and made available in ```Map``` and String/JSON.
> ### API supports Python 2.7
> ### Current Schema supported is 1.3

## Install 

    $ git clone 
    $ cd openbmp-python-api-message
    $ python setup.py install
    
## Usage
 
Use this library in any existing python project.

### Code

```python
from openbmp.api.parsed.message import Message
from openbmp.api.parsed.message import Peer

raw_kafka_message_data = '...';

msg = Message(raw_kafka_message_data)

#Parse the content data by its type
peer = Peer(msg);

#Do something with peer.getRowMap() or peer.toJson() or peer.toJsonPretty()

```

#### Message
Normally the first thing to do is parse the raw Kafka received message by using the ```Message``` class.  This class
will parse the headers and content data. 


#### Message Specific Classes
Each message type, such as ***Router***, ***Peer***, ***UnicastPrefix***, ***LsPrefix***, ***LsNode***, ***LsLink***, ***Collector***, ***BmpStat***, ***BaseAttribute*** are parsed based on  [MESSAGE_BUS_API.md](http://openbmp.org/#!docs/MESSAGE_BUS_API.md).  This is why
there is a separate class for each type.  All classes return the same data for use by your application.  

```python

    def getRowMap(self):
        """
        Get rowMap as array of dictionaries.
    
        :return: parsed rowMap is returned as an array of dictionaries.
        """
    
    def toJson(self):
        """
        Get rowMap as Json
        
        :return: JSON String representing the parsed rowMap
        """

    def toJsonPretty(self):
        """
        Get rowMap as Pretty Json.
    
        :return: Pretty formatted JSON String representing the parsed rowMap.
        """

```
