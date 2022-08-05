import datetime

import dd_content


class DailyDigestEmail:
    def __init__(self):
        self.content = {
            'quote': {'include': True, 'content': dd_content.get_random_quote()},
            'weather': {'include': True, 'content': dd_content.get_weather_forecast()},
            'wikipedia': {'include': True, 'content': dd_content.get_wikipedia_article()},
        }

    def send_email(self):
        pass

    def format_message(self):
        text = f'Daily Digest - {datetime.date.today().strftime("%d %b %Y")}\n\n'

        if self.content['quote']['include'] and self.content['quote']['content']:
            text += 'Quote of the day\n'
            text += f'"{self.content["quote"]["content"]["quote"]}" - {self.content["quote"]["content"]["author"]}\n\n'

        if self.content['weather']['include'] and self.content['weather']['content']:
            text += f'Forecast for {self.content["weather"]["content"]["city"]} - ' \
                    f'{self.content["weather"]["content"]["country"]}\n\n'
            for forecast in self.content['weather']['content']['periods']:
                text += f'{forecast["timestamp"].strftime("%d %b %H:%M")} - {forecast["temp"]} - {forecast["description"]}\n'
            text += '\n'

        if self.content['wikipedia']['include'] and self.content['wikipedia']['content']:
            text += 'Random wiki page\n'
            text += f'{self.content["wikipedia"]["content"]["title"]}\n{self.content["wikipedia"]["content"]["extract"]}\n' \
                    f'{self.content["wikipedia"]["content"]["url"]}'

        return text


if __name__ == '__main__':
    email = DailyDigestEmail()
    message = email.format_message()

    with open('message.txt', 'w', encoding='utf-8') as f:
        f.write(message)
