# Network Automation Internship -  Evaluation Assignment

This repository contains my solution for the Network Analytics and Automation Internship Candidate Evaluation assignment.

## Task 01 - Configuration Data Extraction

The Python script reads the provided Cisco and Huawei router configuration files and extracts the following information:

- Main Interface
- Description
- VRF
- Vendor

The vendor is detected automatically from the configuration content.

The extracted records are saved to:

`output/extracted_services.xlsx`

## Project Structure

- `configs/router_a.txt` - Cisco sample configuration
- `configs/router_b.txt` - Huawei sample configuration
- `task01_config_extractor.py` - Configuration extraction script
- `output/extracted_services.xlsx` - Generated Excel output
- `requirements.txt` - Required Python package

## Requirements

- Python 3
- openpyxl 3.1.5

Install the required package using:

```bash
python -m pip install -r requirements.txt
```

## How to Run Task 01

Open a terminal in the project directory and run:

```bash
python task01_config_extractor.py
```

The program reads both router configuration files, extracts the required information, and creates the Excel file inside the `output` folder.

## Assumptions

- Cisco configurations are identified using `show running-config`.
- Huawei configurations are identified using `display current-configuration`.