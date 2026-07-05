# 🤖 AI Enrichment

## Overview

The **Fabric AI Customer Intelligence Platform** integrates **Generative AI** directly into the Microsoft Fabric Medallion Architecture to enrich customer reviews with business-ready insights before they are loaded into the analytical warehouse.

Unlike traditional reporting solutions where AI is executed inside dashboards or applications, this platform performs AI enrichment as part of the **Silver Layer** transformation process.

This approach transforms unstructured customer feedback into trusted analytical data that can be reused across multiple business reports, dashboards and downstream applications.

---

# Design Objectives

The AI enrichment process was designed to:

- Transform unstructured customer reviews into structured business attributes
- Create reusable AI-generated datasets
- Improve customer intelligence reporting
- Eliminate repeated AI processing across reports
- Integrate AI directly into the enterprise data engineering pipeline
- Support scalable analytical workloads

---

# AI Architecture

![AI Enrichment Architecture](images/ai-enrichment-flow.png)

The AI enrichment workflow is integrated into the Silver layer.

```text
Raw Reviews
      │
      ▼
Bronze Lakehouse
      │
      ▼
Silver Transformation
      │
      ▼
Business Feature Engineering
      │
      ▼
Azure AI Foundry (GPT-5)
      │
      ▼
AI Enriched Reviews
      │
      ▼
Silver Lakehouse (Enriched)
      │
      ▼
Data Factory Pipeline
      │
      ▼
Gold Warehouse
      │
      ▼
Power BI
```

This architecture ensures AI-generated attributes become part of the governed enterprise dataset before analytical modelling.

---

# Why AI in the Silver Layer?

The AI enrichment process was intentionally positioned between the Silver and Gold layers.

Rather than executing AI during reporting, enrichment is performed once after data cleansing and feature engineering have been completed.

This provides several advantages.

## Trusted Input Data

Customer reviews are standardized and validated before being submitted to the AI model.

This improves response quality and reduces inconsistencies.

---

## Reusable Intelligence

AI-generated attributes become part of the enterprise dataset and can be reused across:

- Executive dashboards
- Customer analytics
- Operational reporting
- Future machine learning models
- External applications

---

## Improved Performance

Reports consume pre-computed AI attributes rather than executing AI requests at runtime.

Benefits include:

- Faster report performance
- Reduced API costs
- Lower latency
- Improved scalability

---

## Consistent Business Logic

AI processing occurs once during data engineering.

Every report consumes identical AI outputs, ensuring consistent business definitions across the organization.

---

# Business Feature Engineering

Before AI processing, customer reviews undergo feature engineering.

Typical transformations include:

- Text standardization
- Whitespace removal
- Null handling
- Duplicate detection
- Data validation
- Business rule validation

Preparing the data before AI enrichment improves response quality and consistency.

---

# Prompt Engineering

Azure AI Foundry (GPT-5) is instructed to analyze each customer review and return structured business information.

Rather than generating free-text responses, the model produces predictable structured attributes suitable for analytical processing.

The prompt was designed to encourage:

- Deterministic output
- Structured formatting
- Business-oriented categorization
- Consistent sentiment classification

---

# AI Output

Each customer review is enriched with additional business attributes.

Generated fields include:

- Sentiment
- Review Category
- Business Priority
- Summary
- Keywords
- Recommended Action

Example output:

```json
{
  "sentiment": "Negative",
  "category": "Delivery",
  "priority": "High",
  "summary": "Customer experienced delayed delivery and damaged packaging.",
  "keywords": [
    "delivery",
    "damage",
    "shipping"
  ],
  "recommended_action": "Escalate to logistics team."
}
```

---

# Gold Layer Integration

Once AI enrichment has completed successfully, the enriched Silver dataset is promoted into the Gold Warehouse through Microsoft Fabric Data Factory.

The enriched attributes populate the **FactCustomerSentiment** table within the enterprise Galaxy Schema.

This enables AI-generated insights to become first-class analytical entities within the semantic model.

---

# Reporting Integration

The enriched data powers the **AI Customer Insights** dashboard.

Business users can analyze:

- Customer sentiment distribution
- Review categories
- High-priority issues
- Recommended business actions
- AI-generated summaries

Because AI attributes are stored within the warehouse, reports remain responsive while maintaining consistent analytical results.

---

# Business Value

Integrating AI directly into the engineering pipeline provides measurable business benefits.

The platform enables organizations to:

- Detect customer dissatisfaction earlier
- Prioritize operational issues
- Identify recurring complaint themes
- Improve customer service response
- Support executive decision-making
- Build reusable AI-enhanced datasets

The architecture also allows future analytical models to consume AI-generated attributes without additional processing.

---

# Design Decisions

Several architectural decisions influenced the AI implementation.

### AI executes after Silver transformations

Ensures trusted, standardized input data.

---

### AI executes before Gold loading

Allows AI-generated attributes to become part of the governed analytical model.

---

### AI output stored in warehouse

Provides reusable business intelligence across multiple reports.

---

### AI processing is centralized

Prevents duplicate processing within Power BI reports or downstream applications.

---

# Future Enhancements

The AI enrichment layer can be extended with:

- Multilingual sentiment analysis
- Aspect-based sentiment analysis
- Named Entity Recognition (NER)
- Product issue classification
- Customer churn prediction
- Automatic ticket routing
- RAG-powered customer support assistant
- Batch and streaming AI enrichment

---

# Design Summary

The AI enrichment layer transforms customer feedback from unstructured text into governed business intelligence.

By integrating GPT-5 directly into the Microsoft Fabric Medallion Architecture, the platform extends traditional data engineering with enterprise AI capabilities while maintaining scalability, consistency and analytical performance.

This architecture demonstrates how Generative AI can become an integral component of a modern enterprise analytics platform rather than an isolated reporting feature.

---

# Related Documentation

- architecture.md
- semantic-model.md
- deployment.md
- cicd.md
