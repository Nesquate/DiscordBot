import discord, json
from discord.ext import commands

# 使用 json 是為了要使用 setting.json 儲存敏感資料

# 開檔
# 把開檔後的變數名稱設定為 jFile
with open('setting.json', 'r', encoding='utf8') as jFile:
    # 並且使用 json 的方式讀入
    jData = json.load(jFile)

# Prefix
# 就是呼叫 bot 時的前褟是什麼
bot = commands.Bot(command_prefix='!')


# 如果 Bot Server 準備好就在後端上顯示訊息
@bot.event
async def on_ready():
    print("I am Okay!")


# 加入訊息與離開訊息
# 用 get_channel 取得要發送訊息的 Channel ID
# 再用 send() 把加入訊息發送到指定頻道上
@bot.event
async def on_member_join(member):
    # 利用 json 的方式載入 Channel ID
    channel = bot.get_channel(int(jData['WelcomeChannel']))
    await channel.send(f'{member} Join!')
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jData['LeaveChannel']))
    await channel.send(f'{member} Leave!')


# Ctx = context (上下文)
# 根據上下文判別是誰發送這個訊息、在哪個頻道發送這個訊息等等
# 根據 ctr 的資訊去做回應
@bot.command()
# def foo(ctx)
# foo = 你要的指令名稱
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')
    # 之後去研究一下 f 字串格式化的問題

while 1:
    bot.run(jData['TOKEN'])