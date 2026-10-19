"""
Generate policy-relevant themes from researcher publication titles.

The resulting themes are used as an intermediate representation
between academic research outputs and Parliamentary inquiries.
"""

response = client.chat.completions.create(
    model="nvidia/Nemotron-3_5-Lightning",
    messages=[
        {
            "role": "system",
            "content": """
You are a UK Parliamentary research impact analyst.

Review the publication titles and generate ten concise
policy-facing themes that could be used to identify
relevant Parliamentary inquiries.

Use language that is likely to appear in inquiry titles
or policy discussions.

Return only a numbered list of themes.
"""
        }
    ],
    temperature=0,
)