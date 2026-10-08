# Reproducibility

The raw Ghana DHS microdata are restricted and are not stored in this repository.

## 1. Obtain the data

Request the **2022 Ghana Individual Recode (IR)** file from The DHS Program.

Either place it at:

```text
data/raw/GHIR8CFL.DTA
```

or point the environment variable `DHS_IR_PATH` to the authorized local file.

PowerShell example:

```powershell
$env:DHS_IR_PATH="C:\path\to\GHIR8CFL.DTA"
```

Linux/macOS:

```bash
export DHS_IR_PATH="/path/to/GHIR8CFL.DTA"
```

## 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 3. Run the core pipeline

```bash
python run_analysis.py
```

This currently regenerates:

- overall survey-weighted anaemia prevalence;
- subgroup prevalence estimates with design-based confidence intervals;
- standard and Erreygers-corrected concentration indices;
- the fully adjusted survey-weighted logistic model with stratified PSU sandwich standard errors.

Outputs are written to:

```text
results/reproduced/
```

## Scope

The core pipeline reproduces the principal descriptive, inequality, and adjusted-regression results.

The decomposition bootstrap and multilevel random-intercept analyses are documented separately and will be added to the executable pipeline after their implementation is fully cross-checked against the locked manuscript outputs.

## Data protection

Do not commit the raw IR file, extracted row-level data, or any derived record-level dataset. The repository's `.gitignore` excludes the expected DHS file formats and Ghana DHS ZIP archives.
