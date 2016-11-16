# Log Consumer Example - OpenBMP API Message Python Library

Log consumer example uses OpenBMP API Message Python library.


## Install Dependencies:

```sh
sudo apt-get install python-dev python-pip libsnappy-dev
sudo pip install python-snappy
sudo pip install kafka-python
sudo pip install pyyaml
``` 

## Configuration

config.yaml file can be modified to change Kafka server address as below:

```yaml
bootstrap_servers: kafka-int.openbmp.org # Kafka server address.
```

## Run 

You can run log consumer example as below:

```sh
python log_consumer.py
```
