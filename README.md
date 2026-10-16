# Security Alert Processing Pipeline

## Overview
This is a Python program that reads security alerts from a JSON file, validates their data, and enriches valid alerts with recommended response actions. Invalid alerts are logged and skipped, allowing the program to continue processing the remaining alerts.

## Features
- Reads security alerts from a JSON file
- Validates required fields and data types
- Validates IP addresses using Python's ipaddress module
- Normalizes severity values
- Enriches valid alerts with recommended response actions
- Logs validation failures and processing status
- Handles missing files and malformed JSON
- Includes automated tests using pytest

## Project Structure
```text
security-alert-pipeline/
├── main.py
├── validator.py
├── processor.py
├── alerts.json
├── test_validator.py
├── test_processor.py
├── requirements-dev.txt
├── .gitignore
└── README.md
```

## Installation

### Prerequisites
- Python 3.12 (tested with 3.12.4)
- Git

### Setup
1. Clone the repository:
```powershell
git clone https://github.com/trixiahorner/security-alert-pipeline.git
```

2. Navigate to the project directory:
```powershell
cd security-alert-pipeline
```

3. Create a virtual environment:
```powershell
python -m venv .venv
```

4. Activate the virtual environment (Windows PowerShell):
```powershell
.\.venv\Scripts\Activate.ps
```

5. Install development dependencies:
```powershell
python -m pip install -r requirements-dev.txt
```

## Usage
Run the security alert processing pipeline:
```powershell
python main.py
```

The application reads security alerts from `alerts.json`, validates each alert, and enriches valid alerts with recommended response actions.

Invalid alerts are logged and skipped.
### Example Output
The following example shows processed alerts with their recommended response actions:
```text
{'ip': '192.168.1.20', 'severity': 'low', 'source': 'firewall', 'action': 'monitor'}

{'ip': '10.0.0.55', 'severity': 'critical', 'source': 'endpoint', 'device': {'hostname': 'WORKSTATION-22', 'os': 'Windows 11'}, 'action': 'block_ip'}

{'ip': '172.16.0.8', 'severity': 'medium', 'source': 'ids', 'action': 'investigate'}
```

The application also generates log messages indicating validation results and errors.

## Testing
The project uses pytest for automated unit testing.

Run all tests:
```powershell
python -m pytest
```

Run tests with detailed output:
```powershell
python -m pytest -v
```

### Tested Behaviors
The project includes 15 automated tests covering:

- Required field validation
- IP address validation
- Severity validation and normalization
- Empty and whitespace-only input
- Incorrect data types
- Alert enrichment and recommended actions
- Handling invalid severity values

All 15 tests currently pass.

## Security Design
This project incorporates several security-focused design practices:

- **Input validation:** Checks required fields, data types, allowed severity values, and IP address formats before processing alerts.
- **Data normalization:** Standardizes severity values to ensure consistent processing.
- **Error handling:** Handles missing files and malformed JSON without producing an unhandled traceback for those cases.
- **Logging:** Records validation failures and processing status to support troubleshooting.
- **Separation of concerns:** Keeps validation and processing logic in separate modules for easier maintenance and testing.
- **Automated testing:** Uses pytest to verify expected behavior and identify regressions.

The application generates recommended response actions but does not execute changes to firewalls or other security systems.

## Future Improvements

Potential enhancements include:

- Integrate with security APIs to ingest alerts from external sources.
- Add structured JSON output for integration with other automation tools.
- Introduce configurable response actions.
- Implement human approval workflows for high-impact actions.
- Expand automated testing and measure code coverage.
- Add audit logging for security-sensitive operations.
