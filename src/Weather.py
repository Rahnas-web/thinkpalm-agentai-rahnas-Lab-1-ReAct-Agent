from IPython.display import Markdown, display

# =========================================
# Minimal ReAct Agent (Weather Example)
# Works Based on User Input
# =========================================

# -----------------------------
# Tool Definition
# -----------------------------

def weather_tool(city):
    """Weather tool"""

    weather_data = {
        "kochi": "Rainy, 28°C",
        "delhi": "Hot, 38°C",
        "mumbai": "Cloudy, 31°C",
        "chennai": "Sunny, 35°C",
        "bangalore": "Cool, 24°C"
    }

    return weather_data.get(city.lower(), "Weather data not found")


# -----------------------------
# ReAct Agent
# -----------------------------

def react_agent(user_query):
    output_parts = []
    output_parts.append("### ReAct Agent Output")
    output_parts.append(f"\n**User Query:** {user_query}\n")

    # Step 1 - Reasoning
    output_parts.append("**Thought:**")
    output_parts.append("* User is asking about weather.")
    output_parts.append("* I should use the weather tool.\n")

    # Step 2 - Extract City
    words = user_query.lower().split()

    city = ""

    for word in words:
        if word in ["kochi", "delhi", "mumbai", "chennai", "bangalore"]:
            city = word
            break

    # Step 3 - Tool Call
    output_parts.append(f"**Action:** `weather_tool('{city}')`")

    observation = weather_tool(city)

    # Step 4 - Observation
    output_parts.append(f"\n**Observation:** {observation}\n")

    # Step 5 - Final Answer - styled as a box
    final_answer_text = f"**Final Answer:** The weather in {city.capitalize()} is {observation}"
    output_parts.append(f"<div style='background-color:#e0f7fa; border-left: 5px solid #00bcd4; padding: 10px; margin: 10px 0;'>{final_answer_text}</div>")

    return "\n".join(output_parts)


# -----------------------------
# User Input
# -----------------------------

user_input = input("Enter your weather query: ")

display(Markdown(react_agent(user_input)))
