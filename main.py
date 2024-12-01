import os
import nextcord
from nextcord.ext import commands

from myserver import server_on

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


roleverify = 1136220565762482176
welcome_channel = 1136244686735024209
goodbye_channel = 1310972132792074281

@bot.event
async def on_ready():
    embed = nextcord.Embed(title="ยืนยันตัวตน")
    view = button()
    await bot.get_channel(1311662370598158336).send(embed=embed, view=view)
    print(f"{bot.user} ออนไลน์แล้ว")


@bot.event
async def on_member_join(member):
    embed = nextcord.Embed(title=f"ยินดีต้อนรับ คุณ {member.name} เข้าสู่ เซิฟเวอร์ {member.guild.name}", description=f"{member.mention} เข้าสู่ เซิฟเวอร์แล้ว")
    embed.set_image(member.avatar.url)
    await bot.get_channel(welcome_channel).send(embed=embed)
    print(f" {member.name} ได้เข้าสู่เซิฟเวอร์")

@bot.event
async def on_member_remove(member):
    embed = nextcord.Embed(title=f"คุณ {member.name} ได้ออกจากเซิร์ฟเวอร์ {member.guild.name}", description="{member.mention} ได้ออกจากเซิร์ฟเวอร์แล้ว")
    embed.set_image(member.avatar.url)
    await bot.get_channel(goodbye_channel).send(embed=embed)
    print(f" {member.name} ได้ออกจากเซิฟเวอร์")

class button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="ยืนยันตัวตน", style=nextcord.ButtonStyle.red)
    async def verify(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role = interaction.guild.get_role(roleverify)
        if role in interaction.user.roles:
            await interaction.response.send_message("💢คุณมียศนี้อยู่แล้วครับ", ephemeral=True)
            return
        else:
            await interaction.user.add_roles(role)
            await interaction.user.send(f"คุณได้รับยศ {role} ในเซิฟเวอร์ {interaction.guild.name}")
            await interaction.response.send_message(f"✅คุณได้รับยศ {role}", ephemeral=True)

server_on()

bot.run(os.getenv('TOKEN'))