class Agent:
    def __init__(self, client, system, model="deepseek-chat") -> None:
        self.client = client
        self.system = system
        self.model = model
        self.messages: list = []
        if self.system:
            self.messages.append({"role": "system", "content": self.system})
    
    def __call__(self, message):
        if message:
            self.messages.append({"role":"user", "content": message})
        result = self.execute()
        self.messages.append({"role":"assistant", "content": result})
        return result

    def execute(self):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=False
        )
        return response.choices[0].message.content