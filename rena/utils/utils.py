from typing import Any, Optional

from classes import Database


def private_bool(value: Any) -> str:
    if value:
        return "❌ 비공개"
    else:
        return "⭕ 공개"


async def is_registered(user_id: int, db: Database) -> bool:
    data = await db.select("User", user_id)
    return bool(data)


async def ephemeral_check(
        user_id: Optional[int] = None, data: Optional[tuple[int, str]] = None, db: Optional[Database] = None
) -> bool:
    if (user_id and db) or data:
        data_returned = data or await db.select("User", user_id)
        return bool(data_returned[5])
    else:
        raise ValueError("user_id or data is required")
