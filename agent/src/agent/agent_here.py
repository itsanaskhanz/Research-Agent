from tools import scrape_page, search_web
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, enable_verbose_stdout_logging
from agents.run import RunConfig

gemini_api_key = ""

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful Research Assistant",
    tools=[scrape_page, search_web]
)

result = Runner.run_sync(
    agent, "Use the web search and scrape tools to find the current Prime Minister of Pakistan, then tell me who it is.", run_config=config)

print(result.final_output)
