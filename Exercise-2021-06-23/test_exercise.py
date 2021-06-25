"""
Test file for exercise.py
"""
import os
from exercise import FileParser,WriteConfig,Operations

def test_config():
    w = WriteConfig()
    w.write_config()
    assert w.get_config() == os.path.join(os.getcwd(),'.config')
