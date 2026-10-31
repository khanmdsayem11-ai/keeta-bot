import os
import requests

# গিটহাব সিক্রেট থেকে টোকেন এবং চ্যাট আইডি নেওয়া হবে
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')


def send_telegram_message(message):
  url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
  data = {'chat_id': CHAT_ID, 'text': message}
  try:
    requests.post(url, data=data)
    print('Message sent successfully!')
  except Exception as e:
    print('Error sending message:', e)


if __name__ == '__main__':
  # টেস্ট মেসেজ পাঠানোর জন্য
  send_telegram_message(
      '🤖 Keeta ড্যাশবোর্ড ট্র্যাকিং গিটহাব অ্যাকশনস দ্বারা চালু হয়েছে!'
  )
