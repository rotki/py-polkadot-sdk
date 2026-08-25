# Python Substrate Interface Library
#
# Copyright 2018-2023 Stichting Polkascan (Polkascan Foundation).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

"""Public Substrate account representation.

This rotki-focused build deliberately does not create or hold private keys. It
only keeps the public-key-to-SS58 conversion used when importing xpub-derived
Substrate accounts.
"""

from typing import Optional, Union

from scalecodec.utils.ss58 import ss58_decode, ss58_encode

__all__ = ['Keypair']


class Keypair:
    """Represent a public Substrate account without seed or signing support."""

    def __init__(
            self,
            ss58_address: Optional[str] = None,
            public_key: Optional[Union[bytes, str]] = None,
            ss58_format: Optional[int] = None,
    ) -> None:
        if ss58_address and not public_key:
            public_key = ss58_decode(ss58_address, valid_ss58_format=ss58_format)

        if not public_key:
            raise ValueError('No SS58 formatted address or public key provided')

        if isinstance(public_key, str):
            public_key = bytes.fromhex(public_key[2:] if public_key.startswith('0x') else public_key)

        if len(public_key) != 32:
            raise ValueError('Public key should be 32 bytes long')

        if not ss58_address:
            ss58_address = ss58_encode(public_key, ss58_format=ss58_format)

        self.ss58_format = ss58_format
        self.public_key = public_key
        self.ss58_address = ss58_address

    def sign(self, data) -> bytes:
        raise NotImplementedError('This build does not support private keys or signing')

    def __repr__(self) -> str:
        return f'<Keypair (address={self.ss58_address})>'
