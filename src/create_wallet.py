#!/usr/bin/env python3

from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import qrcode


def get_pair():
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    return private_key, public_key


def get_addr(public_key):
    return keccak_256(public_key).digest()[-20:].hex()

def create_qr(name, addr):
    img = qrcode.make(addr)
    img.save(name + '.png')

def run():
    private_key, public_key = get_pair()
    addr = get_addr(public_key)
    create_qr('qr', '0x' + addr)
    print('Addr: 0x' + addr)
    print('Private key:', private_key.hex())
    print('Public key :', public_key.hex())

if __name__ == "__main__":
    run()
