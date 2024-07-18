import os
import autogen
from dotenv import load_dotenv
from typing import Dict, Any
from langchain_community.tools.tavily_search import TavilySearchResults
from autogen import config_list_from_json
import argparse
from datetime import datetime
from autogen_utils import redirect_stdout_to_file_and_terminal
# Load environment variables
load_dotenv()

# Implement the tavily_search function
def tavily_search(query):
    tool = TavilySearchResults(max_results=4)
    results = tool.invoke({"query": query})
    return results

class ResearchPlotGroupChat:
    def __init__(self):
        config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
        llm_config = {"config_list": config_list, "seed": 42}

        # Create a list of tools, including the web search tool
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "tavily_search",
                    "description": "A tool for performing web searches and retrieving information.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query"
                            }
                        },
                        "required": ["query"]
                    }
                }
            }
        ]

        formatted_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        dir_name = f"research_plot_work_dir_{formatted_datetime}"

        self.researcher = autogen.AssistantAgent(
            name="researcher",
            system_message="You are a research specialist. Your role is to gather and analyze data. Use the tavily_search function when you need to look up information on the web.",
            llm_config={**llm_config, "tools": tools},
            function_map={"tavily_search": tavily_search}
        )

        self.coder = autogen.AssistantAgent(
            name="coder",
            system_message="You are a Python expert. Your role is to write Python code for data analysis and visualization. Do not execute the code yourself; instead, pass it to the debugger agent for execution.",
            llm_config=llm_config,
        )

        self.debugger = autogen.AssistantAgent(
            name="debugger",
            system_message="You are a debugging agent. Your role is to execute Python code provided by the coder agent and report the results back to the group. If there are any errors, work with the coder to fix them.",
            code_execution_config={"work_dir": dir_name, "use_docker": False},
            llm_config=llm_config,
        )

        self.groupchat = autogen.GroupChat(
            agents=[self.debugger, self.researcher, self.coder],
            messages=[],
            max_round=10
        )
        self.manager = autogen.GroupChatManager(
            groupchat=self.groupchat,
            llm_config=llm_config,
            is_termination_msg=lambda x: x.get("content", "").rstrip().find("TERMINATE") >= 0,
        )

    def start_chat(self, message):
        self.debugger.initiate_chat(
            self.manager,
            message=message
        )

def main():
    default_message = "Fetch the UK's GDP over the past 5 years, then write a Python script to draw a line graph of it and save the image to the current folder. After that, run the Python script."
    parser = argparse.ArgumentParser(description="Research and Plot Chat initiation script")
    parser.add_argument("-f", "--filename", type=str,
                        help="filename that has the message to initiate the chat")
    args = parser.parse_args()

    if args.filename:
        try:
            with open(args.filename, 'r', encoding='utf-8') as file:
                message = file.read().strip()
                print(f"File content: {message}")
        except FileNotFoundError:
            print(f"The file {args.filename} does not exist.")
            message = default_message
    else:
        message = default_message

    group_chat = ResearchPlotGroupChat()
    print(f"Starting chat...")
    # group_chat.start_chat(message)
    #
    # group_chat = GroupChat()
    # print(f"Starting chat...")

    # Use the new context manager
    with open('research_plot_output.txt', 'w') as f:
        with redirect_stdout_to_file_and_terminal(f):
            group_chat.start_chat(message)

if __name__ == "__main__":
    main()