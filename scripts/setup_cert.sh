#!/bin/bash

# === scripts/setup_cert.sh ===
# Generate a GPG key for testing use with nanosignfs

gpg --batch --gen-key <<EOF
%no-protection
Key-Type: default
Key-Length: 2048
Name-Real: NanoSigner
Name-Email: nano@example.com
Expire-Date: 0
%commit
EOF

echo "GPG key generated. Use 'gpg --list-keys' to find the key ID."
