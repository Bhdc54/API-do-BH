from pydantic import BaseModel

class SensorData(BaseModel):
    uid_usuario: str
    aquario_id: str
    temperatura: float
    ph: float
    nivel_agua: float
