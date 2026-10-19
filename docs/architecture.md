# Architecture

## Research Impact Explorer Workflow

```text
ORCID
  ↓
Researcher Identification
  ↓
Publication Harvesting
  ↓
Theme Generation
  ↓
Semantic Retrieval
  ↓
Inquiry Matching
  ↓
Why-Matched Explanations
```

## Parliamentary Assistant Workflow

```text
User Question
  ↓
ChromaDB Retrieval
  ↓
Relevant Inquiry Documents
  ↓
Large Language Model
  ↓
Grounded Response
  ↓
Source References
```

## Data Pipeline

```text
UK Parliament Committees API
  ↓
Inquiry Collection
  ↓
Document Preparation
  ↓
Embedding Generation
  ↓
ChromaDB Vector Store
  ↓
Semantic Retrieval
```

## Core Components

### Data Sources

- UK Parliament Committees API
- ORCID

### Retrieval Layer

- ChromaDB
- Vector embeddings
- Semantic search

### Application Layer

- Researcher profiling
- Publication analysis
- Theme generation
- Inquiry matching
- Match explanations

### Technology Stack

Frontend:

- React
- TypeScript
- Vite

Backend:

- Python
- FastAPI

AI Components:

- ChromaDB
- Embedding models
- NVIDIA Nemotron (Nebius)
```
