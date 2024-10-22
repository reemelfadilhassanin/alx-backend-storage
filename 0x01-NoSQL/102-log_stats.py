#!/usr/bin/env python3
from pymongo import MongoClient
from collections import Counter

def print_log_stats():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count methods
    methods = collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ])

    print("Methods:")
    for method in methods:
        print(f"\tmethod {method['_id']}: {method['count']}")

    # Count status checks
    status_counts = collection.aggregate([
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ])
    total_status_checks = sum(status['count'] for status in status_counts)
    print(f"{total_status_checks} status check")

    # Count IP addresses
    ip_counts = Counter(log['remote_addr'] for log in collection.find())
    
    # Get the top 10 IPs
    top_ips = ip_counts.most_common(10)
    
    print("IPs:")
    for ip, count in top_ips:
        print(f"\t{ip}: {count}")

if __name__ == "__main__":
    print_log_stats()

