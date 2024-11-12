from django.conf import settings
from pinecone import Pinecone

pc = Pinecone(api_key=settings.PINECONE_API_KEY)

def new_index():
    """
    Create a new Pinecone index.

    Returns:
        name:      The name of the index
        dimension: The dimension of the index
        metric:    The metric of the index

    Raises:
        Exception: If there's an error accessing the database
    """
    from pinecone.grpc import PineconeGRPC as Pinecone
    from pinecone import ServerlessSpec

    try:
        pc.create_index(
            name=settings.PINECONE_INDEX,
            dimension=int(settings.EMBEDDING_DIMENSIONS),
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            ),
            deletion_protection="disabled"
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return {
        "name": settings.PINECONE_INDEX,
        "dimension": int(settings.EMBEDDING_DIMENSIONS),
        "metric": "cosine"
    }
