import sys
import os
from core import scanner, exploit_simulator, malware_detector, zero_day_checker
import subprocess

def print_usage():
    print("""
🔥 DEEP SCANNER V3.0 🔥
Usage: python main.py [mode] [target]
Modes:
  scan      - Subdomain bruteforce & vulnerability scanning
  exploit   - Simulasi SQLi/XSS eksploitasi + AI fuzzing
  hunt      - Malware detection & 0day vulnerability check
""")

if len(sys.argv) < 3:
    print_usage()
    sys.exit(1)

mode = sys.argv[1].lower()
target = sys.argv[2]

if mode == "scan":
    print(f"🚀 Starting SCAN on {target}")
    scanner.start_scan(target)  # scanner.py harus punya fungsi start_scan(target)

elif mode == "exploit":
    print(f"💥 Running EXPLOIT simulation + AI fuzzing on {target}")
    exploit_simulator.simulate_exploit(target)  # exploit_simulator.py harus punya simulate_exploit(target)
    # Jalankan train.py otomatis
    subprocess.run(["python", "ai/train.py"])

elif mode == "hunt":
    print(f"🔍 Starting HUNT on {target}")
    malware_detector.detect_malware(target)  # malware_detector.py harus punya detect_malware(target)
    zero_day_checker.check_vulnerabilities(target)  # zero_day_checker.py harus punya check_vulnerabilities(target)

else:
    print("❌ Unknown mode!")
    print_usage()
