import sys
from core.state import SystemState

class SpiderOrchestrator:
    def __init__(self):
        self.state = SystemState()

    def initialize_system(self):
        """Initializes all sub-modules and confirms readiness."""
        print("[*] Initializing Spider Core...")
        print(f"[*] Default Key OID Bound: {self.state.active_oid}")
        print(f"[*] Symmetric Bit-Plane Level: AES-{self.state.bit_plane}")
        print("[*] Cryptographic Legs Loaded: Lattice, HashChain, GoppaVault")

    def initiate_cycle_shift(self):
        """Executes a polymorphic parameter shift when a canary exception occurs."""
        print("\n[!] CRITICAL: Vibration detected on perimeter canary!")
        print("[!] Orchestrator initiating Polymorphic Cycle Shift...")
        
        # Shift state variables silently away from compromised parameters
        self.state.trigger_posture("TARPIT")
        self.state.update_oid("1.3.6.1.4.1.99999.9.9")  # Migrated OID
        self.state.shift_bit_plane(512)                 # Max out symmetric resilience
        
        print(f"[+] Active OID rotated dynamically.")
        print(f"[+] Internal Symmetric Bit-Planes maximized to {self.state.bit_plane} bits.")
      
