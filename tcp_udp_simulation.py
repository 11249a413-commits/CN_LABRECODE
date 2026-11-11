"""
Experiment 7: Simplified TCP vs UDP performance simulation.
Models packet delivery over a lossy link with a configurable retransmission policy.
This is an educational abstraction, not a full TCP/IP implementation.
"""
import argparse
import random
import statistics
import time

def simulate(protocol, packets, loss, delay_ms, bandwidth_mbps, seed=7):
    rng = random.Random(seed)
    delivered = 0
    attempts = 0
    total_delay = 0.0
    start = time.perf_counter()

    for _ in range(packets):
        retries = 0
        while True:
            attempts += 1
            serialization_ms = (1200 * 8) / (bandwidth_mbps * 1_000_000) * 1000
            packet_delay = delay_ms + serialization_ms + rng.uniform(0, delay_ms * 0.15)
            total_delay += packet_delay
            if rng.random() >= loss:
                delivered += 1
                break
            if protocol == "UDP" or retries >= 5:
                break
            retries += 1
            # Simplified retransmission/timeout cost.
            total_delay += delay_ms * 2

    elapsed = time.perf_counter() - start
    return {
        "protocol": protocol,
        "sent": packets,
        "delivered": delivered,
        "delivery_pct": delivered / packets * 100 if packets else 0,
        "attempts": attempts,
        "avg_delay_ms": total_delay / attempts if attempts else 0,
        "goodput_kbps": (delivered * 1200 * 8 / 1000) / max(elapsed, 1e-9),
    }

def main():
    p = argparse.ArgumentParser(description="Compare simplified TCP-like and UDP delivery.")
    p.add_argument("--packets", type=int, default=1000)
    p.add_argument("--loss", type=float, default=0.05, help="Packet loss probability, 0 to 1")
    p.add_argument("--delay", type=float, default=20, help="One-way base link delay in ms")
    p.add_argument("--bandwidth", type=float, default=10, help="Link bandwidth in Mbps")
    args = p.parse_args()
    if args.packets <= 0 or not 0 <= args.loss <= 1 or args.delay < 0 or args.bandwidth <= 0:
        p.error("Use packets > 0, loss in [0,1], delay >= 0 and bandwidth > 0.")

    print("TCP/UDP performance simulation")
    print(f"Packets={args.packets}, loss={args.loss:.1%}, delay={args.delay} ms, bandwidth={args.bandwidth} Mbps\n")
    for proto in ("TCP", "UDP"):
        r = simulate(proto, args.packets, args.loss, args.delay, args.bandwidth)
        print(f"{r['protocol']}:")
        print(f"  Delivered       : {r['delivered']}/{r['sent']} ({r['delivery_pct']:.2f}%)")
        print(f"  Transmission tries: {r['attempts']}")
        print(f"  Mean per-attempt delay: {r['avg_delay_ms']:.3f} ms")
        print(f"  Approx. goodput  : {r['goodput_kbps']:.2f} kbit/s")
        print()
    print("Interpretation: TCP-like mode retransmits lost packets; UDP sends once and may lose data.")
    print("The goodput value is based on program execution time and is illustrative, not a physical link benchmark.")

if __name__ == "__main__":
    main()
