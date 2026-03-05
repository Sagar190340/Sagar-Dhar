import socket
import sys
from datetime import datetime

print("=================================")
print("        SagarScan v1.0")
print("  Simple Network Port Scanner")
print("=================================")

if len(sys.argv) != 2:
    print("Usage: python sagarscan.py <target_ip>")
    sys.exit()

target = sys.argv[1]

print(f"\nScanning target: {target}")
print("Scan started at:", datetime.now())
print("---------------------------------")

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        s.close()

except KeyboardInterrupt:
    print("\nScan interrupted by user")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Server not responding")
    sys.exit()

print("---------------------------------")
print("Scan completed")
