# Python Substrate Interface Library
#
# Copyright 2018-2020 Stichting Polkascan (Polkascan Foundation).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

import unittest

from substrateinterface import Keypair


class KeyPairTestCase(unittest.TestCase):
    public_key = '0xe4359ad3e2716c539a1d663ebd0a51bdc5c98a12e663bb4c4402db47828c9446'
    address = '16ADqpMa4yzfmWs3nuTSMhfZ2ckeGtvqhPWCNqECEGDcGgU2'

    def test_only_provide_ss58_address(self):
        keypair = Keypair(ss58_address=self.address)
        self.assertEqual(keypair.public_key, bytes.fromhex(self.public_key[2:]))

    def test_only_provide_public_key(self):
        keypair = Keypair(public_key=self.public_key, ss58_format=0)
        self.assertEqual(keypair.ss58_address, self.address)

    def test_provide_no_ss58_address_and_public_key(self):
        self.assertRaises(ValueError, Keypair)

    def test_incorrect_public_key(self):
        self.assertRaises(ValueError, Keypair, public_key='0x23')

    def test_repr(self):
        self.assertEqual(
            repr(Keypair(public_key=self.public_key, ss58_format=0)),
            f'<Keypair (address={self.address})>',
        )


if __name__ == '__main__':
    unittest.main()
