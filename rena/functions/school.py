from logging import getLogger

from discord import SlashCommandGroup, ApplicationContext, Option
from discord.ext.commands import Cog
from neispy.error import DataNotFound

from classes import Bot
from rena.utils import school_embed, ephemeral_check
from rena.views import SelectView

logger = getLogger(__name__)


class School(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    school = SlashCommandGroup("학교")

    @school.command(name="검색", description="학교를 검색합니다.")
    async def search(self, ctx: ApplicationContext, school_name: Option(str, description="학교 이름")):
        try:
            schools = await self.bot.neis.schoolInfo(SCHUL_NM=school_name)
            embed = school_embed(schools, 0)
            await ctx.respond(embed=embed, view=SelectView(schools, 0))
        except DataNotFound:
            await ctx.respond("내가 방금 친구들한테 물어봤는데, 그런 정보는 없던것 같아!", ephemeral=True)

    @school.command(name="설정", description="학교를 설정합니다.")
    async def set(
            self, ctx: ApplicationContext,
            school_name: Option(str, description="설정할 학교 이름입니다."),
            grade: Option(int, description="설정할 학년입니다."),
            room: Option(int, description="설정할 반입니다.")
            ):
        try:
            schools = await self.bot.neis.schoolInfo(SCHUL_NM=school_name)
            embed = school_embed(schools, 0)
            await ctx.respond(
                embed=embed,
                view=SelectView(schools, 0, True, self.bot.db, (grade, room)),
                ephemeral=await ephemeral_check(ctx.user.id, db=self.bot.db)
            )
        except DataNotFound:
            await ctx.respond("내가 방금 친구들한테 물어봤는데, 그런 정보는 없던것 같아!", ephemeral=True)


def setup(bot: Bot):
    logger.info("Loaded")
    bot.add_cog(School(bot))
