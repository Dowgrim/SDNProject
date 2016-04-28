from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches 
        sw1 = self.addSwitch( 's1' )
        sw2 = self.addSwitch( 's2' )
        sw3 = self.addSwitch( 's3' )
        sw4 = self.addSwitch( 's4' )
        sw5 = self.addSwitch( 's5' )
        
        fw1 = self.addSwitch( 'fw1')
        fw2 = self.addSwitch( 'fw2')
        
        lb1 = self.addSwitch( 'lb1')
        lb2 = self.addSwitch( 'lb2')
        
        ids  = self.addSwitch( 'ids1')
        napt = self.addSwitch( 'napt1')
        
        h1 = self.addHost( 'h1', ip='100.0.0.10/24' )
        h2 = self.addHost( 'h2', ip='100.0.0.11/24' )
        h3 = self.addHost( 'h3', ip='100.0.0.50/24' )
        h4 = self.addHost( 'h4', ip='100.0.0.51/24' )
        
        ds1 = self.addHost( 'ds1', ip='100.0.0.20/24' )
        ds2 = self.addHost( 'ds2', ip='100.0.0.21/24' )
        ds3 = self.addHost( 'ds3', ip='100.0.0.22/24' )
        ws1 = self.addHost( 'ws1', ip='100.0.0.40/24' )
        ws2 = self.addHost( 'ws2', ip='100.0.0.41/24' )
        ws3 = self.addHost( 'ws3', ip='100.0.0.42/24' )

        insp = self.addHost( 'insp1', ip='100.0.0.30/24' )
        
        # Add links
        # Public Zone
        self.addLink( h1, sw1 )
        self.addLink( h2, sw1 )
        #Firewall 1
        self.addLink( sw1, fw1)
        self.addLink( sw2, fw1)
        #Demilitarized zone
        self.addLink( ds1, sw3 )
        self.addLink( ds2, sw3 )
        self.addLink( ds3, sw3 )
        self.addLink( ws1, sw4 )
        self.addLink( ws2, sw4 )
        self.addLink( ws3, sw4 )
       
        self.addLink( sw2, lb1 )
        self.addLink( sw3, lb1 )
        self.addLink( sw2, ids ) 
        self.addLink( lb2, ids )
        self.addLink( lb2, sw4 )
        self.addLink( ids, insp )

        #Firewall 2 , NAPT, Private zone
        self.addLink( fw2, sw2)
        self.addLink( fw2, napt)
        self.addLink( sw5, napt)
        self.addLink( h3 , sw5)
        self.addLink( h4 , sw5)


topos = { 'mytopo': ( lambda: MyTopo() ) }