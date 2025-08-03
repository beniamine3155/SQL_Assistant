from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from module.config import OPENAI_API_KEY, MODEL_NAME

def get_sql_query(user_query: str, schema_description: str) -> str:
    prompt = ChatPromptTemplate.from_template(f"""
        You are a professional SQL assistant. Given an English question,
        convert it into a valid SQL query using the provided schema.

        Schema:
        {schema_description}

        Guidelines:
        - Use standard SQL syntax only.
        - Always wrap string values in double quotes.
        - Use JOINs where necessary.
        - Do NOT include code fences (e.g., ```).
        - Return only the SQL query as output.

        Question: {{user_query}}
        SQL Query:
    """)

    llm = ChatGroq(
        groq_api_key=OPENAI_API_KEY,
        model_name=MODEL_NAME
    )

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"user_query": user_query}).strip()