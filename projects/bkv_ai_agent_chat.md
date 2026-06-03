---
title: AI Agent Chat
description: Full-stack conversational AI agent that answers oil & gas operational questions over corporate well data and internal documentation.
image_url: ./images/covers/agent.png
image_url_global: https://raw.githubusercontent.com/manolosolalinde/cv/main/projects/images/covers/agent.png
date: 2026-05-18
order: 1
technologies: Python, FastAPI, TypeScript, React, Vite, Tailwind CSS, shadcn/ui, Amazon Bedrock AgentCore (Runtime, Gateway, Memory, Code Interpreter), Strands Agents, LangGraph, Claude Agent SDK, AWS (ECS Fargate, ALB, Lambda, DynamoDB, SSM, Cognito), Pulumi, Docker, Nginx, Microsoft Entra ID, Server-Sent Events.
category: Full Stack
---

# AI Agent Chat - BKV Corporation

Software Engineer/Developer: Manuel Solalinde [(manolosolalinde@gmail.com)](mailto:manolosolalinde@gmail.com)

A full-stack **conversational AI agent** that lets reservoir, production, and operations staff ask natural-language questions about the company's wells and get grounded, tool-backed answers. The agent reasons over the corporate **well database**, searches internal documentation, browses the web, and runs Python in a sandbox — streaming each step (tool calls, intermediate results, and the final answer) back to the user in real time. It is built on **Amazon Bedrock AgentCore** and was forked and substantially extended from AWS Labs' fullstack AgentCore solution template (FAST).

## Overview

A user opens the chat, asks a question in plain English (e.g. *"find all wells spud in 2026"* or *"when was the last time the bumper spring was pulled on this well?"*), and the agent decides which tools to call to answer it. The model writes and runs read-only SQL against the corporate well-data warehouse, looks up table/column documentation, retrieves internal datadocs, searches the web, or executes Python — then synthesizes a cited answer. Conversations are persisted with searchable history, auto-generated titles, and per-message feedback, so the tool behaves like an internal ChatGPT scoped to the company's own operational data.

## Applications

- **Natural-language data access** — engineers query well headers, production, directional surveys, stimulation stages, and more without writing SQL themselves; the agent translates intent into validated read-only queries and explains its results.
- **Operational Q&A** — answers grounded questions about specific wells, pads, and JV/GU units, citing the rows and documents it used.
- **Internal knowledge retrieval** — hybrid (embedding + keyword) search over the company's internal documentation index, with full-document fetch.
- **Web research & code analysis** — on-demand web search/fetch and a secure Python sandbox for ad-hoc computation, all inside the same conversation.

## Architecture

A containerized, cloud-native stack on AWS, provisioned entirely as code with **Pulumi (Python)**:

- **Frontend** — a **React 19 + TypeScript** single-page app (Vite, Tailwind CSS 4, shadcn/ui) served by **Nginx** on **ECS Fargate** behind an **Application Load Balancer**. A custom AgentCore streaming client parses Server-Sent Events to render tool calls, inputs, and results live as the agent works.
- **Backend API** — a **FastAPI** service handling conversations, feedback, dynamic runtime config, and the agent proxy.
- **Agent Runtime** — a containerized agent on **Bedrock AgentCore Runtime** (model: Claude Sonnet 4.5). The codebase ships **four interchangeable agent patterns** — Strands Agents (primary), LangGraph, and the Claude Agent SDK in both single- and multi-agent (Opus-orchestrates-Sonnet) configurations — selectable without touching the rest of the stack.
- **Tools via Gateway** — Lambda-backed tools exposed over the **AgentCore Gateway** (MCP protocol): read-only SQL execution against the corporate well database, well-database table/column documentation lookup, internal datadocs hybrid search and retrieval, web search and page extraction, plus a Bedrock **Code Interpreter** sandbox.
- **Memory** — **AgentCore Memory** provides session-scoped, persistent conversation history.
- **Data** — **DynamoDB** stores conversations and feedback; **SSM Parameter Store** holds runtime ARNs and config.

## Authentication

Two distinct auth paths keep user and service identities separate:

- **User auth** — users sign in through **Microsoft Entra ID (OIDC)**, handled at the **ALB**, which injects the Entra access token downstream; the same token is forwarded to the Runtime and validated by a JWT authorizer.
- **Machine-to-machine** — the Runtime authenticates to the Gateway as a service using **Cognito** OAuth2 client-credentials, with AgentCore Identity managing token retrieval — no user credentials ever cross that boundary.

## CI/CD & Local Development

- **Two deployment paths** — infrastructure, frontend, backend, and Gateway tools deploy via **Pulumi** (`pulumi up`), while agent code (system prompt, model, agent logic) deploys independently through the **AgentCore CLI** (`agentcore deploy`) which builds the agent container via CodeBuild.
- **Local environment** — a `docker compose` stack runs the frontend, backend API, and agent together on a developer machine. A local-agent mode mocks authentication (no OIDC popup) and sources AWS credentials from the host profile, so the full chat flow can be exercised without deploying.

> _Note: Screenshots and internal application URLs are omitted, as they display proprietary client data. Available on request, subject to client approval._
