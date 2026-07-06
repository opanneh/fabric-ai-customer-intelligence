# 🤖 AI Enrichment

## Overview

The **Fabric AI Customer Intelligence Platform** integrates **Generative AI** directly into the Microsoft Fabric **Medallion Architecture**, enriching customer reviews with structured business intelligence before they are loaded into the enterprise analytical warehouse.

Unlike traditional reporting solutions where AI executes inside dashboards or applications, this platform performs AI enrichment during the **Silver Layer** transformation process. This design converts unstructured customer feedback into trusted analytical data that can be reused consistently across dashboards, reports and future analytical solutions.

---

# 🎯 Design Objectives

The AI enrichment process was designed to:

- Transform unstructured customer reviews into structured business attributes
- Generate reusable AI-enhanced datasets
- Improve customer intelligence reporting
- Eliminate repeated AI processing
- Integrate AI into the enterprise data engineering pipeline
- Support scalable analytical workloads

---

# 🤖 AI Enrichment Workflow

Customer reviews are enriched immediately after Silver-layer processing. Once data has been cleansed and standardized, Azure AI Foundry (GPT-5) generates structured business attributes that are persisted back into the Lakehouse before loading into the Gold Warehouse.

```text
Customer Reviews
        │
        ▼
Bronze Lakehouse
        │
        ▼
Silver Transformation
        │
        ▼
Feature Engineering
        │
        ▼
Azure AI Foundry (GPT-5)
        │
        ▼
AI-Enriched Reviews
        │
        ▼
Silver Lakehouse
        │
        ▼
Fabric Data Factory
        │
        ▼
Fabric Warehouse
        │
        ▼
Power BI Semantic Model
```

| Stage | Purpose | Technology |
|--------|---------|------------|
| Bronze | Preserve raw customer reviews | OneLake Lakehouse |
| Silver | Cleanse and validate customer reviews | PySpark |
| Feature Engineering | Prepare text for AI inference | PySpark |
| AI Enrichment | Generate structured business attributes | Azure AI Foundry (GPT-5) |
| Gold | Store AI-enriched analytical data | Fabric Warehouse |
| Reporting | Deliver governed business insights | Power BI |

This workflow ensures AI-generated attributes become part of the governed enterprise dataset before analytical modelling.

---

# ⭐ Why AI in the Silver Layer?

Positioning AI enrichment between the Silver and Gold layers provides several enterprise benefits.

| Benefit | Business Value |
|----------|----------------|
| Trusted Input | AI processes validated and standardized customer reviews |
| Reusable Intelligence | AI-generated attributes are reused across multiple reports |
| Improved Performance | Reports consume precomputed AI attributes rather than invoking AI at runtime |
| Consistent Business Logic | All reports use the same governed AI-generated insights |

---

# 🛠 Business Feature Engineering

Before AI processing, customer reviews undergo several preparation steps:

- Text standardization
- Null handling
- Duplicate removal
- Data validation
- Business rule validation
- Feature engineering

Preparing high-quality input data improves the consistency and reliability of AI-generated outputs.

---

# 💬 Prompt Engineering

Azure AI Foundry (GPT-5) is instructed to generate structured business information rather than free-text responses.

The prompt is designed to produce:

- Deterministic outputs
- Structured JSON responses
- Business-oriented categorization
- Consistent sentiment classification

---

# 📄 AI Output

Each customer review is enriched with additional business attributes.

Generated fields include:

- Sentiment
- Category
- Priority
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
  "recommended_action": "Escalate to Logistics Team."
}
```

---

# 🥇 Gold Layer Integration

After enrichment, the AI-generated attributes are promoted to the **Fabric Warehouse**, where they populate the **FactCustomerSentiment** table within the enterprise **Galaxy Schema**.

This allows AI-generated insights to become governed analytical assets that are consumed consistently across the semantic model.

---

# 📊 Business Intelligence Consumption

The enriched data powers the **AI Customer Insights** dashboard.

Business users can analyse:

- Customer sentiment
- Complaint categories
- Business priorities
- Recommended actions
- AI-generated summaries

Because AI attributes are stored within the warehouse, dashboards remain responsive while delivering consistent analytical results.

---

# 💼 Business Value

Integrating AI into the engineering pipeline enables organisations to:

- Detect customer dissatisfaction earlier
- Prioritize operational issues
- Identify recurring complaint themes
- Improve customer service response
- Support executive decision-making
- Build reusable AI-enhanced datasets

This architecture also enables future machine learning models and enterprise applications to consume AI-generated attributes without additional processing.

---

# 🚀 Future Enhancements

The AI enrichment layer can be extended with:

- Multilingual sentiment analysis
- Aspect-based sentiment analysis
- Named Entity Recognition (NER)
- Product issue classification
- Customer churn prediction
- Automatic ticket routing
- RAG-powered customer support assistant
- Streaming AI enrichment

---

# 📌 Design Summary

The AI enrichment layer transforms customer feedback from unstructured text into governed enterprise intelligence.

By integrating Azure AI Foundry (GPT-5) directly into the Microsoft Fabric Medallion Architecture, the platform demonstrates how Generative AI can become a reusable enterprise data asset rather than an isolated reporting feature.

---

# 📚 Related Documentation

- 📖 [Solution Architecture](architecture.md)
- 🌌 [Semantic Model](semantic-model.md)
- 🚀 [Deployment Strategy](deployment.md)
- ⚙️ [CI/CD & DevOps](cicd.md)
