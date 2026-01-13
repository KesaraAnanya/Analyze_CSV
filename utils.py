from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd 
from langchain_openai import OpenAI

def query_agent(data, query):
    df = pd.read_csv(data)
    llm = OpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    agent = create_pandas_dataframe_agent(
        llm, 
        df, 
        verbose=True, 
        allow_dangerous_code=True
    )


    response = agent.invoke(query)
    return response['output']

