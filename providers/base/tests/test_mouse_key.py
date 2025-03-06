#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import mouse


class TestMouse(unittest.TestCase):
    def test_main_successful(self):
        mouse.main()

    @patch("mouse.rand_mouse_moves", side_effect=Exception())
    def test_main_failure(self):
        mouse.main()
