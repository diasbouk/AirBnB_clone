#!/usr/bin/python3
""" Creating New instance for the storage
    class
"""

from models.engine import file_storage

# init instance
storage = file_storage.FileStorage()
# Reload it
storage.reload()
