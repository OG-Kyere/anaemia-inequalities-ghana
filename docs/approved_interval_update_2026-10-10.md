# Approved inequality interval update — 10 October 2026

The corresponding author approved replacing the previous untraceable draft interval (-0.0914 to -0.0212) with the reproducible full-sample stratified PSU percentile bootstrap interval **-0.0924 to -0.0249**. The point estimate remains -0.0589. The run used 7,557 women, 5,000 replicates and seed 20261008; unrounded limits are -0.09237167274547348 and -0.02494165401130471.

The decomposition retains its 200-replicate bootstrap and all other locked results remain unchanged. Earlier validation records preserve the previous interval for audit history. Current manuscript, abstract, figure captions and curve annotation use the approved interval. Contributor roles and final approval remain pending confirmation from all authors.

Reproduction: `python run_analysis.py --extended --bootstrap-reps 200 --inequality-bootstrap-reps 5000` (with authorized data and the pinned validation environment). Check the runner help for available model options; multilevel fits are separately seeded at gradient tolerance 1e-5.
