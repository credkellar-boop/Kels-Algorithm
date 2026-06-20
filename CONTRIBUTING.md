# Contributing to Kel's Algorithm

Thank you for your interest in hardening post-quantum cryptography! 

## Adding a New Cryptographic Primitive
If you want to add a new primitive (e.g., a new Isogeny-based spider leg):
1. Create a new file in `src/crypto/`.
2. Ensure it does not break the `SystemState` tracking in `src/core/state.py`.
3. Add a dedicated test in `tests/`.

## Pull Request Process
1. Fork the repository.
2. Ensure your code passes all simulations via the `Makefile` commands.
3. Submit a PR with a detailed breakdown of the mathematical properties of your addition.
4. 
