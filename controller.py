#!/usr/bin/python
from pox.core import core
from pox.lib.util import dpid_to_str
from pox.lib.revent import *
from pox.forwarding.l2_learning import LearningSwitch

log = core.getLogger()

class ConnectionUp(Event):
    def __init__(self,connection,ofp):
        Event.__init__(self)
        self.connection = connection
        self.dpid = connection.dpid
        self.ofp = ofp
class ConnectionDown(Event):
    def __init__(self,connection,ofp):
        Event.__init__(self)
        self.connection = connection
        self.dpid = connection.dpid

class Firewall(LearningSwitch):
    def __init__(self,connection):
        LearningSwitch.__init__(self,connection,False)
        log.info("Created Firewall")


class MyComponent(object):
    def __init__(self):
        core.openflow.addListeners(self)

    def _handle_ConnectionUp(self,event):
        ConnectionUp(event.connection,event.ofp)
        #log.info("Switch %s has come up.",dpid_to_str(event.dpid))
        if event.dpid in [1,2,3,4,5]:
           LearningSwitch(event.connection,False)
        elif event.dpid == 6:
           Firewall(event.connection)
        elif event.dpid == 7:
           Firewall(event.connection)
        else:
           LearningSwitch(event.connection,False)
           log.info("Not supported Switch")

    def _handle_ConnectionDown(self,event):
        ConnectionDown(event.connection,event.dpid)
        log.info("Switch %s has shutdown.",dpid_to_str(event.dpid))

def launch():
    core.registerNew(MyComponent)