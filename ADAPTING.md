# Adapting for Other Platforms

This template is designed for Claude Code with Telegram, but the core concepts -- agent definitions, brain system, and slash commands -- are portable. This guide covers how to adapt the system for other platforms.

## What's Claude Code-Specific

| Feature | Claude Code Mechanism | Portable? |
|---------|----------------------|-----------|
| Agent definitions | `.md` files read as system prompts | Yes -- works as system prompts anywhere |
| Brain (markdown files) | Read/Write tools on local filesystem | Yes -- any system that can read/write files |
| Slash commands | Claude Code skills system | Partially -- logic is portable, trigger mechanism varies |
| Telegram integration | `telegram@claude-plugins-official` plugin | No -- Claude Code plugin |
| Web search | `WebSearch` tool | Varies by platform |
| Web fetch | `WebFetch` tool | Varies by platform |
| Scheduled tasks | `CronCreate` tool | No -- Claude Code specific |
| MCP integrations | MCP server connections (Calendar, Email, etc.) | Partially -- MCP is an open protocol |
| File operations | `Read`, `Write`, `Edit` tools | Yes -- most platforms have file access |

## Adaptation Strategies

### OpenAI / ChatGPT Custom GPTs

The agent definitions can be used as system prompts for Custom GPTs.

**What works:**
- Copy each agent's `.md` file as the system prompt for a Custom GPT
- Create one GPT per agent, or one GPT with all agent prompts combined
- Brain files can be uploaded as knowledge files
- Slash commands can be described in the system prompt as "when the user says /brief, do X"

**What doesn't work:**
- No multi-channel routing (one GPT = one conversation)
- Brain doesn't auto-update (knowledge files are static)
- No Telegram integration
- No file system access for brain read/write

**Recommended approach:**
1. Create a single "Chief of Staff" Custom GPT with all agent definitions in the system prompt
2. Upload brain files as knowledge documents
3. Manually update knowledge files periodically
4. Use GPT Actions for external integrations (Calendar, Email)

### Local LLMs (Ollama, LM Studio, llama.cpp)

The agent definitions work as system prompts for any model.

**What works:**
- Agent `.md` files as system prompts
- Brain files as RAG (Retrieval-Augmented Generation) context
- Local file system access for brain updates
- Full privacy -- everything stays on your machine

**What doesn't work:**
- Quality depends heavily on the model (needs a capable model for multi-agent routing)
- No native Telegram integration (need a custom bot)
- No web search (need external tools)
- Smaller context windows may not fit full brain + agent prompts

**Recommended approach:**
1. Use a capable model (Llama 3.1 70B+ or Qwen 2.5 72B+)
2. Set up a RAG pipeline over the `brain/` directory
3. Use the Chief of Staff agent definition as the primary system prompt
4. Build a simple Telegram bot with python-telegram-bot or similar
5. Route messages through the LLM with appropriate agent context

**Example RAG setup:**
```python
# Pseudocode for brain-as-RAG
from pathlib import Path

def load_brain_context(query: str, brain_dir: str = "brain/") -> str:
    """Load relevant brain files based on the query."""
    # Always load core context
    core_files = [
        "context/role-and-goals.md",
        "context/projects.md",
    ]
    context = ""
    for f in core_files:
        path = Path(brain_dir) / f
        if path.exists():
            context += path.read_text() + "\n\n"

    # Add query-relevant files via embedding search or keyword matching
    # ... your RAG implementation here ...

    return context
```

### LangChain / LangGraph

Map directly to LangChain's agent abstractions.

**What works:**
- Agent `.md` files as agent system prompts
- Brain files as document store
- LangChain tools for web search, file operations
- Multi-agent orchestration via LangGraph

**Mapping:**
```python
# Each agent becomes a LangChain agent
from langchain.agents import create_react_agent

chief_of_staff = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=load_prompt("agents/chief-of-staff.md")
)

analyst = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=load_prompt("agents/analyst.md")
)

# LangGraph for multi-agent routing
from langgraph.graph import StateGraph

graph = StateGraph(State)
graph.add_node("chief_of_staff", chief_of_staff)
graph.add_node("analyst", analyst)
graph.add_node("strategist", strategist)
# ... add routing edges ...
```

**Recommended approach:**
1. Create a LangGraph workflow with the Chief of Staff as the router node
2. Each specialist agent is a node that the Chief routes to
3. Use a LangChain document loader for the brain directory
4. Use LangChain's Telegram integration for messaging
5. Implement brain updates as a tool the Librarian agent can call

### CrewAI

Maps naturally to CrewAI's agent/task model.

**What works:**
- Agent `.md` files define CrewAI agents
- Tasks map to slash commands
- Crew orchestration handles multi-agent workflows
- Built-in tool support for web search, file ops

**Mapping:**
```python
from crewai import Agent, Task, Crew

analyst = Agent(
    role="Analyst",
    goal="Provide deep analysis with structured output",
    backstory=open("agents/analyst.md").read(),
    tools=[search_tool, file_tool]
)

strategist = Agent(
    role="Strategist",
    goal="Develop strategic plans and frameworks",
    backstory=open("agents/strategist.md").read(),
    tools=[search_tool, file_tool]
)

# Tasks map to slash commands
analyze_task = Task(
    description="Analyze {topic} using relevant frameworks",
    agent=analyst,
    expected_output="Structured analysis with findings and recommendations"
)

crew = Crew(
    agents=[analyst, strategist, writer, critic],
    tasks=[analyze_task],
    verbose=True
)
```

### AutoGen (Microsoft)

Maps to AutoGen's multi-agent conversation model.

**Recommended approach:**
1. Each agent `.md` file becomes an AutoGen AssistantAgent system message
2. Use GroupChat for multi-agent coordination
3. The Chief of Staff becomes the GroupChatManager
4. Brain files loaded as context in each agent's system message

## Feature Degradation Reference

What happens when specific integrations are missing:

| Missing Integration | Impact | Workaround |
|--------------------|--------|------------|
| Telegram plugin | No mobile messaging | Use Claude Code terminal directly |
| WebSearch | Market Researcher cannot search the web | Manually provide research data via `/ingest` |
| WebFetch | Cannot fetch URLs | Copy-paste content into the conversation |
| CronCreate | No scheduled briefings or reminders | Manually trigger `/brief` each morning |
| Calendar MCP | No calendar awareness | Tell the assistant your schedule manually |
| Email MCP | No email drafting/reading | Copy-paste emails for review |
| ClickUp/Jira MCP | No task management integration | Describe task status verbally |
| File system access | Cannot update brain files | Brain becomes read-only (no learning) |

## Tips for Any Platform

1. **Start with the brain.** The brain system (markdown files as structured memory) works everywhere. Even without auto-learning, manually maintained brain files dramatically improve assistant quality.

2. **The Chief of Staff prompt is the most important.** If you can only use one agent definition, use the Chief of Staff. It contains the routing logic and orchestration patterns.

3. **Brain loading order matters.** Always load `role-and-goals.md` and `projects.md` first. They provide the foundation that makes everything else useful.

4. **Channel context is optional but powerful.** Even without Telegram, you can maintain separate "modes" by switching which channel context file is loaded.

5. **Test with `/onboard` first.** The onboarding flow populates the brain with your context. Without it, the system gives generic responses. Run the equivalent of `/onboard` on any platform before expecting good results.
