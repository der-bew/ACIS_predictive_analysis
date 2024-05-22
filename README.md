# AlphaCare Insurance Solutions (ACIS) Predictive Analysis
Welcome to the ACIS Predictive Analysis repository. This project focuses on predictive analysis using data from the ACIS dataset. The repository contains various scripts and notebooks for exploratory data analysis (EDA), hypothesis testing, and modeling.

# Directory Structure

ACIS_predictive_analysis/

- .dvc/
- .github/
     - workflows/
- data/
- notebooks/
     - EDA.ipynb
     - README.md
     -  __init__.py
     - ab_hypothesis_test.ipynb
     - modeling.ipynb

- scripts/
     - __init__.py
     - handler.py
     - unzip_file.py
     - visualizer.py
- .dvcignore
- .gitignore
- README.md
- requirements.txt

### .dvc/
Contains the configuration files for Data Version Control (DVC), which helps in managing and versioning large datasets.

### .github/workflows/
Contains the GitHub Actions workflows for Continuous Integration and Continuous Deployment (CI/CD).

### data/
A directory intended for storing datasets used in the project. Note that data files are not included in the repository.

### notebooks/
Contains Jupyter notebooks for various stages of the analysis:

  - EDA.ipynb: Exploratory Data Analysis
  - README.md: Documentation for the notebooks
  - __init__.py: Makes this directory a Python package
  - ab_hypothesis_test.ipynb: A/B Hypothesis Testing
  - modeling.ipynb: Model building and evaluation
### scripts/
Contains Python scripts used throughout the project:

  -  __init__.py: Makes this directory a Python package
  -  handler.py: Script for handling data processing tasks
  - unzip_file.py: Utility script to unzip data files
  - visualizer.py: Script for creating visualizations
### .dvcignore
Specifies files and directories for DVC to ignore.

### .gitignore
Specifies files and directories for Git to ignore.

### README.md
This file, providing an overview and instructions for the repository.

### requirements.txt
Lists the Python dependencies required for the project.

# Getting Started
## Prerequisites
Ensure you have the following installed:

   - Python 3.x
   - Jupyter Notebook
   - Git
   - DVC
Install the required Python packages using:

```
pip install -r requirements.txt
```

## Setting Up
1. Clone the Repository:
   
   ```
   git clone https://github.com/der-bew/ACIS_predictive_analysis.git
   cd ACIS_predictive_analysis
    ```

2. Set Up DVC:
Initialize DVC and pull the data:

```
dvc init
dvc pull
```
3. Running Notebooks:
Launch Jupyter Notebook and open the desired notebook:

```
jupyter notebook
```
# Usage
## Exploratory Data Analysis
Open notebooks/EDA.ipynb to explore the data and understand its structure and main characteristics.

## A/B Hypothesis Testing
Use notebooks/ab_hypothesis_test.ipynb to perform A/B testing and derive insights from the results.

## Modeling
notebooks/modeling.ipynb contains the steps for building, evaluating, and selecting predictive models.

## Scripts
   - Data Handling: scripts/handler.py
   - Unzipping Files: scripts/unzip_file.py
   - Visualizations: scripts/visualizer.py
# Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
  1. Create a new branch (`git checkout -b feature-branch`).
  2. Commit your changes (`git commit -m 'Add new feature'`).
  3. Push to the branch (`git push origin feature-branch`).
  4. Create a pull request.
