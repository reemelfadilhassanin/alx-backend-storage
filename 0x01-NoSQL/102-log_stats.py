#!/usr/bin/env python3
from pymongo import MongoClient
from collections import Counter

def print_log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # Collecting and counting IPs
    ip_addresses = collection.find({}, {"ip": 1})
    ip_counter = Counter(ip["ip"] for ip in ip_addresses)

    # Getting the top 10 IPs
    top_ips = ip_counter.most_common(10)

    print("IPs:")
    for ip, count in top_ips:
        print(f"\t{ip}: {count}")

if __name__ == "__main__":
    print_log_stats()
