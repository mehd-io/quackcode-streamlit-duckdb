from ollama import Client

client = Client(host="http://host.docker.internal:11434")
response = client.chat(
    model="duckdb-nsql",
    messages=[
        {
            "role": "user",
            "content": "get me a query to write from a csv",
        },
    ],
)
print(response["message"]["content"])
