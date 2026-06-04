---
title: Gas Injection Optimization App
description: Data-driven app that recommends optimal gas-injection rates for gas-lift wells.
image_url: ./images/covers/gas_injection.png
image_url_global: https://raw.githubusercontent.com/manolosolalinde/cv/main/projects/images/covers/gas_injection.png
date: 2026-02-01
order: 1
technologies: Python, Streamlit, Pandas, NumPy, Scikit-learn (DecisionTreeRegressor clustering), scikit-optimize (Bayesian optimization), Plotly, AWS (S3, Lambda, DynamoDB), Parquet, Jupyter, MkDocs.
category: Data Science Development
---

# Gas Injection Optimization App - BKV Corporation

Data Scientist/Developer: Manuel Solalinde [(manolosolalinde@gmail.com)](mailto:manolosolalinde@gmail.com)

On gas-lift wells, operators routinely over- or under-inject gas, leaving production on the table or wasting injection. This production data-analytics platform helps reservoir and production engineers **right-size gas injection on gas-lift wells**: for each well it turns noisy daily production and injection history into a single recommended injection rate, produced by a data-driven model trained against engineer-labeled data. On top of the per-well recommendation it generates the report emailed to operators, ranking every injecting well by how far it has drifted from its recommendation — contributing to a measurable improvement in net sales.

> _Note: In production use, the tool flagged over-injecting wells and guided operators to reduce injection, contributing to a measurable improvement in net sales. Specific production and financial figures are confidential client data and are omitted._

## Applications

The platform bundles five sub-applications, selected from a dropdown:

- **Gas Injection Estimator** *(production)* — interactive, single-well analysis. Shows the well's full timeseries, the model's cluster analysis, and the recommended injection rate.
- **Gas Injection Report** *(production)* — the report emailed to operators, ranking every injection well by how far current injection deviates from the recommendation. Regenerates on demand via a parallel Lambda fan-out.
- **Gas Injection Report History** *(production)* — tracks which wells were flagged across all historical reports, counts consecutive flags, and surfaces wells that have since resolved.
- **Gas Injection Report Preview** *(research)* — single-well report generator for testing and validating the per-well computation on demand.
- **Gas Injection Labeler** *(research)* — manual annotation tool used to build the training data behind the model's penalty weights.

## The Recommendation Model

The core of the app is a model that converts a well's daily history into one injection recommendation. Rather than a closed-form physics calculation, it groups the history into stable operating regimes and scores them. The pipeline:

1. **Clean** — drop shut-in-extended days to remove transient recovery noise.
2. **Cluster** — fit a `DecisionTreeRegressor(criterion="absolute_error")` to injection rate versus time, segmenting the history into stretches that each held a roughly constant injection target; adjacent similar segments are merged into a **cluster**.
3. **Aggregate** — compute per-cluster statistics: mean injection/production, stability ratios, production trend, net production-minus-injection, and more.
4. **Filter** — discard unreliable clusters (too little injection, too few days, or excessive variance).
5. **Score** — each surviving cluster gets a penalty (lower is better) combining a production penalty, a production-minus-injection efficiency penalty, an injection-stability penalty, and (optionally) production-volatility and trend penalties.
6. **Recommend** — invert the score and select the best-ranked cluster; its mean injection target becomes the recommendation.

The penalty weights are the only part of the recommendation learned from data — see below.

## Model Training (data-driven weights)

The penalty weights are fitted **offline** against ground truth collected with the Labeler:

- **Ground truth** — a set of usable wells, each labeled by an engineer with their chosen optimal injection rate.
- **Feature cache** — a notebook runs the exact same clustering pipeline the live app uses and caches each well's cluster table, with diagnostics confirming the clustering almost always produces a good candidate, so the weights' only job is to **pick the right cluster**.
- **Objective** — a custom loss that primarily minimizes the share of wells missed beyond a tolerance, with light elastic-net (L1 + L2) regularization on the weights.
- **Optimization** — a train/test split and **Bayesian optimization** (`skopt.gp_minimize`, a Gaussian-process surrogate) in a coordinate stage followed by a joint refinement.

> _Note: Specific tuned weight values, well counts and model accuracy figures are derived from proprietary client data and are omitted._

## Design decisions & trade-offs

- **Data-driven penalty weights over a closed-form physics calculation.** Engineers can label ground-truth optimal rates, and the clustering pipeline already surfaces a good candidate cluster, so the learned weights only have to **pick the right one** — a far easier and more robust problem than modeling the physics directly.
- **`DecisionTreeRegressor` clustering of injection-rate-versus-time.** This segments history into stretches of roughly constant injection target, matching how operators actually think about a well rather than imposing an arbitrary windowing.

## Hard problems solved

- **Custom training objective.** A loss that primarily minimizes the share of wells whose recommendation is missed beyond a tolerance, with light elastic-net (L1 + L2) regularization on the weights to keep the solution simple and generalizable.
- **Bayesian optimization over a train/test split.** A Gaussian-process surrogate (`skopt.gp_minimize`) tunes the weights in a coordinate stage followed by a joint refinement, avoiding overfitting to the labeled set.
- **Train/inference parity.** A shared engineering library is imported by **both** the live app and the offline training notebooks, guaranteeing the trained weights are evaluated against the exact pipeline that runs in production.

## Report

The Gas Injection Report ranks every injecting well by the difference between its recent injection and its recommendation (using the operator's saved decision as the baseline if one exists, else the model recommendation). Regeneration fans out **Lambda** functions in parallel to recompute every well's metrics and uploads the results to **S3**. Three views are available: an email-ready **CSV view**, a fully filterable **Research view** (GLR, production and injection thresholds, route, minimum delta), and an unfiltered **Raw view**. Engineers can override the model for any well from the sidebar; **operator decisions are stored in DynamoDB** and replace the recommendation as the baseline across all views.

## Architecture

Python + **Streamlit** web app with **Plotly** visualization. Per-well daily production and injection data lives in **AWS S3** as parquet, read on demand. The report regenerates through a **parallel Lambda fan-out**; operator overrides persist in **DynamoDB**. The recommendation logic lives in a shared engineering library imported by **both** the live app and the offline **Jupyter** training notebooks, guaranteeing the trained weights are evaluated against the exact pipeline that runs in production. User documentation is published with **MkDocs**.

> _Note: Screenshots are omitted, as they display proprietary client data. Available on request, subject to client approval._
