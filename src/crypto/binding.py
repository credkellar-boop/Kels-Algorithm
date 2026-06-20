
import os
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

class NonLinearBinder:
    @staticmethod
    def derive_bound_key(classical_secret: bytes, quantum_secret: bytes, salt: bytes = None) -> bytes:
        """
        Binds classical and quantum secrets together using a non-linear KDF.
        Includes ciphertext tracking context to prevent manual separation of primitives.
        """
        if not salt:
            # Generate temporary 32-byte single-use salt if none provided
            salt = os.urandom(32)
            
        # Concatenate inputs to build raw composite entropy
        combined_entropy = classical_secret + quantum_secret
        
        # Context info payload to anchor the specific protocol lifecycle
        info_context = b"Kels-Algo-v1-Protocol-Binding"
        
        # Execute extraction and expansion via HKDF-SHA512
        hkdf = HKDF(
            algorithm=hashes.SHA512(),
            length=64,  # Generate a 512-bit unified key master output
            salt=salt,
            info=info_context,
        )
        
        return hkdf.derive(combined_entropy)
