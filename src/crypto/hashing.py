import hashlib
from blake3 import blake3

class MultiHashChainer:
    @staticmethod
    def hash_leaf(data: bytes, salt: bytes) -> bytes:
        """
        Hashes a leaf data node by cascading a BLAKE3 tree pass 
        into a SHA3-512 sponge execution stage.
        """
        # Step 1: Execute BLAKE3 over the message and unique leaf salt
        blake_engine = blake3()
        blake_engine.update(data + salt)
        intermediate_digest = blake_engine.digest()
        
        # Step 2: Cascade intermediate output into a SHA3-512 sponge structure
        sha3_engine = hashlib.sha3_512()
        sha3_engine.update(intermediate_digest + salt)
        
        return sha3_engine.digest()

    @staticmethod
    def combine_nodes(left_node: bytes, right_node: bytes) -> bytes:
        """Combines two tree branch nodes together using the dual hash model."""
        blake_engine = blake3()
        blake_engine.update(left_node + right_node)
        intermediate = blake_engine.digest()
        
        sha3_engine = hashlib.sha3_512()
        sha3_engine.update(intermediate)
        return sha3_engine.digest()
      
