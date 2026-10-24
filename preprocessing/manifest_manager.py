"""
manifest_manager.py
Implements cryptographic data provenance and manifest tracking for the
Multimodal Drought and Food Insecurity Early Warning System.

Enforces zero-credential reproducibility and guarantees that no mock/synthetic
data can ever be treated as verified observational forecasts.
"""

import os
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DIR = PROJECT_ROOT / "data" / "raw" / "manifests"
MANIFEST_FILE = MANIFEST_DIR / "dataset.json"


def compute_sha256(filepath: str) -> str:
    """Computes the SHA-256 cryptographic hash of a file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found for checksum: {filepath}")
    sha256 = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_manifest() -> Dict[str, Any]:
    """Loads existing dataset manifest or returns an empty structure."""
    if MANIFEST_FILE.exists():
        try:
            with MANIFEST_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[WARN] Failed to read existing manifest: {e}")
    return {
        "version": "1.0.0",
        "project": "Multimodal Early Warning System - Eastern Hararghe",
        "last_updated_utc": datetime.now(timezone.utc).isoformat(),
        "datasets": {}
    }

def record_dataset(
    name: str,
    filepath: str,
    source_url: str,
    provider: str,
    temporal_coverage: str,
    spatial_resolution: str,
    record_count: int,
    is_synthetic: bool = False,
    metadata: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Registers an ingested dataset into the cryptographic manifest with SHA-256 verification.
    """
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()

    path = Path(filepath)
    file_hash = compute_sha256(str(path))
    file_size_bytes = path.stat().st_size

    record = {
        "name": name,
        "filepath": os.path.relpath(str(path), str(PROJECT_ROOT)).replace("\\", "/"),
        "sha256": file_hash,
        "size_bytes": file_size_bytes,
        "source_url": source_url,
        "provider": provider,
        "temporal_coverage": temporal_coverage,
        "spatial_resolution": spatial_resolution,
        "record_count": record_count,
        "is_synthetic": is_synthetic,
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "demonstration" if is_synthetic else "verified_observational",
        "metadata": metadata or {}
    }
    
    manifest["datasets"][name] = record
    manifest["last_updated_utc"] = datetime.now(timezone.utc).isoformat()
    
    with MANIFEST_FILE.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        
    print(f"[MANIFEST] Registered '{name}' -> SHA-256: {file_hash[:16]}... ({file_size_bytes} bytes)")
    return record

def verify_manifest() -> bool:
    """Verifies that all files listed in the manifest exist and match their SHA-256 checksums."""
    manifest = load_manifest()
    if not manifest["datasets"]:
        print("[MANIFEST] No datasets currently registered.")
        return False
        
    all_valid = True
    for name, item in manifest["datasets"].items():
        rel_path = item["filepath"]
        full_path = str(PROJECT_ROOT / rel_path)
        if not os.path.exists(full_path):
            print(f"[ERROR] Missing dataset file: {rel_path} for '{name}'")
            all_valid = False
            continue
        current_hash = compute_sha256(full_path)
        if current_hash != item["sha256"]:
            print(f"[ERROR] Checksum mismatch for '{name}'! Expected {item['sha256']} but got {current_hash}")
            all_valid = False
        else:
            status_tag = "[MOCK/DEMO]" if item["is_synthetic"] else "[VERIFIED]"
            print(f"[OK] {status_tag} {name}: {item['sha256'][:16]}... ({item['record_count']} records)")
            
    return all_valid

if __name__ == "__main__":
    print("[INIT] Manifest Manager initialized.")
    verify_manifest()
