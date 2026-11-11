# Experiment 14 – Build a simple network in Cisco Packet Tracer

## Topology
Create:
- 1 × Cisco 2911 router (R1)
- 1 × 2960 switch (S1)
- 2 × PCs (PC0 and PC1)

Connect PC0 → S1, PC1 → S1, and S1 → R1 GigabitEthernet0/0 using copper straight-through cables.

## IP addressing
| Device | Interface | IP address | Mask | Default gateway |
|---|---|---|---|---|
| R1 | G0/0 | 192.168.10.1 | 255.255.255.0 | — |
| PC0 | FastEthernet0 | 192.168.10.10 | 255.255.255.0 | 192.168.10.1 |
| PC1 | FastEthernet0 | 192.168.10.11 | 255.255.255.0 | 192.168.10.1 |

## Router configuration
Open R1 → CLI and enter:

```text
enable
configure terminal
hostname R1
interface gigabitEthernet 0/0
 ip address 192.168.10.1 255.255.255.0
 no shutdown
exit
end
write memory
```

## PC configuration
For each PC, open **Desktop → IP Configuration** and enter the IP address, subnet mask and default gateway from the table.

## Verification
1. Wait until links turn green.
2. On PC0, open **Desktop → Command Prompt**.
3. Run `ping 192.168.10.11`.
4. Run `ping 192.168.10.1`.
5. Use **Simulation** mode to observe ARP and ICMP packets.
6. Save the project as `simple_network.pkt`.

## Expected result
PC0 and PC1 are in the same subnet and should ping each other through the switch. The router interface provides the default gateway for the LAN. This starter topology does not require routing between multiple LANs.
