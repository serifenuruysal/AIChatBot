# chatbot/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from openai import OpenAI
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

client = OpenAI(api_key=settings.OPENAI_API_KEY )

@api_view(['POST'])
def chat_view(request):
    user_message = request.data.get('message', '')
    
    try:
        logger.debug(f"Sending message to OpenAI: {user_message}")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        
        ai_message = response.choices[0].message.content
        logger.debug(f"Received response from OpenAI: {ai_message}")
        return Response({"message": ai_message})
    except Exception as e:
        logger.error(f"Error in chat_view: {str(e)}")
        return Response({"error": str(e)}, status=500)

# Make sure your settings.py includes the logging configuration as shown in previous responses