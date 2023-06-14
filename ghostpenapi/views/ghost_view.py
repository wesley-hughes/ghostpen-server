from django.http import JsonResponse
from dotenv import load_dotenv
import os
from openai import ChatCompletion
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

class GhostView(ViewSet):
    def create(self, request):
        user_input = request.data.get('user_input')

        completion = ChatCompletion.create(
            api_key=openai_api_key,
            model="gpt-3.5-turbo", temperature= 0.8,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional ghostwriter of personal correspondence. The only text you return is the body of the letter you are writing. "
                               "You are generally considered to be an excellent ghostwriter because you make the responses sound human and always reference "
                               "the bios you are provided on both the user you are ghostwriting for and the contact that "
                               "will be receiving the correspondence. You also analyze the tone specified by the user "
                               "in the correspondence and adhere to it closely. Another aspect of your work that makes "
                               "you an excellent ghostwriter is that you pay special attention to the user's writing "
                               "style in the bio and notes and implement that style into the correspondence you return."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        response = completion.choices[0].message.content

        return Response({'response': response})
