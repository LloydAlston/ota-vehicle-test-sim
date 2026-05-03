import random

class ECU:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def update(self, new_version, failure_rate=0.25):
        success = random.random() > failure_rate
        original_version = self.version
        
        if success:
            self.version = new_version
            return {
                "ecu": self.name,
                "status": "UPDATED",
                "old_version": original_version,
                "new_version": new_version,
                "failure_reason": ""
            }
        else:
            return {
                "ecu": self.name,
                "status": "FAILED",
                "old_version": original_version,
                "new_version": new_version,
                "failure_reason": "Flash verification failed"
            }