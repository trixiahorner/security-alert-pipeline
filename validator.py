import ipaddress

required_fields = {
    "ip": str,
    "severity": str,
    "source": str
}

allowed_severities = {"low", "medium", "critical"}

def is_valid_alert(alert):
    if not isinstance(alert, dict):
        return False, "Alert must be a dictionary"

    for field, expected_type in required_fields.items():
        if field not in alert:
            return False, f"Missing required field: {field}"

        if not isinstance(alert[field], expected_type):
            return False, f"Field {field} has incorrect type"

    if not alert["ip"].strip():
        return False, "IP cannot be empty"

    try:
        ipaddress.ip_address(alert["ip"])
    except ValueError:
        return False, "Not a valid IP address"

    severity = (alert["severity"]).strip().lower()
    if severity not in allowed_severities:
        return False, f"Invalid severity: {alert['severity']}"

    return True, None