import discord, asyncio, random
import os

game = discord.Game("인사봇 성공!")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in ad {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '지니야':
        await message.channel.send('네? 부르셨나요?')

    if message.content.startswith('안녕'):
        await message.channel.send('안녕!')

    if message.content.startswith('(끝)'):
        await message.channel.send('그런 명령어 없다 ㅡㅡ')
    
    ##if message.content.startswith('앵무새'):
        ##await message.channel.send('앵무새 죽이기')

    if message.content.startswith('엄'):
        await message.channel.send('준')
    if message.content.startswith('준'):
        await message.channel.send('식')
    if message.content.startswith('식'):
        await message.channel.send('엄')

    if message.content.startswith('?'):
        await message.channel.send('?')

    if message.content.startswith('ㄷ'):
        await message.channel.send('ㄷ')

    if message.content.startswith('덜'):
        await message.channel.send('덜덜?')

    if message.content.startswith('헬프'):
        await message.channel.send('도움!!!')

    if message.content.startswith('헲'):
        await message.channel.send('도움!!!')

    if message.content.startswith('살려'):
        await message.channel.send('도움!!!')

    if message.content.startswith('도와'):
        await message.channel.send('도움!!!')

    if message.content.startswith('ㅋㅋㅋㅋ'):
        await message.channel.send('ㅋㅋㅋㅋㅋㅋㅋ')

    if message.content.startswith('!채널메시지'):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[25: ])

    if message.content.startswith('임베드 테스트'):
        embed = discord.Embed(colour=discord.Colour.blue(), title="제-목", description="설-명")
        await message.channel.send(embed=embed)

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지 청소 완료!")
        await message.channel.send("이제 깨끗하게 사용해요!")

    if message.content == "주사위":
        await message.channel.send(f"{message.author.mention}님의 주사위 결과")
        await message.channel.send(random.randint(1,6))

    if message.content == "지니팩":
        await message.channel.send(f"{message.author.mention}님의 지니팩 결과")
        await message.channel.send(random.choice(['남동진 7일', '이유리 7일', '남동진 7일', '이유리 7일', '남동진 7일', '이유리 7일', '남동진 7일', '이유리 7일','남동진 7일', '이유리 7일', '남동진 7일', '이유리 7일', '남동진 7일', '이유리 7일', '남동진 7일', '이유리 7일', '남동진 30일', '이유리 30일', '남동진 30일', '이유리 30일', '남동진 무제한', '남동진 무제한']))

        
eccess_token = os.environ["BOT_TOKEN"]
client.run(eccess_token)
