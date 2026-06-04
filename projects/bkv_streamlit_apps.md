---
title: BKV Streamlit Apps
description: A multi-page Streamlit platform of reservoir & production engineering tools for gas wells.
image_url: ./images/covers/streamlit_apps.png
image_url_global: https://raw.githubusercontent.com/manolosolalinde/cv/main/projects/images/covers/streamlit_apps.png
date: 2026-05-20
order: 1
technologies: Python, Streamlit, Plotly, Pandas, NumPy, SciPy (exp1, Huber regression), Scikit-learn, AWS (ECS Fargate, Lambda, S3, DynamoDB, ECR, CloudWatch, Bedrock), Pulumi, Docker, GitHub Actions, Parquet, MkDocs.
category: Data Science Development
---

# BKV Streamlit Apps - BKV Corporation

Data Scientist/Developer: Manuel Solalinde [(manolosolalinde@gmail.com)](mailto:manolosolalinde@gmail.com)

A single, unified **multi-page Streamlit platform** that bundles a growing collection of reservoir and production engineering tools, each selectable from the sidebar. The apps share one data pipeline — daily production, injection and SCADA sensor data live in **AWS S3** as parquet and are read on demand by well ID — and one deployment, a containerized Streamlit service running on **ECS Fargate**. Heavier batch jobs (per-well report generation) fan out across **parallel Lambda** functions; in-app user documentation is published with **MkDocs**.

This page covers the engineering toolkit; the platform's flagship optimization app is documented separately:

- **Gas Injection Optimization** — a data-driven app that recommends optimal gas-injection rates for gas-lift wells and ranks every injecting well against its recommendation. [See the dedicated page →](./bkv_gas_injection.md)

## Applications

- **Resolution Visualizer** — visualizes SCADA sensor reading frequency per well, broken down by day and channel.
- **Salt Water Injection** — an infinite-reservoir radial pressure-propagation calculator based on the Theis equation.
- **Well Communication** — detects inter-well pressure interference from correlated, detrended gas-production residuals.
- **Critical Rate Sensitivities** — computes the minimum gas rate required to lift liquids out of the wellbore.
- **CO2 Runtime History** — real-time sensor dashboard for the active CO2 injection sites.
- **Horner Plots** — pressure-transient analysis on shut-in data, estimating reservoir permeability.
- **Hall Plots** — injection-well performance analysis from cumulative pressure vs. cumulative injected volume.

## Resolution Visualizer

Shows the data-collection frequency (resolution) of a well's SCADA sensor readings, broken down by day and by sensor channel — a quick way to spot logging gaps or changes in sampling rate.

- Paginated well search across SCADA ID, well name, well ID and API number.
- Plotly line chart of resolution (data points ÷ 86,400 s) per day, one trace per channel (line/tubing/casing pressure, gas rate).
- Dashed reference lines at standard measurement intervals (15 s, 30 s, 1 min, 5 min, 15 min, 1–24 h) for easy comparison.

## Salt Water Injection

An **Infinite Reservoir Radial Pressure Propagation Calculator** that models how pressure spreads outward from an injection well into an assumed infinite, homogeneous aquifer using the Theis equation, `ΔP = (ρ·g·Q / 4πT)·E₁(u)`, with the exponential integral evaluated via `scipy.special.exp1`.

- Configurable storativity and transmissivity, each derived from rock/fluid properties or supplied directly via an override.
- Point-pressure readout plus four visualizations: pressure-vs-distance, pressure-vs-time, a distance×time contour, and a spatial plan-view (top-down) map.
- Downloadable CSV of the spatial pressure matrix; all inputs converted to SI internally and reported in both psi and Pa.

## Well Communication

Detects potential pressure communication between wells by correlating their detrended gas-production residuals, exposed through three sub-applications: **Map Selection Analysis** (pick wells on an interactive map and run all pairwise correlations), **Trend Production Analysis** (inspect a single well's decomposition), and **Well Pair Analysis** (compare two wells by well ID).

- 7-day centered rolling-median smoothing of daily production.
- Reciprocal decline-curve trend fit (starting 365 days after first production) to isolate residuals.
- Pairwise Pearson correlation with a minimum of 365 overlapping observations; high positive correlation flags likely interference.

## Critical Rate Sensitivities

Calculates the minimum gas flow rate needed to lift liquids out of a wellbore (preventing liquid loading), across three modes: an interactive **Default** sensitivity view, a batch **CRS Report**, and a single-well **Report Preview**.

- 2D contour plots of critical rate over a pressure grid versus a chosen sensitivity variable (inclination, specific gravity, bottomhole temperature, or surface tension).
- Turner, Coleman, and Belfroid-Coleman (TNO-Shell, inclination-corrected) velocity models; tubing, casing, or annulus flow paths.
- Batch report fans out **Lambda** functions in parallel across all wells and writes results to S3, with an optional probe point and CSV export.

## CO2 Runtime History

A real-time sensor dashboard for the active CO2 injection sites, remapping raw SCADA tags to human-readable fields.

- Interactive Plotly WebGL chart with four independent stacked Y-axes (temperature, casing pressure, pressure, mass flow rate); legend groups toggle whole sensor categories.
- Adaptive resampling (1 min → 1 day) once a date range grows large, to keep charts interactive, with the active resolution shown above the plot.
- Data-quality warnings for stale sensor fields and a CSV export of the resampled series.

## Horner Plots

Performs pressure-transient analysis on well shut-in data: it auto-detects pressure-drop events, fits a Horner regression, and estimates reservoir permeability.

- CSV upload (resampled to 1-minute data) or S3 source, with automatic drop detection by configurable duration/magnitude thresholds.
- Timeseries view with adjustable baseline / shut-in-start / shut-in-end markers for fine-tuning on 1-minute data.
- Robust **HuberRegressor** fit of `bhp` vs `ln(t/Δt)` extrapolated to infinite shut-in time, yielding slope, perm-thickness (`kh = 162.6·q/m`), and permeability estimate.

## Hall Plots

Analyzes injection-well performance via the Hall method — cumulative pressure differential vs. cumulative injected volume — where slope changes reveal injectivity decline or improvement over time.

- CSV upload or direct S3 load of the CO2 runtime-history parquet; data resampled to daily averages with forward/backward fill.
- Configurable flowing-pressure column, assumed reservoir pressure (Pe), tangent window (n_days), and analysis start date.
- Plotly scatter of cumulative ΔP vs. cumulative flow with a fitted tangent line and shaded slope window; rising slope indicates declining injectivity (potential formation damage).

## Design decisions & trade-offs

- **One multi-page Streamlit app** instead of a separate app per tool — shared sidebar navigation, a single deployment to maintain, and a consistent UX across the whole toolkit.
- **Read-on-demand S3 parquet by well ID** rather than a pre-built cache or index — prioritizes data freshness and low storage cost over the marginal latency a cache would save.
- **Parallel Lambda fan-out for batch reports** (Critical Rate Sensitivities, Gas Injection) instead of synchronous computation — handles per-well parallelization at fleet scale without blocking the interactive app.
- **Robust HuberRegressor for Horner-plot fitting** rather than ordinary least squares — tolerates outliers in noisy pressure-transient data for more reliable permeability estimates.

## Architecture

All tools run inside **one** containerized Streamlit application using Streamlit's multi-page architecture — each tool is a numbered page in the sidebar — deployed to **AWS ECS Fargate**. Per-well production, injection and sensor data is stored in **S3** as parquet and read on demand by well ID; batch report generation (Critical Rate Sensitivities, Gas Injection) fans out across **parallel Lambda** functions that write results back to S3, and operator decisions persist in **DynamoDB**. Numerical work is done with **Pandas / NumPy / SciPy** (exponential integral, robust regression) and **Plotly** for interactive visualization, drawing on shared in-house engineering libraries (PVT, critical-rate and reservoir calculations). Infrastructure is managed with **Pulumi**, packaged with **Docker**, and shipped through **GitHub Actions** CI/CD. In-app user documentation is built and served with **MkDocs**.

> _Note: Screenshots and internal application URLs are omitted, as they display proprietary client data. Available on request, subject to client approval._
