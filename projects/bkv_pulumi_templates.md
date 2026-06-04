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

An internal **infrastructure-as-code library** that standardizes how the data and engineering teams ship containerized applications to AWS. Instead of each project re-implementing networking, authentication, load balancing and CI/CD from scratch, every app starts from a small set of reusable building blocks and ready-made scaffolding — so a new app is deployable in minutes rather than rebuilt from the ground up. It eliminates per-project re-implementation of the same infrastructure and is the deployment foundation behind **6+ production apps**: Surveillance Dashboard, Gas Targets, Gas Injection, Plunger Optimization, AI Agent Chat, and the broader Streamlit toolkit.

## What it provides

- **A single application-stack component** — one declaration provisions a complete, production-ready ECS Fargate application end to end: container registry (ECR) with Docker build and push, an Application Load Balancer fronted by **corporate SSO (Azure AD OIDC)**, DNS and TLS (Route53 + ACM), WAF, scoped IAM, centralized logging (CloudWatch), and target-tracking autoscaling. The whole library is implemented as reusable Pulumi **ComponentResources**, so apps assemble infrastructure from typed, parameterized parts rather than hand-wiring resources.
- **Project scaffolding** — generates a new, immediately deployable project pre-wired to the library and to CI/CD: GitHub Actions run `pulumi preview` on every pull request and `pulumi up` on merge, so every scaffolded app ships with preview-on-PR and deploy-on-merge from day one.

## Design decisions & trade-offs

- **One orchestrator over many loose components** — a single top-level application-stack component composes the underlying pieces instead of asking each project to wire them together by hand. This reduces parameter explosion and enforces consistency across apps.
- **Composable add-ons over a monolithic template** — analytics integrations attach to an existing application stack rather than baking every integration into one template. Teams adopt features gradually, without rewriting the base deployment.
- **Consume shared infrastructure, don't redeclare it** — applications consume the shared base network (VPC, subnets, ECS cluster, WAF) through a stack-reference pattern instead of re-creating it. One owner manages the base network; apps simply reference it.
- **Dual-path corporate auth** — SSO at the load balancer (Azure AD OIDC) governs *app access*, while SAML federation governs *analytics query access*. Keeping these as separate identities lets app sign-in and data-query permissions evolve independently.

## Hard problems solved

- **Standardized enterprise authentication for every app** — corporate SSO (Azure AD OIDC) at the ingress plus SAML-federated analytics access, so every app gets enterprise sign-in essentially for free instead of reinventing auth each time.
- **Least-privilege cross-account data access** — secure, scoped access into a central Redshift data warehouse living in a separate account, granted through an assumable role rather than broad, shared credentials.
- **Reusable multi-environment deployments** — the same code yields `dev`, `stage`, and `prod` environments, with secrets sourced at runtime from Pulumi secrets and AWS Secrets Manager and never placed in the codebase.
- **Consistent tagging and naming at scale** — a uniform, predictable scheme for naming and tagging every resource so cost allocation and ownership tracking stay reliable across a growing fleet of apps.

## Key Features

- **One-command application stack** — a single application-stack component provisions ECR, ALB, DNS, certificates, WAF, IAM, logging, the Fargate service, and autoscaling.
- **Corporate SSO built in** — Azure AD OIDC at the load balancer for app access, and SAML federation for analytics query access.
- **Reusable and multi-environment** — components are parameterized and environment-scoped, so the same code deploys `dev`, `stage`, and `prod`.
- **Standardized CI/CD** — scaffolded projects ship with GitHub Actions preview-on-PR and deploy-on-merge workflows.
- **Secrets-safe by design** — secret values flow through Pulumi secrets and AWS Secrets Manager, never the codebase.
- **Composable add-ons** — Athena and Redshift integrations attach to an existing application stack without rewriting it.
