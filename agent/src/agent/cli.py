from agents import Runner
from agent_here import agent, config
import asyncio


async def main():
    print("🔍 Research Agent ready. Type 'exit' to quit.\n")

    while True:
        try:
            user_query = input("Research query: ").strip()

            if not user_query:
                print("Please enter a valid research query.\n")
                continue

            if user_query.lower() in {"exit", "quit"}:
                print("Exiting Research Agent. Goodbye!")
                break

            result = await Runner.run(
                agent,
                f"Use the available tools to {user_query}",
                run_config=config
            )

            print("\n Result:\n", result.final_output, "\n")

        except KeyboardInterrupt:
            print("\n Exiting Research Agent. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    asyncio.run(main())
