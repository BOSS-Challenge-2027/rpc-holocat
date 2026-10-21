#!/usr/bin/env python3
# Copyright (c) The Bitcoin Core developers
# Copyright (c) ChaincodeLabs BOSS Program
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Verify that starting bitcoin with -h works as expected."""

from test_framework.test_framework import BitcoinTestFramework

class HolocatTest(BitcoinTestFramework):
    def set_test_params(self):
        self.num_nodes = 1

    def run_test(self):
        assert False, "Missing Holocat test"

if __name__ == '__main__':
    HolocatTest(__file__).main()
