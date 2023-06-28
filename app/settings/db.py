from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

from app.settings.env import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_SCHEME, DB_NAME

DATABASE_URL = "".join(["postgresql://", DB_USER, ":", DB_PASSWORD,
                        "@", DB_HOST, ":", DB_PORT, "/", DB_NAME])

engine = create_engine(
    DATABASE_URL,
    echo=True
)
metadata = MetaData(schema=DB_SCHEME)
Base = declarative_base(metadata=metadata)
