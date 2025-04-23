from ollama_agents.qa_agent import QnAAgent

agent = QnAAgent(data_path='data/inventory_monitoring.csv')
question = "Which products need restocking based on stock and expiry?"
response = agent.ask_question(question)
print("\n🤖 Response from Mistral:\n", response)
