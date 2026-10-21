#!/usr/bin/env python3
# Copyright (c) The Bitcoin Core developers
# Copyright (c) ChaincodeLabs BOSS Program
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Verify that starting bitcoin with -h works as expected."""

from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import (
    assert_equal,
    assert_not_equal,
    assert_raises_rpc_error
)

class HolocatTest(BitcoinTestFramework):
    def set_test_params(self):
        self.setup_clean_chain = True
        self.num_nodes = 1

    def run_test(self):
        assert_raises_rpc_error(-1, "holocat", self.nodes[0].holocat, "unexpected_args")
        init = self.nodes[0].holocat()
        init_again = self.nodes[0].holocat()
        assert_equal(init, init_again)
        self.generate(self.nodes[0], 1)
        one = self.nodes[0].holocat()
        assert_not_equal(init, one)
        block_two = self.generate(self.nodes[0], 1)
        two = self.nodes[0].holocat()
        assert_not_equal(init, two)
        assert_not_equal(one, two)
        self.nodes[0].invalidateblock(block_two[0])
        two_again = self.nodes[0].holocat()
        assert_not_equal(init, two_again)
        assert_not_equal(one, two_again)
        assert_equal(two, two_again)

if __name__ == '__main__':
    HolocatTest(__file__).main()
