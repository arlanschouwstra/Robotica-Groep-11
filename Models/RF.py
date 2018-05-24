#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging

from rpi_rf import RFDevice


class RF:
    def __init__(self, servos):
        self.servos = servos
        pass

    def send(self):
        rfdevice = None

        # pylint: disable=unused-argument
        def exithandler(signal, frame):
            rfdevice.cleanup()
            sys.exit(0)


        logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                            format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

        parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
        parser.add_argument('-g', dest='gpio', type=int, default=27,
                            help="GPIO pin (Default: 27)")
        args = parser.parse_args()

        signal.signal(signal.SIGINT, exithandler)
        rfdevice = RFDevice(args.gpio)
        rfdevice.enable_rx()
        timestamp = None
        logging.info("Listening for codes on GPIO " + str(args.gpio))
        while True:
            if rfdevice.rx_code_timestamp != timestamp:
                timestamp = rfdevice.rx_code_timestamp
                logging.info(str(rfdevice.rx_code) +
                             " [pulselength " + str(rfdevice.rx_pulselength) +
                             ", protocol " + str(rfdevice.rx_proto) + "]")
            time.sleep(0.01)
        rfdevice.cleanup()
        pass

    def receive(self):
            logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                                format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

            parser = argparse.ArgumentParser(description='Sends a decimal code via a 433/315MHz GPIO device')
            parser.add_argument('code', metavar='CODE', type=int,
                                help="Decimal code to send")
            parser.add_argument('-g', dest='gpio', type=int, default=17,
                                help="GPIO pin (Default: 17)")
            parser.add_argument('-p', dest='pulselength', type=int, default=None,
                                help="Pulselength (Default: 350)")
            parser.add_argument('-t', dest='protocol', type=int, default=None,
                                help="Protocol (Default: 1)")
            args = parser.parse_args()

            rfdevice = RFDevice(args.gpio)
            rfdevice.enable_tx()

            if args.protocol:
                protocol = args.protocol
            else:
                protocol = "default"
            if args.pulselength:
                pulselength = args.pulselength
            else:
                pulselength = "default"
            logging.info(str(args.code) +
                         " [protocol: " + str(protocol) +
                         ", pulselength: " + str(pulselength) + "]")

            rfdevice.tx_code(args.code, args.protocol, args.pulselength)
            rfdevice.cleanup()
            pass