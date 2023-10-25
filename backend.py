import openai
class ChatBot:
  def __init__(self):
    openai.api_key="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"

  def get_response(self, user_input):
     response = openai.Completion.create(
       engine="text-davinci-003",
       prompt=user_input,
       max_tokens=1000,
       temperature=0.3
     ).choices[0].text
     return response


if __name__ == "__main__":

    bot = ChatBot()
    response = bot.get_response("What is the live cricket World cup score?")
    print(response)
