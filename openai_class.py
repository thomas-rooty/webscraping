import openai


class TextProcessor:
    def __init__(self):
        self.openai = openai
        self.openai.api_key = "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"

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
        print(f'Original text:{text}\nTheme: {theme}\nGenerated text: ')
        response = self.openai.Completion.create(
            engine="davinci",
            prompt=f"Original text: {text}\nTheme: {theme}\nText: ",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        return response.choices[0].text

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
