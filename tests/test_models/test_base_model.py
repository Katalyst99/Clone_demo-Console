#!/usr/bin/python3
"""Unittest module for the BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing BaseModel class"""
    def setUp(self):
        self.model_b = BaseModel()
