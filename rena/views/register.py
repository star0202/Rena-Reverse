from discord import Interaction, User
from discord.enums import ButtonStyle
from discord.ui import View, button

from classes import Bot


class RegisterView(View):
    def __init__(self, bot: Bot):
        super().__init__(timeout=60)
        self.bot = bot

    @button(label="확인", style=ButtonStyle.green, emoji="✅")
    async def confirm(self, _, interaction: Interaction):
        if isinstance(interaction.user, User):
            await self.bot.db.insert("User", (interaction.user.id, "", "", 0, 0, True, True))
            await interaction.response.edit_message(content="성공적으로 가입 됐어! 레나가 학교생활을 도와줄게!", embed=None, view=None)

    @button(label="취소", style=ButtonStyle.red, emoji="✖️")
    async def cancel(self, _, interaction: Interaction):
        await interaction.response.edit_message(content="가입이 취소됐어... ", embed=None, view=None)

    async def on_timeout(self):
        await self.message.edit(content="가입이 취소됐어... ", embed=None, view=None)


class UnRegisterView(View):
    def __init__(self, bot: Bot):
        super().__init__(timeout=60)
        self.bot = bot

    @button(label="확인", style=ButtonStyle.green, emoji="✅")
    async def confirm(self, _, interaction: Interaction):
        if isinstance(interaction.user, User):
            await self.bot.db.delete("User", interaction.user.id)
            await interaction.response.edit_message(content="탈퇴됐어... 다음에 또 만나자...!!", embed=None, view=None)

    @button(label="취소", style=ButtonStyle.red, emoji="✖️")
    async def cancel(self, _, interaction: Interaction):
        await interaction.response.edit_message(content="마음이 바뀌었구나! 계속 레나가 학교생활을 도와줄게!", embed=None, view=None)

    async def on_timeout(self):
        await self.message.edit(content="마음이 바뀌었구나! 계속 레나가 학교생활을 도와줄게!", embed=None, view=None)
