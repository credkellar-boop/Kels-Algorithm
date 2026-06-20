import threading

class SystemState:
    def __init__(self):
        self._lock = threading.Lock()
        # Baseline configurations
        self.active_oid = "1.3.6.1.4.1.99999.1.1"  # Custom mock OID for Kel-V1
        self.bit_plane = 256                         # Initial symmetric block strength
        self.security_level = "STANDARD"            # Options: STANDARD, TARPIT, LOCKDOWN
        self.active_connections = {}

    def update_oid(self, new_oid: str):
        with self._lock:
            self.active_oid = new_oid

    def shift_bit_plane(self, new_size: int):
        with self._lock:
            if new_size in [256, 384, 512]:
                self.bit_plane = new_size

    def trigger_posture(self, posture: str):
        with self._lock:
            if posture in ["STANDARD", "TARPIT", "LOCKDOWN"]:
                self.security_level = posture
              
