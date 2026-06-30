# 🚀 Fabric AI Customer Intelligence Platform

An end-to-end **Microsoft Fabric** solution implementing a modern **Medallion Architecture** to ingest, transform, enrich, and analyze customer data. The platform combines **Data Engineering**, **Business Intelligence**, and **Generative AI** to provide actionable customer insights through Microsoft Fabric, Azure AI Foundry, and Power BI.

---

## 📌 Project Overview

Organizations collect customer information from multiple channels such as:

- Customer transactions
- Product catalog
- Customer reviews
- Social media
- Website activity

This project demonstrates how Microsoft Fabric can unify these data sources into a **Customer 360 Analytics Platform**, enriched with **GPT-5 AI insights** and presented through interactive Power BI dashboards.

---

## 🏗 Solution Architecture

```text
                   GitHub / External Sources
                              │
                              ▼
                     Fabric Data Pipeline
                              │
                              ▼
                     OneLake - Raw Layer
                              │
                              ▼
                     OneLake - Bronze Layer
                              │
                              ▼
                  PySpark Data Transformation
                              │
                              ▼
                     OneLake - Silver Layer
                              │
                              ▼
                  Feature Engineering Notebook
                              │
                              ▼
                Azure AI Foundry (GPT-5)
                              │
                              ▼
                     AI Enrichment Layer
                              │
                              ▼
                      OneLake - Gold Layer
                              │
                              ▼
                    Power BI Semantic Model
                              │
                              ▼
                   Executive Dashboards
```

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Microsoft Fabric | End-to-end analytics platform |
| Fabric Data Factory | Data ingestion & orchestration |
| OneLake | Centralized storage |
| Lakehouse | Medallion architecture |
| PySpark | Data transformation |
| Delta Lake | Reliable data storage |
| Azure AI Foundry | GPT-5 AI enrichment |
| Power BI | Reporting & visualization |
| GitHub | Version control |

---

# 📂 Project Structure

```
fabric-ai-customer-intelligence
│
├── data
│   ├── raw
│   ├── bronze
│   ├── silver
│   └── gold
│
├── notebooks
│   ├── 01_Bronze_to_Silver
│   ├── 02_Feature_Engineering
│   ├── 03_AI_Review_Enrichment
│   ├── 04_Gold_Data_Model
│   └── 05_PowerBI_Dataset
│
├── pipelines
│   └── PL_01_Ingest_Customer_Data
│
├── dashboards
│   └── Customer_Intelligence.pbix
│
├── docs
│   ├── architecture.png
│   ├── dataflow.png
│   └── erd.png
│
└── README.md
```

---

# 📊 Data Sources

| Dataset | Format |
|----------|--------|
| Customers | CSV |
| Products | CSV |
| Orders | CSV |
| Customer Reviews | JSON |
| Social Media | JSON |
| Website Activity | JSON |

---

# 🥉 Bronze Layer

The Bronze layer stores the first managed copy of the source data.

Operations:

- Schema enforcement
- Metadata enrichment
- Delta conversion
- Ingestion logging

No business transformations are applied.

---

# 🥈 Silver Layer

The Silver layer prepares data for analytics.

Processing includes:

- Data cleansing
- Duplicate removal
- Null handling
- Data validation
- Standardization
- Business rule validation

---

# 🤖 AI Enrichment

Customer reviews are enriched using **Azure AI Foundry GPT-5**.

Each review is analyzed to generate:

- Sentiment
- Category
- Priority
- Summary
- Keywords
- Customer Emotion
- Recommended Department
- Suggested Resolution

Example:

```json
{
  "sentiment": "Negative",
  "category": "Delivery",
  "priority": "High",
  "summary": "Customer experienced delayed delivery and damaged packaging.",
  "keywords": [
    "delivery",
    "shipping",
    "damage"
  ]
}
```

---

# 🥇 Gold Layer

The Gold layer contains curated business-ready datasets.

### Customer360

- Customer Lifetime Value
- Total Orders
- Revenue
- Satisfaction
- Sentiment

### Product360

- Units Sold
- Revenue
- Rating
- Stock
- AI Insights

### Executive KPIs

- Revenue
- Orders
- Average Rating
- Customer Satisfaction
- Top Products
- Top Categories

---

# 📈 Power BI Dashboards

The project includes several business dashboards:

### Executive Overview

- Revenue
- Orders
- Growth
- Customer Satisfaction

### Customer 360

- Customer Segments
- Lifetime Value
- Purchase Behaviour

### Product Performance

- Best Selling Products
- Inventory
- Ratings

### AI Customer Insights

- Sentiment Analysis
- Complaint Categories
- Customer Emotions
- Recommended Actions

### Customer Journey

- Website Activity
- Purchase Flow
- Customer Feedback

---

# 🔄 Data Flow

```text
GitHub
   │
   ▼
Fabric Data Factory
   │
   ▼
Raw
   │
   ▼
Bronze
   │
   ▼
Silver
   │
   ▼
Feature Engineering
   │
   ▼
Azure AI Foundry GPT-5
   │
   ▼
Gold
   │
   ▼
Power BI
```

---

# 🎯 Business Value

The platform enables organizations to:

- Build a Customer 360 view
- Understand customer sentiment
- Identify customer pain points
- Improve customer support
- Optimize product quality
- Support data-driven decision making

---

# 🚀 Future Improvements

- Incremental data ingestion
- Streaming customer events
- AI-powered customer segmentation
- Customer churn prediction
- Product recommendation engine
- RAG-powered customer support assistant
- CI/CD with GitHub Actions and Microsoft Fabric deployment pipelines

---

# 📌 Skills Demonstrated

- Microsoft Fabric
- Fabric Data Factory
- OneLake
- Medallion Architecture
- PySpark
- Delta Lake
- Azure AI Foundry
- GPT-5 Integration
- Prompt Engineering
- Power BI
- Data Modeling
- Feature Engineering
- Git & GitHub

---

## 👨‍💻 Author

**Ousainou Panneh**

Data Engineer | BI Developer | AI & Data Science Enthusiast

```

---

### One recommendation

To make this repository stand out even more, add these images to the `docs/` folder and reference them in the README:

1. **Architecture Diagram** (overall platform)
2. **Medallion Architecture Diagram**
3. **Fabric Data Factory Pipeline Screenshot**
4. **Lakehouse Structure**
5. **Power BI Dashboard Screenshots**
6. **GPT-5 AI Enrichment Flow**

Those visuals make the repository much more engaging and help recruiters quickly understand the end-to-end solution.
