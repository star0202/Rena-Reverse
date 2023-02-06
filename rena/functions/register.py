from logging import getLogger

from discord import ApplicationContext, Embed
from discord.ext.commands import Cog

from classes import Bot
from rena import COLOR
from rena.views import RegisterView, UnRegisterView
from rena.utils import is_registered
from utils import slash_command

logger = getLogger(__name__)


class Register(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @slash_command(name="가입", description="레나에 가입합니다.")
    async def register(self, ctx: ApplicationContext):
        if await is_registered(ctx.user.id, db=self.bot.db):
            await ctx.respond("이미 가입되어있다구!!", ephemeral=True)
            return
        embed = Embed(title="레나 서비스 약관", description="""
        Rena를 사용하면 [팀 크레센도 이용약관](https://team-crescendo.me/policy/bot-terms/) 과 [개인정보 취급방침](https://team-crescendo.me/policy/privacy/) 및 다음 Rena 추가 서비스 약관에 동의하는 것으로 간주됩니다.

본 Rena 추가 서비스 약관은 Rena의 실행 가능한 코드 버전에 적용됩니다.

대부분의 Rena 소스 코드는 [페이지](https://github.com/team-crescendo/Crenata/blob/main/LICENSE) 에 명시된 오픈소스 소프트웨어 라이선스 계약에 따라 무료로 제공됩니다.
""", color=COLOR)
        await ctx.respond(embed=embed, ephemeral=True, view=RegisterView(self.bot))

    @slash_command(name="탈퇴", description="레나에 탈퇴합니다.")
    async def unregister(self, ctx: ApplicationContext):
        if not await is_registered(ctx.user.id, db=self.bot.db):
            await ctx.respond("가입을해야 탈퇴도하지!! `/가입`명령어를 사용해서 가입해줘!", ephemeral=True)
            return
        embed = Embed(title="탈퇴", description="**정말 탈퇴하시겠습니까?**\n탈퇴하시면 레나에 가입되신 모든 정보가 지체없이 파기됩니다.", color=COLOR)
        await ctx.respond(embed=embed, ephemeral=True, view=UnRegisterView(self.bot))


def setup(bot: Bot):
    logger.info("Loaded")
    bot.add_cog(Register(bot))
