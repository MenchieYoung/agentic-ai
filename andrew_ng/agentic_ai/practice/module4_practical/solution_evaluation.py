"""
Module 4: Agent Evaluation Solution
Complete implementation of an evaluation framework with metrics.
"""

from typing import List, Dict, Any, Set
import time
import random


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
    {
        "id": 6,
        "input": "Government announces new infrastructure spending plan",
        "ground_truth": ["Politics", "Economy", "Business"],
        "description": "Political news"
    },
    {
        "id": 7,
        "input": "Scientists discover new species in Amazon rainforest",
        "ground_truth": ["Science", "Environment"],
        "description": "Scientific discovery"
    },
    {
        "id": 8,
        "input": "Tech giant reports record quarterly earnings",
        "ground_truth": ["Business", "Technology", "Finance"],
        "description": "Earnings report"
    },
    {
        "id": 9,
        "input": "Olympic athlete breaks world record",
        "ground_truth": ["Sports"],
        "description": "Sports achievement"
    },
    {
        "id": 10,
        "input": "New renewable energy project to power 100,000 homes",
        "ground_truth": ["Environment", "Technology", "Business"],
        "description": "Energy project"
    },
]


class EvaluationMetrics:
    """Calculate standard evaluation metrics."""
    
    @staticmethod
    def calculate_precision(true_positives: int, false_positives: int) -> float:
        """
        Calculate precision: TP / (TP + FP)
        Precision measures: of items identified, how many were correct?
        """
        if true_positives + false_positives == 0:
            return 0.0
        return true_positives / (true_positives + false_positives)
    
    @staticmethod
    def calculate_recall(true_positives: int, false_negatives: int) -> float:
        """
        Calculate recall: TP / (TP + FN)
        Recall measures: of all correct items, how many were found?
        """
        if true_positives + false_negatives == 0:
            return 0.0
        return true_positives / (true_positives + false_negatives)
    
    @staticmethod
    def calculate_f1(precision: float, recall: float) -> float:
        """
        Calculate F1-score: 2 * (P * R) / (P + R)
        F1 is the harmonic mean of precision and recall.
        """
        if precision + recall == 0:
            return 0.0
        return 2 * (precision * recall) / (precision + recall)
    
    @staticmethod
    def calculate_confusion_matrix(predictions: List[str], ground_truth: List[str]) -> Dict[str, int]:
        """
        Calculate TP, FP, FN from predictions and ground truth.
        
        TP (True Positives): Items in both predictions and ground truth
        FP (False Positives): Items in predictions but not in ground truth
        FN (False Negatives): Items in ground truth but not in predictions
        """
        pred_set = set(predictions)
        truth_set = set(ground_truth)
        
        tp = len(pred_set & truth_set)  # Intersection
        fp = len(pred_set - truth_set)  # In predictions only
        fn = len(truth_set - pred_set)  # In ground truth only
        
        return {
            'tp': tp,
            'fp': fp,
            'fn': fn
        }
    
    @staticmethod
    def calculate_all_metrics(predictions: List[str], ground_truth: List[str]) -> Dict[str, float]:
        """Calculate precision, recall, and F1 in one call."""
        confusion = EvaluationMetrics.calculate_confusion_matrix(predictions, ground_truth)
        
        precision = EvaluationMetrics.calculate_precision(confusion['tp'], confusion['fp'])
        recall = EvaluationMetrics.calculate_recall(confusion['tp'], confusion['fn'])
        f1 = EvaluationMetrics.calculate_f1(precision, recall)
        
        return {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'tp': confusion['tp'],
            'fp': confusion['fp'],
            'fn': confusion['fn']
        }


class MockClassificationAgent:
    """
    A mock agent that classifies documents.
    Simulates varying performance based on temperature.
    """
    
    # Keyword mapping for classification
    KEYWORD_MAP = {
        "AI": ["ai", "artificial intelligence", "machine learning", "deep learning", "neural"],
        "Technology": ["tech", "technology", "smartphone", "computer", "software", "digital"],
        "Science": ["science", "scientific", "research", "discovery", "breakthrough", "species"],
        "Sports": ["sport", "team", "championship", "athlete", "olympic", "wins", "record"],
        "Business": ["business", "market", "company", "earnings", "quarterly", "project", "spending"],
        "Finance": ["finance", "stock", "earning", "economy", "economic"],
        "Economy": ["economy", "economic", "recovery", "spending", "infrastructure"],
        "Environment": ["environment", "climate", "renewable", "energy", "rainforest", "green"],
        "Politics": ["government", "political", "policy", "announces", "urgent", "action"],
        "Consumer": ["consumer", "latest", "features", "product", "smartphone"],
    }
    
    def __init__(self, temperature: float = 0.7, prompt_version: str = "v1"):
        """
        Initialize the mock agent.
        
        Args:
            temperature: Controls randomness/accuracy
                - 0.0: Very conservative, high precision, lower recall
                - 0.5: Balanced
                - 1.0: More creative, may add irrelevant tags
            prompt_version: Different prompt versions (for testing)
        """
        self.temperature = temperature
        self.prompt_version = prompt_version
        random.seed(42)  # For reproducibility
    
    def classify(self, document: str) -> List[str]:
        """
        Classify a document and return predicted tags.
        
        Logic:
        - Lower temperature: only add tags with strong evidence
        - Higher temperature: more liberal with tags
        """
        document_lower = document.lower()
        predictions = []
        
        for tag, keywords in self.KEYWORD_MAP.items():
            # Count keyword matches
            matches = sum(1 for keyword in keywords if keyword in document_lower)
            
            # Threshold based on temperature
            if self.temperature <= 0.3:
                # Conservative: need strong evidence
                threshold = 2
            elif self.temperature <= 0.7:
                # Balanced: one keyword match is enough
                threshold = 1
            else:
                # Liberal: might add tags with weaker evidence
                threshold = 0 if random.random() < 0.3 else 1
            
            if matches >= threshold:
                predictions.append(tag)
        
        # Higher temperature: might add random noise
        if self.temperature > 0.8 and random.random() < 0.2:
            noise_tags = ["Misc", "General", "News"]
            predictions.append(random.choice(noise_tags))
        
        # Lower temperature: might miss some tags
        if self.temperature < 0.3 and len(predictions) > 2:
            predictions = predictions[:2]  # Keep only top matches
        
        return predictions


class AgentEvaluator:
    """Evaluate agent performance on a golden dataset."""
    
    def __init__(self, agent, golden_dataset: List[Dict]):
        """Initialize the evaluator."""
        self.agent = agent
        self.golden_dataset = golden_dataset
        self.results = []
    
    def evaluate(self) -> Dict[str, Any]:
        """
        Run evaluation on the full golden dataset.
        
        Returns comprehensive results including metrics and details.
        """
        start_time = time.time()
        test_results = []
        
        # Evaluate each test case
        for test_case in self.golden_dataset:
            result = self.evaluate_single(test_case)
            test_results.append(result)
        
        # Aggregate metrics
        total_tp = sum(r['metrics']['tp'] for r in test_results)
        total_fp = sum(r['metrics']['fp'] for r in test_results)
        total_fn = sum(r['metrics']['fn'] for r in test_results)
        
        overall_precision = EvaluationMetrics.calculate_precision(total_tp, total_fp)
        overall_recall = EvaluationMetrics.calculate_recall(total_tp, total_fn)
        overall_f1 = EvaluationMetrics.calculate_f1(overall_precision, overall_recall)
        
        # Calculate per-case averages
        avg_precision = sum(r['metrics']['precision'] for r in test_results) / len(test_results)
        avg_recall = sum(r['metrics']['recall'] for r in test_results) / len(test_results)
        avg_f1 = sum(r['metrics']['f1'] for r in test_results) / len(test_results)
        
        # Count successes (F1 > 0.7 considered good)
        successes = sum(1 for r in test_results if r['metrics']['f1'] >= 0.7)
        
        evaluation_time = time.time() - start_time
        
        return {
            'overall_metrics': {
                'precision': overall_precision,
                'recall': overall_recall,
                'f1': overall_f1,
                'tp': total_tp,
                'fp': total_fp,
                'fn': total_fn,
            },
            'average_metrics': {
                'precision': avg_precision,
                'recall': avg_recall,
                'f1': avg_f1,
            },
            'summary': {
                'total_cases': len(test_results),
                'successes': successes,
                'failures': len(test_results) - successes,
                'success_rate': successes / len(test_results),
            },
            'test_results': test_results,
            'evaluation_time': evaluation_time,
            'agent_config': {
                'temperature': self.agent.temperature,
                'prompt_version': self.agent.prompt_version,
            }
        }
    
    def evaluate_single(self, test_case: Dict) -> Dict[str, Any]:
        """Evaluate agent on a single test case."""
        start_time = time.time()
        
        # Get predictions from agent
        predictions = self.agent.classify(test_case['input'])
        ground_truth = test_case['ground_truth']
        
        # Calculate metrics
        metrics = EvaluationMetrics.calculate_all_metrics(predictions, ground_truth)
        
        latency = time.time() - start_time
        
        # Identify errors
        pred_set = set(predictions)
        truth_set = set(ground_truth)
        
        return {
            'test_id': test_case['id'],
            'description': test_case.get('description', ''),
            'input': test_case['input'][:60] + '...' if len(test_case['input']) > 60 else test_case['input'],
            'predictions': predictions,
            'ground_truth': ground_truth,
            'metrics': metrics,
            'latency': latency,
            'errors': {
                'false_positives': list(pred_set - truth_set),
                'false_negatives': list(truth_set - pred_set),
            },
            'success': metrics['f1'] >= 0.7,  # F1 > 0.7 considered good
        }
    
    def generate_report(self, results: Dict) -> str:
        """Generate a human-readable evaluation report."""
        report = []
        report.append("=" * 70)
        report.append("AGENT EVALUATION REPORT")
        report.append("=" * 70)
        
        # Configuration
        config = results['agent_config']
        report.append(f"\nConfiguration:")
        report.append(f"  Temperature: {config['temperature']}")
        report.append(f"  Prompt Version: {config['prompt_version']}")
        
        # Overall metrics
        overall = results['overall_metrics']
        report.append(f"\nOverall Metrics (Micro-averaged):")
        report.append(f"  Precision: {overall['precision']:.3f}")
        report.append(f"  Recall:    {overall['recall']:.3f}")
        report.append(f"  F1-Score:  {overall['f1']:.3f}")
        report.append(f"  TP: {overall['tp']}, FP: {overall['fp']}, FN: {overall['fn']}")
        
        # Average metrics
        avg = results['average_metrics']
        report.append(f"\nAverage Metrics (Macro-averaged):")
        report.append(f"  Precision: {avg['precision']:.3f}")
        report.append(f"  Recall:    {avg['recall']:.3f}")
        report.append(f"  F1-Score:  {avg['f1']:.3f}")
        
        # Summary
        summary = results['summary']
        report.append(f"\nTest Summary:")
        report.append(f"  Total cases: {summary['total_cases']}")
        report.append(f"  Successes:   {summary['successes']} ({summary['success_rate']:.1%})")
        report.append(f"  Failures:    {summary['failures']}")
        
        # Performance
        report.append(f"\nPerformance:")
        report.append(f"  Total time:    {results['evaluation_time']:.3f}s")
        avg_latency = sum(r['latency'] for r in results['test_results']) / len(results['test_results'])
        report.append(f"  Avg latency:   {avg_latency:.3f}s per case")
        
        # Failed cases
        failed_cases = [r for r in results['test_results'] if not r['success']]
        if failed_cases:
            report.append(f"\n{'='*70}")
            report.append("ERROR ANALYSIS")
            report.append("="*70)
            report.append(f"\nFailed Cases ({len(failed_cases)}):")
            
            for case in failed_cases:
                report.append(f"\n  Test #{case['test_id']}: {case['description']}")
                report.append(f"    Input: {case['input']}")
                report.append(f"    Predicted:    {case['predictions']}")
                report.append(f"    Ground truth: {case['ground_truth']}")
                report.append(f"    F1: {case['metrics']['f1']:.3f}")
                
                if case['errors']['false_positives']:
                    report.append(f"    False Positives: {case['errors']['false_positives']}")
                if case['errors']['false_negatives']:
                    report.append(f"    False Negatives: {case['errors']['false_negatives']}")
        else:
            report.append(f"\n✓ All test cases passed!")
        
        report.append("\n" + "="*70)
        
        return "\n".join(report)
    
    def compare_configurations(self, configurations: List[Dict]) -> Dict:
        """
        Compare multiple agent configurations.
        
        Args:
            configurations: List of dicts with 'temperature', 'prompt_version', etc.
        
        Returns:
            Comparison results showing which config performed best.
        """
        print("="*70)
        print("CONFIGURATION COMPARISON")
        print("="*70)
        
        comparison_results = []
        
        for idx, config in enumerate(configurations, 1):
            print(f"\nEvaluating configuration {idx}/{len(configurations)}...")
            print(f"  Temperature: {config.get('temperature', 0.7)}")
            print(f"  Prompt: {config.get('prompt_version', 'v1')}")
            
            # Create agent with this configuration
            agent = MockClassificationAgent(
                temperature=config.get('temperature', 0.7),
                prompt_version=config.get('prompt_version', 'v1')
            )
            
            # Evaluate
            evaluator = AgentEvaluator(agent, self.golden_dataset)
            results = evaluator.evaluate()
            
            comparison_results.append({
                'config': config,
                'results': results
            })
            
            print(f"  F1-Score: {results['overall_metrics']['f1']:.3f}")
        
        # Find best configuration
        best = max(comparison_results, key=lambda x: x['results']['overall_metrics']['f1'])
        
        # Generate comparison report
        print("\n" + "="*70)
        print("COMPARISON SUMMARY")
        print("="*70)
        print(f"\n{'Config':<20} {'Temp':<8} {'Precision':<12} {'Recall':<12} {'F1':<12}")
        print("-"*70)
        
        for item in comparison_results:
            config_name = f"Config {configurations.index(item['config'])+1}"
            temp = item['config'].get('temperature', 0.7)
            metrics = item['results']['overall_metrics']
            
            print(f"{config_name:<20} {temp:<8.1f} "
                  f"{metrics['precision']:<12.3f} {metrics['recall']:<12.3f} {metrics['f1']:<12.3f}")
        
        print("\n" + "="*70)
        print(f"BEST CONFIGURATION: Temperature = {best['config'].get('temperature', 0.7)}")
        print(f"  F1-Score: {best['results']['overall_metrics']['f1']:.3f}")
        print(f"  Precision: {best['results']['overall_metrics']['precision']:.3f}")
        print(f"  Recall: {best['results']['overall_metrics']['recall']:.3f}")
        print("="*70)
        
        return {
            'comparison_results': comparison_results,
            'best_config': best['config'],
            'best_results': best['results']
        }


def main():
    """Test the evaluation framework."""
    print("=== Agent Evaluation Solution Demo ===\n")
    
    # Test 1: Metric calculations
    print("Test 1: Metric Calculations")
    print("-" * 50)
    metrics = EvaluationMetrics()
    
    # Example: predicted ["A", "B", "C"], ground truth ["A", "B", "D"]
    # TP=2 (A,B), FP=1 (C), FN=1 (D)
    precision = metrics.calculate_precision(2, 1)
    recall = metrics.calculate_recall(2, 1)
    f1 = metrics.calculate_f1(precision, recall)
    print(f"Example: TP=2, FP=1, FN=1")
    print(f"  Precision: {precision:.3f}")
    print(f"  Recall:    {recall:.3f}")
    print(f"  F1-Score:  {f1:.3f}")
    print()
    
    # Test 2: Single agent evaluation
    print("Test 2: Single Agent Evaluation")
    print("-" * 50)
    agent = MockClassificationAgent(temperature=0.5)
    evaluator = AgentEvaluator(agent, GOLDEN_DATASET)
    results = evaluator.evaluate()
    print(evaluator.generate_report(results))
    print()
    
    # Test 3: Configuration comparison
    print("\nTest 3: Configuration Comparison")
    print("-" * 50)
    configurations = [
        {"temperature": 0.0, "prompt_version": "v1"},
        {"temperature": 0.5, "prompt_version": "v1"},
        {"temperature": 0.7, "prompt_version": "v1"},
        {"temperature": 1.0, "prompt_version": "v1"},
    ]
    
    comparison = evaluator.compare_configurations(configurations)
    
    print("\n=== Key Insights ===")
    print("- Lower temperature (0.0-0.3): High precision, may miss some tags")
    print("- Medium temperature (0.5-0.7): Best balance for most tasks")
    print("- High temperature (0.8-1.0): May add noise, lower precision")
    print("\nRecommendation: Start with temperature ~0.5 and adjust based on")
    print("whether precision or recall is more important for your use case.")


if __name__ == "__main__":
    main()
