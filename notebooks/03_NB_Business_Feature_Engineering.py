#!/usr/bin/env python
# coding: utf-8

# ## NB_Business_Feature_Engineering
# 
# null

# In[2]:


# ==========================================================
# Notebook : NB_Business_Feature_Engineering
# Purpose  : Generate reusable business feature tables
# Layer    : Silver
# ==========================================================

from pyspark.sql.functions import *
from pyspark.sql import DataFrame

# ==========================================================
# Configuration
# ==========================================================

SILVER_PATH = "Tables/Silver"

# ==========================================================
# Helper Functions
# ==========================================================

def read_silver(table_name: str) -> DataFrame:

    return (
        spark.read
        .format("delta")
        .load(f"{SILVER_PATH}/{table_name}")
    )


def write_silver(df: DataFrame, table_name: str):

    (
        df.write
        .mode("overwrite")
        .format("delta")
        .save(f"{SILVER_PATH}/{table_name}")
    )

    print(f"✓ Silver.{table_name} created")


def validate(df: DataFrame, table_name: str):

    print(f"{table_name:<25}{df.count():>10} rows")


# ==========================================================
# Read Silver Tables
# ==========================================================

customers = read_silver("Customers")

products = read_silver("Products")

orders = read_silver("Orders")

reviews = read_silver("Reviews")

social = read_silver("SocialMedia")

web = read_silver("WebLogs")

# ==========================================================
# Customer Features
# ==========================================================

customer_orders = (

    orders

    .groupBy("CustomerID")

    .agg(

        countDistinct("OrderID").alias("TotalOrders"),

        round(sum("TotalAmount"),2).alias("TotalRevenue"),

        round(avg("TotalAmount"),2).alias("AverageOrderValue")

    )

)

customer_reviews = (

    reviews

    .groupBy("customer_id")

    .agg(

        round(avg("rating"),2).alias("AverageRating")

    )

)

customer_features = (

    customers

    .join(customer_orders,"CustomerID","left")

    .join(
        customer_reviews,
        customers.CustomerID == customer_reviews.customer_id,
        "left"
    )

    .drop("customer_id")

)

write_silver(customer_features,"CustomerFeatures")

validate(customer_features,"CustomerFeatures")

# ==========================================================
# Product Features
# ==========================================================

product_sales = (

    orders

    .groupBy("ProductID")

    .agg(

        sum("Quantity").alias("UnitsSold"),

        round(sum("TotalAmount"),2).alias("Revenue")

    )

)

product_reviews = (

    reviews

    .groupBy("product_id")

    .agg(

        round(avg("rating"),2).alias("AverageRating")

    )

)

product_features = (

    products

    .join(product_sales,"ProductID","left")

    .join(
        product_reviews,
        products.ProductID == product_reviews.product_id,
        "left"
    )

    .drop("product_id")

)

write_silver(product_features,"ProductFeatures")

validate(product_features,"ProductFeatures")

# ==========================================================
# Sales Features
# ==========================================================

sales_features = (

    orders

    .groupBy(

        to_date("OrderDate").alias("OrderDate"),

        "PaymentMethod"

    )

    .agg(

        countDistinct("OrderID").alias("Orders"),

        sum("Quantity").alias("UnitsSold"),

        round(sum("TotalAmount"),2).alias("Revenue")

    )

)

write_silver(sales_features,"SalesFeatures")

validate(sales_features,"SalesFeatures")

# ==========================================================
# Customer Journey
# ==========================================================

web_activity = (

    web

    .groupBy("user_id")

    .agg(

        count("*").alias("TotalVisits"),

        max("timestamp").alias("LastActivity")

    )

)

customer_journey = (

    web_activity

    .join(

        customer_orders,

        web_activity.user_id == customer_orders.CustomerID,

        "left"

    )

    .drop("CustomerID")

)

write_silver(customer_journey,"CustomerJourney")

validate(customer_journey,"CustomerJourney")

# ==========================================================
# Review Features
# ==========================================================

review_features = (

    reviews

    .groupBy("product_id")

    .agg(

        count("*").alias("ReviewCount"),

        round(avg("rating"),2).alias("AverageRating")

    )

)

write_silver(review_features,"ReviewFeatures")

validate(review_features,"ReviewFeatures")

# ==========================================================
# Summary
# ==========================================================

print("="*60)
print("BUSINESS FEATURE ENGINEERING SUMMARY")
print("="*60)

validate(customer_features,"CustomerFeatures")
validate(product_features,"ProductFeatures")
validate(sales_features,"SalesFeatures")
validate(customer_journey,"CustomerJourney")
validate(review_features,"ReviewFeatures")

