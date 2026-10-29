# Agentic AI - Andrew Ng's Course (Jupyter Notebooks)

If you don't want to pay for the DeepLearning.AI course **Agentic AI**, this is a good repo you can star.

It includes the Jupyter notebooks of all modules, along with all dependent files like `utils.py` and datasets (e.g., `coffee_sales.csv`), so you can study and run them locally.

## Project Structure

```
Module2/
  ├── M2_UGL_1.ipynb      # Reflection Pattern - Chart Generation
  ├── utils.py             # Helper functions (API calls, data loading, display)
  └── coffee_sales.csv     # Dataset
```

## Setup for Local Use

1. Install dependencies:
   ```bash
   pip install pandas matplotlib pillow openai anthropic
   ```

2. Add your API keys in `utils.py`:
   ```python
   openai_api_key = "<your OpenAI API key here>"
   anthropic_api_key = "<your Anthropic API key here>"
   ```

3. Open the notebook and run:
   ```bash
   jupyter notebook
   ```
