# # from dotenv import load_dotenv
# # import os
# # from agents import Agent, OpenAIChatCompletionsModel, RunConfig ,Runner
# # from openai import AsyncOpenAI

# # load_dotenv()
# # gemini_api_key=os.getenv("GEMINI_API_KEY")




# # if not gemini_api_key:
# #     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


# # external_client = AsyncOpenAI(
# #     api_key=gemini_api_key,
# #     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# # )

# # model = OpenAIChatCompletionsModel(
# #     model="gemini-1.0-flash",
# #     openai_client=external_client
# # )

# # config = RunConfig(
# #     model=model,
# #     model_provider=external_client,
# #     tracing_disabled=True
# # )


# # agent = Agent(
# #     name = "translator",
# #     instructions = "You are a helpful translator.  always Translate english sentences into clear and simple urdu"
# # )

# # response = Runner.run_sync(
# #     agent,
# #     input ="My name is syeda Mahnoor Kazim",
# #     run_config = config
# # )
# # print(response)
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")

# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set")

# genai.configure(api_key=gemini_api_key)

# model = genai.GenerativeModel("gemini-1.0-flash")

# response = model.generate_content("My name is Syeda Mahnoor Kazim. Translate into simple Urdu.")
# print(response.text)
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set")

genai.configure(api_key=gemini_api_key)

# Use a supported Gemini 2.5 model instead of the retired 1.0
model_name = "gemini-2.5-flash"  # or "gemini-2.5-pro"

model = genai.GenerativeModel(model_name)

response = model.generate_content("My name is Syeda Mahnoor Kazim. Translate into simple Urdu.")
print(response.text)
