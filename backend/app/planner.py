
import json

class Planner:
    def __init__(self):
        pass

    def create_plan(self, user_query: str) -> list:
        actions = []
        q = user_query.lower()
        if 'supplier' in q or 'order' in q or 'ord-' in q:
            actions.append({"tool": "GRAPH", "intent": "find_order_suppliers", "params": {"query": user_query}})
            actions.append({"tool": "SQL", "intent": "shipment_history", "params": {"query": user_query}})
            actions.append({"tool": "VECTOR", "intent": "search_docs", "params": {"query": user_query}})
        else:
            actions.append({"tool": "VECTOR", "intent": "search_docs", "params": {"query": user_query}})
        return actions

    def generate_answer(self, user_query: str, tool_results: dict) -> str:
        summaries = []
        for k, v in tool_results.items():
            try:
                s = str(v)
                summaries.append(f"{k}: {s[:1000]}")
            except Exception:
                summaries.append(f"{k}: <unserializable>")
        return "\n\n".join(summaries)
