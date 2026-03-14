class OptimizationAgent:

    def recommend(self, inefficient_instances):

        recommendations = []

        for instance in inefficient_instances:

            recommendations.append(
                f"Instance {instance['instance_id']} has low CPU usage. Consider downsizing or shutting it down."
            )

        print("Optimization Agent: Recommendations generated")

        return recommendations
