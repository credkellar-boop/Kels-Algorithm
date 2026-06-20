import os

class AgileSymmetricCipher:
    @staticmethod
    def generate_grover_resistant_key(bit_plane: int = 512) -> bytes:
        """Generates a symmetric key massive enough to render Grover's search useless."""
        if bit_plane not in [256, 384, 512]:
            raise ValueError("Invalid bit-plane size.")
        return os.urandom(bit_plane // 8)
