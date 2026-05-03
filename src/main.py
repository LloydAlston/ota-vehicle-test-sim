from ecu_sim import ECU
from report import save_report
import logging
import os

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename='logs/test.log', level=logging.INFO)

def main():
    logging.info("Starting OTA test run")

    ecus = [
        ECU("Powertrain Control Module", "v1.0"),
        ECU("ADAS System", "v1.2"),
        ECU("Infotainment Head Unit", "v2.0")
    ]

    results = []

    for ecu in ecus:
        base_version = ecu.version
        for _ in range(5):
            ecu.version = base_version
            logging.info(f"Testing ECU: {ecu.name}")
            result = ecu.update("v2.1", failure_rate=0.4)
            logging.info(f"Result: {result['status']}")
            results.append(result)

    save_report(results)

    for r in results:
        print(r)

if __name__ == "__main__":
    main()