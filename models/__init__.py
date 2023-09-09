#!/usr/bin/python3
"""This module creates a unique FileStorage
instance for your application.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
"""This ceates var. storage, an instance of FileStorage."""

storage.reload()
"""This calls tyhe reload() func on storage"""
