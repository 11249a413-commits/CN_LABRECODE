"""
Experiment 10: CRC error-detection demonstration.
Usage:
  python crc_demo.py
  python crc_demo.py --data 1101011011 --generator 10011
"""
import argparse

def modulo2_division(bit_string, generator):
    work = list(bit_string)
    gen = list(generator)
    for i in range(len(work) - len(gen) + 1):
        if work[i] == "1":
            for j in range(len(gen)):
                work[i + j] = str(int(work[i + j]) ^ int(gen[j]))
    return "".join(work[-(len(gen) - 1):]) if len(gen) > 1 else ""

def crc_encode(data, generator):
    if not data or set(data) - {"0", "1"}:
        raise ValueError("Data must be a non-empty binary string.")
    if len(generator) < 2 or generator[0] != "1" or set(generator) - {"0", "1"}:
        raise ValueError("Generator must be a binary string of length >= 2 beginning with 1.")
    remainder = modulo2_division(data + "0" * (len(generator) - 1), generator)
    return data + remainder, remainder

def crc_check(frame, generator):
    if len(frame) < len(generator):
        raise ValueError("Frame must be at least as long as generator.")
    return modulo2_division(frame, generator)

def main():
    parser = argparse.ArgumentParser(description="CRC encoding and error detection demo.")
    parser.add_argument("--data", default="1101011011")
    parser.add_argument("--generator", default="10011")
    parser.add_argument("--flip", type=int, default=None, help="Optional zero-based bit index to corrupt before checking")
    args = parser.parse_args()
    frame, remainder = crc_encode(args.data, args.generator)
    print("Data bits       :", args.data)
    print("Generator       :", args.generator)
    print("CRC remainder   :", remainder)
    print("Transmitted frame:", frame)
    received = frame
    if args.flip is not None:
        if not 0 <= args.flip < len(frame):
            parser.error("--flip index is outside the transmitted frame")
        bits = list(frame)
        bits[args.flip] = "1" if bits[args.flip] == "0" else "0"
        received = "".join(bits)
        print("Corrupted frame :", received)
    check = crc_check(received, args.generator)
    print("Receiver remainder:", check)
    print("Result          :", "NO ERROR DETECTED" if set(check) <= {"0"} else "ERROR DETECTED")
    print("\nCRC detects errors; it does not repair/correct the damaged bits.")

if __name__ == "__main__":
    main()
