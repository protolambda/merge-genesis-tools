from eth_utils.crypto import keccak_256
from eth_utils.hexadecimal import encode_hex
from hashlib import sha256

# branch: storage slots [0, 32)
# deposit count: storage slot 32
# zero hashes: storage slots [33, 65) fixed-length array of bytes32 elements.
prev_zero_hash = b"\x00" * 32
# start at 33, but also skip another slot: the first zero-hash is all zeroes, and not actually stored in storage.
for i in range(32+1+1, 32+1+32):
    h = sha256(prev_zero_hash * 2).digest()
    print('"0x%064x": "0x%s",' % (i, h.hex()))
    prev_zero_hash = h
