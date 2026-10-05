import pytest
import processor

def test_get_action_low():

    action = processor.get_action("low")
    
    assert action == "monitor"


def test_get_action_medium():

    action = processor.get_action("medium")
    
    assert action == "investigate"


def test_get_action_critical():

    action = processor.get_action("critical")
    
    assert action == "block_ip"


def test_get_action_invalid_severity():

    with pytest.raises(ValueError):
        processor.get_action("banana")


def test_process_alert():

    alert = {
    "ip": "192.168.1.20",
    "severity": "critical",
    "source": "firewall"
    }

    processed_alert = processor.process_alert(alert)
    assert processed_alert["action"] == "block_ip"


def test_process_alert_normalized_severity():

    alert = {
        "ip": "192.168.1.20",
        "severity": "   CrItIcAl   ",
        "source": "firewall"
    }

    processed_alert = processor.process_alert(alert)
    assert processed_alert["action"] == "block_ip"

