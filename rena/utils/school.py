from datetime import datetime

from discord import Embed

from rena import COLOR


def school_embed(school_list: list, index: int) -> Embed:
    school = school_list[index]
    embed = Embed(
        title=school.SCHUL_NM,
        description=f"{school.ENG_SCHUL_NM}\n\n--------------------", color=COLOR)
    embed.set_author(name="🔍 학교 검색 결과")
    embed.add_field(name="❓ 학교 분류", value=f"{school.SCHUL_KND_SC_NM}\n\n--------------------")
    fond = datetime.strptime(school.FOND_YMD, "%Y%m%d")
    embed.add_field(name="⚒️ 설립일", value=fond.strftime("%Y년 %m월 %d일"
                                                       .encode('unicode-escape').decode())
                    .encode().decode('unicode-escape'))
    embed.add_field(name="🏫 주소 (도로명)", value=school.ORG_RDNMA, inline=False)
    embed.add_field(name="📮 우편번호", value=school.ORG_RDNZC)
    embed.add_field(name="📲 대표 전화", value=school.ORG_TELNO)
    embed.add_field(name="기타", value=f"🔗 [학교 홈페이지 바로가기]({school.HMPG_ADRES})", inline=False)
    embed.set_footer(text=f"{index + 1}/{len(school_list)}")
    return embed
