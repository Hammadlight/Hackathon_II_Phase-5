# backend/app/database.py

import os
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

from sqlmodel import create_engine
from dotenv import load_dotenv

load_dotenv()


def _ensure_pg_sslmode_require(db_url: str) -> str:
    """
    Neon / managed Postgres requires SSL.
    Force sslmode=require if missing
    """
    if not db_url:
        return db_url

    if not db_url.startswith(("postgresql://", "postgres://")):
        return db_url

    parsed = urlparse(db_url)
    query = parse_qs(parsed.query)

    if "sslmode" not in query:
        query["sslmode"] = ["require"]

    return urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parsed.params,
            urlencode(query, doseq=True),
            parsed.fragment,
        )
    )


DATABASE_URL = _ensure_pg_sslmode_require(os.getenv("DATABASE_URL", ""))

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is missing")

# ✅ IMPORTANT FIXES:
# - pool_pre_ping → fixes 'SSL connection closed unexpectedly'
# - pool_recycle → avoids long idle SSL drop
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=1800,
)
