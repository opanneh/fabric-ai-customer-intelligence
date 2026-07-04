#!/usr/bin/env python
# coding: utf-8

# ## NB_Customer_Insight_Enrichment
# 
# null

# In[2]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %pip install openai


# In[3]:


# ==========================================================
# Notebook : NB_Customer_Insight_Enrichment
# Purpose  : Generate AI-powered customer insights
# Layer    : Silver
# ==========================================================

from openai import OpenAI
import json
import pandas as pd
from pyspark.sql.functions import *

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

SILVER_PATH = "Tables/Silver"

ENDPOINT = "https://pannehousai-4112-resource.services.ai.azure.com/openai/v1"

API_KEY = "MY-API-KEY"

DEPLOYMENT_NAME = "gpt-5-mini"

AI_SAMPLE_FRACTION = 0.05
AI_SAMPLE_SEED = 42

client = OpenAI(
    base_url=ENDPOINT,
    api_key=API_KEY
)

# ----------------------------------------------------------
# Read Silver Tables
# ----------------------------------------------------------

reviews = spark.read.format("delta").load(
    f"{SILVER_PATH}/Reviews"
)

customer_features = spark.read.format("delta").load(
    f"{SILVER_PATH}/CustomerFeatures"
)

product_features = spark.read.format("delta").load(
    f"{SILVER_PATH}/ProductFeatures"
)

# ----------------------------------------------------------
# Join Business Context
# ----------------------------------------------------------

reviews_context = (
    reviews
    .join(
        customer_features,
        reviews.customer_id == customer_features.CustomerID,
        "left"
    )
    .drop("CustomerID")
    .join(
        product_features,
        reviews.product_id == product_features.ProductID,
        "left"
    )
    .drop("ProductID")
)

# ----------------------------------------------------------
# Random Sample for AI Enrichment
# ----------------------------------------------------------

pdf = (
    reviews_context
    .sample(False, AI_SAMPLE_FRACTION, seed=AI_SAMPLE_SEED)
    .toPandas()
)

print(f"Reviews selected for AI enrichment: {len(pdf)}")

# ----------------------------------------------------------
# GPT-5 Customer Insight Enrichment
# ----------------------------------------------------------

results = []

for _, row in pdf.iterrows():

    prompt = f"""
You are a Customer Experience Analyst.

Analyse the following customer review using the available customer and product information.

Customer
---------
Location: {row.get('Location', '')}
Total Orders: {row.get('TotalOrders', 0)}
Total Revenue: {row.get('TotalRevenue', 0)}

Product
--------
Product Name: {row.get('ProductName', '')}
Category: {row.get('Category', '')}

Review
------
Rating: {row.get('rating', '')}

Review Text:
{row.get('review_text', '')}

Return ONLY valid JSON.

{{
  "sentiment":"",
  "category":"",
  "priority":"",
  "summary":"",
  "keywords":[],
  "recommended_action":""
}}

Rules

Sentiment MUST be ONLY:
- Positive
- Negative
- Neutral

Priority MUST be ONLY:
- High
- Medium
- Low

Category MUST be ONE of:
- Product Quality
- Customer Service
- Pricing
- Delivery
- Website
- Security
- Payment
- General Feedback

Recommended Action MUST be ONE of:
- No Action Required
- Monitor Customer Feedback
- Forward to Customer Support
- Notify Product Team
- Review Pricing Strategy
- Contact Logistics Team
- Escalate to Security Team

Summary:
- One concise sentence.

Keywords:
- Between 3 and 5 keywords.

Return ONLY valid JSON.
"""

    try:

        response = client.responses.create(
            model=DEPLOYMENT_NAME,
            input=prompt
        )

        result = json.loads(response.output_text)

    except Exception as ex:

        result = {
            "sentiment": "Neutral",
            "category": "General Feedback",
            "priority": "Low",
            "summary": str(ex),
            "keywords": [],
            "recommended_action": "Monitor Customer Feedback"
        }

    results.append({

        "customer_id": row["customer_id"],

        "product_id": row["product_id"],

        "rating": row["rating"],

        "review_text": row["review_text"],

        "timestamp": row["timestamp"],

        "sentiment": result.get("sentiment", "Neutral"),

        "category": result.get("category", "General Feedback"),

        "priority": result.get("priority", "Low"),

        "summary": result.get("summary", ""),

        "keywords": ", ".join(result.get("keywords", [])),

        "recommended_action": result.get(
            "recommended_action",
            "Monitor Customer Feedback"
        ),

        "ai_model": DEPLOYMENT_NAME,

        "analysis_timestamp": pd.Timestamp.now()

    })

# ----------------------------------------------------------
# Create Spark DataFrame
# ----------------------------------------------------------

insights_df = spark.createDataFrame(
    pd.DataFrame(results)
)

# ----------------------------------------------------------
# Save Review Insights
# ----------------------------------------------------------

(
    insights_df.write
    .mode("overwrite")
    .format("delta")
    .saveAsTable("Silver.ReviewInsights")
)

# ----------------------------------------------------------
# Validation
# ----------------------------------------------------------

display(insights_df)

print("=" * 60)
print("CUSTOMER INSIGHT ENRICHMENT SUMMARY")
print("=" * 60)
print(f"AI Model          : {DEPLOYMENT_NAME}")
print(f"Reviews Analysed  : {insights_df.count()}")
print(f"Output Table      : Silver.ReviewInsights")
print("=" * 60)

