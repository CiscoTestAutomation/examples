from genie import parsergen as pg

marked_up_show_interface_xrvr_output = '''\
OS: iosxr

CMD: show_interface_<WORD>

SHOWCMD: show interface {ifname}

PREFIX: show.intf

ACTUAL:
show interface MgmtEth0/0/CPU0/0
Fri Mar  6 12:03:11.409 EST
XW<if_name>XMgmtEth0/0/CPU0/0 is up, line protocol is up 
  Interface state transitions: 1
  Hardware is Management Ethernet, address is 5254.00d6.36c9 (bia 5254.00d6.36c9)
  Internet address is 10.30.108.132/23
  MTU 1514 bytes, BW 0 Kbit
     reliability 255/255, txload Unknown, rxload Unknown
  Encapsulation ARPA,
  Duplex unknown, 0Kb/s, unknown, link type is autonegotiation
  output flow control is off, input flow control is off
  Carrier delay (up) is 10 msec
  loopback not set,
  ARP type ARPA, ARP timeout 04:00:00
  Last input 00:00:00, output 00:00:48
  Last clearing of "show interface" counters never
  5 minute input rate 79000 bits/sec, 32 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2459211 packets input, 774707935 bytes, 0 total input drops
     0 drops for unrecognized upper-level protocol
     Received 2216135 broadcast packets, 233738 multicast packets
              0 runts, 0 giants, 0 throttles, 0 parity
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     349 packets output, 58930 bytes, 0 total output drops
     Output 4 broadcast packets, 0 multicast packets
     0 output errors, 0 underruns, 0 applique, 0 resets
     0 output buffer failures, 0 output buffers swapped out
     1 carrier transitions


MARKUP:
show interface MgmtEth0/0/CPU0/0
Fri Mar  6 12:03:11.409 EST
XI<if_name>XMgmtEth0/0/CPU0/0 is XC<admin_state>Xup, line protocol is XW<line_protocol>Xup 
  Interface state transitions: XN<intf_trans>X1
  Hardware is XXX<[^,]+><hardware>XXXManagement Ethernet, address is XA<mac_address>X5254.00d6.36c9 (bia Xa<via>X5254.00d6.36c9)
  Internet address is XA<ip_address>X10.30.108.132/Xn<mask>X23
  MTU XN<mtu>X1514 bytes, BW XN<bw>X0 Kbit
     reliability 255/255, txload Unknown, rxload Unknown
  Encapsulation XW<encap>XARPA,
  Duplex unknown, 0Kb/s, unknown, link type is XW<link_type>Xautonegotiation
  output flow control is XW<output_flowcontrol>Xoff, input flow control is XW<input_flowcontrol>Xoff
  Carrier delay (up) is XN<carrier_delay_up>X10 msec
  loopback XXX<[^,]+><loopback_status>XXXnot set,
  ARP type ARPA, ARP timeout XT<arp_timeout>X04:00:00
  Last input XT<last_input>X00:00:00, output XT<last_output>X00:00:48
  Last clearing of "show interface" counters XR<last_clear_counter>Xnever
  5 minute input rate XN<input_rate_bits>X79000 bits/sec, XN<input_rate>X32 packets/sec
  5 minute output rate XN<output_rate_bits>X0 bits/sec, XN<output_rate>X0 packets/sec
     XN<input_pkts>X2459211 packets input, XN<input_bytes>X774707935 bytes, XN<input_total_drops>X0 total input drops
     XN<drops_unrec_upper_level_proto>X0 drops for unrecognized upper-level protocol
     Received XN<broadcasts>X2216135 broadcast packets, XN<multicasts>X233738 multicast packets
              XN<runts>X0 runts, XN<giants>X0 giants, XN<throttles>X0 throttles, XN<parity>X0 parity
     XN<input_errors>X0 input errors, XN<crc>X0 CRC, XN<frame>X0 frame, XN<overrun>X0 overrun, XN<ignored>X0 ignored, XN<abort>X0 abort
     XN<output_pkts>X349 packets output, XN<output_bytes>X58930 bytes, XN<output_total_drops>X0 total output drops
     Output XN<output_broadcast>X4 broadcast packets, XN<output_multicast>X0 multicast packets
     XN<output_errors>X0 output errors, XN<output_underruns>X0 underruns, XN<output_applique>X0 applique, XN<output_resets>X0 resets
     XN<output_buf_failures>X0 output buffer failures, XN<output_buf_swapped>X0 output buffers swapped out
     XN<carrier_trans>X1 carrier transitions

OS: ios

CMD: show_interface_<WORD>

SHOWCMD: show interface {ifname}

PREFIX: show.intf

ACTUAL:
GigabitEthernet0/0 is up, line protocol is up 
  Hardware is iGbE, address is 5254.00f7.4fe8 (bia 5254.00f7.4fe8)
  Internet address is 10.10.10.2/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full Duplex, 1Gbps, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:45, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     96 packets input, 22961 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     364 packets output, 37751 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     12 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out

MARKUP:
XI<if_name>XGigabitEthernet0/0 is XC<admin_state>Xup, line protocol is XW<line_protocol>Xup 
  Hardware is XXX<[^,]+><hardware>XXXiGbE, address is XA<mac_address>X5254.00d6.36c9 (bia Xa<via>X5254.00d6.36c9)
  Internet address is XA<ip_address>X10.30.108.132/Xn<mask>X24
  MTU XN<mtu>X1500 bytes, BW XN<bw>X1000000 Kbit/sec, DLY XN<dly>X10 usec, 
     reliability XXX<[a-z0-9/]+><reliability>XXX255/255, txload XXX<[a-z0-9/]+><txload>XXX1/255, rxload XXX<[a-z0-9/]+><rxload>XXX1/255
  Encapsulation XW<encapsulation>XARPA, loopback XR<loopback_status>Xnot set
  Keepalive XW<keepalive>Xset (10 sec)
  XW<duplex>XFull Duplex, 1Gbps, media type is XR<media_type>XRJ45
  output flow-control is XW<output_flowcontrol>Xunsupported, input flow-control is XW<input_flowcontrol>Xunsupported
  ARP type: XW<arp_type>XARPA, ARP Timeout XT<arp_timeout>X04:00:00
  Last input XT<last_input>X00:00:45, output XT<last_output>X00:00:00, output hang XR<last_output_hang>Xnever
  Last clearing of "show interface" counters XR<last_clear_counter>Xnever
  Input queue: XXX<[0-9/]+><input_queue>XXX0/75/0/0 (size/max/drops/flushes); Total output drops: XN<output_drops>X0
  Queueing strategy: XW<queueing_strategy>Xfifo
  Output queue: X<[0-9/]+><output_queue>X0/40 (size/max)
  5 minute input rate XN<input_rate_bits>X0 bits/sec, XN<input_rate_packets>X0 packets/sec
  5 minute output rate XN<output_rate_bits>X0 bits/sec, XN<output_rate_packets>X0 packets/sec
     XN<pkts_in>X96 packets input, XN<bytes_in>X22961 bytes, 0 no buffer
     Received XN<broadcasts>X0 broadcasts (XN<multicasts>X0 IP multicasts)
              XN<runts>X0 runts, XN<giants>X0 giants, XN<throttles>X0 throttles
     XN<input_errors>X0 input errors, XN<crc>X0 CRC, XN<frame>X0 frame, XN<overrun>X0 overrun, XN<ignored>X0 ignored
     XN<watchdog>X0 watchdog, XN<multicast>X0 multicast, XN<pause_input>X0 pause input
     XN<pkts_out>X364 packets output, XN<bytes_out>X37751 bytes, XN<underruns>X0
     XN<output_errors>X0 output errors, XN<collisions>X0 collisions, XN<interface_resets>X2 interface resets
     XN<unknown_protocol_drops>X12 unknown protocol drops
     XN<babbles>X0 babbles, XN<late_collision>X0 late collision, XN<deferred>X0 deferred
     XN<lost_carrier>X0 lost carrier, XN<no_carrier>X0 no carrier, XN<pause_output>X0 pause output
     XN<output_buffer_failures>X0 output buffer failures, XN<output_buffer_swap_out>X0 output buffers swapped out


OS: iosxe

CMD: show_interface_<WORD>

SHOWCMD: show interface {ifname}

PREFIX: show.intf

ACTUAL:
GigabitEthernet0/0 is up, line protocol is up 
  Hardware is iGbE, address is 5254.00f7.4fe8 (bia 5254.00f7.4fe8)
  Internet address is 10.10.10.2/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Auto Duplex, Unknown, link type is auto, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:45, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     96 packets input, 22961 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     364 packets output, 37751 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     12 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out

MARKUP:
XI<if_name>XGigabitEthernet0/0 is XC<admin_state>Xup, line protocol is XW<line_protocol>Xup 
  Hardware is XXX<[^,]+><hardware>XXXiGbE, address is XA<mac_address>X5254.00d6.36c9 (bia Xa<via>X5254.00d6.36c9)
  Internet address is XA<ip_address>X10.30.108.132/Xn<mask>X24
  MTU XN<mtu>X1500 bytes, BW XN<bw>X1000000 Kbit/sec, DLY XN<dly>X10 usec, 
     reliability XXX<[a-z0-9/]+><reliability>XXX255/255, txload XXX<[a-z0-9/]+><txload>XXX1/255, rxload XXX<[a-z0-9/]+><rxload>XXX1/255
  Encapsulation XW<encapsulation>XARPA, loopback XR<loopback_status>Xnot set
  Keepalive XW<keepalive>Xset (10 sec)
  XW<duplex>XAuto Duplex, Xw<link_speed>XUnknown, link type is XW<link_type>Xauto, media type is XR<media_type>XRJ45
  output flow-control is XW<output_flowcontrol>Xunsupported, input flow-control is XW<input_flowcontrol>Xunsupported
  ARP type: XW<arp_type>XARPA, ARP Timeout XT<arp_timeout>X04:00:00
  Last input XT<last_input>X00:00:45, output XT<last_output>X00:00:00, output hang XR<last_output_hang>Xnever
  Last clearing of "show interface" counters XR<last_clear_counter>Xnever
  Input queue: XXX<[0-9/]+><input_queue>XXX0/75/0/0 (size/max/drops/flushes); Total output drops: XN<output_drops>X0
  Queueing strategy: XW<queueing_strategy>Xfifo
  Output queue: X<[0-9/]+><output_queue>X0/40 (size/max)
  5 minute input rate XN<input_rate_bits>X0 bits/sec, XN<input_rate_packets>X0 packets/sec
  5 minute output rate XN<output_rate_bits>X0 bits/sec, XN<output_rate_packets>X0 packets/sec
     XN<pkts_in>X96 packets input, XN<bytes_in>X22961 bytes, 0 no buffer
     Received XN<broadcasts>X0 broadcasts (XN<multicasts>X0 IP multicasts)
              XN<runts>X0 runts, XN<giants>X0 giants, XN<throttles>X0 throttles
     XN<input_errors>X0 input errors, XN<crc>X0 CRC, XN<frame>X0 frame, XN<overrun>X0 overrun, XN<ignored>X0 ignored
     XN<watchdog>X0 watchdog, XN<multicast>X0 multicast, XN<pause_input>X0 pause input
     XN<pkts_out>X364 packets output, XN<bytes_out>X37751 bytes, XN<underruns>X0
     XN<output_errors>X0 output errors, XN<collisions>X0 collisions, XN<interface_resets>X2 interface resets
     XN<unknown_protocol_drops>X12 unknown protocol drops
     XN<babbles>X0 babbles, XN<late_collision>X0 late collision, XN<deferred>X0 deferred
     XN<lost_carrier>X0 lost carrier, XN<no_carrier>X0 no carrier, XN<pause_output>X0 pause output
     XN<output_buffer_failures>X0 output buffer failures, XN<output_buffer_swap_out>X0 output buffers swapped out


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

XW<if_name>Xmgmt0 is XW<line_protocol>Xup
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

OS: aireos

CMD: show_interface_<WORD>

SHOWCMD: show interface detailed {ifname}

PREFIX: show.intf

ACTUAL:
>show interface detailed management 

Interface Name................................... management
MAC Address...................................... 80:e0:1d:23:98:a0
IP Address....................................... 1.1.1.1
IP Netmask....................................... 255.255.0.0
IP Gateway....................................... 1.1.1.5
External NAT IP State............................ Disabled
External NAT IP Address.......................... 0.0.0.0
Link Local IPv6 Address.......................... fe80::82e0:1dff:fe23:98a0/64
STATE ........................................... REACHABLE
Primary IPv6 Address............................. ::/128
STATE ........................................... NONE
Primary IPv6 Gateway............................. ::
Primary IPv6 Gateway Mac Address................. 00:00:00:00:00:00
STATE ........................................... INCOMPLETE
VLAN............................................. untagged  
Quarantine-vlan.................................. 0
Active Physical Port............................. 1         
Primary Physical Port............................ 1         
Backup Physical Port............................. Unconfigured
DHCP Proxy Mode.................................. Global
Primary DHCP Server.............................. 1.1.1.10
Secondary DHCP Server............................ Unconfigured
DHCP Option 82................................... Disabled
DHCP Option 82 bridge mode insertion............. Disabled
IPv4 ACL......................................... Unconfigured
IPv6 ACL......................................... Unconfigured
mDNS Profile Name................................ Unconfigured
AP Manager....................................... Yes
Guest Interface.................................. No
L2 Multicast..................................... Enabled

MARKUP:
Interface Name................................... XI<if_name>Xmanagement
MAC Address...................................... XM<mac_address>X80:e0:1d:23:98:a0
IP Address....................................... XA<ip_address>X1.1.1.1
IP Netmask....................................... XP<ip_prefix>X255.255.0.0
IP Gateway....................................... XA<ip_gateway>X1.1.1.5
External NAT IP State............................ XR<ext_nat_ip_state>XDisabled
External NAT IP Address.......................... XA<ext_nat_ip_address>X0.0.0.0
Link Local IPv6 Address.......................... XA<link_local_ipv6_address>Xfe80::82e0:1dff:fe23:98a0/64
STATE ........................................... XR<link_local_if_state>XREACHABLE
Primary IPv6 Address............................. XP<primary_ipv6_address>X::/128
STATE ........................................... XR<primary_ipv6_if_state>XNONE
Primary IPv6 Gateway............................. XA<primary_ipv6_gw>X::
Primary IPv6 Gateway Mac Address................. XM<primary_ipv6_mac_address>X00:00:00:00:00:00
STATE ........................................... XR<primary_ipv6_gw_if_state>XINCOMPLETE
VLAN............................................. XR<vlan>Xuntagged  
Quarantine-vlan.................................. XR<quarantine_vlan>X0
Active Physical Port............................. XR<active_phys_port>X1         
Primary Physical Port............................ XR<primary_phys_port>X1         
Backup Physical Port............................. XR<backup_phys_port>XUnconfigured
DHCP Proxy Mode.................................. XR<dhcp_proxy_mode>XGlobal
Primary DHCP Server.............................. XA<primary_dhcp_server>X1.1.1.10
Secondary DHCP Server............................ XA<secondary_dhcp_server>XUnconfigured
DHCP Option 82................................... XR<dhcp_option_82>XDisabled
DHCP Option 82 bridge mode insertion............. XR<dhcp_option_82_br_mode_insertion>XDisabled
IPv4 ACL......................................... XR<ipv4_acl>XUnconfigured
IPv6 ACL......................................... XR<ipv6_acl>XUnconfigured
mDNS Profile Name................................ XR<mdns_profile_name>XUnconfigured
AP Manager....................................... XR<ap_manager>XYes
Guest Interface.................................. XR<guest_interface>XNo
L2 Multicast..................................... XR<l2_multicast>XEnabled


OS: IOSXR

CMD: show_eth_driver_interface_<WORD>
SHOWCMD: show eth-drvr interface {ifname}
PREFIX: show.ethdrvr

ACTUAL:
RP/0/0/CPU0:ios#show eth-drvr interface gigabitEthernet 0/0/0/0
Thu Mar 19 03:56:35.976 PDT
Interface Gi0/0/0/0:
  Policy (internal, version=0, size=40)
    ether_if_type: PHY
    interface_ready: 1
    is_l2: 0
    not provisioned
    l2pt: off
    mac_addr: 02fe:08cb:26c5
    trunk.native_vlan: 0
    trunk.native_is_svlan: 0
    trunk.qinq_tunneling_etype: 0x8100
    trunk.mac_acc_ingress: 0
    trunk.mac_acc_egress: 0
    trunk.filter_dot1q: 0
    trunk.filter_dot1ad: 0
    trunk.filter_mac_relay: 0
  Unicast MAC Addresses: 0


RP/0/0/CPU0:ios#show eth-drvr interface gigabitEthernet 0/0/0/0.0
Thu Mar 19 03:57:23.096 PDT
Interface Gi0/0/0/0.0:
  Policy (internal, version=0, size=60)
    ether_if_type: PHY_L3_SUB
    interface_ready: 1
    is_l2: 0
    sub.parent: 0x00000100
    sub.admin_up: 0
    EFP MATCH: (none)
    EFP REWRITE: (none)
  Unicast MAC Addresses: 0


MARKUP:
Interface XXX<[-A-Za-z0-9\.+/]+><if_name>XXXGi0/0/0/0:
  Policy (internal, version=0, size=XN<policy_size>X40)
    ether_if_type: XR<ether_if_type>XPHY
    interface_ready: XN<if_ready>X1
    is_l2: XN<is_l2>X0
    XW<provisioned>Xnot provisioned
    l2pt: XR<l2pt>Xoff
    mac_addr: XM<mac_addr>X02fe:08cb:26c5
    trunk.native_vlan: XN<trunk.native_vlan>X0
    trunk.native_is_svlan: XN<trunk.native_is_svlan>X0
    trunk.qinq_tunneling_etype: XH<trunk.qinq_tunneling_etype>X0x8100
    trunk.mac_acc_ingress: XN<trunk.mac_acc_ingress>X0
    trunk.mac_acc_egress: XN<trunk.mac_acc_egress>X0
    trunk.filter_dot1q: XN<trunk.filter_dot1q>X0
    trunk.filter_dot1ad: XN<trunk.filter_dot1ad>X0
    trunk.filter_mac_relay: XN<trunk.filter_mac_relay>X0
    sub.parent: XH<sub.parent>X0x00000100
    sub.admin_up: XN<sub.admin_up>X0
    EFP MATCH: XR<sub.efp_match>X(none)
    EFP REWRITE: XR<sub.efp_rewrite>X(none)
  Unicast MAC Addresses: XN<unicast_mac_addr>X0

'''

pg.extend_markup(marked_up_show_interface_xrvr_output)

show_cmds = {
    'iosxr': {
        'SHOW_ARP' : "show arp",
    },
    'ios': {
        'SHOW_ARP' : "show arp",
    },
    'iosxe': {
        'SHOW_ARP' : "show arp",
    },
    'nxos': {
        'SHOW_ARP' : "show {=ip} arp",
    },
    'aireos': {
        'SHOW_ARP' : "show arp kernel",
    }
}
pg.extend(show_cmds=show_cmds)

