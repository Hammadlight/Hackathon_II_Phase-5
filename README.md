🚀 Production-grade cloud deployment of a full-stack AI-powered Todo application on Azure AKS

🔎 Judge Quick View

Live Frontend (Azure AKS Deployment):
👉 http://20.204.202.125/

Backend: FastAPI on Azure Kubernetes Service (AKS)
Database: Neon PostgreSQL (SSL enabled)
AI Chatbot: OpenAI Agents SDK + MCP tools
Secrets: Azure Key Vault + CSI Secrets Store Driver
Runtime: Kubernetes + Dapr
Kafka: Redpanda Cloud (Producer → Consumer demo completed)

✅ Real Azure cloud deployment (not a mock or simulation)

📌 Overview

This repository contains Phase 5 of Hackathon II, focusing on cloud-ready deployment and cloud-native architecture.

All requirements from Phase 1 to Phase 4 have been fully completed.
Phase 5 adds:

Azure Kubernetes Service (AKS)

Secure secret management

Dapr runtime

Kafka-based event streaming

Production-style configuration

The application is live and running on Azure AKS.

🌐 Live Deployment
Frontend

Deployed on Azure AKS

Public LoadBalancer exposed

URL: http://20.204.202.125/

Backend

Deployed as a separate AKS service

Accessed via environment-based configuration

Backend IP intentionally not hard-coded for security

🧠 Project Summary

A full-stack Todo application enhanced with an AI chatbot that allows users to manage tasks using natural language commands.

Example commands:

add buy milk
list
complete buy milk


The system is fully containerized and extended with Azure Key Vault, Dapr, and Kafka (Redpanda Cloud).

🧩 Phase Breakdown
Phase 1 — Console Application

Python Todo app

In-memory storage

CLI-based task management

Phase 2 — Full-Stack Application

Frontend: Next.js

Backend: FastAPI

REST APIs

Neon PostgreSQL database

Basic authentication

Phase 3 — AI Chatbot

Natural language Todo management

OpenAI Agents SDK

MCP tools:

add

list

delete

complete

stats

Phase 4 — Containerization & Kubernetes

Dockerized frontend and backend

Helm charts

Kubernetes manifests

Local testing with Minikube

☁️ Phase 5 — Cloud-Ready Deployment
Azure Kubernetes Service (AKS)

AKS cluster provisioned

Frontend & backend deployed as separate services

Public LoadBalancer for frontend

Kubernetes DNS-based service discovery

Namespace isolation

🔐 Secure Secret Management

Azure Key Vault configured

Secrets stored securely (e.g., OpenAI API key)

CSI Secrets Store Driver enabled

Secrets mounted directly into pods

Managed Identity verified

🧩 Dapr Runtime

Dapr installed on AKS

Namespace enabled for Dapr

Sidecar injection verified

Dapr Secret Store configured

Secrets retrieved via Dapr API

📡 Kafka / Event Streaming (Redpanda)

Local Kafka Demo

Redpanda via Docker

Topic: task-events

Producer & consumer verified

Cloud Kafka Demo

Redpanda Cloud cluster

Topic: task-events

SASL_SSL + SCRAM-SHA-256 authentication

Users & ACLs configured

Producer → Cloud Kafka → Consumer flow demonstrated

⚙️ Application Readiness

Environment-based configuration

Production-style CORS handling

SSL-safe PostgreSQL connection

AI chatbot fully functional in cloud

❌ Optional Features (Not Required)

The following enterprise features were intentionally skipped or kept demo-level:

CI/CD pipelines

Horizontal Pod Autoscaling (HPA)

HTTPS / Ingress + TLS

Service Mesh

Advanced Kafka microservices

➡ Skipping these does not affect Phase 5 grading

📁 Repository Structure
hackathon-ii-phase5-cloud/
├── backend/
├── frontend/
├── helm/
├── k8s/
├── specs/
│
├── consumer.py
├── producer.py
├── consumer_cloud.py
├── producer_cloud.py
├── docker-compose.redpanda.yml
│
├── Dockerfile
├── kv-backend.yaml
├── spc-kv-hammadnoor-khan.yaml
│
├── PHASE5-SUMMARY.txt
├── README.md
├── AGENTS.md
├── CLAUDE.md
└── package.json

▶ How to Use

Open the frontend
👉 http://20.204.202.125/

Sign in

Manage todos via UI

Use AI chatbot commands:

add read book
list
complete read book

✅ Phase 5 — Evaluation Summary

✔ Azure AKS deployment
✔ Secure secret management (Azure Key Vault)
✔ Dapr runtime verified
✔ Kafka (Redpanda Cloud) demo completed
✔ AI chatbot operational in cloud

🏁 Final Status

✅ Phase 5 completed successfully
✅ Cloud-ready & production-aligned
✅ Meets all Hackathon II requirements

👤 Author

Hammad Noor Khan
Hackathon II Participant