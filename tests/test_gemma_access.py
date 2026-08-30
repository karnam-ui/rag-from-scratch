import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from generation.gemma_gen import GemmaGenerator


def test_gemma_generator_allows_public_model_without_login(monkeypatch):
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("HUGGINGFACE_HUB_TOKEN", raising=False)
    monkeypatch.delenv("HUGGINGFACE_TOKEN", raising=False)

    assert GemmaGenerator._validate_access("TinyLlama/TinyLlama-1.1B-Chat-v1.0") is None


def test_gemma_generator_uses_public_default_without_login(monkeypatch):
    monkeypatch.delenv("HF_TOKEN", raising=False)
    monkeypatch.delenv("HUGGINGFACE_HUB_TOKEN", raising=False)
    monkeypatch.delenv("HUGGINGFACE_TOKEN", raising=False)

    assert GemmaGenerator.DEFAULT_MODEL == "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


