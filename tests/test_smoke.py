"""Smoke test: the reconstructed visionquantech_complete.py must stay intact.

Verifies (stdlib only, no tkinter/display needed):
  - the file parses
  - all four expected classes exist
  - VisionQuantechOS exposes the full method surface the UI wires up
  - no hardcoded API key / secret literal is present
"""
import ast
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
TARGET = ROOT / "visionquantech_complete.py"

EXPECTED_METHODS = {
    "__init__", "check_license", "validate_license", "show_license_screen",
    "setup_main_ui", "create_sections",
    "add_field", "add_text", "ai_generate", "ai_generate_colors",
    "edit_color", "send_ai_message", "upload_logo",
    "generate", "get_data", "build_website",
    "edit", "export", "preview_web", "deploy",
    "save_project", "load_project", "start_autosave", "serve",
}


def test_file_parses():
    tree = ast.parse(TARGET.read_text(encoding="utf-8"))
    assert isinstance(tree, ast.Module)


def test_expected_classes_exist():
    tree = ast.parse(TARGET.read_text(encoding="utf-8"))
    names = {n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)}
    assert {"ExpandableSection", "AIAssistant", "SupportTicket",
            "VisionQuantechOS"} <= names


def test_visionquantech_os_method_surface():
    tree = ast.parse(TARGET.read_text(encoding="utf-8"))
    cls = next(n for n in ast.walk(tree)
               if isinstance(n, ast.ClassDef) and n.name == "VisionQuantechOS")
    methods = {n.name for n in cls.body
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    assert EXPECTED_METHODS <= methods, EXPECTED_METHODS - methods


def test_no_hardcoded_secrets():
    text = TARGET.read_text(encoding="utf-8")
    hits = re.findall(r'(?m)^[A-Z_]*?(?:API_KEY|SECRET|TOKEN|PASSWORD)\s*=\s*["\'][^"\']{8,}["\']', text)
    assert not hits, hits
