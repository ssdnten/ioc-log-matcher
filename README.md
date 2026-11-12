# IOC Log Matcher

Match exact IP and domain indicators against structured offline event logs with normalized values.

Educational cybersecurity portfolio project. Built with AI assistance and supplied with synthetic fixtures and automated tests. It is a learning implementation, not a production security product.

## Quick start

Requires Python 3.11 or newer. Uses only the Python standard library; no pip installation or network access is needed.

From this repository's directory:

```console
python main.py samples/indicators.json samples/events.jsonl
```

On Windows, use `py` in place of `python` if that is your installed launcher. Output is JSON on stdout. To save it, append `> report.json` in your terminal. Paths are relative to your current working directory.

## How it works

Normalize and index typed indicators once, merge duplicate labels, then perform exact lookups per event field. Event numbers refer to nonempty parsed JSONL records. Complexity is O(indicators + events), apart from label sorting.

## Input and example

The `samples/` directory contains the complete minimal input schema and fictional data. The checked `samples/expected-output.json` records the output of the quick-start command (for the integrity monitor, the final check command).

## Tests

```console
python -m unittest discover -s tests -v
```

Tests cover core behavior, boundary cases and invalid input. GitHub Actions is configured to run them on Windows and Ubuntu with Python 3.11–3.13; see the Actions tab for actual remote results.

## Limitations

Indicators in the sample are fictional. No threat feeds, expiry handling, confidence scores, substring extraction or subdomain inheritance. A match provides context for investigation and does not prove malicious activity.

Successful analysis exits 0 unless stated otherwise above; command/input errors exit 2. Findings are not automatically remediated. Only use data you are authorized to analyze. Do not commit real credentials, customer logs or personal data.

## Learning notes

See [LEARNING_RU.md](LEARNING_RU.md) for an exercise and interview questions. Explain the algorithm, run the demo and implement an extension before presenting this as a skill you can use independently.
