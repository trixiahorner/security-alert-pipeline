def get_action(severity):
    if severity == "critical":
        return "block_ip"
    elif severity == "medium":
        return "investigate"
    elif severity == "low":
        return "monitor"
    else:
        raise ValueError(f"Invalid severity: {severity}")


def process_alert(alert):
    severity = alert["severity"].strip().lower()
    action = get_action(severity)

    alert["action"] = action

    return alert

