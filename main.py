from agents.monitoring_agent import MonitoringAgent
from agents.analysis_agent import AnalysisAgent
from agents.prediction_agent import PredictionAgent
from agents.optimization_agent import OptimizationAgent

def main():

    monitor = MonitoringAgent()
    analyzer = AnalysisAgent()
    predictor = PredictionAgent()
    optimizer = OptimizationAgent()

    metrics = monitor.collect_metrics("data/sample_metrics.json")

    inefficient = analyzer.analyze_resources(metrics)

    cost = predictor.predict_cost(metrics)

    recommendations = optimizer.recommend(inefficient)

    print("\nEstimated Monthly Cost:", cost)

    print("\nOptimization Suggestions:")
    for r in recommendations:
        print("-", r)


if __name__ == "__main__":
    main()
