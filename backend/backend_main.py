"""
Shared backend entrypoint.

Canonical way to run the backend API server::

    from backend.backend_main import serve
    serve()

This module is a thin launcher around the working FastAPI application in
``api_backend.py``. (A previous revision defined a separate "WorldMind OS" app
here that imported the non-existent ``app.core`` / ``app.api`` packages, so it
could never be imported. This module now delegates to the real app instead.)
"""
import logging

logger = logging.getLogger("shared.backend_main")

try:
    # Normal case: imported as part of the ``backend`` package from the repo root.
    from backend.api_backend import app, serve
except ImportError:  # pragma: no cover - running directly from inside backend/
    from api_backend import app, serve

__all__ = ["app", "serve"]

if __name__ == "__main__":
    serve()
