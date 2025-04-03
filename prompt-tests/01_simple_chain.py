from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Define the prompt
template = "Rewrite this sentence in a more professional tone:\n\n{sentence}"
prompt = PromptTemplate.from_template(template)

# Create the chain
llm = ChatOpenAI(temperature=0.7)
chain = LLMChain(llm=llm, prompt=prompt)

# Run test
input_text = "i need a quote for fixing my bathroom, it's a mess"
response = chain.run({"sentence": input_text})

print("🗣 Original:", input_text)
print("🧠 Rewritten:", response)
