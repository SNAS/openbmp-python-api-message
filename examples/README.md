# Log Consumer Example - OpenBMP API Message Python Library

Log consumer example uses OpenBMP API Message Python library.

## Dependency

Kafka client is a dependency of log consumer example (http://kafka-python.readthedocs.io/en/master/install.html).
Yaml is a dependency of log consumer example (https://pypi.python.org/pypi/PyYAML/3.12).

You can install Kafka consumer and Yaml as below:

    $ pip install kafka-python
    $ pip install pyyaml

## Configuration

config.yaml file can be modified to change Kafka server address as below:

    bootstrap_servers: kafka-int.openbmp.org # Kafka server address.

## Run 

You can run log consumer example as below:

    $ python log_consumer.py 
