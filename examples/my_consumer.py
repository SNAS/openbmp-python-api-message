#!/usr/bin/env python3

import yaml
import datetime
import time
import kafka

from openbmp.api.parsed.message.Message import Message
from openbmp.api.parsed.message.BmpStat import BmpStat
from openbmp.api.parsed.message.Collector import Collector
from openbmp.api.parsed.message.LsLink import LsLink
from openbmp.api.parsed.message.LsNode import LsNode
from openbmp.api.parsed.message.LsPrefix import LsPrefix
from openbmp.api.parsed.message.Peer import Peer
from openbmp.api.parsed.message.Router import Router
from openbmp.api.parsed.message.UnicastPrefix import UnicastPrefix
from openbmp.api.parsed.message.MsgBusFields import MsgBusFields


def process_message(msg):
    """ Process the message

    :param msg:     Message consumed

    :return:
    """

    m = Message(msg.value)  # Gets body of kafka message.
    t = msg.topic  # Gets topic of kafka message.
    m_tag = t.split('.')[2].upper()
    t_stamp = str(datetime.datetime.now())

    if t == "openbmp.parsed.unicast_prefix":
        unicast_prefix = UnicastPrefix(m)
        # print ('\n' + 'Received Message (' + t_stamp + ') : ' + m_tag + '(V: ' + str(m.version) + ')')
        for row in unicast_prefix.get_row_map():
            print(("%s | %s | %20s | %s" % (row[MsgBusFields.TIMESTAMP.get_name()],
                   row[MsgBusFields.ACTION.get_name()],
                   "%s/%d" % (row['prefix'],
                              row[MsgBusFields.PREFIX_LEN.get_name()]),
                   row[MsgBusFields.AS_PATH.get_name()])))

            #print ("row_map: %r" % unicast_prefix.get_row_map())



def main():
    # Enable to topics/feeds
    topics = [
        'openbmp.parsed.unicast_prefix'
#        'openbmp.parsed.router', 'openbmp.parsed.peer', 'openbmp.parsed.collector',
#        'openbmp.parsed.bmp_stat', 'openbmp.parsed.unicast_prefix', 'openbmp.parsed.ls_node',
#        'openbmp.parsed.ls_link', 'openbmp.parsed.ls_prefix'
    ]

    # Read config file
    with open('config.yaml', 'r') as f:
        config_content = yaml.load(f)

    bootstrap_server = config_content['bootstrap_servers']

    try:
        # connect and bind to topics
        print ("Connecting to kafka... takes a minute to load offsets and topics, please wait")
        consumer = kafka.KafkaConsumer(
            *topics,
            bootstrap_servers=bootstrap_server,
            client_id="dev-testing" + str(time.time()),
            group_id="dev-testing" + str(time.time()),
            enable_auto_commit=True,
            auto_commit_interval_ms=1000,
            auto_offset_reset="largest"
        )

        print ("Now consuming/waiting for messages...")
        for m in consumer:
            process_message(m)

    except kafka.common.KafkaUnavailableError as err:
        print(("Kafka Error: %s" % str(err)))

    except KeyboardInterrupt:
        print ("User stop requested")


if __name__ == '__main__':
    main()
