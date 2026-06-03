---
title: BKV Pulumi Templates
description: An internal Pulumi component library and project scaffolding that standardizes deployment of containerized apps on AWS ECS Fargate with Azure AD auth, autoscaling, and Athena/Redshift integrations.
image_url: ./images/covers/pulumi_templates.png
image_url_global: https://raw.githubusercontent.com/manolosolalinde/cv/main/projects/images/covers/pulumi_templates.png
date: 2026-05-31
order: 1
technologies: Python, Pulumi, AWS (ECS Fargate, ALB, ECR, Route53, ACM, WAF, CloudWatch, IAM, S3, Athena, Glue, Redshift, Secrets Manager), Azure AD (OIDC + SAML SSO), Docker, GitHub Actions.
category: Cloud Infrastructure / DevOps
---

# BKV Pulumi Templates - BKV Corporation

Developer: Manuel Solalinde [(manolosolalinde@gmail.com)](mailto:manolosolalinde@gmail.com)

An internal **infrastructure-as-code library** that standardizes how the data and engineering teams ship containerized applications to AWS. Instead of each project re-implementing networking, authentication, load balancing and CI/CD from scratch, every app composes a small set of reusable **Pulumi components** and starts from a ready-made project template. It is the deployment foundation behind the team's Streamlit and full-stack apps (Surveillance Dashboard, Gas Targets, Gas Injection, Plunger Optimization, AI Agent Chat, and the broader Streamlit toolkit).

## Overview

The repository is split into two parts:

- **`bkv_pulumi_templates`** — a pip-installable Python library of reusable Pulumi components. One top-level component, `ECSApplicationStack`, provisions a complete, production-ready ECS Fargate application; optional add-ons wire up Athena and Redshift access.
- **`bkv_pulumi_project_templates`** — project scaffolding (`bkv-ecs-aws-python`) that generates a new Pulumi project pre-wired to the library, including config scripts and GitHub Actions workflows, so a new app is deployable in minutes.

A standalone Claude Code skill ships alongside the library to scaffold and modify projects, encapsulating the full parameter reference and common modification patterns.

## Library Components

- **`ECSApplicationStack`** — the top-level orchestrator. Composes three sub-stacks into a single deployable application:
  - **RepositoryStack** — ECR repository plus Docker image build and push.
  - **LoadBalancerStack** — ACM certificate, Application Load Balancer with **Azure AD (OIDC)** authentication, Route53 DNS record, and WAF.
  - **ECSFargateStack** — IAM task role, security group, CloudWatch log group, Fargate service, and target-tracking autoscaling (CPU or memory).
- **`AthenaStack`** — adds Athena access with **Azure AD SAML SSO** federation: SAML identity provider, federated read role, Athena database/workgroup over the app's S3 bucket, and the IAM policies tying it to the ECS task role.
- **`RedshiftAccessSetup`** — cross-account Redshift wiring, creating an assumable role in the data-warehouse account and granting the ECS task role scoped `redshift-data` access.
- **ECS IAM helpers** — small functions to attach common S3-bucket and CloudWatch Logs policies to a task role after stack creation.

## Project Templates

The `bkv-ecs-aws-python` template scaffolds a complete, deployable project:

- `__main__.py` showing the canonical usage pattern, with `src/base_config.py` parsing Pulumi stack config into typed `*StackArgs` objects.
- `config_yaml.sh` — an automated configuration script that sets all required Pulumi config values for a new stack.
- `.github/workflows/` — `preview.yaml` (runs `pulumi preview` on PRs) and `deploy_pulumi.yaml` (runs `pulumi up` on merge), giving every scaffolded project CI/CD out of the box.
- `destroy_and_recreate.sh` and a curated `.gitignore`.

## Architecture

Every component follows a consistent, composable pattern: a `*StackArgs` dataclass holds configuration, a `*Stack` class extends `pulumi.ComponentResource`, child resources are created with `ResourceOptions(parent=self)` for correct parent–child tracking, and tags are propagated through the entire hierarchy. Shared network infrastructure (VPC, subnets, ECS cluster, WAF) is consumed through a `MicroAppBaseStackReference` wrapper around `pulumi.StackReference`, so applications never re-declare the base network — they reference it.

Resources follow a uniform `{app_name}-{environment}-{resource-type}` naming convention, secrets are never hardcoded (sourced from Pulumi secrets or AWS Secrets Manager ARNs injected as container environment variables), and stacks map to environments (`prod`, `stage`, `dev`).

## Key Features

- **One-command application stack** — a single `ECSApplicationStack` provisions ECR, ALB, DNS, certificates, WAF, IAM, logging, the Fargate service, and autoscaling.
- **Corporate SSO built in** — Azure AD OIDC at the load balancer for app access, and Azure AD SAML SSO federation for Athena query access.
- **Reusable and multi-environment** — components are parameterized and environment-scoped, so the same code deploys `dev`, `stage`, and `prod` stacks.
- **Standardized CI/CD** — scaffolded projects ship with GitHub Actions preview-on-PR and deploy-on-merge workflows.
- **Secrets-safe by design** — secret values flow through Pulumi secrets and Secrets Manager, never the codebase.
- **Composable add-ons** — Athena and Redshift integrations attach to an existing application stack without rewriting it.
