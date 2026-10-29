"""
Module 4: Agent Evaluation Exercise
Build an evaluation framework for measuring agent performance.
"""

from typing import List, Dict, Any, Set
import time


# Golden Dataset - documents with ground truth labels
GOLDEN_DATASET = [
    {
        "id": 1,
        "input": "New breakthrough in deep learning allows AI models to learn with 50% less data",
        "ground_truth": ["Technology", "AI", "Science"],
        "description": "AI research article"
    },
    {
        "id": 2,
        "input": "Local team wins championship in overtime thriller",
        "ground_truth": ["Sports"],
        "description": "Sports news"
    },
    {
        "id": 3,
        "input": "Stock market reaches new highs amid economic recovery",
        "ground_truth": ["Business", "Finance", "Economy"],
        "description": "Financial news"
    },
    {
        "id": 4,
        "input": "New climate report warns of urgent need for action",
        "ground_truth": ["Environment", "Science", "Politics"],
        "description": "Climate change article"
    },
    {
        "id": 5,
        "input": "Latest smartphone features advanced AI camera capabilities",
        "ground_truth": ["Technology", "AI", "Consumer"],
        "description": "Product review"
    },
]


class EvaluationMetrics:
    """Calculate standard evaluation metrics."""
    
    @staticmethod
    def calculate_precision(true_positives: int, false_positives: int) -> float:
        """
        Calculate precision: TP / (TP + FP)
        
        TODO: Implement precision calculation
        Hint: Handle division by zero
        """
        pass
    
    @staticmethod
    def calculate_recall(true_positives: int, false_negatives: int) -> float:
        """
        Calculate recall: TP / (TP + FN)
        
        TODO: Implement recall calculation
        Hint: Handle division by zero
        """
        pass
    
    @staticmethod
    def calculate_f1(precision: float, recall: float) -> float:
        """
        Calculate F1-score: 2 * (P * R) / (P + R)
        
        TODO: Implement F1 calculation
        Hint: Handle cases where precision + recall = 0
        """
        pass
    
    @staticmethod
    def calculate_confusion_matrix(predictions: List[str], ground_truth: List[str]) -> Dict[str, int]:
        """
        Calculate TP, FP, FN from predictions and ground truth.
        
        Args:
            predictions: List of predicted labels
            ground_truth: List of actual labels
            
        Returns:
            Dict with 'tp', 'fp', 'fn' keys
            
        TODO: Implement confusion matrix calculation
        Hints:
        - Convert to sets for easier comparison
        - TP: items in both predictions and ground truth
        - FP: items in predictions but not in ground truth
        - FN: items in ground truth but not in predictions
        """
        pass


class MockClassificationAgent:
    """
    A mock agent that classifies documents.
    Simulates varying performance based on temperature.
    """
    
    def __init__(self, temperature: float = 0.7, prompt_version: str = "v1"):
        """
        TODO: Initialize the mock agent
        """
        self.temperature = temperature
        self.prompt_version = prompt_version
    
    def classify(self, document: str) -> List[str]:
        """
        Classify a document and return predicted tags.
        
        TODO: Implement mock classification
        Hints:
        - Look for keywords in the document
        - Vary accuracy based on temperature
        - Lower temperature = more conservative/accurate
        - Higher temperature = more creative/errors
        """
        pass


class AgentEvaluator:
    """Evaluate agent performance on a golden dataset."""
    
    def __init__(self, agent, golden_dataset: List[Dict]):
        """
        TODO: Initialize the evaluator
        """
        self.agent = agent
        self.golden_dataset = golden_dataset
        self.results = []
    
    def evaluate(self) -> Dict[str, Any]:
        """
        Run evaluation on the full golden dataset.
        
        Returns:
            Dictionary with metrics and detailed results
            
        TODO: Implement evaluation
        Steps:
        1. For each test case:
           a. Run agent to get predictions
           b. Compare with ground truth
           c. Calculate metrics
        2. Aggregate results
        3. Calculate overall metrics
        4. Return comprehensive report
        """
        pass
    
    def evaluate_single(self, test_case: Dict) -> Dict[str, Any]:
        """
        Evaluate agent on a single test case.
        
        TODO: Implement single-case evaluation
        Returns dict with predictions, ground truth, and metrics
        """
        pass
    
    def generate_report(self, results: Dict) -> str:
        """
        Generate a human-readable evaluation report.
        
        TODO: Implement report generation
        Include:
        - Overall metrics
        - Per-case results
        - Error analysis
        - Performance summary
        """
        pass
    
    def compare_configurations(self, configurations: List[Dict]) -> Dict:
        """
        Compare multiple agent configurations.
        
        Args:
            configurations: List of dicts with 'temperature', 'prompt_version', etc.
            
        Returns:
            Comparison results showing which config performed best
            
        TODO: Implement configuration comparison
        Steps:
        1. For each configuration, create an agent and evaluate
        2. Compare metrics across configurations
        3. Identify best configuration
        4. Return comparison report
        """
        pass


def main():
    """Test the evaluation framework."""
    print("=== Agent Evaluation Exercise ===\n")
    
    # TODO: Test metric calculations
    print("Testing metric calculations...")
    # metrics = EvaluationMetrics()
    # precision = metrics.calculate_precision(8, 2)
    # recall = metrics.calculate_recall(8, 3)
    # f1 = metrics.calculate_f1(precision, recall)
    # print(f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1: {f1:.2f}\n")
    
    # TODO: Create and evaluate an agent
    print("Evaluating agent...")
    # agent = MockClassificationAgent(temperature=0.7)
    # evaluator = AgentEvaluator(agent, GOLDEN_DATASET)
    # results = evaluator.evaluate()
    # print(evaluator.generate_report(results))
    
    # TODO: Compare configurations
    print("\nComparing configurations...")
    # configurations = [
    #     {"temperature": 0.0, "prompt_version": "v1"},
    #     {"temperature": 0.5, "prompt_version": "v1"},
    #     {"temperature": 1.0, "prompt_version": "v1"},
    # ]
    # comparison = evaluator.compare_configurations(configurations)
    # print(comparison)


if __name__ == "__main__":
    main()
