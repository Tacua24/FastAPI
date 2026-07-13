from sqlalchemy import Column, Integer, String, Boolena, Date, Foreignkey
from datetime import date
from app.database import Base


class LibroMode1(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    disponible = Column(Boolena, default=True)


class EstudianteMode1(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    carrera = Column(String, nullable=False)


class PrestamoMode1(Base):
    __tablename__ = "prestamo"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    libro_id = Column(Integer, Foreignkey("libros.id"), nullable=False)
    estudiante_id = Column(Integer, Foreignkey("estudiantes.id"), nullable=False)
    fecha_prestamo = Column(Date, default=date.today)
    devuelto = Column(Boolena, default=True)
