import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from backend import LinkedInSearchAgent


# Initialize agent
agent = LinkedInSearchAgent(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)


st.set_page_config(page_title="LinkedIn Search Agent", layout="centered")


# UI HEADER
st.title("🔎 LinkedIn Intelligence Search")
st.caption("Search people, companies, colleges — powered by Tavily + Groq")


# Search Type Selection
search_type = st.radio(
    "Search Type",
    ["person", "company"],
    horizontal=True
)

# Input Fields
name = st.text_input(
    "Name",
    placeholder="Enter name... (e.g., John Smith, Google, Amazon)"
)

city = st.text_input("City (optional)", placeholder="Surat, Mumbai, Bengaluru...")
role = st.text_input("Role (optional)", placeholder="Software Engineer, AI Lead...")
college = st.text_input("College (optional)", placeholder="NIT, IIT, SSASIT...")
company = st.text_input("Company (optional)", placeholder="Infosys, AppStoneLab...")


# Search Button
if st.button("Search 🔍", use_container_width=True):
    if not name.strip():
        st.error("Name field cannot be empty.")
        st.stop()

    with st.spinner("Fetching LinkedIn data..."):
        result = agent.search(
            type=search_type,
            name=name,
            city=city if city else None,
            role=role if role else None,
            college=college if college else None,
            company=company if company else None
        )

    # Response Handling
    if result["status"] == "Error":
        st.error(result["output"])
    else:
        # The agent's final answer
        output = result["output"]["output"] if isinstance(result["output"], dict) else result["output"]

        if not output or "No LinkedIn profiles found" in output:
            st.warning(output if output else "No results returned.")
        else:
            st.subheader("📌 Search Results")
            
            # Simple parsing to make it look like cards
            parts = output.split("\n\n")
            
            # First part is usually the "Found X profiles" header
            if parts:
                st.markdown(f"#### {parts[0]}")
                
                for part in parts[1:]:
                    if not part.strip():
                        continue
                        
                    if "Note:" in part:
                        st.caption(part)
                        continue
                    
                    # Create a card for each profile
                    with st.container(border=True):
                        lines = [l.strip() for l in part.split("\n") if l.strip()]
                        if not lines:
                            continue
                            
                        # Extract name (e.g., "1. John Doe")
                        name = lines[0]
                        if ". " in name:
                            name = name.split(". ", 1)[1]
                        
                        st.markdown(f"**{name}**")
                        
                        url = ""
                        info = ""
                        score = ""
                        
                        for line in lines:
                            if "URL:" in line:
                                url = line.split("URL:")[1].strip()
                            elif "Info:" in line:
                                info = line.split("Info:")[1].strip()
                            elif "Relevance" in line:
                                score = line.split(":")[1].strip()
                        
                        if info:
                            st.markdown(f"*{info}*")
                        
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            if url:
                                st.link_button("Open LinkedIn 🔗", url)
                        with col2:
                            if score:
                                st.caption(f"Score: {score}")
