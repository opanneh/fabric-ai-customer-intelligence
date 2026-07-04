#!/usr/bin/env python
# coding: utf-8

# ## NB_RAW_To_Bronze
# 
# null

# In[1]:


# ==========================================================
# Notebook : NB_RAW_To_Bronze
# Purpose  : Ingest raw source files into the Bronze layer
# Layer    : Bronze
# ==========================================================

from pyspark.sql import DataFrame
from pyspark.sql.functions import *

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

RAW_PATH = "Files/RAW"

BRONZE_SCHEMA = "Bronze"

SOURCE_SYSTEM = "GitHub"

# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def add_metadata(df: DataFrame, source_file: str) -> DataFrame:
    """
    Add ingestion metadata.
    """

    return (
        df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("ingestion_date", current_date())
        .withColumn("source_system", lit(SOURCE_SYSTEM))
        .withColumn("source_file", lit(source_file))
    )


def write_bronze(df: DataFrame, table_name: str):
    """
    Save dataframe as a managed Delta table
    in the Bronze schema.
    """

    (
        df.write
        .mode("overwrite")
        .format("delta")
        .saveAsTable(f"{BRONZE_SCHEMA}.{table_name}")
    )

    print(f"✓ Bronze.{table_name} loaded")


def read_csv(file_name: str) -> DataFrame:
    """
    Read CSV file from RAW.
    """

    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(f"{RAW_PATH}/{file_name}")
    )


def read_json(file_name: str) -> DataFrame:
    """
    Read JSON file from RAW.
    """

    return spark.read.json(
        f"{RAW_PATH}/{file_name}"
    )


def load_csv(file_name: str, table_name: str) -> DataFrame:
    """
    Load CSV file into Bronze.
    """

    print(f"Loading {file_name}...")

    df = read_csv(file_name)

    df = add_metadata(df, file_name)

    write_bronze(df, table_name)

    return df


def load_json(file_name: str, table_name: str) -> DataFrame:
    """
    Load JSON file into Bronze.
    """

    print(f"Loading {file_name}...")

    df = read_json(file_name)

    df = add_metadata(df, file_name)

    write_bronze(df, table_name)

    return df


def validate(df: DataFrame, table_name: str):
    """
    Display row count.
    """

    print(
        f"{table_name:<20}"
        f"{df.count():>10} rows"
    )

# ----------------------------------------------------------
# Load CSV Files
# ----------------------------------------------------------

customers_df = load_csv(
    "customers.csv",
    "Customers"
)

products_df = load_csv(
    "products.csv",
    "Products"
)

orders_df = load_csv(
    "orders.csv",
    "Orders"
)

# ----------------------------------------------------------
# Load JSON Files
# ----------------------------------------------------------

reviews_df = load_json(
    "reviews.json",
    "Reviews"
)

social_df = load_json(
    "social_media.json",
    "SocialMedia"
)

web_df = load_json(
    "web_logs.json",
    "WebLogs"
)

# ----------------------------------------------------------
# Validation
# ----------------------------------------------------------

print("=" * 60)
print("RAW TO BRONZE SUMMARY")
print("=" * 60)

validate(customers_df, "Customers")
validate(products_df, "Products")
validate(orders_df, "Orders")
validate(reviews_df, "Reviews")
validate(social_df, "SocialMedia")
validate(web_df, "WebLogs")

print("=" * 60)

