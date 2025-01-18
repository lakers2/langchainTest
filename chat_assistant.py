from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

class ChatAssistant:
    def __init__(self, model_name="llama3.2:latest"):
        # Initialize Ollama chat model
        self.chat = ChatOllama(
            model=model_name,
            temperature=0.7
        )
        
        # Initialize conversation memory
        self.memory = ConversationBufferMemory(
            return_messages=True,
            memory_key="chat_history"
        )
        
        # Create prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant. Respond in a friendly and concise manner."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        
        # Create the chain
        self.chain = self.prompt | self.chat | StrOutputParser()

    def chat_with_ai(self, user_input: str) -> str:
        response = self.chain.invoke({
            "input": user_input,
            "chat_history": self.memory.chat_memory.messages
        })
        self.memory.save_context({"input": user_input}, {"output": response})
        return response 