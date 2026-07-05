# 🏗️ Solution Architecture

## Overview

The **Microsoft Fabric AI Customer Intelligence Platform** is an end-to-end analytics solution designed to transform raw customer and sales data into actionable business insights using Microsoft Fabric, PySpark, AI-powered enrichment, and Power BI.

The solution follows the **Medallion Architecture** pattern (Bronze, Silver, Gold) to progressively improve data quality while separating ingestion, transformation, enrichment, and analytical workloads.

The project demonstrates a complete enterprise analytics workflow including:

- Data ingestion using Microsoft Fabric Data Factory
- Bronze, Silver and Gold data architecture
- AI-powered customer review enrichment
- Enterprise dimensional data warehouse
- Semantic modelling
- Interactive Power BI dashboards
- Multi-environment deployment using Microsoft Fabric Deployment Pipelines

---

# Solution Architecture

![End-to-End Architecture](images/end-to-end-architecture.png)

---

# Business Problem

Retail organizations receive customer information from multiple operational systems including sales transactions, product catalogs, customer master data and customer reviews.

Although this data contains valuable business insights, it is often:

- Stored in multiple formats
- Difficult to analyze together
- Missing customer sentiment information
- Not optimized for reporting
- Lacking enterprise governance

This solution centralizes operational data into Microsoft Fabric and enriches customer reviews using AI before delivering curated datasets for business intelligence.

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Data Integration | Microsoft Fabric Data Factory |
| Storage | OneLake |
| Bronze Layer | Fabric Lakehouse |
| Silver Layer | Fabric Lakehouse |
| AI Enrichment | GPT-5 |
| Processing | PySpark |
| Gold Layer | Fabric Warehouse |
| Data Warehouse | Star (Galaxy) Schema |
| Semantic Layer | Power BI Semantic Model |
| Reporting | Power BI |
| Deployment | Fabric Deployment Pipelines |

---

# End-to-End Data Flow

The solution processes data through several stages to improve quality, enrich business value and prepare analytical datasets.

```
CSV / JSON Files
        │
        ▼
Data Factory Pipelines
        │
        ▼
Bronze Lakehouse
(Raw Storage)
        │
        ▼
Notebook 01
RAW → Bronze
        │
        ▼
Notebook 02
Bronze → Silver
        │
        ▼
Notebook 03
Business Feature Engineering
        │
        ▼
Notebook 04
AI Customer Insight Enrichment
        │
        ▼
Silver Lakehouse (Enriched)
        │
        ▼
Data Factory Pipeline
Silver → Gold
        │
        ▼
Notebook 05
Create Dimensions & Facts
        │
        ▼
Gold Warehouse
        │
        ▼
Semantic Model
        │
        ▼
Power BI Dashboards
```

---

# Medallion Architecture

The project follows Microsoft's recommended Medallion Architecture.

![Medallion Architecture](images/medallion-architecture.png)

### Bronze Layer

The Bronze layer stores raw operational data exactly as received from the source systems.

Characteristics:

- Immutable raw data
- Original schema preserved
- Audit and lineage support
- Historical storage

---

### Silver Layer

The Silver layer standardizes, cleans and enriches data.

Operations performed include:

- Data cleansing
- Standardization
- Feature engineering
- Business rule validation
- AI-powered customer review enrichment

The Silver layer represents the trusted enterprise dataset.

---

### Gold Layer

The Gold layer provides business-ready analytical datasets.

The Gold Warehouse contains:

- Dimension tables
- Fact tables
- Reporting views
- Stored procedures
- Semantic model

This layer is optimized for Power BI reporting.

---

# AI Enrichment

A key differentiator of this project is the AI enrichment stage.

Customer reviews are processed using GPT-5 to generate additional business attributes including:

- Sentiment
- Review Category
- Business Priority
- Recommended Action
- Keywords
- Confidence information

These attributes are written back into the Silver layer before being loaded into the analytical warehouse.

---

# Enterprise Data Warehouse

The Gold Warehouse implements a **Galaxy (Fact Constellation)** schema.

![Galaxy Schema](images/semantic-model-galaxy.png)

The warehouse contains:

### Dimensions

- DimCustomer
- DimProduct
- DimDate

### Facts

- FactSales
- FactReviews
- FactCustomerSentiment

This design allows multiple analytical subject areas to share common conformed dimensions.

---

# Semantic Model

Power BI connects directly to the Gold Warehouse through a semantic model.

The semantic model provides:

- Business relationships
- DAX measures
- Time intelligence
- KPI calculations
- Interactive filtering

This layer simplifies report development while maintaining a governed analytical model.

---

# Reporting Layer

Three business dashboards were developed.

## Executive Overview

Provides executive KPIs including:

- Revenue
- Orders
- Products
- Customers
- Revenue trends
- Category performance

---

## Customer Feedback

Provides customer review analytics including:

- Review distribution
- Product ratings
- Customer feedback
- Review categories

---

## AI Customer Insights

Provides AI-generated business insights including:

- Sentiment analysis
- Business priorities
- Recommended actions
- AI review categorization

---

# Deployment Strategy

The solution supports enterprise deployment through Microsoft Fabric Deployment Pipelines.

Environments include:

- Development
- Test
- Production

This enables controlled promotion of artifacts while maintaining environment isolation.

---

# Key Features

- Microsoft Fabric Data Factory
- Medallion Architecture
- OneLake Storage
- PySpark Data Engineering
- AI Customer Review Enrichment
- Enterprise Data Warehouse
- Galaxy Schema
- Power BI Semantic Model
- Interactive Dashboards
- Deployment Pipelines

---

# Author

**Ousainou Panneh**

Microsoft Fabric AI Customer Intelligence Platform

2026
