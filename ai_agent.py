from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3:instruct",
    temperature=0
)


def explain_result(question, data):

    prompt = f"""
You are an Oracle DBA assistant.

User question:
{question}

Database result:
{data}

Explain the result clearly for a DBA.
"""

    response = llm.invoke(prompt)

    # Print to command line
    print("\n===== LLM RESPONSE =====")
    print(response.content)
    print("========================\n")

    return response.content