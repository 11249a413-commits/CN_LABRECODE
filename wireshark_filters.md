# Experiment 11 – Wireshark capture and display filter expressions

Wireshark has two different filter types:
- **Capture filters** are set before/during capture and use libpcap syntax.
- **Display filters** are applied after packets have been captured and use Wireshark syntax.

## Common capture filters
| Purpose | Capture filter |
|---|---|
| Host | `host 192.168.1.10` |
| Source host | `src host 192.168.1.10` |
| Destination host | `dst host 192.168.1.20` |
| TCP traffic | `tcp` |
| UDP traffic | `udp` |
| DNS | `port 53` |
| HTTP | `tcp port 80` |
| HTTPS | `tcp port 443` |
| ICMP | `icmp` |
| Traffic between two hosts | `host 192.168.1.10 and host 192.168.1.20` |

## Common display filters
| Purpose | Display filter |
|---|---|
| TCP | `tcp` |
| UDP | `udp` |
| DNS | `dns` |
| ICMP | `icmp` |
| HTTP | `http` |
| TLS/HTTPS records | `tls` |
| IPv4 address | `ip.addr == 192.168.1.10` |
| Source IP | `ip.src == 192.168.1.10` |
| Destination IP | `ip.dst == 192.168.1.20` |
| TCP port 80 | `tcp.port == 80` |
| UDP port 53 | `udp.port == 53` |
| SYN packets | `tcp.flags.syn == 1` |
| TCP retransmissions | `tcp.analysis.retransmission` |
| TCP resets | `tcp.flags.reset == 1` |
| DHCP | `dhcp` |
| ARP | `arp` |
| RTP | `rtp` |
| IPv6 | `ipv6` |
| DNS query responses | `dns.flags.response == 1` |
| Large frames | `frame.len > 1000` |

## Practical exercise
1. Open Wireshark and select the network interface currently carrying traffic.
2. Start capture. Visit a website or run `ping` to a host you are allowed to test.
3. Stop capture.
4. Enter `dns`, `tcp`, `udp`, and `icmp` one at a time in the display-filter bar.
5. Select a packet and expand Ethernet, IP, TCP/UDP and application-layer sections.
6. Record source/destination addresses, ports, protocol, frame length and timestamp.

Only capture traffic on your own device/network or where you have explicit authorization.
