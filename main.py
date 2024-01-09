# Pycordを読み込む
import discord

# アクセストークンを設定
TOKEN = ""  # 自分のアクセストークンと置換してください

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Activity(name='チャット', type=discord.ActivityType.watching)
)

# 起動時に自動的に動くメソッド
# #03で詳しく説明します
@bot.event
async def on_ready():
    # 起動すると、実行したターミナルに"Hello!"と表示される
    print("start")

# Botが見える場所でメッセージが投稿された時に動くメソッド
@bot.event
async def on_message(message: discord.Message):
    # メッセージ送信者がBot(自分を含む)だった場合は無視する
    if message.author.bot:
        return



@bot.command(name="おみくじ", description="おみくじを引きます")
async def omikuji(ctx: discord.ApplicationContext):
    import random
    omikuji = ["大吉", "中吉", "小吉", "吉", "凶", "大凶"]
    await ctx.respond(f"{ctx.author.name}さんの今日の運勢は" + random.choice(omikuji) + "です")
# Botを起動
bot.run(TOKEN)
