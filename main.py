import nextcord
import os
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Manually define role and channel IDs
ROLE_VERIFY_ID = 1337073443723546736
WELCOME_CHANNEL_ID = 1136244686735024209
GOODBYE_CHANNEL_ID = 1310972132792074281
VERIFY_CHANNEL_ID = 1311349947429556275

# Get the token from the environment variable
TOKEN = ("token_you")


class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="ยืนยันตัวตน", style=nextcord.ButtonStyle.red)
    async def verify(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role = interaction.guild.get_role(ROLE_VERIFY_ID)
        if role in interaction.user.roles:
            await interaction.response.send_message("💢คุณมียศนี้อยู่แล้วครับ", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.user.send(f"คุณได้รับยศ {role} ในเซิฟเวอร์ {interaction.guild.name}")
            await interaction.response.send_message(f"✅คุณได้รับยศ {role}", ephemeral=True)


@bot.event
async def on_ready():
    embed = nextcord.Embed(title="ยืนยันตัวตน")
    view = Button()
    channel = bot.get_channel(VERIFY_CHANNEL_ID)
    if channel:
        await channel.send(embed=embed, view=view)
    print(f"{bot.user} ออนไลน์แล้ว")


@bot.event
async def on_member_join(member):
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    embed = nextcord.Embed(title=f"ยินดีต้อนรับ {member.name} เข้าสู่ {member.guild.name}")
    embed.set_image(url=avatar_url)
    await bot.get_channel(WELCOME_CHANNEL_ID).send(embed=embed)
    print(f"{member.name} ได้เข้าสู่เซิฟเวอร์")


@bot.event
async def on_member_remove(member):
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    embed = nextcord.Embed(title=f"{member.name} ได้ออกจาก {member.guild.name}")
    embed.set_image(url=avatar_url)
    await bot.get_channel(GOODBYE_CHANNEL_ID).send(embed=embed)
    print(f"{member.name} ได้ออกจากเซิฟเวอร์")

server_on()

bot.run(TOKEN)

