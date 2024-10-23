#!/usr/bin/env python3
""" task 8 """


def list_all(mongo_collection):
    """ lists all documents in a collection """
    return [docu for docu in mongo_collection.find()]
