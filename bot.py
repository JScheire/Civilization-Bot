import discord
import random
from discord.ext import commands

TOKEN = 'Njk3MTkyNDIxMDk1NjM3MDYy.XoztHQ.yK5lsoLlJAKX5Cl06n9r-PArH5U'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def draft(ctx, players):
    result = ''
    counter = 0
    civs = ['America',
            'Arabia',
            'Australia',
            'Aztec',
            'Brazil',
            'Canada',
            'China',
            'Egypt',
            'England',
            'France',
            'Germany',
            'Greece',
            'India',
            'Indonesia',
            'Japan',
            'Kongo',
            'Khmer',
            'Macedon',
            'Norway',
            'Poland',
            'Persia',
            'Rome',
            'Russia',
            'Scythia',
            'Spain',
            'Sumeria',
            'Mongolia',
            'Cree',
            'Korea',
            'Netherlands',
            'Nubia',
            'Ottomans',
            'Georgia',
            'Scotland',
            'Mapuche',
            'Zulu',
            'Hungary',
            'Maori',
            'Inca',
            'Mali',
            'Sweden'
        ]

    civlist = random.sample(civs, 3 * int(players))    

    for i in  range(0, int(players)):
        result += (f'Player {i + 1}: {civlist[counter]} {civlist[counter + 1]} {civlist[counter + 2]}\n') 
        counter += 3
    
    await ctx.send(result)

client.run(TOKEN)
