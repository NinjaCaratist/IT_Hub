from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import *

#1
def add_pipe(session: AsyncSession, length: float, weight : float, add_date: Date,  delete_date: Date):
    new_pipe = Pipe(length=length, weight=weight, add_date=add_date, delete_date = delete_date)
    session.add(new_pipe)
    return new_pipe

#2
def delete_pipe(session: AsyncSession, id: int):
    session.execute(str('Delete from pipes where id = ' + id))
  
#3
async def get_by_id(session: AsyncSession, id_f: int, id_l: int) -> list[Pipe]:
    result = await session.execute(str('SELECT * from pipes WHERE id BETWEEN ' + id_f + ' and ' + id_l))
    return result.scalars().all()

async def get_by_length(session: AsyncSession, l_f: float, l_l: float) -> list[Pipe]:
    result = await session.execute(str('SELECT * from pipes WHERE id BETWEEN ' + l_f + ' and ' + l_l))
    return result.scalars().all()

async def get_by_weight(session: AsyncSession, w_f: int, w_l: int) -> list[Pipe]:
    result = await session.execute(str('SELECT * from pipes WHERE id BETWEEN ' + w_f + ' and ' + w_l))
    return result.scalars().all()


#, id_f: int, id_l: int
# 

    