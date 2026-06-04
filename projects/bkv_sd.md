---
title: Surveillance Dashboard
description: Full-stack web platform for real-time visualization and analysis of gas-well sensor and production data.
image_url: ./images/covers/surveillance.png
image_url_global: https://raw.githubusercontent.com/manolosolalinde/cv/main/projects/images/covers/surveillance.png
date: 2023-12-01
order: 1
technologies: Python, FastAPI, React 17, Redux, JavaScript, Plotly, DuckDB, PostgreSQL, AWS (ECS Fargate, App Runner, Lambda, S3, RDS, ECR, EventBridge), Azure AD / MSAL, Docker, GitHub Actions, Parquet, ArcGIS, PWA / Service Workers, Pytest, HTML/CSS.
category: Full Stack Development
---

# Surveillance Dashboard - BKV Corporation

Full Stack Developer: Manuel Solalinde [(manolosolalinde@gmail.com)](mailto:manolosolalinde@gmail.com)

A full-stack web platform that lets production and petroleum engineers visualize, analyze, and annotate real-time data from gas wells. It brings high-frequency sensor readings (pressures, flow rates, temperatures and other UDCs), daily production volumes, and engineering-calculation plots together in a single interface — replacing slower custom Power BI reports and delivering a far more responsive, interactive experience.

The system is a React + Redux single-page application backed by a FastAPI service, secured by corporate Azure AD single sign-on, and deployed on AWS. It reads high-frequency and daily data from S3 parquet files (queried and resampled on the fly with DuckDB) and stores comments, saved well groups, and usage logs in PostgreSQL.

## Applications

The platform is organized as a portal of focused sub-applications, all sharing a common **left-pane settings / right-pane interactive plot** layout:

- **Single Well Surveillance** — study one well in depth, plotting multiple sensors/UDCs over a chosen time range.
- **Multi Well Surveillance** — compare one sensor type across many wells as color-coded overlaid lines.
- **Daily Production & Engineering Plots** — daily gas/oil/water volumes and engineering-calculation charts (including material-balance-time).
- **Admin Dashboard** — usage analytics and API-call log summaries, restricted to administrators.

#### Single Well Surveillance

Visualizes high-frequency time-series sensor data for a single well. The engineer selects a facility/well (from a list or directly on an interactive ArcGIS map), picks one or more sensors (UDCs) and a time range, and reads an interactive Plotly chart. Comments and annotations can be added directly on the data to flag events or share observations with teammates.

#### Multi Well Surveillance

Overlays a single UDC/sensor across many wells on one chart, each well a differently colored line — ideal for portfolio-level checks such as spotting underperformers, confirming a fleet-wide trend, or finding the odd well out. Selection is capped (max 5 wells, 2 sensors) to keep responses fast.

#### Daily Production & Engineering Plots

Displays daily production volumes (gas, oil, water) and engineering-calculation plots for selected facilities, with a toggle between the two plot types. Engineering plots include a material-balance-time chart and other calculation-based views.

#### Portal & Admin

The **Portal** is the landing hub — a grid of cards linking to each application. The **Admin Dashboard** surfaces usage statistics and API-call logs, with role-based admin access enforced on the backend.

## Architecture

The application runs on a stateless AWS architecture: the FastAPI backend on **ECS Fargate**, the React frontend on **App Runner**, with a **Lambda** DB-updater on a daily **EventBridge** schedule.

**How it fits together:**

- Container images for the backend, frontend, and Lambda DB-updater are published to **Amazon ECR**; App Runner serves the frontend and ECS Fargate runs the stateless backend.
- The backend reaches **RDS PostgreSQL** (via a VPC connector) and **S3** (via IAM authentication) for state and analytics data; the **Azure AD (MSAL)**-authenticated frontend reaches data only through the backend.
- A daily **EventBridge** rule triggers the **Lambda** DB-updater, which refreshes the database from the latest S3 data.

**Data sources:** PostgreSQL (comments, saved well groups, API-call logs, a wells reference table), S3 parquet (high-frequency sensor data, daily production data, external comments), **DuckDB** (on-the-fly querying and resampling of the parquet data), and the ArcGIS API (short-lived map tokens). All API endpoints except the health check require an Azure AD bearer token, enforced by a `@requires_auth` decorator.

**CI/CD:** Deployments are automated with GitHub Actions, which builds and pushes the Docker images, runs the backend test suite, and updates the AWS services.

## Design decisions & trade-offs

- **React + Redux SPA over server-rendered reports** — a single-page application was chosen to deliver the responsive, interactive experience that the previous Power BI reports could not, with client-side state driving fast view switching.
- **DuckDB on parquet, queried on the fly** — rather than pre-computing and storing every possible view, DuckDB queries and resamples S3 parquet at request time, keeping data fresh and storage requirements low.
- **Split storage by purpose** — S3 parquet for analytical time-series data and PostgreSQL for application state (comments, saved well groups, logs), matching each store to its access pattern.
- **Capped multi-well selection** — limiting multi-well plots (5 wells / 2 sensors) is a deliberate latency-vs-scope trade-off, keeping responses fast for the common case rather than optimizing for unbounded comparisons.

## Performance & Reliability Engineering

A significant share of the work focused on making large time-series payloads fast and the service resilient under load:

- **Memory optimization** — switched string columns to categorical types and `float64` to `float32`, substantially reducing the backend's memory footprint; guided by `tracemalloc` / `memory_profiler` profiling.
- **Faster serialization** — replaced `jsonable_encoder` with `ORJSONResponse`, cutting response times for large engineering-data payloads.
- **Parallel I/O** — multi-threaded S3 parquet reads (`ThreadPoolExecutor`) for multi-well requests, improving throughput on multi-core hosts.
- **Concurrency control** — a middleware returns `429 Too Many Requests` past a configurable limit, with the frontend showing a "server busy" message instead of failing silently.
- **Resilient frontend** — a PWA service worker provides offline handling and a maintenance page when the backend is unreachable; well selection uses infinite scroll (capped at 500 displayed wells) for snappy navigation.
- **Tested** — Pytest backend suite (including endpoint security tests) runs in CI on every tagged deploy.

> _Note: Screenshots and architecture diagrams are omitted, as they display proprietary client data and systems. Available on request, subject to client approval._
