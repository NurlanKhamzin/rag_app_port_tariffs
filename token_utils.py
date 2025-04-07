def split_text_into_chunks(text, max_tokens=5000):
    """Split large text into manageable chunks within the token limit."""
    words = text.split()
    chunks = []
    while words:
        chunk = words[:max_tokens]
        chunks.append(" ".join(chunk))
        words = words[max_tokens:]
    return chunks