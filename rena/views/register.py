from discord import Interaction
from discord.enums import ButtonStyle
from discord.ui import View, button
from classes import Bot


class RegisterView(View):
    def __init__(self, bot: Bot):
        super().__init__(timeout=60)
        self.bot = bot

    @button(label="확인", style=ButtonStyle.green, emoji="✅")
    async def confirm(self, _, interaction: Interaction):
        await self.bot.db.insert("User", (interaction.user.id, "", 0, 0, True, True))
        await interaction.response.edit_message(content="성공적으로 가입 됐어! 레나가 학교생활을 도와줄게!", embed=None, view=None)

    @button(label="취소", style=ButtonStyle.red, emoji="✖️")
    async def cancel(self, _, interaction: Interaction):
        await interaction.response.edit_message(content="가입이 취소됐어... ", embed=None, view=None)

    async def on_timeout(self):
        await self.message.edit(content="가입이 취소됐어... ", embed=None, view=None)
