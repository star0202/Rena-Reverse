from logging import getLogger

from discord import SlashCommandGroup, ApplicationContext, Option
from discord.ext.commands import Cog

from classes import Bot
from rena.utils import school_embed
from rena.views import SearchView

logger = getLogger(__name__)


class School(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    school = SlashCommandGroup("학교")

    @school.command(name="검색", description="학교를 검색합니다.")
    async def search(self, ctx: ApplicationContext, school_name: Option(str, description="학교 이름")):
        schools = await self.bot.neis.schoolInfo(SCHUL_NM=school_name)
        if schools:
            embed = school_embed(schools, 0)
            await ctx.respond(embed=embed, view=SearchView(schools, 0))
        else:
            await ctx.respond("내가 방금 친구들한테 물어봤는데, 그런 정보는 없던것 같아!", ephemeral=True)


def setup(bot: Bot):
    logger.info("Loaded")
    bot.add_cog(School(bot))
