---
title: MatchMaking
description: A simple flask application to balance team players for video game matches. 
image_url: ./images/matchmaking.png
date: 2018-12-12
order: 4
technologies: Python, Flask, MySQL, SQLAlchemy, Jinja, Bootstrap, html, css.
category: Full Stack Development
---

# MatchMaking

A simple flask application to balance team players for video game matches.

[Live Demo](https://matchmaking-u2rlwnoy2a-uc.a.run.app/)

# Steps to run:

1. Clone the repo:
```bash
git clone https://github.com/manolosolalinde/matchmaking.git
```

2. Start a postgresql server

3. Create a .env file with the following content
```.env
DATABASE_URL="postgres://postgres:<password>@<databaseurl>:5432/mydatabase"
```

4. Run:
```bash
python create.py
python import.py
flask run
```

# Deployment to cloud run:

Commands to build
```bash
# Build and push to remote repository
gcloud builds submit --tag gcr.io/<projectname>/matchmaking --project <projectname>
    # ALTERNATIVELY YOU CAN:
        ## step1) building
        # docker build . -t gcr.io/<projectname>/matchmaking
        ## step2) Upload to google cloud repository
        # docker push gcr.io/<projectname>/matchmaking
# Deploy to Cloud Run
gcloud config set run/region us-central1
gcloud run deploy --image gcr.io/<projectname>/matchmaking --platform managed --port=5000 --project <projectname>
```