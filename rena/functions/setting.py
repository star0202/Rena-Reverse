from logging import getLogger

from discord import ApplicationContext, SlashCommandGroup, Option
from discord.ext.commands import Cog

from classes import Bot

logger = getLogger(__name__)


class Setting(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    settings = SlashCommandGroup("환경설정")

    @settings.command(name="변경", description="환경설정을 변경합니다.")
    async def change(
            self, ctx: ApplicationContext,
            private: Option(bool, description="학교 이름을 비공개로 할지 여부입니다."),
            ephemeral: Option(bool, description="자기 자신에게만 보이게 할지 여부입니다.")
    ):
        if await self.bot.db.select("User", ctx.user.id):
            await self.bot.db.update("User", "private", private, ctx.user.id)
            await self.bot.db.update("User", "ephemeral", ephemeral, ctx.user.id)
            await ctx.respond("성공적으로 수정했어! 다음부터는 이 설정값으로 알려줄게!", ephemeral=True)
        else:
            await ctx.respond("방금 코끼리한테 물어보고왔는데 없다고했어! `/가입`명령어를 사용해서 먼저 가입해줘!.", ephemeral=True)


def setup(bot: Bot):
    logger.info("Loaded")
    bot.add_cog(Setting(bot))
