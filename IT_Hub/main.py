import asyncio
import typer
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from exeptions import DuplicatedEntryError
from base import init_models
from base import get_session
import service
     

app = FastAPI()
cli = typer.Typer()


class PipeSchema(BaseModel):
    length : float
    weight : float
    add_date : date
    delete_date : date


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")


@app.get("/pipes/getbyid", response_model=list[PipeSchema])
async def get_pipes_by_id(session: AsyncSession = Depends(get_session)):
    pipes = await service.get_by_id(session)
    return [PipeSchema(length=p.length, weight=p.weight, add_date=p.add_date, delete_date=p.delete_date) for p in pipes]

async def get_pipes_by_length(session: AsyncSession = Depends(get_session)):
    pipes = await service.get_by_length(session)
    return [PipeSchema(length=p.length, weight=p.weight, add_date=p.add_date, delete_date=p.delete_date) for p in pipes]

async def get_pipes_by_weight(session: AsyncSession = Depends(get_session)):
    pipes = await service.get_by_weight(session)
    return [PipeSchema(length=p.length, weight=p.weight, add_date=p.add_date, delete_date=p.delete_date) for p in pipes]


@app.post("/pipes/")
async def add_pipe(pipe: PipeSchema, session: AsyncSession = Depends(get_session)):
    pipe = service.add_pipe(session, pipe.length, pipe.weight, pipe.add_date, pipe.delete_date)
    try:
        await session.commit()
        return pipe
    except IntegrityError as ex:
        await session.rollback()
        raise DuplicatedEntryError("The pipe is already stored")

if __name__ == "__main__":
    cli()
    app()
    