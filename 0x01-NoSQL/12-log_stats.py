#!/usr/bin/env python3
""" 12-log_stats  """
from pymongo import MongoClient


def log_stats():
    """  provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('localhost', '27017')
    collection = client.logs.nginx
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    if __name__ == "__main__":
        log_stats()
