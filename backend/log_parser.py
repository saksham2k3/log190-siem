import re

def parse_logs(log_data):
    """
    Parses raw log data into structured tuples (timestamp, log_level, message).
    """
    log_pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}) (?P<log_level>\w+) (?P<message>.+)'
    parsed_logs = []
    for line in log_data.splitlines():
        match = re.match(log_pattern, line)
        if match:
            parsed_logs.append((
                match.group('timestamp'),
                match.group('log_level'),
                match.group('message')
            ))
    return parsed_logs
