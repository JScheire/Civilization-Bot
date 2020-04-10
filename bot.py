import discord
import random
from discord.ext import commands

key = open('key.txt', 'r')
TOKEN = key.read()

client = commands.Bot(command_prefix = '!')

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

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def list(ctx):
    result = ''
    result += civs[0]
    for i in range(1, len(civs)):
        result += (', ' + civs[i])
    
    await ctx.send(result)

@client.command()
async def ban(ctx, banned):
    civs.remove(banned.capitalize())

    await ctx.send(f'{banned.capitalize()} has been banned!')

@client.command()
async def reset(ctx):
    global civs
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

    await ctx.send('Civs have been reset.')

@client.command()
async def draft(ctx, players):
    result = ''
    counter = 0
    civlist = random.sample(civs, 5 * int(players))    

    for i in range(0, int(players)):
        result += (f'Player {i + 1}: {civlist[counter]} {civlist[counter + 1]} {civlist[counter + 2]} {civlist[counter + 3]} {civlist[counter + 4]}\n') 
        counter += 5
    

    await ctx.send(result)

@client.command()
async def gay(ctx):
    await ctx.send(file = discord.File('smax.jpg'))

@client.command()
async def picklerick(ctx):
    await ctx.send(file = discord.File('pickle.png'))

@client.command()
async def toes(ctx):
    await ctx.send(':weary:')

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error: Type !help')


client.run(TOKEN)
