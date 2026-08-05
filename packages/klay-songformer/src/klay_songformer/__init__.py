from pathlib import Path

__version__ = "0.1.0"

_VENDOR = Path(__file__).parent / "_vendor"

SONGFORMER_SRC = _VENDOR / "SongFormer"
SONGFORMER_THIRD_PARTY = _VENDOR / "third_party"

__all__ = ["SONGFORMER_SRC", "SONGFORMER_THIRD_PARTY", "__version__"]
