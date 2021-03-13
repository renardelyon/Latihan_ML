#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase="Lovelace, Ada"
    expected="Ada Lovelace"
    self.assertEqual(rearrange_name(testcase),expected)
 
  def test_empty(self):
    testcase=""
    expected=""
    self.assertEqual(rearrange_name(testcase),expected)
  
  def test_single_name(self):
    testcase="Siegfried"
    expected="Siegfried"
    self.assertEqual(rearrange_name(testcase),expected)
  
  def test_isnumeric(self):
    testcase="1"
    self.assertRaises(TypeError,rearrange_name(testcase))
  
  def test_double_name(self):
    testcase="Imawanto, Renard I."
    expected="Renard I. Imawanto"
    self.assertEqual(rearrange_name(testcase),expected)
  
unittest.main()
