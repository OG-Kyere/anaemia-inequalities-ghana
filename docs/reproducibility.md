# Reproducibility

The raw Ghana DHS microdata are restricted and are not stored in this repository.

## 1. Obtain the data

Request the **2022 Ghana Individual Recode (IR)** file from The DHS Program.

Either place it at:

\`\`\`text
data/raw/GHIR8CFL.DTA
\`\`\`

or point the environment variable \`DHS_IR_PATH\` to the authorized local file.

PowerShell example:

\`\`\`powershell
$env:DHS_IR_PATH="C:\\path\\to\\GHIR8CFL.DTA"
\`\`\`

Git Bash / Linux / macOS:

\`\`\`bash
export DHS_IR_PATH="/path/to/GHIR8CFL.DTA"
\`\`\`

## 2. Install dependencies

\`\`\`bash
python -m pip install -r requirements.txt
\`\`\`

## 3. Run the core pipeline

\`\`\`bash
python run_analysis.py
\`\`\`

This regenerates:

- overall survey-weighted anaemia prevalence;
- subgroup prevalence estimates using survey-domain variance estimation;
- standard and Erreygers-corrected concentration indices;
- the fully adjusted survey-weighted logistic model with stratified PSU sandwich standard errors.

Outputs are written to:

\`\`\`text
results/reproduced/
\`\`\`

## Validation status

The core pipeline was rerun successfully on **2026-10-08** using the authorized Ghana 2022 IR file.

The rerun reproduced:

- 7,557 women with valid anaemia measurements;
- weighted denominator 7,655.051315;
- anaemia prevalence 41.1225% (95% CI 39.6050%–42.6399%);
- standard concentration index -0.035831;
- Erreygers index -0.058938;
- adjusted-model sample 7,550;
- pregnancy aOR 1.7746;
- overweight aOR 0.7337;
- obesity aOR 0.5972;
- Bono aOR 0.6105;
- Oti aOR 1.4808.

These agree with the locked manuscript results.

See \`docs/core_reproducibility_validation.md\` for the validation table.

## Remaining reproducibility work

The decomposition bootstrap and multilevel random-intercept analyses are documented but still need to be incorporated into the executable pipeline and cross-checked against the locked outputs.

## Data protection

Do not commit the raw IR file, extracted row-level data, or any derived record-level dataset. The repository's \`.gitignore\` excludes the expected DHS file formats and Ghana DHS ZIP archives.
