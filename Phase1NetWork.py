from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI

def firstNetwork():

	net = Mininet( controller=Controller )
	net.addController( 'c0' )

	#Public Zone

	h1 = net.addHost('h1', ip='100.0.0.10/24')
    h2 = net.addHost('h2', ip='100.0.0.11/24')
    
    sw1 = net.addSwitch('s1')

    net.addLink(h1, sw1)
    net.addLink(h2, sw1)

    #Demilitarized Zone

    ds1 = net.addHost('h5', ip='100.0.0.20/24')
    ds2 = net.addHost('h6', ip='100.0.0.21/24')
    ds3 = net.addHost('h7', ip='100.0.0.22/24')

    ws1 = net.addHost('h8', ip='100.0.0.40/24')
    ws2 = net.addHost('h9', ip='100.0.0.41/24')
    ws3 = net.addHost('h10', ip='100.0.0.42/24')

    insp = net.addHost('h11', ip='100.0.0.30/24')

    sw2 = net.addSwitch('s2')
    sw3 = net.addSwitch('s3')
    sw4 = net.addSwitch('s4')
    lb1 = net.addSwitch('s6')
    lb2 = net.addSwitch('s7')
    ids = net.addSwitch('s8')

    net.addLink(ds1, sw3)
    net.addLink(ds2, sw3)
    net.addLink(ds3, sw3)

    net.addLink(sw3, lb1)
    net.addLink(lb1, sw2)
    net.addLink(sw2, ids)
	net.addLink(ids, lb2)
	net.addLink(lb2, sw4)

	net.addLink(sw4, ws1)
	net.addLink(sw4, ws2)
	net.addLink(sw4, ws3)

    #Private Zone

    h3 = net.addHost('h3', ip='100.0.0.50/24')
    h4 = net.addHost('h4', ip='100.0.0.51/24')

    sw5 = net.addSwitch('s5')

    net.addLink(h3, sw5)
    net.addLink(h4, sw5)


    #Link   Public Zone---Demilitarized Zone

    fw1 = net.addSwitch('s9')

    net.addLink(sw1, fw1)
    net.addLink(fw1, sw2)

    #Link 	Demilitarized Zone---Private 

    fw2 = net.addSwitch('s10')
    napt = net.addSwitch('s11')

    net.addLink(sw2, fw2)
    net.addLink(fw2, napt) 
    net.addLink(napt, sw5)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )