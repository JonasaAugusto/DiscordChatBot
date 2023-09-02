import asyncio
from itertools import cycle
import discord
from discord import app_commands, ui
from discord import Embed
from discord.ext import commands, tasks
from datetime import datetime
import sqlite3
import config
from config import database, host, password, token, user

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def setup_hook(self) -> None:
        pass
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
            print(f"Bot Online!") 
        
        statuses = [f'Feito por LCssx#4061']
        displaying = cycle(statuses)
        running = True

        while running:
            current_status = next(displaying)
            await self.change_presence(status=discord.Status.online, activity=discord.Game(name=current_status, type=3))
            await asyncio.sleep(20)

intents = discord.Intents.default()
aclient = Client()
tree = app_commands.CommandTree(aclient)


@tree.command(description='Lista dos dados para o comando tutorial')
async def lista(ctx: discord.Interaction):
    await ctx.response.send_message(f'Todos os itens para saber o que pesquisar no comando /tutorial:\n\n**Construção\nElétrica ou Engenharia\nPZwiki\nSaúde\nAgronomia\nCulinária\nMecânica** ')

@tree.command(description='Exibe todos os tutoriais sobre um assunto')
async def tutorial(ctx: discord.Interaction, subject: str):

    if subject.lower() in ['construção','Construção', 'construcao', 'construçao', 'construction', 'Construcao', 'Construçao', 'Construction']:
        Carpintaria = Embed(title="Manual Completo de Carpintaria", url="https://www.youtube.com/watch?v=FaCQuyXbp1I", description="**Aprenda e desenvolva seu conhecimento sobre carpintaria!**")
        Carpintaria.set_thumbnail(url="https://projectzomboid.com/blog/content/uploads/2014/12/108600_screenshots_2014-11-25_00001.jpg")
        Metalurgia = Embed(title="Manual completo de Metalurgia", url="https://www.youtube.com/watch?v=zTyzEx1ews8", description="**Aprenda como subir de nivel em metalurgia e como fazer portas, janelas, caixas de metal e muito mais!**")
        Metalurgia.set_thumbnail(url="https://th.bing.com/th/id/OIG.Rxzx08da2EOcfpqD4xFr?pid=ImgGn")
        links = [Carpintaria, Metalurgia]

        await ctx.response.send_message(f'Olá {ctx.user.mention}, aqui estão os tutoriais sobre {subject} que talvez possa ajudar você:')

        for link in links:
            await ctx.followup.send(embed=link)

    if subject.lower() in ['eletric','elétrica', 'engenharia', 'eletrica', 'engineering', 'Engineer','Eletric','Elétrica', 'Engenharia', 'Eletrica', 'Engineering', 'Engineer']:
        Elétrica = Embed(title="Manual Completo Elétrica e Engenharia", url="https://www.youtube.com/watch?v=o-O-Z05dRCM", description="**Aprenda sobre Elétrica e Engenharia!**")
        Elétrica.set_thumbnail(url="https://th.bing.com/th/id/OIG.uvlG2ojnRJE_VCJX8J7X?pid=ImgGn")
        links = [Elétrica]

        await ctx.response.send_message(f'Olá {ctx.user.mention}, aqui estão os tutoriais de {subject} que possa ajudar você:')

        for link in links:
            await ctx.followup.send(embed=link)

    if subject.lower() in ['pzwiki','PZwiki']:
        PZwiki = Embed(title="Wiki completa para qualquer assunto do jogo", url="https://pzwiki.net/wiki/Main_Page/pt")
        links = [PZwiki]

        await ctx.response.send_message(f'Olá {ctx.user.mention}, aqui estão os tutoriais de {subject} que possa ajudar você:')

        for link in links:
            await ctx.followup.send(embed=link)

    if subject.lower() in ['health','primeiros socorros', 'cura','saude','saúde','medicina','Health','Primeiros Socorros', 'Cura','Saude','Saúde','Medicina']:
        Medicine = Embed(title="Manual Completo sobre Medicina", url="https://www.youtube.com/watch?v=_ojrSjjncJU", description="**Aumente seu conhecimento sobre Medicina!**")
        Medicine.set_thumbnail(url="https://th.bing.com/th/id/OIG.NdCVJs7wOC0PN1DFHEfr?pid=ImgGn")
        Firstaid = Embed(title="Manual Completo sobre Primeiros Socorros", url="https://www.youtube.com/watch?v=Xv5e5PZNM5U", description="**Aprenda como se fazer Primeiros Socorros!**")
        Firstaid.set_thumbnail(url="https://th.bing.com/th/id/OIG.LgfuoeVneH23jkOCtpfu?pid=ImgGn")
        links = [Firstaid, Medicine]

        await ctx.response.send_message(f'Olá {ctx.user.mention}, aqui estão os tutoriais de {subject} que possa ajudar você:')

        for link in links:
            await ctx.followup.send(embed=link)

    if subject.lower() in ['farming','agricultura','agro','agronomia','Farming','Agricultura','Agro','Agronomia']:
        Farming = Embed(title="Manual Completo sobre Agronomia", url="https://www.youtube.com/watch?v=niU9DxZckWo", description="**Desenvolva seu conhecimento sobre Farming!**")
        Farming.set_thumbnail(url="https://th.bing.com/th/id/OIG.nM8YlEKsr7ByoKVp7abT?pid=ImgGn")
        Fertilizer = Embed(title="Manual Completo sobre Adubagem", url="https://www.youtube.com/watch?v=zAuQ3m3ylWQ", description="**Saiba como usar merda corretamente!**")
        Fertilizer.set_thumbnail(url="https://th.bing.com/th/id/OIG.eOgCXGsKHHtvfQu954zb?pid=ImgGn")
        Trapping = Embed(title="Manual Completo sobre armadilhas de animais", url="https://www.youtube.com/watch?v=niU9DxZckWo", description="**Aprenda sobre Trapping!**")
        Trapping.set_thumbnail(url="https://th.bing.com/th/id/OIG.owKRCiuFSpeI9_pnE8FZ?pid=ImgGn")
        links = [Farming, Fertilizer, Trapping]

        await ctx.response.send_message(f'Olá {ctx.user.mention}, aqui estão os tutoriais de {subject} que possa ajudar você:')

        for link in links:
            await ctx.followup.send(embed=link)

    if subject.lower() in ['cozinha','comida','food','cooking','culinaria','culinária','Culinária','Culinaria']:
        Cooking = Embed(title="Manual Completo sobre Culinária", url="https://www.youtube.com/watch?v=mEhFXEnDW1U", description="**Aprenda a fazer um bom lanche!**")
        Cooking.set_thumbnail(url="https://th.bing.com/th/id/OIG.nenBHDuWdWx4nZ38z9._?pid=ImgGn")
        links = [Cooking]

        await ctx.response.send_message(f'Olá {ctx.user.mention}, aqui estão os tutoriais de {subject} que possa ajudar você:')

        for link in links:
            await ctx.followup.send(embed=link)
    if subject.lower() in ['mechanic','mecanica','Mecânica','Mecanica']:
        CarMechanic = Embed(title="Manual Completo sobre Mecânica", url="https://www.youtube.com/watch?v=_p50RgEbwIE", description="**Saiba como fazer um projetinho no seu carro dos sonhos!**")
        CarMechanic.set_thumbnail(url="https://th.bing.com/th/id/OIG.TjCZfn9W4irFDo9ER20f?pid=ImgGn")
        Mechanic = Embed(title="Manual Completo sobre Mecânica", url="https://www.youtube.com/watch?v=T_KVvJxjE0k", description="**Tudo o que você precisa saber sobre Mecânica!**")
        Mechanic.set_thumbnail(url="https://th.bing.com/th/id/OIG.x3oFo3xpaVfIb0AJb8q.?pid=ImgGn")
        links = [CarMechanic, Mechanic]

        await ctx.response.send_message(f'Olá {ctx.user.mention}, aqui estão os tutoriais de {subject} que possa ajudar você:')

        for link in links:
            await ctx.followup.send(embed=link)

    else:
        await ctx.response.send_message(f'Desculpe, eu não tenho tutoriais sobre o assunto "{subject}".')

@tree.command(description='Envia um link para o mapa do Project Zomboid')
async def mapa(ctx):
    description = f'Mapa interativo de Project Zomboid!'
    
    embed = discord.Embed(description=description, url="https://map.projectzomboid.com", title= "Mapa Project Zomboid")
    embed.set_image(url="https://th.bing.com/th/id/OIG..tC0wbUyWBjmHIRUHHbN?pid=ImgGn")

    await ctx.response.send_message(embed=embed)


@tree.command()
@commands.is_owner()
async def bemvindo(ctx):
    description = f'**É muito bom ter você aqui!\n\n Espero que tenha habilidade o suficiente para retardar a sua morte.**\n\n **Leia o canal INTRODUÇÃO para saber o que o Zombot pode fazer.**\n\n Clique no joinha para verificarmos se você é um humano de verdade.'
    
    embed = discord.Embed(description=description)
    embed.set_image(url="https://th.bing.com/th/id/OIG.eO3rSsWpIj.wzP_QQSzI?pid=ImgGn")
    
    await ctx.response.send_message("**Olá**")
    message = await ctx.followup.send(embed=embed)
    await message.add_reaction('👍')

@aclient.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '👍':
        role = discord.utils.get(user.guild.roles, id=1146770045196828712)
        if role not in user.roles:
            await user.add_roles(role)




@tree.command(description='Apagar Mensagens')
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: int):
    await interaction.response.defer(thinking=True, ephemeral=True)
    deleted_messages = await interaction.channel.purge(limit=amount)
    await interaction.followup.send(f"{len(deleted_messages)} mensagens foram deletadas.", ephemeral=True)

@clear.error
async def on_error(interaction: discord.Interaction, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        await interaction.response.send_message("Você não tem permissão pra usar esse comando.", ephemeral=True)
    elif isinstance(error, commands.BotMissingPermissions):
        await interaction.response.send_message("Não tenho permissão pra usar esse comando!")

aclient.run(token)