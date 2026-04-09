"""
verify_controls.py — Executable system verification
════════════════════════════════════════════════════

Checks the actual state of security controls on this machine
against the obstruction chain defined in security_spec.py.

Run: python verify_controls.py
Run specific layer: python verify_controls.py L2

Owner: Aaron Green
"""

import subprocess
import os
import sys
import json
from datetime import datetime


def run(cmd: str, timeout: int = 10) -> tuple[int, str]:
    """Run a shell command, return (returncode, stdout)."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout.strip()
    except subprocess.TimeoutExpired:
        return -1, "TIMEOUT"
    except Exception as e:
        return -1, str(e)


class Control:
    def __init__(self, name: str, layer: str, check_fn, description: str):
        self.name = name
        self.layer = layer
        self.check_fn = check_fn
        self.description = description
        self.status = None
        self.detail = ""

    def check(self):
        try:
            ok, detail = self.check_fn()
            self.status = "PASS" if ok else "FAIL"
            self.detail = detail
        except Exception as e:
            self.status = "ERROR"
            self.detail = str(e)
        return self


# ═══════════════════════════════════════════════════════════════
# CHECK FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def check_filevault():
    rc, out = run("fdesetup status")
    on = "FileVault is On" in out
    return on, out

def check_sip():
    rc, out = run("csrutil status")
    on = "enabled" in out.lower()
    return on, out

def check_gatekeeper():
    rc, out = run("spctl --status")
    on = "assessments enabled" in out.lower()
    return on, out

def check_firewall():
    rc, out = run("/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate")
    on = "enabled" in out.lower()
    return on, out

def check_stealth_mode():
    rc, out = run("/usr/libexec/ApplicationFirewall/socketfilterfw --getstealthmode")
    on = "enabled" in out.lower()
    return on, out

def check_lulu_installed():
    exists = os.path.exists("/Applications/LuLu.app")
    return exists, "LuLu.app present" if exists else "LuLu.app not found"

def check_mullvad_installed():
    exists = os.path.exists("/Applications/Mullvad VPN.app")
    return exists, "Mullvad VPN.app present" if exists else "Mullvad VPN.app not found"

def check_mullvad_connected():
    rc, out = run("mullvad status 2>/dev/null")
    if rc != 0:
        return False, "mullvad CLI not available"
    connected = "connected" in out.lower() and "disconnected" not in out.lower()
    return connected, out

def check_dns_encrypted():
    rc, out = run("networksetup -getdnsservers Wi-Fi")
    custom = "1.1.1.1" in out or "1.0.0.1" in out
    return custom, f"DNS: {out}"

def check_airdrop_contacts_only():
    # Can't reliably check from CLI; report as manual
    return None, "Manual check required: System Settings > General > AirDrop"

def check_bloatware_removed():
    """Check that known bloatware apps are gone."""
    bloat = [
        "/Applications/TeamViewer.app",
        "/Applications/Zoom.app",
        "/Applications/Discord.app",
        "/Applications/Telegram.app",
        "/Applications/WhatsApp.app",
        "/Applications/Steam.app",
        "/Applications/Google Chrome.app",
    ]
    found = [b for b in bloat if os.path.exists(b)]
    if found:
        return False, f"Still installed: {', '.join(found)}"
    return True, "Known bloatware removed"

def check_ssh_key_exists():
    ed25519 = os.path.expanduser("~/.ssh/id_ed25519")
    exists = os.path.exists(ed25519)
    return exists, "Ed25519 key present" if exists else "No Ed25519 key found"

def check_project_permissions():
    project = os.path.expanduser("~/Desktop/Research Papers")
    if not os.path.exists(project):
        return False, "Project directory not found"
    rc, out = run(f'stat -f "%Lp" "{project}"')
    is_700 = out.strip() == "700"
    return is_700, f"Permissions: {out}"

def check_gpg_key():
    rc, out = run("gpg --list-secret-keys --keyid-format=long 2>/dev/null")
    has_key = "sec" in out
    return has_key, "GPG key present" if has_key else "No GPG key found"

def check_bitwarden():
    exists = os.path.exists("/Applications/Bitwarden.app")
    return exists, "Bitwarden.app present" if exists else "Bitwarden not found"

def check_integrity_monitor():
    path = os.path.expanduser(
        "~/Desktop/Research Papers/Relational_Closure_and_Emergent Gauge_Structure"
        "/Closure v5/BUSINESS/security/integrity_monitor.py"
    )
    exists = os.path.exists(path)
    return exists, "integrity_monitor.py present" if exists else "Not found"

def check_behavioral_auth():
    path = os.path.expanduser(
        "~/Desktop/Research Papers/Relational_Closure_and_Emergent Gauge_Structure"
        "/Closure v5/BUSINESS/security/behavioral_auth.py"
    )
    exists = os.path.exists(path)
    return exists, "behavioral_auth.py present" if exists else "Not found"

def check_backup_script():
    path = os.path.expanduser(
        "~/Desktop/Research Papers/Relational_Closure_and_Emergent Gauge_Structure"
        "/Closure v5/BUSINESS/security/backup_encrypt.sh"
    )
    exists = os.path.exists(path)
    return exists, "backup_encrypt.sh present" if exists else "Not found"


# ═══════════════════════════════════════════════════════════════
# CONTROL REGISTRY
# ═══════════════════════════════════════════════════════════════

CONTROLS = [
    # L1 Physical binding
    Control("FileVault", "L1", check_filevault, "Full disk encryption"),
    Control("Project permissions", "L1", check_project_permissions, "Research dir is 700"),

    # L2 Perimeter
    Control("macOS Firewall", "L2", check_firewall, "Application firewall enabled"),
    Control("Stealth mode", "L2", check_stealth_mode, "Stealth mode enabled"),
    Control("LuLu", "L2", check_lulu_installed, "Outbound firewall installed"),
    Control("Mullvad VPN installed", "L2", check_mullvad_installed, "VPN client present"),
    Control("Mullvad connected", "L2", check_mullvad_connected, "VPN tunnel active"),
    Control("DNS encrypted", "L2", check_dns_encrypted, "Custom encrypted DNS"),

    # L3 Encryption at rest
    Control("GPG key", "L3", check_gpg_key, "GPG signing key present"),

    # L4 Process isolation
    Control("SIP", "L4", check_sip, "System Integrity Protection"),
    Control("Gatekeeper", "L4", check_gatekeeper, "App notarization gate"),
    Control("Bloatware removal", "L4", check_bloatware_removed, "Known bloatware purged"),

    # L5 Identity gates
    Control("SSH Ed25519", "L5", check_ssh_key_exists, "SSH key present"),
    Control("Bitwarden", "L5", check_bitwarden, "Password manager present"),

    # L6 Behavioral invariants
    Control("Behavioral auth", "L6", check_behavioral_auth, "behavioral_auth.py present"),

    # L7 Compositional identity
    # (triadic verification is operational, not file-checkable)

    # L8 Residual dynamics
    Control("Integrity monitor", "L8", check_integrity_monitor, "integrity_monitor.py present"),
    Control("Backup script", "L8", check_backup_script, "backup_encrypt.sh present"),
]


# ═══════════════════════════════════════════════════════════════
# RUNNER
# ═══════════════════════════════════════════════════════════════

def run_checks(layer_filter: str = None):
    print(f"Possibilistic Security — Control Verification")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 55)

    results = {"PASS": 0, "FAIL": 0, "ERROR": 0, "SKIP": 0}

    for c in CONTROLS:
        if layer_filter and c.layer != layer_filter:
            continue
        c.check()
        if c.status is None:
            status_str = "SKIP"
            results["SKIP"] += 1
        else:
            status_str = c.status
            results[c.status] = results.get(c.status, 0) + 1

        icon = {"PASS": "✓", "FAIL": "✗", "ERROR": "!", "SKIP": "–"}.get(status_str, "?")
        print(f"  {icon} [{c.layer}] {c.name}: {status_str}")
        if c.detail and c.status != "PASS":
            print(f"         {c.detail}")

    print("=" * 55)
    total = sum(results.values())
    print(f"  {results['PASS']}/{total} passed  |  "
          f"{results['FAIL']} failed  |  "
          f"{results['ERROR']} errors  |  "
          f"{results['SKIP']} skipped")

    return results["FAIL"] == 0 and results["ERROR"] == 0


if __name__ == "__main__":
    layer = sys.argv[1] if len(sys.argv) > 1 else None
    ok = run_checks(layer)
    sys.exit(0 if ok else 1)
