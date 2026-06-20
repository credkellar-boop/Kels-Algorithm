import unittest
from core.orchestrator import SpiderOrchestrator
from defensive.canaries import CanaryTrap
from defensive.quarantine import ExecutionQuarantine

class TestAttackTrapLifecycle(unittest.TestCase):
    def setUp(self):
        self.orchestrator = SpiderOrchestrator()
        self.orchestrator.initialize_system()
        self.trap = CanaryTrap(self.orchestrator)

    def test_canary_trip_and_zeroize(self):
        print("\n--- Starting Attacker Simulation ---")
        self.assertEqual(self.orchestrator.state.security_level, "STANDARD")
        
        # Simulate malicious actor reading the fallback master key parameter
        response = self.trap.access_parameter("mock_secret_key", attacker_ip="192.168.1.50")
        
        # Verify the state engine shifted dynamically into defensive posture
        self.assertEqual(response["status"], "REDIRECTED")
        self.assertEqual(self.orchestrator.state.security_level, "TARPIT")
        self.assertEqual(self.orchestrator.state.bit_plane, 512)
        
        # Execute memory quarantine on target telemetry data buffers
        test_buffer = bytearray(b"attacker_stolen_state_payload")
        ExecutionQuarantine.zeroize_buffer(test_buffer)
        
        # Confirm zeroization wiped the structure
        self.assertEqual(test_buffer, bytearray(len(test_buffer)))
        print("--- Attacker Simulation Passed Cleanly ---")

if __name__ == '__main__':
    unittest.main()
  
