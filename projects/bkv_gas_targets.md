---
title: Gas Targets App (React/FastAPI)
description: Web application that generates and sets monthly gas-production targets for every well.
image_url: ./images/covers/gas_targets.png
image_url_global: https://raw.githubusercontent.com/manolosolalinde/cv/main/projects/images/covers/gas_targets.png
date: 2026-02-01
order: 1
technologies: Python, JavaScript, React, Redux, FastAPI, SQLAlchemy, PostgreSQL, Amazon Redshift, AWS (App Runner, Lambda, SQS, RDS, VPC, ECR, IAM, Elastic IP), Pulumi, Docker, Docker Compose, GitHub Actions, Azure AD, Pandas, Plotly.js, MkDocs.
category: Full Stack
---

# Gas Targets App (React/FastAPI) - BKV Corporation

Software Engineer/Developer: Manuel Solalinde [(manolosolalinde@gmail.com)](mailto:manolosolalinde@gmail.com)

A full-stack web application that helps reservoir and production engineers **generate the monthly gas-production targets for every well**. It combines an interpolation/trend tool purpose-built for this task with guided manual review of the edge cases, then exports the finalized targets as the operator CSV consumed downstream. *(This page documents the **v2.1.0** architecture — a React frontend with a FastAPI backend on AWS App Runner — since superseded by a unified Streamlit redesign on ECS Fargate.)* The heavy lifting — reading raw production history from the corporate data warehouse and fitting a trend per well — runs as a **parallel, queue-driven Lambda fan-out**, so an engineer can process the entire well set in a single analysis.

## Overview

Each month an engineer creates an **analysis** (defined by its start/end date) and walks it through a four-stage workflow in the app. The application loads the analysis data from the corporate **Amazon Redshift** warehouse into a private working database, generates a production trend for every well in parallel, then surfaces two case-study reviews so the engineer can spot wells that need manual overrides before the final targets are exported.

## Workflow

The user flow is organized as a set of sequential tabs:

- **Database control** — start/stop the RDS working-database instance on demand, so the database only runs (and only bills) while an analysis is in progress.
- **Analysis selection** — create a new analysis (the start/end dates form its ID), load an existing one, or delete one to reset its trends and overrides.
- **Update DB & Generate Trends** — two one-time-per-analysis operations: *Update DB* pulls header, raw production, and restim data from Redshift into the working DB; *Generate Trends* fans out one job per well to compute its trend. Both run asynchronously and report live status, well counts, and any wells that errored.
- **Overrides & Well Review** — two case studies flag wells that need attention: a *Last-7-days production review* (wells producing in the recent window) and a *Trend review* (wells whose computed trend disagrees with their producing status). The engineer reviews each flagged well's timeseries — production vs. forecast, target, and budget — and uploads an Excel overrides sheet (well ID, code, override volume, comments) that is immediately reflected back in the review tables.
- **Download final output** — export the finalized monthly gas-targets operator CSV, with all manual overrides applied.

## Architecture

The system is a containerized, cloud-native stack provisioned entirely as code with **Pulumi**:

- **Frontend** — a **React** (Redux) single-page app served by an **AWS App Runner** service, authenticated through **Azure AD**, talking to the backend over the internet.
- **Backend** — a **Python / FastAPI** API on a second **App Runner** service. It reaches the working database through a **VPC connector** and pushes work onto **SQS** using IAM authentication.
- **Worker** — a **Lambda** function triggered by SQS messages. It reads production data from the cross-account **Amazon Redshift** warehouse (by assuming a role in the Redshift account) and reads/writes the working database. Both the backend and the Lambda are given Elastic IPs for outbound internet access.
- **Data** — a **PostgreSQL RDS** instance inside a dedicated VPC (two subnets across availability zones) holds the per-analysis header, raw, restim, trends, and overrides tables.
- **Queue** — an **SQS** queue decouples the API from the workers and is the trigger that drives the parallel fan-out.

The asynchronous operations follow a consistent pattern: the frontend calls a backend endpoint (`/update_db`, `/generate_trends`), then polls `/get_state` until the work reports `finished`. The backend enqueues one SQS message per unit of work (per table for the DB update, per well for trend generation); each message triggers an independent Lambda invocation, and a `trend_invocation` table tracks per-well status so the state endpoint knows when the whole batch is complete.

## CI/CD & Local Development

- **Deployment** — automated with **GitHub Actions**, which runs the backend test suite, builds Docker images for the frontend, backend, and Lambda, pushes them to **Amazon ECR**, then updates the App Runner / Lambda services.
- **Local environment** — a `docker compose` stack runs the frontend, backend, database, and Lambda together on a developer machine. Because the local environment can't reach Redshift or SQS, the warehouse reads are **mocked** and the backend **invokes the Lambda directly** instead of going through the queue — reproducing the production data flow without the cloud dependencies.

> _Note: Screenshots and architecture diagrams are omitted, as they display proprietary client data and systems. Available on request, subject to client approval._
