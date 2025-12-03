# Azul Workflows – AI Automation Marketing Website

Azul Workflows is a production-ready marketing website built for an AI workflow automation startup.  
It combines a polished React frontend with a FastAPI backend, a lead-capture system, and a fully containerised deployment on AWS.

## Features

- **Marketing Site** – Responsive, modern landing page describing AI automation services and value proposition.
- **Service Showcases** – Sections for AI agents, workflow automation, and integration solutions.
- **Lead Capture Form** – Contact form that stores leads in PostgreSQL and triggers email workflows.
- **Email Automation** – SMTP integration for customer confirmation emails and internal notifications.
- **Secure API** – FastAPI backend with async SQLAlchemy, validation, and admin-only endpoints.
- **Production Deployment** – Dockerised services, Nginx reverse proxy, HTTPS, and environment-based configuration on AWS Lightsail.

## Tech Stack

- **Frontend:** React (Vite), CSS
- **Backend:** FastAPI, Python, async SQLAlchemy
- **Database:** PostgreSQL
- **Email:** SMTP-based transactional emails
- **Infra:** Docker, Nginx, AWS Lightsail
- **Other:** GitHub, environment variables for secrets

> This project was originally built as a client deliverable and adapted (with sensitive details removed) as a portfolio piece.
