# -*- coding: utf-8 -*-
from pi_switch import RCSwitchReceiver
import re

class RF:

    # for test purposes
    def receive(self):

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        num = 0

        while True:
            if receiver.available():
                received_value = receiver.getReceivedValue()

                if received_value:
                    num += 1
                    print("Received[%s]:" % num)
                    print(received_value)
                    print("%s / %s bit" % (received_value, receiver.getReceivedBitlength()))
                    print("Protocol: %s" % receiver.getReceivedProtocol())
                    print("")

                receiver.resetAvailable()

    def get_XL_position(self):

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        if receiver.available():
            regex = r"(1)0*(.+)"
            received_value = receiver.getReceivedValue()
            if received_value:
                matches = re.finditer(regex, received_value, re.MULTILINE)

                for match in enumerate(matches):

                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1
                        if groupNum == 2:
                            return match.group(groupNum)

            receiver.resetAvailable()

    def get_XR_position(self):

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        if receiver.available():
            regex = r"(3)0*(.+)"
            received_value = receiver.getReceivedValue()
            if received_value:
                matches = re.finditer(regex, received_value, re.MULTILINE)

                for match in enumerate(matches):

                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1
                        if groupNum == 2:
                            return match.group(groupNum)

            receiver.resetAvailable()

    def get_YL_position(self):

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        if receiver.available():
            regex = r"(2)0*(.+)"
            received_value = receiver.getReceivedValue()
            if received_value:
                matches = re.finditer(regex, received_value, re.MULTILINE)

                for match in enumerate(matches):

                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1
                        if groupNum == 2:
                            return match.group(groupNum)

            receiver.resetAvailable()

    def get_YR_position(self):

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        if receiver.available():
            regex = r"(4)0*(.+)"
            received_value = receiver.getReceivedValue()
            if received_value:
                matches = re.finditer(regex, received_value, re.MULTILINE)

                for match in enumerate(matches):

                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1
                        if groupNum == 2:
                            return match.group(groupNum)

            receiver.resetAvailable()


