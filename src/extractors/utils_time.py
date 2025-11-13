thonfrom datetime import datetime

def format_timestamp(timestamp):
    """Converts a Unix timestamp to a human-readable format"""
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')