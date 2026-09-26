import pytest
from backend.main import get_db
from sqlalchemy import text


@pytest.mark.asyncio
async def test_get_db_yields_working_session():
    gen = get_db()
    session = await gen.__anext__()

    # session should be usable
    result = await session.execute(text("SELECT 1"))
    assert result.scalar() == 1

    # closing the generator should trigger cleanup (session close)
    with pytest.raises(StopAsyncIteration):
        await gen.__anext__()