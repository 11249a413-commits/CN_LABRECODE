"""
Experiment 12: Calculate RTP inter-arrival delay variation and sequence loss from a CSV export.

Export CSV from Wireshark/tshark with these columns:
frame.time_epoch,rtp.ssrc,rtp.seq,rtp.timestamp
Example tshark command:
tshark -r capture.pcapng -Y rtp -T fields -E header=y -E separator=, \
  -e frame.time_epoch -e rtp.ssrc -e rtp.seq -e rtp.timestamp > rtp.csv

Usage:
python rtp_analyzer.py rtp.csv
"""
import argparse
import csv
import statistics
from collections import defaultdict

def analyze(path):
    streams = defaultdict(list)
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        required = {"frame.time_epoch", "rtp.ssrc", "rtp.seq", "rtp.timestamp"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("CSV must contain: " + ", ".join(sorted(required)))
        for row in reader:
            try:
                t = float(row["frame.time_epoch"])
                ssrc = row["rtp.ssrc"].strip() or "unknown"
                seq = int(row["rtp.seq"], 0)
                rtp_ts = int(row["rtp.timestamp"], 0)
                streams[ssrc].append((t, seq, rtp_ts))
            except (ValueError, TypeError):
                continue
    if not streams:
        print("No valid RTP rows found.")
        return
    for ssrc, packets in streams.items():
        packets.sort(key=lambda x: x[0])
        seqs = [p[1] for p in packets]
        # Sequence numbers are 16-bit and wrap around.
        expected = 0
        for a, b in zip(seqs, seqs[1:]):
            diff = (b - a) % 65536
            if diff > 1:
                expected += diff - 1
        gaps = []
        for a, b in zip(packets, packets[1:]):
            gaps.append((b[0] - a[0]) * 1000)
        print(f"\nSSRC: {ssrc}")
        print(f"Packets captured : {len(packets)}")
        print(f"Estimated missing sequence numbers: {expected}")
        print(f"Estimated loss percentage: {expected / (len(packets) + expected) * 100:.2f}%")
        if gaps:
            print(f"Mean inter-arrival time: {statistics.mean(gaps):.3f} ms")
            print(f"Min / max inter-arrival: {min(gaps):.3f} / {max(gaps):.3f} ms")
            if len(gaps) > 1:
                variation = [abs(gaps[i] - gaps[i-1]) for i in range(1, len(gaps))]
                print(f"Mean absolute inter-arrival variation (jitter estimate): {statistics.mean(variation):.3f} ms")
        print("Note: This is a capture-time estimate; RTP clock-rate-aware one-way delay requires synchronized sender/receiver timing.")

def main():
    p = argparse.ArgumentParser(description="Analyze RTP sequence loss and packet inter-arrival timing.")
    p.add_argument("csv_file")
    args = p.parse_args()
    analyze(args.csv_file)

if __name__ == "__main__":
    main()
