from sentence_transformers import SentenceTransformer, util
import torch

class Retriever:
    def __init__(self, document_chunks):
        self.document_chunks = document_chunks
        self.chunk_embeddings = self.embed_chunks()

    def embed_chunks(self):
        embeddings_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", device="cpu")
        embeddings = embeddings_model.encode(self.document_chunks)
        return embeddings

    def embed_query(self, query):
        query_model = SentenceTransformer(model_name_or_path="all-mpnet-base-v2", device="cpu")
        query_embedding = query_model.encode(query)
        return query_embedding

    def retrieve(self, query, top_k=2):
        query_embedding = self.embed_query(query)
        dot_scores = util.dot_score(a=query_embedding, b=self.chunk_embeddings)[0]
        scores, indices = torch.topk(dot_scores, top_k)
        return [self.document_chunks[i] for i in indices]

