import random

def run_test(ecu, target_version):
    """
    Simulates an OTA update. 70% success logic, handles rollback.
    """
    success = random.random() > 0.3
    original_version = ecu.version
    
    if success:
        ecu.version = target_version
        return {
            "ecu": ecu.name,
            "status": "Success",
            "old_version": original_version,
            "new_version": target_version,
            "failure_reason": ""
        }
    else:
        # Simulation of rollback mechanism
        ecu.version = original_version
        return {
            "ecu": ecu.name,
            "status": "Failure",
            "old_version": original_version,
            "new_version": target_version,
            "failure_reason": "Flash verification failed"
        }