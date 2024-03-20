import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from langdetect import detect
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

class evaluation:
    
    def __init__(self):
        pass
    
    def cosine_similarity(self , vec1, vec2):
    
        # Calculating the dot product of the two vectors
        dot_product = np.dot(vec1, vec2)
    
        # Calculating the Euclidean norm of the first vector
        norm1 = np.linalg.norm(vec1)
    
        # Calculating the Euclidean norm of the second vector
        norm2 = np.linalg.norm(vec2)
    
        # Compute the cosine similarity by dividing the dot product by the product of the norms
        return dot_product / (norm1 * norm2)
    
    def get_top_10_code(self , question, embedding, model,list_data,df):
    
        # getting the vector embedding of question
        questions_embeddings = model.encode(question)
    
        # Calculate cosine similarities between the question embedding and all embeddings in the dataset
        cosine_similarities = np.array([self.cosine_similarity(questions_embeddings, emb) for emb in embedding])
    
        # Get the indices of the top 10 cosine similarities
        top_10_indices = np.argsort(cosine_similarities)[-10:][::-1]
    
        # Initialize a list to store the top 10 docstrings
        top_10_docstring = []
    
        # Retrieve the docstrings corresponding to the top 10 indices
        for i in top_10_indices:
            top_10_docstring.append(list_data[i])
        
        # Get the cosine similarities corresponding to the top 10 indices
        top_10_cosine_similarities = cosine_similarities[top_10_indices]
    
        # Initialize a list to store the top 10 code snippets
        top_code = []
    
        # Retrieve the code snippets corresponding to the top 10 indices
        for i in top_10_indices:
            top_code.append(df.loc[i].code)
        
        return top_code
