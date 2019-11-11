from genie.parsergen import extend_markup

marked_up_output = '''\
OS: NXOS

CMD: show_interface_<WORD>

SHOWCMD: show interface {ifname}

PREFIX: show.intf

ACTUAL:
mgmt0 is up
admin state is up
  Hardware: Ethernet, address: 5254.0070.0dff (bia 5254.0070.0dff)
  Internet Address is 10.10.10.5/24
  MTU 1500 bytes, BW 0 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is routed
  auto-duplex, auto-speed
  Auto-Negotiation is turned on
  Auto-mdix is turned off
  EtherType is 0x0000
  1 minute input rate 112 bits/sec, 0 packets/sec
  1 minute output rate 24 bits/sec, 0 packets/sec
  Rx
    71 input packets 2 unicast packets 68 multicast packets
    1 broadcast packets 22451 bytes
  Tx
    33 output packets 1 unicast packets 29 multicast packets
    3 broadcast packets 6527 bytes


MARKUP:

XW<if_name>Xmgmt0 is XR<line_protocol>Xup
admin state is XR<admin_state>Xup
  Hardware: XW<hardware>XEthernet, address: XM<mac_address>X5254.0070.0dff (bia XM<bia_address>X5254.0070.0dff)
  Internet Address is XXX<[0-9\.]+><ip_address>XXX10.10.10.5/24
  MTU XN<mtu>X1500 bytes, BW XN<bw>X0 Kbit, DLY XN<dly>X10 usec
  reliability XXX<[0-9/]+><reliability>XXX255/255, txload XXX<[0-9/]+><txload>XXX1/255, rxload XXX<[0-9/]+><rxload>XXX1/255
  Encapsulation XW<encapsulation>XARPA, medium is broadcast
  Port mode is XR<port_mode>Xrouted
  XW<duplex>Xauto-duplex, XW<speed>Xauto-speed
  Auto-Negotiation is turned XR<auto_negotiation>Xon
  Auto-mdix is turned XR<auto_mdix>Xoff
  EtherType is XH<ether_type>X0x0000
  1 minute input rate XN<input_bits_sec_60>X112 bits/sec, XN<input_packets_sec_60>X0 packets/sec
  1 minute output rate XN<output_bits_sec_60>X24 bits/sec, XN<output_packets_sec_60>X0 packets/sec
  Rx
    XN<input_packets>X71 input packets XN<rx.unicast>X2 unicast packets XN<rx.multicast>X68 multicast packets
    XN<rx.broadcast>X1 broadcast packets XN<rx.bytes>X22451 bytes
  Tx
    XN<output_packets>X33 output packets XN<tx.unicast>X1 unicast packets XN<tx.multicast>X29 multicast packets

'''

extend_markup(marked_up_output)
