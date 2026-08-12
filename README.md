## Overview Simulator

A safe and isolated ransomware simulation tool written in Python for cybersecurity education, malware-analysis practice, and defensive security testing.

# Overview

Ransomware Simulator demonstrates the basic file-encryption and file-restoration workflow associated with ransomware behavior.

The project is intentionally designed for a controlled laboratory environment. It operates only inside the configured "lab/sample_files/" directory and does not attempt to access files outside the laboratory.

# Features

- Generate a local encryption key
- Encrypt laboratory files
- Decrypt simulated encrypted files
- Use the ".simlocked" extension for encrypted copies
- Restrict file operations to the laboratory directory
- Record encryption and decryption events
- Maintain a local simulation log
- Simple interactive terminal interface
- No network propagation
- No persistence mechanism
- No automatic execution
- No deletion of original fifilesProject Structure

ransomware-simulator/
│
├── main.py
├── crypto_engine.py
├── simulator.py
├── logger.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── lab/
│   └── sample_files/
│
└── logs/
    └── simulation.log

Requirements

- Python 3.10+
- "cryptography"

Install the dependency:

pip install -r requirements.txt

Usage

Start the simulator:

python main.py

The terminal menu provides:

[1] Generate encryption key
[2] List laboratory files
[3] Encrypt a file
[4] Encrypt all laboratory files
[5] Decrypt a file
[6] Exit

Laboratory Setup

Create test files only inside:

lab/sample_files/

For example:

lab/
└── sample_files/
    ├── document.txt
    ├── notes.txt
    └── test.txt

Generate an encryption key before running an encryption simulation.

Encrypted files receive the:

.simlocked

extension.

Example:

document.txt

becomes:

document.txt.simlocked

The simulator can subsequently restore the encrypted file using the same key.

Security Design

This project is intentionally constrained to reduce the risk of accidental damage.

The simulator:

- Resolves and validates file paths before processing them.
- Rejects files outside the configured laboratory directory.
- Does not recursively scan the user's computer.
- Does not modify system files.
- Does not implement persistence.
- Does not communicate with a command-and-control server.
- Does not spread across networks.
- Does not delete files.
- Does not attempt to disable security software.

The project is intended for authorized laboratory use only.

Logging

Simulation events are stored in:

logs/simulation.log

Example:

2026-08-12 22:45:10 | INFO | ENCRYPT_REQUEST | file=lab/sample_files/test.txt
2026-08-12 22:45:10 | INFO | ENCRYPT_SUCCESS | source=lab/sample_files/test.txt | output=lab/sample_files/test.txt.simlocked

These logs can later be used to build a ransomware-behavior detection module.

Educational Objectives

This project can be used to study:

- File encryption concepts
- Cryptographic key management
- Ransomware behavior
- File-system monitoring
- Security logging
- Detection engineering
- Incident-response workflows
- SOC alert development

Defensive Testing

The simulator can be used as a controlled source of events for defensive tools such as:

- File Integrity Monitoring
- SIEM platforms
- EDR/XDR laboratories
- Windows event monitoring
- SOC detection rules
- Security alert pipelines

The objective is to understand how defensive systems can identify suspicious file-encryption activity without deploying real ransomware.

Disclaimer

This project is an educational cybersecurity laboratory tool.

Run it only on files created specifically for testing and only in an environment you are authorized to control.

The project must not be used to encrypt, damage, or disrupt data belonging to other users or systems.
