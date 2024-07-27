from dateutil import parser
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model="gpt-4o-mini", api_key="API KEY")

def is_asking_for_uploaded_documents(question):
    response = llm.invoke(f"Only answer Yes or No. Is the following question asking about documents uploaded on a specific date? '{question}'")
    return "yes" in response.content.strip().lower()

def extract_date_from_question(question):
    try:
        cleaned_question = question.lower().replace('?', '').strip()
        if 'uploaded on' in cleaned_question:
            date_str = cleaned_question.split('uploaded on')[1].strip()
        elif 'uploaded' in cleaned_question and 'on' in cleaned_question:
            date_str = cleaned_question.split('uploaded')[1].split('on')[1].strip()
        else:
            date_str = cleaned_question.split()[-3] + ' ' + cleaned_question.split()[-2] + ' ' + cleaned_question.split()[-1]
        return parser.parse(date_str).strftime('%Y-%m-%d')
    except (ValueError, IndexError):
        return None

def initialize_qa_chain(knowledge_base):
    return RetrievalQA.from_chain_type(llm, retriever=knowledge_base.as_retriever())

def answer_question(qa_chain, question):
    return qa_chain.invoke({"query": question})
