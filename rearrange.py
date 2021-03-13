#!/usr/bin/env python3 
import re

def rearrange_name(name):
  result =re.search(r"([\w. ]*), ([\w. ]*)",name)
  if result is None:
    return name
  if result[1].isnumeric() or result[2].isnumeric():
    raise TypeError("Expected word but the input is numeric")
  return "{} {}".format(result[2],result[1])
