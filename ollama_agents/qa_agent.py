import pandas as pd
import ollama

class QnAAgent:
    def __init__(self, data_path):
        self.data_path = data_path

    def generate_prompt(self, question):
        df = pd.read_csv(self.data_path)
        short_df = df.head(2)
        table_data = short_df.to_markdown(index=False)
        return f"""Here is the inventory data:

{table_data}

Answer the following question based on the table above:
Q: {question}
"""

    def ask_question(self, question):
        prompt = self.generate_prompt(question)
        response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
