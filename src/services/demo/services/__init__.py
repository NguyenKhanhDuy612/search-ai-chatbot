from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate
from src.configs.settings import gemini_model, google_api_key


class DemoService:
	# Initialize the Gemini model
	llm = ChatGoogleGenerativeAI(
		model=gemini_model,
		google_api_key=google_api_key,
		temperature=0.7,
	)

	# Create a prompt template
	prompt = PromptTemplate(
		input_variables=["question"],
		template="Answer the following question: {question}"
	)

	# Create a chain
	chain = RunnablePassthrough() | prompt | llm | StrOutputParser()

	@classmethod
	def ask_question(cls, question: str) -> str:
		response = cls.chain.invoke(input=question)
		return response
