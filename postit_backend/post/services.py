import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_social_media_post(context):
    try:

        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Create a social media post based on the following content. Make it engaging and suitable for LinkedIn, Facebook, and Twitter: {context}"}
            ]
        )

        post_content = completion.choices[0].message['content']
        return post_content
    except Exception as e:
        print(f"Error generating post: {e}")
        return None
