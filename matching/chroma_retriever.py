"""
Retrieve relevant Parliamentary inquiries from the ChromaDB vector store.

Used by Impact Compass to identify inquiry records that are semantically
related to researcher themes and publication topics.
"""

import chromadb


def chroma_retrieve(query, n_results=10):

    client = chromadb.PersistentClient(
        path="data/chroma_db"
    )

    collection = client.get_collection(
        "parliament_inquiries"
    )

    if isinstance(query, list):
        query_text = " ".join(query)
    else:
        query_text = str(query)

    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
    )

    inquiries = []

    ids = results["ids"][0]
    metadatas = results["metadatas"][0]
    documents = results["documents"][0]

    for inquiry_id, metadata, document in zip(
        ids,
        metadatas,
        documents,
    ):
        inquiries.append(
            {
                "id": inquiry_id,
                "title": metadata.get(
                    "title",
                    "Unknown Title",
                ),
                "document": document,
            }
        )

    return inquiries