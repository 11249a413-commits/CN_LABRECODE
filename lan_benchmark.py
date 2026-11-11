"""
Experiment 15: Small LAN topology benchmark calculator.
Enter observed values from the LAN trainer kit or lab test. The program calculates
throughput, packet delivery ratio and average delay.
"""
import argparse

def main():
    p = argparse.ArgumentParser(description="Calculate basic LAN benchmark metrics.")
    p.add_argument("--sent", type=int, default=1000, help="Packets transmitted")
    p.add_argument("--received", type=int, default=990, help="Packets received")
    p.add_argument("--bytes", dest="byte_count", type=int, default=1200, help="Payload bytes per packet")
    p.add_argument("--duration", type=float, default=2.0, help="Test duration in seconds")
    p.add_argument("--delay-ms", type=float, default=2.5, help="Observed average delay in milliseconds")
    args = p.parse_args()
    if args.sent <= 0 or args.received < 0 or args.received > args.sent or args.byte_count <= 0 or args.duration <= 0 or args.delay_ms < 0:
        p.error("Check packet counts, payload size, duration and delay.")
    pdr = args.received / args.sent * 100
    throughput = args.received * args.byte_count * 8 / args.duration / 1_000_000
    loss = args.sent - args.received
    print("LAN topology benchmark")
    print(f"Packets sent             : {args.sent}")
    print(f"Packets received         : {args.received}")
    print(f"Packets lost             : {loss}")
    print(f"Packet delivery ratio    : {pdr:.2f}%")
    print(f"Packet loss ratio        : {100-pdr:.2f}%")
    print(f"Average delay            : {args.delay_ms:.3f} ms")
    print(f"Measured throughput      : {throughput:.3f} Mbps")
    print("\nRepeat the test for each topology and compare the measured results.")
    print("These are calculations from your entered measurements, not automatic hardware measurements.")

if __name__ == "__main__":
    main()
