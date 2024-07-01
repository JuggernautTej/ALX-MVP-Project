from sqlalchemy.dialects import registry
import mysql.connector

# Manually register the MySQL dialect
registry.register("mysql.mysqlconnector", "mysql.connector", "MySQLDialect_mysqlconnector")

# List all registered dialects
dialects = registry.impls

print("Available SQLAlchemy Dialects:")
for dialect in dialects:
    print(f" - {dialect}")
