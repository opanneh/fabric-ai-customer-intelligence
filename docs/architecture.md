# 🏗️ Solution Architecture

## Overview

The **Fabric AI Customer Intelligence Platform** is designed as an enterprise-grade analytics solution that transforms raw operational data into trusted, AI-enriched business insights.

The platform follows Microsoft's recommended **Medallion Architecture**, separating data ingestion, transformation, enrichment, and analytical consumption into distinct layers. This layered approach improves maintainability, scalability, governance, and analytical performance while supporting both traditional business intelligence and AI-powered customer analytics.

The solution integrates Microsoft Fabric's unified analytics capabilities, including **Data Factory**, **OneLake**, **Lakehouse**, **PySpark**, **Fabric Warehouse**, **Power BI**, and **Deployment Pipelines** into a single enterprise platform.

---

# Architecture Principles

The solution was designed around the following enterprise architecture principles:

- Separation of storage, processing and reporting workloads
- Layered Medallion Architecture
- Modular and reusable data pipelines
- Centralized enterprise storage using OneLake
- AI enrichment integrated into the trusted data layer
- Dimensional modelling for analytical performance
- Governed semantic modelling
- Multi-environment deployment
- Source-controlled development

These principles enable the platform to scale while remaining maintainable and easy to extend.

---

# End-to-End Architecture

The solution follows a sequential processing pipeline:

```
Source Data
      │
      ▼
Data Factory
      │
      ▼
Bronze Lakehouse
      │
      ▼
PySpark Transformation
      │
      ▼
Silver Lakehouse
      │
      ▼
AI Enrichment
      │
      ▼
Silver (Enriched)
      │
      ▼
Data Factory Pipeline
      │
      ▼
Gold Warehouse
      │
      ▼
Semantic Model
      │
      ▼
Power BI
```

Each stage has a clearly defined responsibility and ownership.

---

# Architecture Components

## Data Sources

The platform ingests structured and semi-structured customer data from multiple operational systems.

Supported data includes:

- Customer Master
- Product Master
- Sales Orders
- Customer Reviews
- Website Activity
- Social Media

Microsoft Fabric Data Factory orchestrates the ingestion process into OneLake.

---

## Bronze Layer

The Bronze layer stores the first managed copy of the incoming data.

Objectives:

- Preserve raw source data
- Maintain historical records
- Enable data lineage
- Support auditing and replay

No business logic is applied at this stage.

Typical operations include:

- Schema validation
- Metadata capture
- Delta conversion
- Ingestion logging

---

## Silver Layer

The Silver layer represents the trusted enterprise dataset.

This layer is responsible for improving data quality and preparing data for downstream analytical workloads.

Transformation activities include:

- Data cleansing
- Standardisation
- Duplicate removal
- Null handling
- Business rule validation
- Feature engineering

At this stage, data is considered suitable for enterprise processing.

---

# AI Enrichment

A distinguishing feature of the platform is the integration of AI directly into the engineering pipeline.

Rather than enriching reports after the warehouse has been built, customer reviews are analysed immediately after the Silver transformation stage.

This design provides several advantages:

- AI attributes become part of the trusted enterprise dataset.
- Multiple downstream consumers can reuse AI-generated insights.
- AI processing occurs once rather than being repeated in every report.
- Analytical consistency is maintained across all reporting solutions.

The enrichment process uses Azure AI Foundry with GPT-5 to generate business attributes including:

- Sentiment
- Category
- Priority
- Summary
- Keywords
- Recommended Action

The enriched attributes are written back into the Silver Lakehouse before loading into the analytical warehouse.

---

# Gold Layer

The Gold layer contains curated business-ready datasets.

Unlike Bronze and Silver, the Gold layer is implemented as a **Fabric Warehouse** optimized for analytical queries.

The warehouse contains:

- Dimension tables
- Fact tables
- Reporting views
- Stored procedures

The warehouse follows a Galaxy (Fact Constellation) schema to support multiple analytical subject areas.

---

# Semantic Model

The Power BI Semantic Model sits directly above the Gold Warehouse.

Responsibilities include:

- Business relationships
- Time intelligence
- DAX calculations
- KPI definitions
- Interactive filtering

Separating the semantic layer from the warehouse enables reusable business definitions while simplifying report development.

---

# Reporting Layer

The platform delivers business insights through interactive Power BI dashboards.

Three reporting domains were developed:

### Executive Overview

Enterprise sales and operational KPIs.

### Customer Feedback

Customer review analytics and engagement metrics.

### AI Customer Insights

AI-generated sentiment, categorisation, priorities and recommended actions.

Each dashboard consumes the same governed semantic model.

---

# Deployment Architecture

The platform supports controlled promotion of Fabric artifacts through Deployment Pipelines.

Environments include:

- Development
- Test
- Production

This deployment strategy reduces operational risk while supporting collaborative development.

---

# Security & Governance

Although this project uses sample data, the architecture was designed to align with enterprise governance practices.

Design considerations include:

- Centralized storage
- Controlled data movement
- Layered data architecture
- Reusable semantic model
- Environment isolation
- Source-controlled development

The architecture can be extended to support:

- Row-Level Security (RLS)
- Sensitivity Labels
- Microsoft Purview
- Incremental Refresh
- Real-Time Analytics

---

# Why This Architecture?

The architecture was intentionally designed to separate operational processing from analytical consumption.

This provides several benefits:

- Improved scalability
- Better maintainability
- Easier troubleshooting
- Reusable AI enrichment
- Enterprise reporting consistency
- Simplified future enhancements

The result is a modern Microsoft Fabric solution that combines Data Engineering, Artificial Intelligence, Data Warehousing and Business Intelligence into a single governed analytics platform.

---

# Related Documentation

- semantic-model.md
- ai-enrichment.md
- deployment.md
- cicd.md
