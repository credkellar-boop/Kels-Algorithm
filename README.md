# Kel's Algorithm: Cycle-Spider PQC Framework

![Build Status](https://img.shields.io/github/actions/workflow/status/credkellar-boop/kels-algorithm/ci-cd.yml?branch=main&style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-Cycle--Spider-blueviolet?style=for-the-badge)
![Security Level](https://img.shields.io/badge/Security-Proactive%20Zeroize-red?style=for-the-badge)
![License](https://img.shields.io/github/license/credkellar-boop/kels-algorithm?style=for-the-badge)

## 🕷️ What is this about?
**Kel's Algorithm** is a next-generation, crypto-agile Post-Quantum Cryptography (PQC) framework. As classical encryption (RSA, ECC) faces an existential threat from the rapid advancement of quantum computing, this framework provides an impenetrable, mathematically robust defense using a highly modular **Cycle-Spider topology**. 

Unlike traditional static cryptography, Kel's Algorithm acts like a living defensive web. It is designed not just to mathematically protect data against Shor's and Grover's algorithms, but to actively hunt, trap, and destroy automated malware attempting to breach the perimeter.

## ⚙️ What does this do?
The framework is divided into interconnected mathematical sub-modules ("Spider Legs") orchestrated by a central nervous system:

1. **Rank-8 Module-Lattice Transport:** Secures data-in-transit by hiding secrets inside high-dimensional geometric grids injected with mathematical noise, bound tightly to classical algorithms via a non-linear HKDF-SHA512 extraction.
2. **Multi-Hash Chaining Authentication:** Eliminates collision vectors by passing digital signatures simultaneously through parallel tree structures (BLAKE3) and sponge permutations (SHA-3), topped with randomized leaf node salting.
3. **Goppa Code Vault:** Secures long-term cold storage by packing data into massive matrices littered with intentional bit-errors and decoy linear code "chaff."
4. **Active Perimeter Defense:** Deploys fake cryptographic variables ("Canaries"). If touched, the system silently shunts the attacker into an infinite computational delay loop (Tarpitting) while safely live-migrating legitimate traffic.

## 🔥 Why is it cool?
Most encryption simply sits there and hopes the math holds up. Kel's Algorithm fights back.

* **It's Polymorphic:** If an attacker touches a canary trap, the system instantly hot-swaps active Object Identifiers (OIDs) and ramps up symmetric bit-planes from 256 to 512 bits in real-time, effectively ghosting the attacker.
* **It Destroys Malware:** Once the framework logs an attacker's telemetry in the honeypot, the Execution Quarantine engine bypasses standard garbage collection and executes a raw, C-level `0x00` overwrite on the volatile memory blocks. It literally vaporizes the malicious payload at the kernel level.
* **It's Mathematically Interlocked:** The classical and quantum layers are inextricably bound. An adversary cannot isolate the classical payload to break it later; tampering with one byte scrambles the entire key expansion.

## 🚀 How to install?

Because this framework relies on modern Python packaging and strict environment controls, it utilizes a `pyproject.toml` configuration rather than legacy requirements files. 

### Option A: Local Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/credkellar-boop/kels-algorithm.git](https://github.com/credkellar-boop/kels-algorithm.git)
cd kels-algorithm
