import os
from database import save_chunks_to_sqlite, get_documents_by_date, is_document_uploaded
from docs_process import load_existing_chunks, save_chunks_cache, process_new_document
from chatbot import is_asking_for_uploaded_documents, extract_date_from_question, initialize_qa_chain, answer_question
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Set environment variables
os.environ["OPENAI_API_KEY"] = "API KEY"

# Paths for caching
faiss_cache_path = "faiss_index.pkl"

# Load existing text chunks
all_text_chunks = load_existing_chunks()

# Load or process new text chunks
new_document_path = input("Enter the path to the new PDF document or type 'skip' to skip: ")

if new_document_path.lower() != 'skip':
    new_text_chunks, title = process_new_document(new_document_path)

    if not is_document_uploaded(title):
        save_chunks_to_sqlite(new_text_chunks, title=title)
        all_text_chunks.extend(new_text_chunks)
        save_chunks_cache(all_text_chunks)
    else:
        print(f"Document '{title}' is already uploaded.")

# Load or create FAISS index
if os.path.exists(faiss_cache_path):
    with open(faiss_cache_path, 'rb') as f:
        knowledge_base = pickle.load(f)
else:
    embeddings = HuggingFaceEmbeddings()
    knowledge_base = FAISS.from_documents(all_text_chunks, embeddings)

# If there are new text chunks, update the FAISS index
if new_document_path.lower() != 'skip' and not is_document_uploaded(title):
    embeddings = HuggingFaceEmbeddings()
    knowledge_base.add_documents(new_text_chunks)
    with open(faiss_cache_path, 'wb') as f:
        pickle.dump(knowledge_base, f)

# Initialize QA chain
qa_chain = initialize_qa_chain(knowledge_base)

def chat_bot():
    print("Welcome to the document-based chatbot! Ask your questions about the document.")
    print("Type 'exit' to end the chat.")
    while True:
        question = input("\nEnter your question: ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        if is_asking_for_uploaded_documents(question):
            query_date = extract_date_from_question(question)
            if query_date:
                documents = get_documents_by_date(query_date)
                if documents:
                    print(f"\nDocuments uploaded on {query_date}:")
                    for doc in documents:
                        print(doc[0])
                else:
                    print(f"\nNo documents found for the date: {query_date}")
            else:
                print("\nInvalid date format. Please try again with a date in the format 'uploaded on <date>'.")
        else:
            response = answer_question(qa_chain, question)
            print("\nAnswer:")
            print(response["result"])

if __name__ == "__main__":
    chat_bot()
