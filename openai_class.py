import openai
import dotenv


class TextProcessor:
    def __init__(self):
        self.openai = openai
        self.openai.api_key = dotenv.get_key('.env', 'OPEN_API_KEY')

    def openai_translate(self, text, language):
        response = self.openai.Completion.create(
            engine="davinci",
            prompt=f"Translate from French to {language}:\nEnglish: {text}\n{language}: ",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        return response.choices[0].text

    def openai_text_summary(self, text):
        response = self.openai.Completion.create(
            engine="davinci",
            prompt=f"Original text: {text}\nSummary: ",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        return response.choices[0].text

    def openai_text_generator(self, theme, text):
        reponse = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": f"Tu es un rédacteur web qui synthétise l'actualité en 50 mots sur la thématique '{theme}' Tu fais des liaisons entre les articles avec des mots tel que 'mais', 'donc', 'or', 'par contre', 'en revanche', 'en effet', 'cependant', 'toutefois', 'par ailleurs', 'par contre', 'par contre, 'enfin'"},
                {"role": "user",
                 "content": "Voici la liste des actualités à synthétiser :" + text},
            ],
            max_tokens=100,
            temperature=0.9,
        )

        return reponse['choices'][0]['message']["content"]

    def openai_codex(self, code):
        response = self.openai.Completion.create(
            engine="davinci-codex",
            prompt=f"\"\"\"\n{code}\n\"\"\"\n\n",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        return response.choices[0].text

    def openai_image(self, prompt):
        response = self.openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        return response['data'][0]['url']
