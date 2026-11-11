# LAN Trainer Kit – Topology Study and Benchmark Record

## Aim
To study the available LAN topology using the LAN trainer kit and compare basic performance measurements.

## Equipment
Record the actual kit/model, PCs, switches, routers, cables and test tools used.

## Topology
Draw the actual physical/logical topology here. Label device names, ports and IP addresses.

## Test procedure
1. Connect devices according to the selected topology (star/bus/ring as supported by the kit).
2. Configure unique IP addresses in the same subnet for a single-LAN test.
3. Verify connectivity using `ping`.
4. Send a known number of packets or transfer a known amount of data.
5. Record sent/received packet counts, test duration and observed delay.
6. Run `python lan_benchmark.py --sent 1000 --received 990 --bytes 1200 --duration 2 --delay-ms 2.5` with your measured values.

## Observation table
| Topology | Sent | Received | Duration (s) | Avg delay (ms) | Throughput (Mbps) | Remarks |
|---|---:|---:|---:|---:|---:|---|
| Star | | | | | | |
| Other (specify) | | | | | | |

## Result
Write a short comparison using the measurements collected from the actual trainer kit. Do not copy the sample/default values as measured results.
