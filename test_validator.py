import validator

def test_valid_alert():

    alert = {
        "ip": "192.168.1.20",
        "severity": "low",
        "source": "firewall"
    }

    is_valid, reason = validator.is_valid_alert(alert)

    assert is_valid is True
    assert reason is None


def test_empty_ip():

    alert = {
        "ip": "",
        "severity": "low",
        "source": "firewall"
    }

    is_valid, reason = validator.is_valid_alert(alert)
    
    assert is_valid is False
    assert reason == "IP cannot be empty"


def test_missing_required_field():

    alert = {
        "ip": "192.168.1.20",
        "severity": "low"
    }

    is_valid, reason = validator.is_valid_alert(alert)

    assert is_valid is False
    assert reason == "Missing required field: source"


def test_wrong_ip_type():

    alert = {
        "ip": 12345,
        "severity": "low",
        "source": "firewall"
    }

    is_valid, reason = validator.is_valid_alert(alert)

    assert is_valid is False
    assert reason == "Field ip has incorrect type"


def test_invalid_ip():

    alert = {
    "ip": "999.999.999.999",
    "severity": "low",
    "source": "firewall"
    }

    is_valid, reason = validator.is_valid_alert(alert)
    
    assert is_valid is False
    assert reason == "Not a valid IP address"


def test_normalized_severity():

    alert = {
    "ip": "192.168.1.20",
    "severity": "   CrItIcAl   ",
    "source": "firewall"
    }

    is_valid, reason = validator.is_valid_alert(alert)
    
    assert is_valid is True
    assert reason is None
    assert alert["severity"] == "   CrItIcAl   "


def test_invalid_severity():

    alert = {
    "ip": "192.168.1.20",
    "severity": "banana",
    "source": "firewall"
    }

    is_valid, reason = validator.is_valid_alert(alert)
        
    assert is_valid is False
    assert reason == f"Invalid severity: {alert['severity']}"


def test_alert_not_dictionary():

    alert = "this is not an alert"

    is_valid, reason = validator.is_valid_alert(alert)
        
    assert is_valid is False
    assert reason == "Alert must be a dictionary"


def test_whitespace_only():

    alert = {
        "ip": "    ",
        "severity": "low",
        "source": "firewall"
        }

    is_valid, reason = validator.is_valid_alert(alert)

    assert is_valid is False
    assert reason == "IP cannot be empty"

