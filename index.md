---
layout: default
---

# Manuel Solalinde

_Software Developer - MSc. Applied Mathematics - Data Scientist_ <br><br>

[Email](mailto:manolosolalinde@gmail.com) / [CV](https://manolosolalinde.github.io/cv/) / [LinkedIn](https://www.linkedin.com/in/nestor-solalinde/) / [Github1](https://github.com/manolosolalinde/) / [Github2](https://github.com/manuelsolalindebkv/) / [Stackoverflow](https://stackoverflow.com/users/9831182/nestor-solalinde) / [Website](https://workwithmanu.com/) 

<br><br>

## 🏢 Work Experience

**Senior Software Engineer** - [BairesDev](https://www.bairesdev.com/) - May 2022 - present <br>
 - Full stack engineer on [TriformaIQ Real Estate Studio](https://www.triformaiq.com/), an AI-powered multi-tenant SaaS platform for commercial real estate. It combines GIS-based site selection with weighted multi-criteria scoring, entitlements, due diligence, document management and audit-ready records.
 - Built LLM-powered document analysis features using retrieval-augmented generation (RAG): document ingestion and chunking, vector embeddings and semantic search, structured LLM outputs grounded in source citations, and regression evaluation of prompt quality.
 - Implemented subscription billing and licensing: payment provider integration via webhooks, subscription lifecycle management, and plan-based feature gating.
 - Developed role-based approval workflows, per-user and per-organization rate limiting of third-party APIs, and geospatial data features with tenant data isolation.
 - Designed AI-assisted development workflows with Claude Code (custom skills and multi-agent orchestration) that automate ticket analysis, implementation, code review and end-to-end verification.
 - Involved in development of web applications and data science projects at BKV Corporation, focusing on creating intuitive surveillance dashboards and engineering tools. 
 - My role includes analyzing and interpreting extensive datasets, employing advanced methods to extract actionable insights
 - Technologies: Python, FastAPI, SQLModel, PostgreSQL/PostGIS, pgvector, Alembic, Celery, Redis, Docker, Anthropic API, Stripe, ESRI ArcGIS, Auth0, React, TypeScript, Pytest, Playwright.

**Senior Software Engineer** - [BKV Corporation](https://www.bkvcorp.com) - May 2022 - June 2026 <br>
 - Designed and developed machine learning applications for optimization of artificial lift systems.
 - Developed AI-powered applications leveraging large language models for event detection and data structuring in gas well operations.
 - Built web applications for real-time visualization, analysis, and processing of gas wells data, to facilitate insightful data interpretation and decision-making for engineers and managers.
 - Significantly enhanced the efficiency of existing data processing algorithms, achieving over 10x improvement in performance. This set of optimizations led to significant increase in the usage of related applications.
 - Developed templates and libraries, streamlining the process of creating new applications and reusing existing components.
 - Architected and implemented AWS Infrastructure Solutions. Development of robust libraries and templates for seamless deployment of infrastructure into AWS, leveraging advanced infrastructure as code techniques with pulumi.
 - Technologies: Python, Javascript, Fastapi, React, Azure AD, Plotly, Redux, Postgres SQL, AWS Cloud Computing Services, Nodejs, HTML/CSS. Testing: Cypress, Jest (frontend), Pytest (backend).
 - Data Science libraries: scikit-learn, pandas, numpy, plotly, tensorflow, keras, streamlit.

<!-- SCE S.A. -->
<!-- - Full Stack Developer for Centralhub Search Engine Platform. A search engine platform based on web scraping automation of regional e-commerce sites. 
- Developer of a tool for converting dual fisheye camera videos to equirectangular stitched videos using NVIDIA CUDA, NVDEC, NVENC.
- Developer of a management system using Excel VBA and SQL.
- Backend developer of ecommerce sites
- Worked in a cross-functional, agile team to rebuild the SPR system for the Paraguayan National Secretary of Planning.
- Assistance with information architecture and UX writing for webapps -->

**Software Developer** - Self Employed / Independent Contractor - Jul 2017 - Jul 2022 <br>
 - Full Stack Developer for Centralhub Search Engine Platform. A search engine platform based on web scraping automation of regional e-commerce sites.
- Developer of a tool for converting dual fisheye camera videos to equirectangular stitched videos using NVIDIA CUDA, NVDEC, NVENC. 
- Developer of a management system using Excel VBA and SQL.
- Backend developer of ecommerce sites.
- Worked in a cross-functional, agile team to rebuild the SPR system for the Paraguayan National Secretary of Planning.
- Assistance with information architecture and UX writing for webapps.

<!-- 2011 - Mar 2013 · 2 yrs 3 mos2011 - Mar 2013 · 2 yrs 3 mos
Main developer for the ARTUR platform (C++ Language, VBA), used for the calculation and pre-dimensioning of hydraulic turbine structural component elements. Assisted in the development of design manuals that set the criteria for calculation and dimensioning of water turbine structural elements. -->

**Software Developer - Engineer** - [IMPSA](https://www.impsa.com/) - Mendoza, Argentina - Jan 2011 - Jul 2013 <br>
 - Lead Developer of the ARTUR platform (C++ Language), used for the calculation and pre-dimensioning of hydraulic turbine structural component elements. 
 - Assisted in the development of design manuals that set the criteria for calculation and dimensioning of water turbine structural elements.

<br>

## 💻 Projects

**TriformaIQ Real Estate Studio** - [project details](./projects/triformaiq.md) <br>
An AI-powered multi-tenant SaaS platform for commercial real estate that unifies site selection, entitlements, due diligence and audit-ready documentation.
 - _Client_: [TriformaIQ](https://www.triformaiq.com/) (via BairesDev)
 - _Focus_: Full Stack, AI/LLM Features, SaaS Infrastructure
 - _Key Features_:
   - LLM-powered document analysis with RAG: ingestion and chunking, vector embeddings and semantic search, citation-grounded structured outputs, and regression evaluation of prompt quality.
   - Subscription billing and licensing with webhook-driven lifecycle management and plan-based feature gating.
   - Role-based approval workflows, per-user and per-organization API rate limiting, and geospatial scoring features with strict tenant isolation.
   - AI-assisted engineering workflows with Claude Code (custom skills and multi-agent orchestration).
 - _Technologies_: Python, FastAPI, PostgreSQL/PostGIS, pgvector, Celery, Redis, Docker, LLMs, Stripe, ESRI ArcGIS, Auth0, React, TypeScript, Pytest, Playwright.

**AI Agent Chat** - [project details](./projects/bkv_ai_agent_chat.md) <br>
A full-stack conversational AI agent that answers oil & gas operational questions over the corporate well database and internal documentation, built on Amazon Bedrock AgentCore.
 - _Client_: BKV Corporation
 - _Focus_: Full Stack, AI Agents, Cloud Infrastructure
 - _Key Features_:
   - Natural-language to read-only SQL over the corporate well-data warehouse, with cited, tool-backed answers.
   - Real-time streaming (SSE) of tool calls, inputs, and results; persistent conversation history with auto-generated titles and feedback.
   - Gateway (MCP) tool suite: SQL + schema docs, internal datadocs hybrid search, web search/fetch, and a Python code interpreter.
   - Four interchangeable agent patterns (Strands, LangGraph, Claude Agent SDK single & multi-agent) on Bedrock AgentCore Runtime (Claude Sonnet 4.5).
   - React 19 SPA + FastAPI on ECS Fargate; Microsoft Entra ID (OIDC) user auth and Cognito M2M; provisioned as code with Pulumi.
 - _Technologies_: Python, FastAPI, TypeScript, React, Tailwind CSS, Amazon Bedrock AgentCore (Runtime, Gateway, Memory, Code Interpreter), Strands Agents, LangGraph, Claude Agent SDK, AWS (ECS Fargate, ALB, Lambda, DynamoDB, Cognito), Pulumi, Docker, Microsoft Entra ID.

 **Gas Injection Optimization App** - [project details](./projects/bkv_gas_injection.md) <br>
A data-driven application that recommends optimal gas-injection rates for gas-lift wells and ranks wells by how far each has drifted from its recommendation.
 - _Client_: BKV Corporation
 - _Focus_: Data Science
 - _Key Features_:
   - Recommendation model: history clustering (DecisionTreeRegressor) plus a per-cluster penalty score.
   - Data-driven penalty weights fitted against engineer-labeled wells via Bayesian optimization.
   - Report ranking wells by injection-vs-recommendation deviation, with operator overrides.
   - Parallel Lambda fan-out for on-demand report regeneration; per-well data in S3 (parquet).
 - _Impact_: Reduced over-injection on flagged wells, contributing to a dramatic improvement in net sales.
 - _Technologies_: Python, Streamlit, Pandas, NumPy, Scikit-learn, scikit-optimize, Plotly, AWS (S3, Lambda, DynamoDB), Pulumi, Parquet.

**Surveillance Dashboard Application** - [project details](./projects/bkv_sd.md) <br>
A set of web applications to visualize, analyze and process real time data from gas wells. Drastically improves performance over custom Power BI applications that serve similar purposes. Comprised of 3 sub applications: Single well, Multi well, Daily and Engineering Plots.
 - _Client_: BKV Corporation
 - _Focus_: Full Stack, Cloud Infrastructure, CI/CD
 - _Key Features_:
   - Azure AD authentication.
   - Support user comments on time series data.
   - Automatic data resampling for time series data.
   - Selection and filter of wells from lists or maps.
   - Multi well selection and data comparison.
   - Can add smoothing and indicators to time series data.
 - _Technologies_: Python, Javascript, Fastapi, React, Azure AD (Corporate authentication), Plotly, Redux, Postgres SQL, AWS Cloud Computing Services, HTML/CSS. Testing: Cypress, Jest (frontend), Pytest (backend).

**Gas Targets App** - [project details](./projects/bkv_gas_targets.md) <br>
A full-stack web application that generates and sets the monthly gas-production targets for every well, combining a purpose-built trend tool with guided manual review of edge cases.
 - _Client_: BKV Corporation
 - _Focus_: Full Stack, Cloud Infrastructure
 - _Key Features_:
   - Four-stage monthly workflow: analysis selection, DB update, trend generation, override review, and final CSV export.
   - Parallel, queue-driven Lambda fan-out (SQS) processing the full well set per analysis.
   - Reads raw production history from a cross-account Amazon Redshift warehouse into a private PostgreSQL working DB.
   - Case-study reviews (last-7-days production, trend review) with Excel-based engineer overrides.
   - Cloud-native stack provisioned as code (Pulumi); Dockerized services deployed to App Runner / Lambda via GitHub Actions and ECR.
 - _Technologies_: Python, JavaScript, React, Redux, FastAPI, PostgreSQL, Amazon Redshift, AWS (App Runner, Lambda, SQS, RDS, VPC, ECR), Pulumi, Docker, GitHub Actions, Azure AD, Plotly.js.

**Plunger Optimization App** - [project details](./projects/bkv_plunger_optimization.md) <br>
A data analytics platform to optimize and diagnose plunger-lift gas wells from real-time SCADA data, combining signal processing, ML classification and interactive visualization.
 - _Client_: BKV Corporation
 - _Focus_: Data Science, Full Stack
 - _Key Features_:
   - Interactive plunger-cycle analysis and stacked-cycle visualization (Streamlit + Plotly).
   - Automated diagnostic report suite (load-factor, pressure sustained-increase, data quality).
   - ML-based continuous-vs-conventional well classification.
   - Daily fleet-wide report generation on AWS (ECS Fargate, Lambda, S3, CloudWatch).
 - _Technologies_: Python, Streamlit, Pandas, NumPy, SciPy, Scikit-learn, Plotly, AWS (S3, ECS Fargate, Lambda, ECR), Pulumi, Docker, GitHub Actions.

**BKV Pulumi Templates** - [project details](./projects/bkv_pulumi_templates.md) <br>
An internal infrastructure-as-code library and project scaffolding that standardizes how the team deploys containerized applications to AWS ECS Fargate — the deployment foundation behind the client's applications.
 - _Client_: BKV Corporation
 - _Focus_: Cloud Infrastructure
 - _Key Features_:
   - Reusable `ECSApplicationStack` Pulumi component: ECR, ALB, Route53, ACM, WAF, IAM, CloudWatch, Fargate service, and autoscaling in one stack.
   - Corporate SSO built in — Azure AD (OIDC) at the load balancer and Azure AD SAML SSO federation for Athena access.
   - Composable add-ons for Athena and cross-account Redshift access.
   - `bkv-ecs-aws-python` project template with config scripts and GitHub Actions CI/CD (preview-on-PR, deploy-on-merge).
 - _Technologies_: Python, Pulumi, AWS (ECS Fargate, ALB, ECR, Route53, ACM, WAF, CloudWatch, IAM, S3, Athena, Glue, Redshift, Secrets Manager), Azure AD (OIDC + SAML SSO), Docker, GitHub Actions.

**BKV Streamlit Apps** - [project details](./projects/bkv_streamlit_apps.md) <br>
A multi-page Streamlit platform bundling a growing collection of reservoir and production engineering tools for gas wells, sharing one S3 parquet data pipeline and a single containerized ECS Fargate deployment.
 - _Client_: BKV Corporation
 - _Focus_: Data Science, Cloud Infrastructure
 - _Applications_:
   - Resolution Visualizer — visualizes SCADA sensor reading frequency per well, by day and channel.
   - Salt Water Injection — infinite-reservoir radial pressure-propagation calculator (Theis equation).
   - Well Communication — detects inter-well pressure interference from correlated production residuals.
   - Critical Rate Sensitivities — computes the minimum gas rate required to lift liquids out of the wellbore.
   - CO2 Runtime History — real-time sensor dashboard for the active CO2 injection sites.
   - Horner Plots — pressure-transient analysis on shut-in data, estimating reservoir permeability.
   - Hall Plots — injection-well performance from cumulative pressure vs. cumulative injected volume.
 - _Technologies_: Python, Streamlit, Plotly, Pandas, NumPy, SciPy, Scikit-learn, AWS (ECS Fargate, Lambda, S3, DynamoDB, ECR, CloudWatch, Bedrock), Pulumi, Docker, GitHub Actions, Parquet, MkDocs.


**Centralhub Search Engine** - [project details](./projects/centralhub.md) <br>
A search engine platform based on web scraping of local e-commerce sites.
 - _Focus_: Full Stack, Web Scraping
 - _Description_: A search engine platform based on web scraping automation of regional e-commerce sites. Consists of 5 sub-projects:
        1. An E-commerce Search Engine Frontend, 
        2. E-commerce Search Engine Admin Backend, 
        3. Web scraping API core and tools, 
        4. Web scraping automation and synchronization tools, 
        5. Devops, Search Engine Implementation, Architecture, and Integrations.
 - _Technologies_: Elasticsearch, Python, Flask, Docker, NoSQL, Scrapy, Selenium, Firebase (Functions, Firestore, Authentication, Hosting), Git, JavaScript, React, Redux, Nodejs, Google Cloud Platform (PubSub, Task Scheduler, Compute Engine, Cloud Run, Task Runner, Logging).
    Testing: Jest, Pytest.
<br><br>

**Dual Fisheye to VR180 - Nvidia GPU Video Stitcher** - [project details](./projects/cuda-stitcher.md) <br>
A tool for converting dual fisheye camera videos to equirectangular stitched videos using NVIDIA CUDA, NVDEC,  NVENC.
 - _Focus_: GPU Computing
 - Results obtained were x100+ faster than those obtained using serial CPU programming.
 - _Technologies_: C++, Cmake, CUDA, OpenGL, OpenCV, Nvidia VRWorks.
<br><br>

**Artur Platform - Predimensioning of hydraulic turbine structural components** - [project details](https://www.impsa.com/en/products/hydro/kaplan-turbines/) <br>
A tool for predimensioning of hydraulic turbine structural components.
 - Lead developer for the ARTUR platform, used for the calculation and pre-dimensioning of hydraulic turbine structural component elements.
 - Assisted in the development of design manuals that set the criteria for calculation and dimensioning of water turbine structural elements.
 - _Employer_: [IMPSA](https://www.impsa.com/en/contact-us/) - [Juan De Miguel](https://www.linkedin.com/in/juan-ram%C3%B3n-de-miguel-198ab51ba/) 
 - _Focus_: Scientific Computing
 - _Technologies_: C++, ANSYS Multiphysics API, Matlab, Excel VBA, SolidEdge API.
<br><br>

**Enertrag WindEnergy-Hydrogen-Biogas Integrated System Simulation Tool** - [project details](./projects/enertrag.md) <br>
A tool for simulation of wind energy systems using hydrogen and biogas.
 - Developed in coordination with the Hochschule Stralsund as a base tool for simulations in the field of Wind Power - Hydrogen integrated systems for the [ENERTRAG](https://enertrag.com/) company.
 - _Employer_: [Hochschule Stralsund](https://www.hochschule-stralsund.de/) - [Prof. Dr. rer. nat. Jochen Lehmann](mailto:jochen.lehmann@fh-stralsund.de) - [Prof. Dr.-Ing. Thomas Luschtinetz](https://www.hochschule-stralsund.de/host/fakultaeten/elektrotechnik-und-informatik/personalseiten/luschtinetz-thomas/#825099_blank)
 - _Focus_: Scientific Computing, Optimization
 - _Technologies_: Matlab, Matlab Genetic Algorithms Toolbox.
<br><br>

**SPR System - Technical Secretary of Planning - Paraguayan Government** - [project details](./projects/stp-fao.md) <br>
Design specifications and UI/UX for the [SPR system](https://spr.stp.gov.py/tablero/public/geografico4.jsp) - Technical Secretary of Planning - Paraguayan Government ([STP](https://www.stp.gov.py/v1/)).
 - Worked in a cross-functional, agile team to rebuild the [SPR system](https://www.stp.gov.py/v1/instrumentos-spr/)
 - Assistance with information architecture and UX writing for the web app
 - _Client_: [STP-Paraguay](https://www.stp.gov.py/v1/) 
 - _Focus_: UX/UI, Information Architecture
<br><br>

**StuffILearned - Personal Software development Notes** - [project details](http://181.126.83.235/) <br>
A software development personal blog to keep track of new technologies, courses and personal notes. **To be replaced soon.**
 - Provide easy access to common software development notes. 
 - _Website_: [http://181.126.83.235/](http://181.126.83.235/) 
 - _Focus_: Web Development
 - _Technologies_: PHP, Wordpress, MySQL, html, css.
<br><br>

**Matchmaking** - [project details](https://github.com/manolosolalinde/matchmaking) <br>
A simple flask web application to balance team players for video games.
 - Small open source project.
 - _Github_: [https://github.com/manolosolalinde/matchmaking](https://github.com/manolosolalinde/matchmaking)
 - _Focus_: Web Development
 - _Technologies_: Python, Flask, MySQL, SQLAlchemy, Jinja, Bootstrap, html, css.
<br><br>
 
**A Finite Element Based Level Set Approach for the Simulation of Two-Phased Flows** - [short summary](https://github.com/manolosolalinde/FEM-Multiphase/blob/master/documentation/NSOLALINDE_EBECEM_v4.pdf) <br>
A Finite Element Based Level Set Approach for the Simulation of Two-Phased Flows.
 - _Description_: **Master Thesis**. Level set approach for the simulation of two-phase immiscible newtonian ﬂuids.
 - _Github_: [https://github.com/manolosolalinde/FEM-Multiphase](https://github.com/manolosolalinde/FEM-Multiphase) 
 - _Dissertation_: [https://www.bdtd.uerj.br:8443/bitstream/1/11742/1/Nestor%20M%20Solalinde.pdf](https://www.bdtd.uerj.br:8443/bitstream/1/11742/1/Nestor%20M%20Solalinde.pdf) 
 - _Focus_: Scientific Computing, Numerical Simulation
 - _Technologies_: C++, Matlab, Wolfram Mathematica, Libmesh Finite Elements Library.
<br><br>


## 👩🏼‍🎓 EDUCATION

**MSc. in Mechanical Engineering – Applied Mathematics** <br>
[UERJ](https://www.uerj.br/) - Rio de Janeiro, Brazil (2009-2011) 
 - Finished with straight A’s. 
 - _Specialization_: Scientific computing, continuum mechanics, finite elements, optimization, fluid mechanics, heat 
transfer. 
 - _Master Thesis_: A finite element level-set approach for the simulation of two-phased flows. [https://www.bdtd.uerj.br:8443/bitstream/1/11742/1/Nestor%20M%20Solalinde.pdf](https://www.bdtd.uerj.br:8443/bitstream/1/11742/1/Nestor%20M%20Solalinde.pdf)
<br><br>

**Electromechanical Engineer** <br>
[Universidad Nacional de Asunción](https://www.una.py/) - Asunción, Paraguay (2001-2008) 
 - Finished as a member of the honor roll (top 5 students). 
 - Initial enrollment test: rank 3 of 120 students admitted. (800 applicants). 
 - Auxiliary Teacher of Vector Mechanics (third semester subject).
 - Course concluded with an average grade of 4.23 in a scale from 1 to 5, 5 being the highest grade.
 - _Thesis_: Analysis of Electrolytic Hydrogen Production in Paraguay. 
<br><br>
 
**International Exchange Semester** <br>
[Hochschule Stralsund](https://www.hochschule-stralsund.de/) - Stralsund, Germany (2007) 
 - Finished a 6 months course on Renewable Energies and Hydrogen Technology, top of the class, with an average of 1.27 in a scale from 1 to 5, 1 being the highest grade. <br><br>
 
**High School** <br>
[San Ignacio de Loyola School](https://www.sil.edu.py/) - Asuncion, Paraguay (1995-2000)
 - Private High School.
 - General average grade in secondary education: 4.26 on a scale from 1 to 5, 5 being the highest grade. 
<br><br>

## 💬 Languages

**English:** Fluent <br>
**Portuguese:** Advanced <br>
**German:** Intermediate <br>
**Spanish:** Native
<br><br>


## 📚 Informal Software Engineering Education


**Build a Backend REST API with Python & Django - Advanced**
- Udemy - [Course details](https://www.udemy.com/course/django-python-advanced/) 
- Course duration: 8hs. Online Course.

**Complete Guide to ElasticSearch**
- Udemy - [Course details](https://www.udemy.com/complete-guide-to-elasticsearch/) 
- Course duration: 12hs. Online Course.

**Intro to Parallel Programming**
- Coursera – Udacity - [Course details](https://developer.nvidia.com/udacity-cs344-intro-parallel-programming) 
- Course duration: 21hs. Online Course.

**Machine Learning**
- Coursera – Standford University - [Course details](https://www.coursera.org/learn/machine-learning) 
- Course duration: 55hs. Online Course.

**CS50's Web Programming with Python and JavaScript**
- edX – Harvard University - [Course details](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) 
- Course duration: 90hs. Online Course.

**HTML, CSS, and Javascript for Web Developers**
- Coursera – Johns Hopkins University - [Course details](https://www.coursera.org/learn/html-css-and-javascript-for-web-developers) 
- Course duration: 33hs. Online Course.

**Computer Vision Intro™ OpenCV4 in Python with Deep Learning**
- Udemy - [Course details](https://www.udemy.com/master-computer-vision-with-opencv-in-python/) 
- Course duration: 10hs. Online Course.

**Convolutional Neural Networks for Visual Recognition**
- Standford University - [Course details](http://cs231n.stanford.edu/index.html) 
- Course duration: 34hs. Online Course.

**Complete Guide to TensorFlow for Deep Learning with Python**
- Udemy - [Course details](https://www.udemy.com/complete-guide-to-tensorflow-for-deep-learning-with-python/) 
- Course duration: 14hs. Online Course.

**OCW 6001 Introduction to Computer Science and Programming in Python**
- MIT OCW - [Course details](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) 
- Course duration: 12hs. Online Course.

**C++**
- TheChernoProject/Youtube - [Course details](https://www.youtube.com/watch?v=18c3MTX0PK0&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb) 
- Duration: 15hs. Online Course.

<br>


### Introduction Courses

Most of these where used as technology introduction material before diving into deeper documentation.
<br>

 **GraphQL** - The Net Ninja - [Course details](https://www.youtube.com/playlist?list=PL4cUxeGkcC9iK6Qhn-QLcXCXPQUov1U7f)<br>

 **Gatsby Tutorial** – The Net Ninja - Youtube - [Course details](https://www.youtube.com/watch?v=Qms4k6y7OgI&list=PL4cUxeGkcC9hw1g77I35ZivVLe8k2nvjB) <br>

 **Next.JS** - The Net Ninja - Youtube - [Course details](https://www.youtube.com/watch?v=A63UxsQsEbU&list=PL4cUxeGkcC9g9gP2onazU5-2M-AzA8eBw) <br>

 **React Native** - The Net Ninja - [Course details](https://www.youtube.com/watch?v=ur6I5m2nTvk&list=PL4cUxeGkcC9ixPU-QkScoRBVxtPPzVjrQ) <br>

 **Javascript Unit Testing with Jest** - Traversy Media - [Course details](https://www.youtube.com/watch?v=7r4xVDI2vho) <br>

 **React, Redux & Firebase** - The Net Ninja - [Course details](https://www.youtube.com/watch?v=Oi4v5uxTY5o&list=PL4cUxeGkcC9iWstfXntcj8f-dFZ4UtlN3) <br>

 **Python REST API** - Tech With Tim - [Course details](https://www.youtube.com/watch?v=GMppyAPbLYk) <br>

 **Asynchronous Python** - Live Python - [Course details](https://www.youtube.com/watch?v=6kNzG0T44SI) <br>

 **React Redux** - The Net Ninja - [Course details](https://www.youtube.com/watch?v=pKYiKbf7sP0&list=PL4cUxeGkcC9ij8CfkAY2RAGb-tmkNwQHG) <br>

 **Firebase Firestore** - The Net Ninja - [Course details](https://www.youtube.com/watch?v=4d-gIPGzmK4&list=PL4cUxeGkcC9itfjle0ji1xOZ2cjRGY_WB) <br>

 **Docker** - freeCodeCamp.org - [Course details](https://www.youtube.com/watch?v=fqMOX6JJhGo) <br>
 
 **Docker Compose** - Jake Wright - [Course details](https://www.youtube.com/watch?v=Qw9zlE3t8Ko) <br>

 <br>


## 🦾 Electromechanical Engineering experience

**Self-Employed / Consultant** <br>
January 2017 to current date
 - Asuncion – Paraguay (January 2017 to current date) 
 - Calculation and assessment of structural components using finite element analysis tools for:
   - Naval industry (tugboats, barges).
   - Cement Industry (mills, structural components).
   - Shipyards.
 - Design and calculation of hydraulic systems (industrial plants).
 - Design and calculation of general steel structures.
 - Electrical, HVAC and Plumbing projects. 
 <br><br>

**Engineer / Manager** @ [SCE S.A.](https://www.facebook.com/sceconstructora/)
Asuncion – Paraguay (2016-2017)
 - Engineering and Design: Design and calculation of steel structures. 
 - Electrical, HVAC and Plumbing projects for houses, several story buildings and residential complex.
 - Management: Construction of a residential complex of 1800m2. Development of excel/SQL tools for management.
 <br><br>

**Engineer** @ [TECNOEDIL S.A.](http://www.tecnoedil.com.py/) <br>
Asuncion – Paraguay (2013-2015) 
 - BIM Management and Implementation with Revit Architecture and Revit MEP for the Engineering technical office. 
 - Coordination of all the task related electrical systems, HVAC, Fire protection and Plumbing, related to the construction of the Regional Hospital of Ciudad del Este. Client: IPS. 
 <br><br>

**Engineer/Developer** @ [IMPSA](http://www.impsa.com) <br>
Mendoza – Argentina (2011 to 2013) 
 - Lead Developer of the ARTUR platform (C++ Language), used for the calculation and pre-dimensioning of hydraulic turbine structural component elements. 
 - Assisted in the development of design manuals that set the criteria for calculation and dimensioning of water turbine structural elements. 
 <br><br>
 
**Engineering Intern** @ [TERMECO S.R.L.](http://www.termeco.com.py) <br>
Asuncion- Paraguay (Apr/2007-Jul/2007) 
 - Intern. Mechanical Designer, drawer.
 - _Tasks_: Industrial Boilers design using Solidworks, Bioethanol Plant Project related design tasks. 
 <br><br>
 
**Mechanical Designer** @ [TEDEC S.R.L.](http://www.tedec.com.py) <br>
Asuncion – Paraguay (Nov/2005-Aug/2006) 
 - Tasks related to electrical installations design, tanks and vessels design and piping design for several industries such as a Stevia Processing Plant, a Shipyard and an alcohol dispensing station. 
 - I made a very successful presentation, using 3D modeling tools, of a Stevia Processing Plant project that led to the approval of the Plant Construction. 
 <br><br>
 
**Technical Drawer** @ [CORSAT S.R.L.](http://www.corsat.com.py) <br>
Asuncion – Paraguay (Jan/2005-Jul/2005) 
 - Calculus and 3D design of a waste dryer for meat industry; several engineering related jobs.  
 <br><br>

## 🦾 Mechanical Engineering Certifications

**ASHRAE HVAC Design: Level I & Level II** - [Details](https://www.ashrae.org/professional-development/all-instructor-led-training/hvac-design-and-operations-training) <br>
December, 2016 - ASHRAE Headquarters, Atlanta, GA, EEUU

**Revit Architecture 2014 Certified Professional** - [Details](https://www.autodesk.com/certification/all-certifications/revit-architectural-design-professional) <br>
Autodesk University 2013 – Las Vegas Nevada
 <br><br>


## 📌 On The Side

**Organizer** @ Energy and Enviroment Workshop (2009) <br>
UNA University Campus, Asuncion, Paraguay.
