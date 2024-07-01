from sqlalchemy.dialects import registry

# List all registered dialects
dialects = registry.impls

print("Available SQLAlchemy Dialects:")
for dialect in dialects:
    print(f" - {dialect}")