# https://medium.com/@Shamimw/langgraph-simplified-how-to-build-ai-workflows-the-smart-way-791c17749663

import os
import sys
import uuid
import subprocess
import urllib.parse

from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from pydantic import BaseModel  # Required for StructuredTool

def weather(city: str) -> str:
    
    ### Some default weather that will always work
    wttr_str = f'In {city}, ' + """
    the current weather MAY be as follows:
    Detailed status: clear sky
    Wind speed: 3.09 m/s, direction: 180°
    Humidity: 48%
    Temperature: 
      - Current: 9.36°C
      - High: 10.49°C
      - Low: 8.3°C
      - Feels like: 7.69°C
    Rain: {}
    Heat index: None
    Cloud cover: 0%
"""

    #cmd = ['curl','-s','-X','GET',f'https://wttr.in/{city}?format=j1']
    cmd = ['curl','-s','-X','GET',f'https://wttr.in/{city}']
    print(' '.join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    val = result.returncode

    if val == 0:
        print("Command executed successfully:")
        wttr_str = result.stdout
    else:
        print(f"Command failed with error code: {val}")
        print(f"Error output: {result.stderr}")

    return wttr_str

# Define LLM Model
MODEL = "llama3.2"
llm = ChatOllama(model=MODEL)

# **Node 1: Extract city from user input**
def agent(state):
    user_input = state["messages"][-1].content  # Extract the latest user message
    print(user_input)
    
    res = llm.invoke(f"""
    You are given one question and you have to extract the city name from it.
    Respond ONLY with the city name. If you cannot find a city, respond with an empty string.

    Here is the question:
    {user_input}
    """)

    city_name = res.content.strip()
    if not city_name:
        return {"messages": [AIMessage(content="I couldn't find a city name in your question.")]}

    return {"messages": [AIMessage(content=f"Extracted city: {city_name}")], "city": city_name}

# **Node 2: Fetch weather information**
def weather_tool(state):
    city_name = state.get("city", "").strip()  # Retrieve city name from state

    if not city_name:
        return {"messages": [AIMessage(content="No city name provided. Cannot fetch weather.")]}

    weather_info = weather(city_name)
    print(weather_info)

    return {"messages": [AIMessage(content=weather_info)]}

# **Define the State**
class State(TypedDict):
    messages: Annotated[list, add_messages]
    city: str  # Adding 'city' key to track extracted city name

# **Setup Workflow**
memory = MemorySaver()
workflow = StateGraph(State)

# **Add Nodes**
workflow.add_node("agent", agent)
workflow.add_node("weather", weather_tool)

# **Define Transitions Between Nodes**
workflow.add_edge(START, "agent")
workflow.add_edge("agent", "weather")
workflow.add_edge("weather", END)

# **Compile Workflow with Memory Checkpointer**
app = workflow.compile(checkpointer=memory)

# **Create a unique config dictionary to satisfy the checkpointer requirements**
config = {"configurable": {"thread_id": str(uuid.uuid4())}}

city = 'Lenexa'
if len(sys.argv) > 1:
    city = sys.argv[1]
    print(f"City = '{city}' was passed as command line arg")
else:
    print(f"City was not passed as command line arg, so taking default city of {city}, unless the user query mentions another city.")

# **Run the Workflow**
# user_query = f"What is the weather in {city}?"
user_query = """
  It was 8:00 am and John was getting ready to go to work. 
  He had to catch the line 1 subway at Times Square and get down at Wall Street.
  A quick walk off Greenwich street and he was at his office in downtown NewYorkCity. 
  A total of 40 minutes of commute!
"""
response = app.invoke({"messages": [HumanMessage(content=user_query)]}, config=config)

# **Print Response**
print("AI:", response["messages"][-1].content)
