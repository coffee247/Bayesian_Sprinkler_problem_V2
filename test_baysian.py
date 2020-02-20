#!/usr/bin/env python3

import unittest
import baysian



class TestMain(unittest.TestCase):

    def test_summing_out_wetGrass(self):
        self.assertEqual(baysian.do_summing_out('wetGrass'), [1.0, 1.0, 1.0, 1.0])

    def test_pIsWet_GrassSummedOut(self):
        self.assertEqual(baysian.pIsWet(sprinkler=False, rain=False, wetGrass=None), 1.0)
        self.assertEqual(baysian.pIsWet(sprinkler=False, rain=True, wetGrass=None), 1.0)
        self.assertEqual(baysian.pIsWet(sprinkler=True, rain=False, wetGrass=None), 1.0)
        self.assertEqual(baysian.pIsWet(sprinkler=True, rain=True, wetGrass=None), 1.0)

    def test_pIsWet_RainSummedOut(self):
        self.assertEqual(baysian.pIsWet(sprinkler=False, rain=None, wetGrass=False), 1.2)
        self.assertEqual(baysian.pIsWet(sprinkler=False, rain=None, wetGrass=True), 0.8)
        self.assertEqual(baysian.pIsWet(sprinkler=True, rain=None, wetGrass=False), 0.11)
        self.assertEqual(baysian.pIsWet(sprinkler=True, rain=None, wetGrass=True), 1.89)

    def test_pIsWet_SprinklerSummedOut(self):
        self.assertEqual(baysian.pIsWet(sprinkler=None, rain=False, wetGrass=False), 1.1)
        self.assertEqual(baysian.pIsWet(sprinkler=None, rain=False, wetGrass=True), 0.9)
        self.assertEqual(baysian.pIsWet(sprinkler=None, rain=True, wetGrass=False), 0.21)
        self.assertEqual(baysian.pIsWet(sprinkler=None, rain=True, wetGrass=True), 1.79)

    def test_makeMask(self):
        self.assertEqual(baysian.makeMask('rain'), 5)
        self.assertEqual(baysian.makeMask('sprinkler'), 3)
        self.assertEqual(baysian.makeMask('wetGrass'), 6)



if __name__ == '__main__':
    unittest.main()
