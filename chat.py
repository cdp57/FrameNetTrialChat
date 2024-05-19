import os
from langserve.client import RemoteRunnable

# set OpenAI api key
os.environ["OPENAI_API_KEY"] = "sk-proj-BmPjizYAgrTPpcmvYCfAT3BlbkFJ8B5OHjooRsnAfteIp48h"

# set Pinecone environment variables
os.environ["PINECONE_API_KEY"] = "a917142b-2398-47c9-a371-f9e63415acd3"
os.environ["PINECONE_ENVIRONMENT"] = "gcp-starter"
os.environ["PINECONE_INDEX"] = "test"

# access the template from the local server
runnable = RemoteRunnable("http://localhost:8000/rag-conversation")

rag_app = RemoteRunnable("http://0.0.0.0:8001/rag_conversation")

# pose question input to the LLM
question = "How does agent memory work?"
answer = rag_app.invoke(
    {
        "question": question,
        "chat_history": [],
    }
)

# output response from the LLM
print(answer)
