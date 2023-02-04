from discord.enums import ButtonStyle
from discord.ui import View, button

from rena.utils import school_embed


class SearchView(View):
    def __init__(self, schools, index):
        super().__init__(timeout=60)
        self.schools = schools
        self.index = index

    @button(label="이전", style=ButtonStyle.blurple, emoji="◀️")
    async def previous(self, _, interaction):
        if self.index == 0:
            self.index = len(self.schools) - 1
        else:
            self.index -= 1
        await interaction.response.edit_message(embed=school_embed(self.schools, self.index), view=self)

    @button(label="다음", style=ButtonStyle.blurple, emoji="▶️")
    async def next(self, _, interaction):
        if self.index == len(self.schools) - 1:
            self.index = 0
        else:
            self.index += 1
        await interaction.response.edit_message(embed=school_embed(self.schools, self.index), view=self)

    @button(label="확인", style=ButtonStyle.green, emoji="✅")
    async def confirm(self, _, interaction):
        await interaction.response.edit_message(view=None)

    @button(label="취소", style=ButtonStyle.red, emoji="✖️")
    async def cancel(self, _, interaction):
        await interaction.response.edit_message(content="취소됐어!", embed=None, view=None)

    async def on_timeout(self):
        await self.message.edit(content="반응할 시간이 지났어!", embed=None, view=None)
