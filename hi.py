import discord, requests
token = ''
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as ' + client.user)

@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content.startswith('!ccu'):
        await message.channel.send('Getting CCU for that game...')
        parts = message.content.split()
        if len(parts) != 2: 
            await message.channel.send('ERROR: could not split.\nCorrect usage: !ccu <game ID>')
            return
        g_id = parts[1]
        u_url = 'https://apis.roblox.com/universes/v1/places/' + g_id + '/universe'
        gr = requests.get(u_url, timeout=5)
        u_id = str(gr.json()['universeId'])
        url = 'https://games.roblox.com/v1/games?universeIds=' + u_id
        print(g_id)
        print(u_url)
        print(gr)
        print(u_id)
        print(url)
        try:
            r = requests.get(url, timeout=5)
            data = r.json()['data']
            print(r)
            print(data)
            if not data:
                await message.channel.send('ERROR: game not found.')
                return
            game = data[0]
            name = str(game['name'])
            ccu = str(game['playing'])
            print(name)
            print(ccu)
            await message.channel.send('The CCU of ' + name + ' is ' + ccu + ' players.')
        except Exception as e:
            await message.channel.send('ERROR: could not fetch ccu.')


    if message.content.startswith('!visits'):
        await message.channel.send('Getting visits for that game...')
        parts = message.content.split()
        if len(parts) != 2: 
            await message.channel.send('ERROR: could not split.\nCorrect usage: !visits <game ID>')
            return
        g_id = parts[1]
        u_url = 'https://apis.roblox.com/universes/v1/places/' + g_id + '/universe'
        gr = requests.get(u_url, timeout=5)
        u_id = str(gr.json()['universeId'])
        url = 'https://games.roblox.com/v1/games?universeIds=' + u_id
        print(g_id)
        print(u_url)        
        print(gr)
        print(u_id)
        print(url)
        try:
            r = requests.get(url, timeout=5)
            data = r.json()['data']
            print(r)
            print(data)
            if not data:
                await message.channel.send('ERROR: game not found.')
                return
            game = data[0]
            name = str(game['name'])
            visits = str(game['visits'])
            print(name)
            print(visits)
            await message.channel.send('The visit count of ' + name + ' is ' + visits + ' players.')
        except Exception as e:
            await message.channel.send('ERROR: could not fetch visits.')


    if message.content.startswith('!creator'):
        await message.channel.send('Finding creator of that game...')
        parts = message.content.split()
        if len(parts) != 2: 
            await message.channel.send('ERROR: could not split.\nCorrect usage: !creator <game ID>')
            return
        g_id = parts[1]
        u_url = 'https://apis.roblox.com/universes/v1/places/' + g_id + '/universe'
        gr = requests.get(u_url, timeout=5)
        u_id = str(gr.json()['universeId'])
        url = 'https://games.roblox.com/v1/games?universeIds=' + u_id
        print(g_id)
        print(u_url)        
        print(gr)
        print(u_id)
        print(url)
        try:
            r = requests.get(url, timeout=5)
            data = r.json()['data']
            print(r)
            print(data)
            if not data:
                await message.channel.send('ERROR: game not found.')
                return
            game = data[0]
            name = str(game['name'])
            creator = str(game['creator']['name'])
            print(name)
            print(creator)
            await message.channel.send('The creator of ' + name + ' is ' + creator)
        except Exception as e:
            await message.channel.send('ERROR: could not fetch creator.')


    if message.content.startswith('!server-size'):
        await message.channel.send('Finding server size of that game...')
        parts = message.content.split()
        if len(parts) != 2: 
            await message.channel.send('ERROR: could not split.\nCorrect usage: !max-players <game ID>')
            return
        g_id = parts[1]
        u_url = 'https://apis.roblox.com/universes/v1/places/' + g_id + '/universe'
        gr = requests.get(u_url, timeout=5)
        u_id = str(gr.json()['universeId'])
        url = 'https://games.roblox.com/v1/games?universeIds=' + u_id
        print(g_id)
        print(u_url)        
        print(gr)
        print(u_id)
        print(url)
        try:
            r = requests.get(url, timeout=5)
            data = r.json()['data']
            print(r)
            print(data)
            if not data:
                await message.channel.send('ERROR: game not found.')
                return
            game = data[0]
            name = str(game['name'])
            ss = str(game['maxPlayers'])
            print(name)
            print(ss)
            await message.channel.send('The server size of ' + name + ' is ' + ss + ' players')
        except Exception as e:
            await message.channel.send('ERROR: could not fetch server size.')
client.run(token)