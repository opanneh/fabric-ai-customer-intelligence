# 📊 Semantic Model

## Overview

The **Fabric AI Customer Intelligence Platform** implements an enterprise **Galaxy (Fact Constellation) Schema** to support multiple analytical subject areas through a single, governed semantic model.

Unlike a traditional Star Schema centered around a single business process, the Galaxy Schema enables multiple fact tables to share common dimensions, allowing sales, customer feedback and AI-generated customer insights to be analyzed together while maintaining consistency across the analytical platform.

This modelling approach provides a scalable foundation for executive reporting, customer analytics and AI-powered business intelligence.

---

# Design Objectives

The semantic model was designed with the following objectives:

- Provide a single source of truth for enterprise reporting
- Support multiple business processes within a unified model
- Enable reusable conformed dimensions
- Simplify DAX calculations
- Improve analytical query performance
- Support AI-enhanced customer analytics
- Enable scalable report development
- Promote consistent business definitions

---

# Galaxy Schema

![Galaxy Schema](images/semantic-model-galaxy.png)

The semantic model consists of three shared dimensions supporting three analytical fact tables.

```text
                 DimDate
                    │
                    │
DimCustomer ─── FactSales ─── DimProduct
      │              │              │
      │              │              │
      │         FactReviews ────────┘
      │
      └──── FactCustomerSentiment ──┘

              Measures Table
           (DAX Calculations)
```

This architecture allows multiple analytical subject areas to reuse the same business entities while maintaining clear separation of business processes.

---

# Dimension Tables

Dimension tables provide descriptive business context for analytical reporting.

---

## DimCustomer

Stores customer master information shared across the analytical platform.

**Business Purpose**

- Customer segmentation
- Geographic analysis
- Customer reporting
- Customer intelligence

**Shared By**

- FactSales
- FactReviews
- FactCustomerSentiment

---

## DimProduct

Stores product master information.

**Business Purpose**

- Product analytics
- Category reporting
- Product performance
- AI review analysis

**Shared By**

- FactSales
- FactReviews

---

## DimDate

Enterprise calendar dimension supporting time intelligence.

**Business Purpose**

- Daily reporting
- Monthly trends
- Quarterly reporting
- Year-over-year analysis
- DAX time intelligence

**Shared By**

- FactSales
- FactReviews
- FactCustomerSentiment

---

# Fact Tables

Fact tables capture measurable business events.

---

## FactSales

Stores transactional sales information.

**Grain**

> One row per sales transaction.

**Business Metrics**

- Revenue
- Quantity Sold
- Orders

**Consumed By**

- Executive Overview Dashboard

---

## FactReviews

Stores customer review activity.

**Grain**

> One row per customer review.

**Business Metrics**

- Ratings
- Review Count

**Consumed By**

- Customer Feedback Dashboard

---

## FactCustomerSentiment

Stores AI-generated customer intelligence derived from customer reviews.

**Grain**

> One row per AI-enriched review.

**Business Metrics**

- Sentiment
- Category
- Priority
- Recommended Action

**Consumed By**

- AI Customer Insights Dashboard

---

# Relationships

The semantic model uses one-to-many relationships between dimensions and facts.

```text
DimCustomer
    │
    ├──────── FactSales
    │
    ├──────── FactReviews
    │
    └──────── FactCustomerSentiment

DimProduct
    │
    ├──────── FactSales
    │
    └──────── FactReviews

DimDate
    │
    ├──────── FactSales
    │
    ├──────── FactReviews
    │
    └──────── FactCustomerSentiment
```

This relationship design enables consistent filtering, drill-down and cross-report analytics.

---

# Measures Strategy

Business calculations are centralized within a dedicated **Measures Table**, following Microsoft Power BI modelling best practices.

Separating measures from physical tables provides several advantages:

- Centralized business logic
- Simplified report development
- Improved model organization
- Easier maintenance
- Reusable KPI definitions
- Consistent calculations across reports

This approach keeps fact and dimension tables focused exclusively on business data while analytical calculations remain isolated within the semantic layer.

---

## Measure Organization

Measures are grouped into logical business categories.

### Revenue Measures

- Total Revenue
- Total Orders
- Average Order Value
- Revenue Growth

---

### Customer Measures

- Total Customers
- Customer Review Count
- Average Rating

---

### Product Measures

- Total Products
- Product Revenue
- Product Review Count

---

### AI Measures

- Positive Reviews
- Neutral Reviews
- Negative Reviews
- High Priority Reviews
- AI Categories

---

### Time Intelligence

- Revenue YTD
- Revenue MTD
- Previous Month Revenue
- Previous Year Revenue

---

## Measure Design Principles

Measures were intentionally implemented within a dedicated semantic layer rather than directly inside report visuals.

This design provides:

- Reusable calculations
- Consistent KPI definitions
- Simplified report development
- Centralized business logic
- Easier long-term maintenance

All Power BI reports consume the same governed DAX calculations, ensuring analytical consistency across the platform.

---

# Why a Galaxy Schema?

A Galaxy Schema was selected instead of a traditional Star Schema because the platform supports multiple independent business processes.

The model combines:

- Sales Analytics
- Customer Feedback Analytics
- AI Customer Intelligence

Each subject area maintains its own fact table while sharing common business dimensions.

This approach provides:

- Reduced data duplication
- Consistent business definitions
- Better scalability
- Simplified semantic modelling
- Improved maintainability

---

# Why Separate Fact Tables?

Each fact table represents a distinct business process.

### FactSales

Captures commercial transactions.

---

### FactReviews

Captures customer feedback.

---

### FactCustomerSentiment

Captures AI-generated analytical outcomes rather than transactional events.

Separating these facts allows each analytical domain to evolve independently while remaining connected through shared dimensions.

---

# Semantic Layer Design

The Power BI Semantic Model sits above the Gold Warehouse and provides:

- Business relationships
- DAX calculations
- KPI definitions
- Time intelligence
- Interactive filtering
- Cross-report consistency

All dashboards consume the same governed semantic model.

---

# Analytical Benefits

The semantic model enables:

- Executive sales reporting
- Customer review analytics
- Product performance reporting
- AI-powered customer intelligence
- Cross-domain analytics
- Consistent KPI calculations
- Enterprise self-service BI

---

# Future Enhancements

The semantic model can be extended with:

- Row-Level Security (RLS)
- Object-Level Security (OLS)
- Calculation Groups
- Incremental Refresh
- Composite Models
- Direct Lake
- Real-Time Analytics

---

# Design Summary

The semantic model was intentionally designed as a **Galaxy (Fact Constellation) Schema** to support multiple analytical domains while maintaining shared business dimensions and consistent enterprise reporting.

This modelling approach aligns with Microsoft Fabric best practices by combining dimensional modelling, semantic modelling and AI-generated business intelligence into a unified analytical platform.

---

# Related Documentation

- architecture.md
- ai-enrichment.md
- deployment.md
- cicd.md
