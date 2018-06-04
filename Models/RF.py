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

    def get_XL_position():

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        if receiver.available():
            regex = r"(\X\L).+?(.+)"
            received_value = receiver.getReceivedValue()
            if received_value:
                matches = re.finditer(regex, received_value, re.MULTILINE)

                for matchNum, match in enumerate(matches):
                    matchNum = matchNum + 1

                    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                end=match.end(), match=match.group()))

                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1

                        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                                    start=match.start(groupNum),
                                                                                    end=match.end(groupNum),
                                                                                    group=match.group(groupNum)))
            receiver.resetAvailable()

    def get_XR_position(self):

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        if receiver.available():
            regex = r"(\X\R).+?(.+)"
            received_value = receiver.getReceivedValue()
            if received_value:
                matches = re.finditer(regex, received_value, re.MULTILINE)

                for matchNum, match in enumerate(matches):
                    matchNum = matchNum + 1

                    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                    end=match.end(), match=match.group()))

                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1

                        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                                        start=match.start(groupNum),
                                                                                        end=match.end(groupNum),
                                                                                        group=match.group(groupNum)))
            receiver.resetAvailable()

    def get_YL_position(self):

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        if receiver.available():
            regex = r"(\X\L).+?(.+)"
            received_value = receiver.getReceivedValue()
            if received_value:
                matches = re.finditer(regex, received_value, re.MULTILINE)

                for matchNum, match in enumerate(matches):
                    matchNum = matchNum + 1

                    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                    end=match.end(), match=match.group()))

                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1

                        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                                        start=match.start(groupNum),
                                                                                        end=match.end(groupNum),
                                                                                        group=match.group(groupNum)))
            receiver.resetAvailable()

    def get_YR_position(self):

        receiver = RCSwitchReceiver()
        receiver.enableReceive(2)

        if receiver.available():
            regex = r"(\X\L).+?(.+)"
            received_value = receiver.getReceivedValue()
            if received_value:
                matches = re.finditer(regex, received_value, re.MULTILINE)

                for matchNum, match in enumerate(matches):
                    matchNum = matchNum + 1

                    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                    end=match.end(), match=match.group()))

                    for groupNum in range(0, len(match.groups())):
                        groupNum = groupNum + 1

                        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                                        start=match.start(groupNum),
                                                                                        end=match.end(groupNum),
                                                                                        group=match.group(groupNum)))
            receiver.resetAvailable()


