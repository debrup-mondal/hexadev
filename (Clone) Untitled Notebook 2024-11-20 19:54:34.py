# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog dev

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog uat

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog uat2

# COMMAND ----------

# MAGIC %sql
# MAGIC create table dev.testschema.table1 (id int primary key, name string)
