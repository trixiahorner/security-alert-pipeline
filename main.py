import json
import logging
import validator
import processor

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def load_alerts(filename):
    with open(filename, "r", encoding="utf-8") as file:
        alerts = json.load(file)

    return alerts


def main():
    try:
        alerts = load_alerts("alerts.json")  

    except FileNotFoundError:
        logger.error("alerts.json was not found")

    except json.JSONDecodeError:
        logger.error("alerts.json contains invalid JSON.")

    else:
        if isinstance(alerts, list):
            for alert in alerts:
                is_valid, reason = validator.is_valid_alert(alert)

                if is_valid:
                    logger.info("Valid alert")

                    processed_alert = processor.process_alert(alert)
                    print(processed_alert)

                else:
                    logger.warning(f"Invalid alert: {reason}")

        else:
            logger.error("Expected a list of alerts.")


if __name__ == "__main__":
    main()