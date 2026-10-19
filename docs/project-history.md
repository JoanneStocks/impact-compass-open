# Project History

This document summarises the evolution of Impact Compass and the lessons learned during development.

## Initial Idea

Impact Compass began as an exploration of whether AI could help researchers identify relevant UK Parliamentary inquiries and engagement opportunities from their existing research outputs.

The core hypothesis was simple:

> If a researcher's expertise can be understood from their publications, then it may be possible to automatically identify Parliamentary inquiries that align with their knowledge and evidence.

---

## Stage 1: Publication Discovery

The first challenge was identifying publications associated with individual researchers.

Early experiments explored OpenAlex as a source of publication data because it provides broad coverage of academic outputs.

### What Worked

- Easy access to publication metadata
- Large coverage of academic research
- Useful for rapid experimentation

### What Didn't

Testing revealed identity-resolution issues where publications could be incorrectly associated with researchers.

Because Impact Compass depends on accurate researcher attribution, this created a significant risk of poor recommendations.

### Result

OpenAlex was not adopted as the primary researcher identity source.

---

## Stage 2: Adoption of ORCID

The project moved towards ORCID as the primary source of researcher information.

### Why ORCID?

ORCID profiles are maintained by researchers themselves and provide stronger confidence that publications belong to the correct individual.

This improved the reliability of publication harvesting and reduced attribution concerns identified during earlier experimentation.

### Result

ORCID became the foundation of the researcher discovery workflow.

---

## Stage 3: Keyword-Based Matching

Initial matching approaches relied heavily on extracted keywords from publication records.

### Strengths

- Simple implementation
- Fast processing
- Easy to explain

### Weaknesses

- Generic recommendations
- Weak handling of contextual relationships
- Difficulty recognising semantically similar concepts

### Result

Keyword matching remained useful but was insufficient as the primary recommendation strategy.

---

## Stage 4: Theme Generation

To improve matching quality, the project experimented with generating policy-relevant themes from publication records.

### Early Themes

Some generated themes were overly broad:

- Public Health
- Education
- Environment

While accurate, these often produced weak retrieval results.

### Later Themes

More useful results emerged when themes resembled Parliamentary inquiry titles:

- Physical Activity and Health Outcomes
- Supporting People with Frailty
- Children and Young People's Mental Health

### Result

Theme generation improved the quality and interpretability of recommendations.

---

## Stage 5: Semantic Retrieval

The project adopted embedding-based retrieval to move beyond exact keyword matching.

### Rationale

Academic publications and Parliamentary inquiries often discuss similar topics using different terminology.

Semantic search allows conceptually related content to be identified even when vocabulary differs.

### Implementation

Parliamentary inquiry records were embedded and stored in ChromaDB to support vector-based retrieval.

### Result

Semantic retrieval became a core component of the matching workflow.

---

## Stage 6: Retrieval-Augmented Exploration

The project expanded beyond simple matching to include retrieval-augmented exploration of Parliamentary activity.

This enabled:

- Inquiry discovery
- Thematic exploration
- Grounded question answering
- Source-linked responses

---

## Current Status

Impact Compass is an active research prototype exploring how AI, semantic retrieval, and Parliamentary data can support research impact and policy engagement discovery.

The project continues to evolve through experimentation and iterative improvement.

---

## Lessons Learned

The most important lesson from the project has been that data quality and retrieval quality matter more than model complexity.

Several planned approaches were replaced or redesigned after testing revealed weaknesses.

Progress was driven less by following an original plan and more by continuously evaluating assumptions and adjusting the system accordingly.

This iterative approach remains central to the ongoing development of Impact Compass.