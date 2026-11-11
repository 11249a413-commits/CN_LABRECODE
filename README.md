# RTP delay and loss analysis

1. Capture a stream that uses RTP, or open an authorized RTP `.pcap`/`.pcapng` capture.
2. Confirm Wireshark recognizes packets as RTP. If needed, use **Analyze → Decode As**.
3. Export the RTP fields to CSV:

```bash
tshark -r capture.pcapng -Y rtp -T fields -E header=y -E separator=, \
  -e frame.time_epoch -e rtp.ssrc -e rtp.seq -e rtp.timestamp > rtp.csv
```

4. Run:

```bash
python rtp_analyzer.py rtp.csv
```

The program estimates missing sequence numbers and packet inter-arrival timing. A precise one-way network delay requires synchronized clocks and sender-side timestamps.
