# OTA Vehicle Test Simulator

A Python-based simulation tool designed to validate Over-the-Air (OTA) software updates across assorted vehicle Electronic Control Units (ECUs).

## Features
- Over-the-Air Update Simulation Engine
- Controlled version rollbacks linked to randomized flash verification failures
- Aggregated verification testing output encoded to CSV
- Streamlit reporting dashboard for analytic visualization

---

## Instructions

```bash
pip install -r requirements.txt
python src/main.py
streamlit run src/dashboard.py
```