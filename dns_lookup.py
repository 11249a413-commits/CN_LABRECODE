"""
Experiment 9: Display the local machine's host name, IP addresses and configured DNS servers.
DNS server discovery is platform-specific; this program uses standard OS configuration files/commands.
"""
import platform
import socket
import subprocess
from pathlib import Path

def local_addresses():
    found = set()
    try:
        for item in socket.getaddrinfo(socket.gethostname(), None):
            found.add(item[4][0])
    except socket.gaierror:
        pass
    try:
        # UDP connect discovers the preferred outbound interface without sending application data.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("192.0.2.1", 80))  # TEST-NET address; no packet payload is sent.
        found.add(s.getsockname()[0])
        s.close()
    except OSError:
        pass
    return sorted(found)

def dns_servers():
    system = platform.system().lower()
    servers = []
    if system == "windows":
        try:
            out = subprocess.check_output(
                ["ipconfig", "/all"], text=True, errors="replace",
                stderr=subprocess.DEVNULL
            )
            active = False
            for line in out.splitlines():
                if "DNS Servers" in line:
                    active = True
                    value = line.split(":", 1)[-1].strip()
                    if value:
                        servers.append(value)
                elif active and line.startswith(" ") and line.strip():
                    value = line.strip()
                    if value and value[0].isdigit():
                        servers.append(value)
                else:
                    active = False
        except (OSError, subprocess.SubprocessError):
            pass
    else:
        resolv = Path("/etc/resolv.conf")
        if resolv.exists():
            for line in resolv.read_text(errors="replace").splitlines():
                parts = line.split()
                if len(parts) >= 2 and parts[0] == "nameserver":
                    servers.append(parts[1])
    return list(dict.fromkeys(servers))

def main():
    print("Local DNS / host information")
    print("Host name (short):", socket.gethostname())
    try:
        print("Fully qualified host name:", socket.getfqdn())
    except OSError as exc:
        print("FQDN lookup failed:", exc)
    print("Local IP address(es):")
    for address in local_addresses() or ["Not detected"]:
        print(" ", address)
    print("Configured DNS server IP address(es):")
    for address in dns_servers() or ["Could not read DNS configuration on this OS"]:
        print(" ", address)
    print("\nNote: DNS server IPs are read from local OS configuration; they are not necessarily the DNS server answering every query.")

if __name__ == "__main__":
    main()
