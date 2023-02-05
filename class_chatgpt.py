import openai
openai.api_key = "Your_API_key"

class Gpt_API:
    def __init__(self,prompt):
        self.prompt = prompt

    def get_result(self):
        completion = openai.Completion.create(engine="text-davinci-002", prompt=self.prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)
        print(completion)
        text = completion.choices[0].text
        return text


# obj = Gpt_API("continue")

# print(obj.get_result())
