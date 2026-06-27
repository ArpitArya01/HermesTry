import os
from dotenv import load_dotenv
from run_agent import AIAgent
from load_skill import load_skill

load_dotenv()

# ── Step 1: Skill load karo ──────────────────────────────────────────────────
skill = load_skill("skills/storytelling_skill.md")

# ── Step 2: Agent banao ──────────────────────────────────────────────────────
agent = AIAgent(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model=os.getenv("KORENA_AGENT_MODEL"),
    quiet_mode=True,
    disabled_toolsets=["browser", "computer"],
    max_iterations=5,
    ephemeral_system_prompt=f"You are a storyteller.\n\n{skill}",
)

# ── Step 3: Multi-turn conversation chalaao ──────────────────────────────────
history = []

# Turn 1
result = agent.run_conversation(
    "Write a short 3-sentence story about a brave little rabbit.",
    conversation_history=history
)
print(result.get("final_response", result))
history = result.get("messages", [])

# Turn 2
result = agent.run_conversation(
    "Now make the rabbit meet a wise old owl.",
    conversation_history=history
)
print(result.get("final_response", result))
history = result.get("messages", [])

# Turn 3
result = agent.run_conversation(
    "Give the story a happy ending.",
    conversation_history=history
)
print(result.get("final_response", result))