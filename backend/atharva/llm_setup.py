import google.generativeai as genai
import os

import os
from pinecone import Pinecone
from transformers import AutoTokenizer, AutoModel
import torch
from IPython.display import Markdown

genai.configure(api_key="AIzaSyB7t4BLUq7lmE-7Es7GGRsTCcNUKULSfPg")
gemini_model = genai.GenerativeModel('gemini-1.5-flash')



# response = gemini_model.generate_content("what is the capitla of spain?")
# print(response.text)

def get_response(question):
    response = gemini_model.generate_content(question)
    return response.text


# Load the multilingual-e5-large model and tokenizer from Huggingface
tokenizer = AutoTokenizer.from_pretrained("intfloat/multilingual-e5-large")
model = AutoModel.from_pretrained("intfloat/multilingual-e5-large")


# Function to generate embeddings
def generate_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        embeddings = model(**inputs)
    return embeddings.last_hidden_state.mean(dim=1).squeeze().numpy()

def make_prompt(query, relevant_passage):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = ("""You are a helpful and informative bot that answers questions using text from the reference passage included below. \
  Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
  However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
  strike a friendly and converstional tone. \
  If the passage is irrelevant to the answer, you may ignore it. Ensure that you still attempt to answer the question to you maximum ability. Do not mention the use of the passage to me.
  QUESTION: \n'{query}'
  PASSAGE: '{relevant_passage}'

    ANSWER:
  """).format(query=query, relevant_passage=escaped)

  return prompt


# Initialize Pinecone
api_key = "0208c975-9131-40cb-97ca-998b8aebbe51"
pc = Pinecone(api_key=api_key)
index = pc.Index("iitm-transcripts")


# Function to fetch context from Pinecone
def fetch_context(query, top_k=10):
    # Generate embedding for the query
    query_embedding = generate_embedding(query)  # Use the same function to generate embedding

    # Query Pinecone
    results = index.query(
        vector=query_embedding.tolist(),
        top_k=top_k,
        include_metadata=True,
        namespace="ns1"
    )

    # Extract and return the context
    context = " ".join([ result['metadata']['transcript'] for result in results['matches']])
    return context

# Example usage

def full_fucntion(question):
    context = fetch_context(question)
    prompt = make_prompt(question, context)
    answer = get_response(prompt)
    return answer.text




# query = "WHAT IS the difference between a story card and user stories?"
# context = fetch_context(query)
# prompt = make_prompt(query, context)
# answer = get_response(prompt)

# print(answer.text)


def get_summary(transcript):
    prompt = ("""You are a helpful and informative bot that sumarizes text and transcripts provided to you below namely the passage. \
    Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
    However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
    strike a friendly and converstional tone. \
    Refer to the passage below as "the lecture". \
    QUESTION: \n'Summarize the passage below'
    PASSAGE: '{transcript}'

        ANSWER:
    """).format( transcript=transcript)
    summary = get_response(prompt)
    return summary


def get_key(transcript):
    prompt = ("""You are a helpful and informative bot that analyzes text and transcripts provided to you below namely the passage and from these generates the key topics discussed in the video. \
    Respond in short bullet points each on a new line in a markdown format. \
    Be very concise and to the point. \
    Ensure that you add a line break after each bullet point. \
    QUESTION: \n'Extract key points and topics covered from the passage below'
    PASSAGE: '{transcript}'

        ANSWER:
    """).format( transcript=transcript)
    key = get_response(prompt)
    return key