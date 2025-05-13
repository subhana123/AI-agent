import requests

def web_search(query):
    response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
    data = response.json()
    return data.get("AbstractText") or "No good results found."
if "search" in user_input:
    result = web_search(user_input.replace("search", ""))
    st.session_state.history.append({"role": "user", "content": result})
