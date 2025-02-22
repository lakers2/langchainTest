from openai import OpenAI
from dotenv import load_dotenv
from agent_utils import Utils
from agent import Agent
import os
import re

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

    agent = Agent(client=client, system=Utils.get_system_prompt())

    tools = [func for func in dir(Utils) if not func.startswith('_') and callable(getattr(Utils, func))]
    print(tools)
    next_prompt = "What is the mass of Earth plus the mass of Saturn and all of that times 2?"

    i = 0
  
    while i < 10:
        i += 1
        result = agent(next_prompt)
        print(result)

        if "PAUSE" in result and "Action" in result:
            # The regex pattern "Action: ([a-z_]+): (.+)" breaks down as:
            # - "Action: " matches the literal text "Action: "
            # - ([a-z_]+) is the first capture group that matches:
            #   - [a-z_]: any lowercase letter or underscore
            #   - +: one or more times
            # - ": " matches the literal text ": "
            # - (.+) is the second capture group that matches:
            #   - .: any character except newline
            #   - +: one or more times
            # re.findall returns a list of tuples, where each tuple contains the captured groups
            action = re.findall(r"Action: ([a-z_]+): (.+)", result, re.IGNORECASE)
            chosen_tool = action[0][0]
            arg = action[0][1].strip()

            if chosen_tool in tools:
                print(f"Utils.{chosen_tool}('{arg}')")
                result_tool = eval(f"Utils.{chosen_tool}('{arg}')")
                next_prompt = f"Observation: {result_tool}"

            else:
                next_prompt = "Observation: Tool not found"

            print(next_prompt)
            continue

        if "Answer" in result:
            break