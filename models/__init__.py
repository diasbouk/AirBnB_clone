#!/usr/bin/python3
""" Import modules
here """


from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
