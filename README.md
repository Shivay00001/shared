# Shared — VisionQuantech OS Website Builder

Two parts:

1. **Desktop GUI app (tkinter)** — `visionquantech_complete.py`: an AI website-builder style desktop app (edits, previews, and exports sites).
   ```bash
   python visionquantech_complete.py
   ```
2. **FastAPI fragment** — `backend/api_backend.py`: a standalone YOU.DAO API with 14 routes (health, decisions, proposals, licenses, metrics). Not wired to the tkinter app; load it on its own:
   ```bash
   pip install fastapi uvicorn
   uvicorn backend.api_backend:app --reload
   ```
   (Also contains unrelated frontend TypeScript sources and a blockchain sketch.)

Requires Python 3.10+ with tkinter for the desktop part. Verified 2026-09-24 on Python 3.12 (Linux, xvfb): tkinter window initializes with no errors; FastAPI app imports cleanly with 14 routes.

The desktop app is not cloud-deployable; the FastAPI fragment is deployable as an API service if wired to a real data source.
