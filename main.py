from pyrogram import Client, filters
from flask import Flask

app = Flask(Client(
    "my_bot",
    api_id=1861278,
    api_hash="f694802640d8019748c2503ee11f237b",
    bot_token="1482891629:AAFx_4DauOFQVoZeOVLJOxmHLEsUwtjGLrw"
))

# @app.on_message(filters.private)
# async def hello(client, message):


@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply_text(f"tu {message.text}")
    await message.reply_text(f"Hello {message.from_user.mention} kaisa hai lavde")

if __name__ == '__main__':
    app.run(debug=True)
