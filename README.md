# Phone Tests — Appium + Pytest Mobile Automation Framework

Mobile automation test framework for Android using Appium, pytest and Jenkins.

## Tech stack

* Python
* pytest
* Appium
* UiAutomator2
* Android Debug Bridge
* Page Object Model
* pytest-html
* Jenkins Pipeline
* GitHub

## Project structure

```text
phone_tests/
├── api/
├── data/
├── pages/
├── tests/
├── utils/
├── conftest.py
├── pytest.ini
├── Jenkinsfile
└── README.md
```

## Features

* Android UI tests with Appium
* Page Object Model structure
* BasePage with reusable methods
* Data-driven tests
* API + mobile test example
* APK installation test
* Device info test
* App version test
* HTML test report
* Screenshots on failure
* Jenkins pipeline
* Automatic Appium server start in Jenkins

## Requirements

* Python 3.14+
* Android SDK
* ADB
* Appium
* UiAutomator2 driver
* Connected Android device with USB debugging enabled

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run tests locally

```bash
python -m pytest
```

Run smoke tests:

```bash
python -m pytest -m smoke
```

Run install tests:

```bash
python -m pytest -m install
```

Run with HTML report:

```bash
python -m pytest -v -s --html=report.html --self-contained-html
```

## Jenkins

The project contains a `Jenkinsfile` which:

1. Checks Android device connection
2. Starts Appium server
3. Runs pytest tests
4. Generates HTML report
5. Archives report, screenshots and Appium logs

## Device used

* Manufacturer: vivo
* Device name: Y19s
* Model: V2419
* Android: 16

## Example test result

```text
10 passed
```

## Author

Marcin Ziółkowski
QA Automation / Mobile Testing
