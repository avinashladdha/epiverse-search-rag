import pandas as pd
import torch
import pytest
from pathlib import Path

# Base directory: one level up from this test file
BASE_DIR = Path(__file__).resolve().parent.parent

@pytest.fixture(scope="module")
def analysis_df():
    return pd.read_csv(BASE_DIR / "analysis_df.csv")

@pytest.fixture(scope="module")
def corpus_embeddings():
    return torch.load(BASE_DIR / "corpus_embeddings.pth", weights_only=True)

def test_embedding_count_matches_unique_clusters(analysis_df, corpus_embeddings):
    unique_clusters = analysis_df["cluster_id"].nunique()
    assert corpus_embeddings.shape[0] == unique_clusters, (
        f"Expected {unique_clusters} embeddings, got {corpus_embeddings.shape[0]}"
    )

def test_cluster_id_used_in_single_package(analysis_df):
    cluster_package_counts = (
        analysis_df.groupby("cluster_id")["package_name"]
        .nunique()
        .reset_index(name="package_count")
    )
    problematic = cluster_package_counts[cluster_package_counts["package_count"] > 1]
    assert problematic.empty, (
        "Some cluster_id values are used in more than one package:\n"
        f"{problematic}"
    )
