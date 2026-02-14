import re

def load_and_chunk_text(path: str):
    """
    Loads the text file and creates smarter semantic chunks.
    Splits by section headers and further divides large sections.
    """

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split by main headers
    sections = re.split(r'\n##\s+', text)

    chunks = []

    for section in sections:
        section = section.strip()

        if not section:
            continue

        # Further split large sections into smaller parts
        paragraphs = section.split("\n\n")

        for para in paragraphs:
            cleaned = para.strip()

            # Ignore very small text
            if len(cleaned) > 80:
                chunks.append(cleaned)

    return chunks
