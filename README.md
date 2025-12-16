# QC Automation – Speaking Review

This project provides an offline, explainable Quality Control (QC) system
for post-test review of speaking assessments.

## Features
- Offline ASR (Whisper)
- Examiner vs Examinee role inference
- Procedural QC rule checks
- Score consistency review (Agree / Borderline / Disagree)
- Human-readable and JSON reports

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
