# Databricks notebook source
# s3 bucket for raw ingestion 
s3_path = f"s3a://jake.wong.sg/"
mount_to = f"/mnt/jake.wong.sg"

try:
  dbutils.fs.mount(s3_path, mount_to)
  print(s3_path, "mount ok")
except:
  print(s3_path, "already mounted to", mount_to)

# COMMAND ----------


