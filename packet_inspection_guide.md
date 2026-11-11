# Experiment 13 – Inspect packets on your network using Wireshark

## Procedure
1. Install/open Wireshark.
2. Choose the active Wi-Fi or Ethernet interface. Start capture.
3. Generate test traffic from your own machine:
   - DNS: `nslookup example.com`
   - ICMP: `ping example.com`
   - HTTPS: open a website in a browser.
4. Stop capture after 20–30 seconds.
5. Apply the display filters below and inspect representative packets.

## Filters to try
- `arp`
- `dns`
- `icmp`
- `tcp`
- `udp`
- `tls`
- `tcp.analysis.retransmission`

## Observation table (complete from your own capture)
| No. | Filter/protocol | Source | Destination | Source port | Destination port | Observation |
|---|---|---|---|---|---|---|
| 1 | ARP | | | | | |
| 2 | DNS | | | | | |
| 3 | ICMP | | | | | |
| 4 | TCP | | | | | |
| 5 | TLS | | | | | |

## What to inspect
- Frame: frame number, capture time and frame length.
- Ethernet: source and destination MAC addresses.
- IP: source/destination IP, TTL/hop limit and protocol.
- TCP/UDP: source/destination ports and flags/length.
- Application protocol: DNS query name, HTTP metadata (if visible), RTP fields, etc.

HTTPS application payload is encrypted; do not expect to read website passwords or page contents from an ordinary TLS capture. Capture only traffic you are authorized to inspect.
