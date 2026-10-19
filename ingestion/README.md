# Parliament Data Ingestion

Impact Compass uses UK Parliament inquiry data as the foundation for semantic retrieval.

This script:

1. Loads inquiry records.
2. Cleans HTML content.
3. Builds textual representations of inquiries.
4. Stores data in ChromaDB for semantic search.

The resulting collection supports retrieval of inquiries relevant to researcher expertise.
