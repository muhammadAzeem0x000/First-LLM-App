from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")

    prompt_template_name= PromptTemplate(
        input_variables=['animal_type','pet_color'],
        template="I have a {animal_type} of color {pet_color}. I want a cool name for it. Generate 5 names of it."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

    return response


# def langchain_agent():
#     llm= ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")

#     tools = load_tools(["wikipedia", "llm-math"], llm=llm)

#     agent = initialize_agent(
#         tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
#     )

#     result = agent.run(
#         "What is the average age of dog? Multiply the age by 3"
#     )

#     print(result)

if __name__ == "__main__":
    # langchain_agent()
    print(generate_pet_name("Dog", "red"))
    print("\n\n Program Ends!")