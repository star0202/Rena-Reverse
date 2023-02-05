from logging import getLogger

from discord import ApplicationContext, Embed
from discord.ext.commands import Cog

from classes import Bot
from rena import COLOR
from rena.utils import private_bool, ephemeral_check
from utils import slash_command

logger = getLogger(__name__)


class UserCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @slash_command(name="프로필", description="내 프로필을 확인합니다.")
    async def profile(self, ctx: ApplicationContext):
        data = await self.bot.db.select("User", ctx.user.id)
        if not data:
            await ctx.respond("방금 코끼리한테 물어보고왔는데 없다고했어! `/가입`명령어를 사용해서 먼저 가입해줘!", ephemeral=True)
            return
        embed = Embed(title=ctx.user.name, color=COLOR)
        embed.set_author(name="프로필")
        embed.set_thumbnail(url=ctx.user.display_avatar.url)
        if data[1] and data[2]:
            if data[5]:
                school = await self.bot.neis.schoolInfo(ATPT_OFCDC_SC_CODE=data[1], SD_SCHUL_CODE=data[2])
                embed.add_field(name="🏫 내 학교 정보", value=f"""
        **[학교]** {school[0].SCHUL_NM}
**[학년/반]** {data[3]}학년 {data[4]}반

> `/학교 설정` 으로 내 학교 정보를 고칠 수 있어요.

-----
""", inline=False)
            else:
                embed.add_field(name="🏫 내 학교 정보", value=f"""
                🏫 내 학교 정보
**[학교]** 비공개
**[학년/반]** 비공개

> `/학교 설정` 으로 내 학교 정보를 고칠 수 있어요.

-----
""", inline=False)
        embed.add_field(name="🔒 공개 여부 설정", value=f"""
        **[ 내 학교 공개하기 ]** {private_bool(data[4])}
**[ 명령어 답변 공개하기 ]** {private_bool(data[5])}

> `/환경설정 변경` 으로 환경설정을 고칠 수 있어요.

-----
""")
        await ctx.respond(embed=embed, ephemeral=await ephemeral_check(data=data))


def setup(bot: Bot):
    logger.info("Loaded")
    bot.add_cog(UserCog(bot))
