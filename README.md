# Protein Classification Using Topological Data Analysis

This project applies **Topological Data Analysis (TDA)** and **persistence landscapes** to classify different types of maltose-binding proteins (MBPs) from the Protein Data Bank. The analysis leverages homological invariants such as Betti numbers to capture the topological features of protein structures.

## Overview

Topological Data Analysis provides powerful tools for analyzing high-dimensional, incomplete, and noisy data. In protein folding studies, TDA can capture essential structural features that traditional methods might miss. This project specifically focuses on:

- **Persistence Diagrams**: Computing homological features (H0 and H1) from protein correlation matrices
- **Persistence Landscapes**: Converting persistence diagrams into vector representations suitable for machine learning
- **Statistical Analysis**: Using permutation tests to assess the significance of observed differences between protein classes

## Project Structure

```
Topology_for_Protein_Classification/
├── api/
│   └── protein_landscape.py      # Core protein analysis functions
├── corr/                         # Original correlation matrices
│   ├── closed/                   # Closed conformation proteins
│   └── open/                     # Open conformation proteins
├── corrRemake/                   # Remade correlation matrices
│   ├── closed/
│   └── open/
├── dgms/                         # Generated persistence diagrams
│   ├── closed/
│   └── open/
├── landscape_values/             # Computed landscape values
│   ├── landscape_values_H0.txt
│   └── landscape_values_H1.txt
├── landscapeRemake/              # Remade landscape values
├── testProteins/                 # Test dataset
│   ├── corr/
│   ├── landscape_values_test/
│   └── proteins.json
├── landscape.ipynb               # Main analysis notebook
├── perm_test.ipynb               # Permutation test analysis
├── landscape.py                  # Simple landscape example
├── remake.py                     # Script to regenerate results
└── README.md
```

## Installation

### Prerequisites

- Python 3.7+
- Jupyter Notebook

### Dependencies

Install the required packages:

```bash
pip install numpy matplotlib gudhi pandas
```

## Usage

### 1. Basic Analysis

Run the main analysis notebook to compute persistence diagrams and landscapes:

```bash
jupyter notebook landscape.ipynb
```

This notebook:
- Loads protein correlation matrices from the `corr/` directory
- Computes persistence diagrams for H0
- Generates persistence landscapes with configurable parameters
- Saves results to `landscape_values/` directory

### 2. Statistical Testing

Perform permutation tests to assess statistical significance:

```bash
jupyter notebook perm_test.ipynb
```

This notebook:
- Computes landscape values for training and test datasets
- Performs permutation tests to evaluate differences between protein classes
- Generates p-values for statistical significance

### 3. Programmatic Usage

Use the API directly in Python:

```python
import api.protein_landscape as prl

# Analyze proteins and generate landscape values
prl.protein_landscape(
    dir="corrRemake",           # Input directory
    n=13,                       # Number of proteins
    target_directory="landscapeRemake",  # Output directory
    k0=370,                     # Number of landscapes for H0
    k1=73,                      # Number of landscapes for H1
    resolution=50       # Landscape resolution
    saveDiagrams=False          # Whether to save persistence diagrams
)
```

## Methodology

### 1. Data Preprocessing
- Protein correlation matrices are computed from structural data
- Distance matrices are derived as `dist =1 - |correlation|`
- Data is organized into open" and "closed" conformation classes

### 2. Persistent Homology
- **Rips Complex**: Constructed from distance matrices with max edge length 10
- **Homology Computation**: Computes H0 and H1 homology groups
- **Diagram Generation**: Creates persistence diagrams showing birth/death times

### 3. Persistence Landscapes
- Converts persistence diagrams into vector representations
- Configurable parameters:
  - `num_landscapes`: Number of landscape functions (370 for H0, 73 for H1)
  - `resolution`: Number of points per landscape (default: 50)
- Landscape values are averaged to create feature vectors

### 4. Statistical Analysis
- **Permutation Tests**: Assess significance of differences between protein classes
- **Test Statistic**: Absolute difference of means between classes
- **P-value Computation**: Based on 1,000,000 random permutations

## Results

The analysis generates:
- **Persistence Diagrams**: Visual representations of topological features
- **Landscape Values**: Numerical features for machine learning
- **Statistical Tests**: P-values for class separation significance

Results are saved in:
- `landscape_values/`: Training dataset landscape values
- `testProteins/landscape_values_test/`: Test dataset landscape values
- `dgms/`: Persistence diagram visualizations

## Dataset

The project analyzes 21 proteins from the Protein Data Bank:
- **Closed Conformation**: 7 proteins (1anf, 1fqc, 1fqd, 1mpd, 3hpi, 3mbp)
- **Open Conformation**: 7 proteins (1ez9, 1fqa, 1fqb, 1jw4, 1jw5, 1lls)
- **Test Set**: 7 additional proteins for validation


## References
If you use this implementation, cite the original book and paper:
- Kaczynski, T. Computational Homology
- Bubenik, P. (2015) Statistical Topological Data Analysis using Persistence Landscapes
- Protein Data Bank: https://www.rcsb.org/
- The GUDHI Project: https://gudhi.inria.fr/