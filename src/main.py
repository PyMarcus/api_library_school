import uvicorn
from typing import Any, TypeVar, Optional
from fastapi import FastAPI, Path, HTTPException, Query, Header
from starlette import status
from starlette.status import HTTP_409_CONFLICT
from models.student import Student
from controllers.getters import Getters
from posters import Posters

app = FastAPI()
length_data = len(Getters().getStudents())
T = TypeVar("T")


# *** GET METHODS STUDENTS ***
@app.get('/')
async def root() -> T:
    return {"status": "OK"}


@app.get('/students')
async def students() -> dict:
    """
    Method returns all students
    :return:
    """
    return Getters().getStudents()


@app.get('/students/{id_student}')
async def students(id_student: int or str = Path(default=None, title="Identificador do estudante", description=f"Deve estar entre 0 e {length_data}", gt=0,lt=length_data)):
    """
    Returns data for id selected
    :param id_student:
    :return:
    """
    try:
        return Getters().getStudentsForId(id_student)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")


@app.get('/students/name/{name}')
async def students(name: str = Path(default=None, title="nome do estudante")):
    """
    Select students for name
    :param name:
    :return:
    """
    try:
        return Getters().getStudentsForName(name)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não há aluno com este nome")


@app.get('/students/email/{email}')
async def students(email: str = Path(default=None, title="email do estudante")):
    """
    Select students for email
    :param email:
    :return:
    """
    try:
        return Getters().getStudentsForEmail(email)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não há aluno com este email")


@app.get('/students/date/{date}')
async def students(date: str = Path(default=None, title="data de nascimento do estudante")):
    """
    Select students by born date
    :param email:
    :return:
    """
    try:
        print(date)
        return Getters().getStudentsByDate(date)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não há aluno nascido neste dia")


# *** GET METHODS BOOKS ***
@app.get("/books")
async def books() -> dict:
    """
    Returns all books
    :return:
    """
    return Getters().getBooks()


@app.get("/books/{book_id}")
async def books(book_id: str or int =Path(default=None, title="Identificador do Livro")) -> T:
    """
    Returns all books by id
    :return:
    """
    try:
        return Getters().getBooksId(book_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Livro não encontrado")


@app.get("/books/query/")
async def books(book_id: int =
                Query(default=None, description="Informe o id", gt=0),
                status: str = Query(default=None, description="Informe o status do livro"),
                other: Optional[T] = None) -> T:
    """
    Returns all books by id
    :return:
    """
    try:
        return Getters().getBooksQueryParameters(book_id, status)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Livro não encontrado")


# *** POST METHODS ***
@app.post('/students')
async def postStudents(data: Student, status_code=status.HTTP_201_CREATED) -> Any:
    """
    Post info in database
    :param data:
    :param status_code:
    :return:
    """

    try:
        if data is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        Posters().posterStudent(dict(data))
        return dict(data)
    except Exception as e:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail=f"Inserção inválida")


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, debug=True, reload=True)
