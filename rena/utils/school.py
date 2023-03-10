from datetime import datetime

from discord import Embed

from rena import COLOR


def school_embed(school_list: list, index: int) -> Embed:
    school = school_list[index]
    embed = Embed(
        title=school.SCHUL_NM,
        description=f"{school.ENG_SCHUL_NM}\n\n--------------------", color=COLOR)
    embed.set_author(name="ð íêµ ê²ì ê²°ê³¼")
    embed.add_field(name="â íêµ ë¶ë¥", value=f"{school.SCHUL_KND_SC_NM}\n\n--------------------")
    fond = datetime.strptime(school.FOND_YMD, "%Y%m%d")
    embed.add_field(name="âï¸ ì¤ë¦½ì¼", value=fond.strftime("%Yë %mì %dì¼"
                                                       .encode('unicode-escape').decode())
                    .encode().decode('unicode-escape'))
    embed.add_field(name="ð« ì£¼ì (ëë¡ëª)", value=school.ORG_RDNMA, inline=False)
    embed.add_field(name="ð® ì°í¸ë²í¸", value=school.ORG_RDNZC)
    embed.add_field(name="ð² ëí ì í", value=school.ORG_TELNO)
    embed.add_field(name="ê¸°í", value=f"ð [íêµ ííì´ì§ ë°ë¡ê°ê¸°]({school.HMPG_ADRES})", inline=False)
    embed.set_footer(text=f"{index + 1}/{len(school_list)}")
    return embed
