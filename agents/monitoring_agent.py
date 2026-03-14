import json

class MonitoringAgent:

    def collect_metrics(self, filepath):
        with open(filepath, "r") as file:
            data = json.load(file)

        print("Monitoring Agent: Metrics collected")
        return data
