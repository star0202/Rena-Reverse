from typing import Any, Optional

from classes import Database


def private_bool(value: Any) -> str:
    if value:
        return "❌ 비공개"
    else:
        return "⭕ 공개"


async def ephemeral_check(
        user_id: Optional[int] = None, data: Optional[tuple[int, str]] = None, db: Optional[Database] = None
) -> bool:
    if user_id and db:
        data_returned = await db.select("user", user_id)
        return bool(data_returned[6])
    elif data:
        return bool(data[6])
    else:
        raise ValueError("user_id or data is required")
