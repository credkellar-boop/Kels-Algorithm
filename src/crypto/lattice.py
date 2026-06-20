import numpy as np

class LatticeEngine:
    def __init__(self, rank: int = 8):
        self.rank = rank
        self.modulus = 3329  # Standard ML-KEM field modulus
        
    def generate_parameter_matrix(self) -> dict:
        """
        Generates a simulated high-dimensional Rank-8 lattice key pair.
        Adds uniform error distributions (noise) to hide coordinate vectors.
        """
        # Create a Rank-8 grid matrix
        matrix_A = np.random.randint(0, self.modulus, size=(self.rank, self.rank))
        # Generate secret vector
        secret_s = np.random.randint(-2, 3, size=(self.rank, 1))
        # Generate error distribution vector (Mathematical Noise)
        error_e = np.random.randint(-1, 2, size=(self.rank, 1))
        
        # Core LWE Equation: t = A * s + e (mod q)
        public_t = (np.dot(matrix_A, secret_s) + error_e) % self.modulus
        
        return {
            "public_key": {"A": matrix_A.tolist(), "t": public_t.tolist()},
            "private_key": secret_s.tolist()
        }
      
