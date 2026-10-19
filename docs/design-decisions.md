# Design Decisions

This document explains the major design decisions made during the development of Impact Compass.

## Why ORCID Instead of OpenAlex?

Early versions of Impact Compass explored using OpenAlex researcher profiles as the primary source of publication data.

During testing, instances were identified where publications appeared to be associated with the wrong researcher. Because Impact Compass aims to match individual researchers to Parliamentary inquiries, accurate researcher attribution is essential.

For this reason, the project moved to ORCID as the primary identity source. ORCID profiles are researcher-maintained and provide greater confidence that publications belong to the intended individual.

## Why Not Keyword Matching Alone?

Initial matching approaches relied heavily on keyword extraction.

While simple and computationally efficient, keyword-based approaches often:

- Produced broad or generic matches
- Missed conceptually related content
- Struggled with differences in terminology between academic publications and Parliamentary inquiries

Keyword matching remains useful as a supporting signal but was not sufficient as the primary matching mechanism.

## Why Semantic Retrieval?

Parliamentary inquiries and academic publications frequently discuss similar topics using different language.

Embedding-based semantic retrieval was introduced to identify conceptual similarity rather than relying solely on exact wording.

This led to the adoption of ChromaDB and vector-based retrieval for inquiry matching.

## Theme Generation Lessons

Several generations of theme extraction were explored.

Early themes were often too broad:

- Public Health
- Education
- Environment

Later iterations sometimes became too specific and difficult to generalise.

The most useful results emerged when generated themes resembled the language typically found in Parliamentary inquiry titles.

Examples include:

- Physical Activity and Health Outcomes
- Supporting People with Frailty
- Children and Young People's Mental Health

## Iterative Development

Impact Compass was developed through repeated experimentation and testing.

Approaches were revised, refined, or replaced when they produced weak recommendations or poor retrieval quality.

The project prioritises empirical iteration and practical testing over strict adherence to an initial design.