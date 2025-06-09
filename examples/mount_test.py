# === examples/mount_test.py ===

from nanosignfs.core import NanoSignFS
from fuse import FUSE
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 mount_test.py <mountpoint>")
        sys.exit(1)

    mountpoint = sys.argv[1]
    if not os.path.exists(mountpoint):
        os.makedirs(mountpoint)
    FUSE(NanoSignFS(), mountpoint, foreground=True, allow_other=True, nonempty=True)
