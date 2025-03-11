import asyncio

from telegram import Bot

from django.conf import settings

from applications.tasks import celery_app
from applications.insta_parser.utils import get_instagram_posts


@celery_app.task(name='Update data instagram')
def auto_update():
    posts = get_instagram_posts('nasa', 'Stars')
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    for post in posts:
        if post.has_required_hashtag:
            message = f"New post with hashtag #Stars:\n{post.url}\nDescription: {post.description}"
            bot.send_message(chat_id=settings.CHAT_ID, text=message)
            asyncio.run(__send_telegram_message(bot))


async def __send_telegram_message(bot):
    message = f"New post with hashtag #Stars:\n\nDescription: "
    await bot.send_message(chat_id=settings.CHAT_ID, text=message)
