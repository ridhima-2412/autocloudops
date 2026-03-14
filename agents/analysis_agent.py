class AnalysisAgent:

    def analyze_resources(self, metrics):

        inefficient_instances = []

        for instance in metrics:
            if instance["cpu_usage"] < 15:
                inefficient_instances.append(instance)

        print("Analysis Agent: Inefficient resources detected")
        return inefficient_instances
