# Module 4: Agent Evaluation Exercise

## Objective
Build an evaluation framework to measure and improve agent performance using metrics like F1-score, precision, and recall.

## Learning Goals
By completing this exercise, you will:
- Implement evaluation metrics (precision, recall, F1-score)
- Create a golden dataset for testing
- Track agent performance across iterations
- Optimize hyperparameters based on metrics
- Understand quality vs. cost/latency tradeoffs

## Scenario
You're deploying a document classification agent that tags documents with relevant categories. You need to:
1. Measure its accuracy using standard metrics
2. Track performance across prompt versions
3. Optimize hyperparameters
4. Monitor production quality

## Task Requirements

### Part 1: Evaluation Metrics (Required)
Implement these metric calculations:

1. **Precision**: Of items identified, how many were correct?
   - Formula: TP / (TP + FP)
   
2. **Recall**: Of all correct items, how many were found?
   - Formula: TP / (TP + FN)
   
3. **F1-Score**: Harmonic mean of precision and recall
   - Formula: 2 * (Precision * Recall) / (Precision + Recall)

### Part 2: Golden Dataset (Required)
Create a test dataset with:
- Input documents
- Ground truth labels
- Expected outputs
- At least 10 test cases

### Part 3: Agent Evaluator (Required)
Build an evaluator that:
- Runs agent on test cases
- Compares outputs to ground truth
- Calculates metrics
- Generates evaluation reports

### Part 4: Hyperparameter Testing (Required)
Test different configurations:
- Temperature values (0.0, 0.5, 1.0)
- Different prompts
- Track impact on metrics

### Part 5: Extensions (Optional)
- Add latency tracking
- Implement cost estimation
- Create visualization of results
- Add error analysis by category

## Starter Code Structure

```python
class EvaluationMetrics:
    @staticmethod
    def calculate_precision(true_positives, false_positives):
        # TODO
        pass
    
    @staticmethod
    def calculate_recall(true_positives, false_negatives):
        # TODO
        pass
    
    @staticmethod
    def calculate_f1(precision, recall):
        # TODO
        pass

class AgentEvaluator:
    def __init__(self, agent, golden_dataset):
        self.agent = agent
        self.golden_dataset = golden_dataset
    
    def evaluate(self):
        # TODO: Run agent on all test cases and calculate metrics
        pass
    
    def compare_configurations(self, configs):
        # TODO: Test multiple hyperparameter settings
        pass
```

## Golden Dataset Format

```python
GOLDEN_DATASET = [
    {
        "input": "Article about machine learning advances...",
        "ground_truth": ["Technology", "AI", "Science"],
        "description": "ML article should be tagged with tech tags"
    },
    # ... more examples
]
```

## Expected Output

```
=== Agent Evaluation Report ===

Configuration: temperature=0.7, prompt=v1

Test Results:
  Total cases: 10
  Correct: 8
  Incorrect: 2
  
Metrics:
  Precision: 0.85
  Recall: 0.80
  F1-Score: 0.82
  
Latency:
  Average: 1.2s
  Min: 0.8s
  Max: 2.1s

=== Error Analysis ===
Failed cases:
  1. Test case 3: Missed "Sports" tag
  2. Test case 7: Incorrectly added "Politics" tag
```

## Implementation Tips

### Mock Agent
```python
class MockClassificationAgent:
    def __init__(self, temperature=0.7):
        self.temperature = temperature
        # Simulate different behaviors based on temperature
    
    def classify(self, document):
        # Return mock classifications
        # Vary quality based on temperature
        pass
```

### Calculating Confusion Matrix Components
```python
def calculate_confusion_matrix(predictions, ground_truth):
    """
    predictions: list of predicted labels
    ground_truth: list of actual labels
    """
    predicted_set = set(predictions)
    truth_set = set(ground_truth)
    
    true_positives = len(predicted_set & truth_set)
    false_positives = len(predicted_set - truth_set)
    false_negatives = len(truth_set - predicted_set)
    
    return true_positives, false_positives, false_negatives
```

## Testing Your Implementation

1. **Metric Accuracy**: Verify calculations with known values
2. **Edge Cases**: Empty predictions, empty ground truth
3. **Consistency**: Same input should give same metrics
4. **Hyperparameter Impact**: Confirm different configs yield different results

## Success Criteria

Your implementation should:
- ✅ Correctly calculate precision, recall, F1
- ✅ Run evaluation on golden dataset
- ✅ Compare multiple configurations
- ✅ Generate readable reports
- ✅ Handle edge cases gracefully

## Common Pitfalls

1. **Division by zero**: Handle cases where TP + FP = 0
2. **Set vs. List**: Be careful with duplicate labels
3. **Case sensitivity**: Normalize labels before comparison
4. **Partial matches**: Define whether to count partial tag matches
5. **Averaging metrics**: Decide on micro vs. macro averaging

## Reflection Questions

1. Which metric matters most for your use case: precision or recall?
2. How much improvement justifies increased latency?
3. What temperature value worked best and why?
4. How would you handle borderline cases in evaluation?
5. What's missing from F1-score that might matter in production?

## Time Estimate
- Part 1: 30-40 minutes
- Part 2: 20-30 minutes
- Part 3: 40-50 minutes
- Part 4: 30-40 minutes
- Part 5 (optional): 45-60 minutes

## Next Steps
After completing:
1. Compare with the provided solution
2. Try evaluating a real agent (if you have API access)
3. Experiment with different golden datasets
4. Move to Module 5: Multi-Agent Collaboration

---

**Focus on understanding the evaluation metrics and their tradeoffs!**
