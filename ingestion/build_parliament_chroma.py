import json
import html
import re
import chromadb

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

try:
    client.delete_collection(
        "parliament_inquiries"
    )
except Exception:
    pass

collection = client.create_collection(
    name="parliament_inquiries"
)

with open(
    "data/parliament_inquiries.json",
    "r",
    encoding="utf-8",
) as f:
    inquiries = json.load(f)

documents = []
ids = []
metadatas = []

for inquiry in inquiries:

    title = inquiry.get("title", "")
    scope = inquiry.get("scope", "")
    report = inquiry.get("latestReport", "")

    if len(scope) + len(report) < 300:
        continue

    scope = html.unescape(scope)
    scope = re.sub(r"<[^>]+>", " ", scope)

    document = f"""
Title:
{title}

Scope:
{scope}

Latest Report:
{report}
"""

    ids.append(str(inquiry["id"]))

    documents.append(document)

    metadatas.append(
        {
            "title": title,
        }
    )

print(
    "Documents:",
    len(documents)
)

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
)

print(
    "Loaded",
    len(documents),
    "inquiries into Chroma",
)