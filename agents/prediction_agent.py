class PredictionAgent:

    def predict_cost(self, metrics):

        estimated_cost = 0

        for instance in metrics:
            estimated_cost += 50

        print("Prediction Agent: Estimated monthly cost calculated")

        return estimated_cost
