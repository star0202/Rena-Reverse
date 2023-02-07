from typing import Optional

from discord import Interaction, User
from discord.enums import ButtonStyle
from discord.ui import View, button

from classes import Database
from rena.utils import school_embed


class SelectView(View):
    def __init__(
            self,
            schools: list,
            index: int,
            is_setting: Optional[bool] = False,
            db: Optional[Database] = None,
            details: Optional[tuple[int, int]] = None
    ):
        super().__init__(timeout=60)
        if is_setting and not db:
            raise ValueError("db is required")
        self.is_setting = is_setting
        self.db = db
        self.schools = schools
        self.index = index
        self.details = details

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
    async def confirm(self, _, interaction: Interaction):
        if self.is_setting and isinstance(self.db, Database) and isinstance(interaction.user, User):
            await self.db.update("user", "ooe", str(self.schools[self.index].ATPT_OFCDC_SC_CODE), interaction.user.id)
            await self.db.update("user", "school", self.schools[self.index].SD_SCHUL_CODE, interaction.user.id)
            await self.db.update("user", "grade", self.details[0], interaction.user.id)
            await self.db.update("user", "room", self.details[1], interaction.user.id)
            await interaction.response.edit_message(content="성공적으로 등록되었어요.", embed=None, view=None)
        await interaction.response.edit_message(view=None)

    @button(label="취소", style=ButtonStyle.red, emoji="✖️")
    async def cancel(self, _, interaction):
        await interaction.response.edit_message(content="취소됐어!", embed=None, view=None)

    async def on_timeout(self):
        await self.message.edit(content="반응할 시간이 지났어!", embed=None, view=None)
