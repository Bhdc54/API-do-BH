from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.sensor_model import SensorData
from app.firestore_config import db

router = APIRouter()

@router.post("/enviar-dados/")
async def enviar_dados(data: SensorData):
    try:
        doc_ref = db.collection("usuarios").document(data.uid_usuario)\
                   .collection("aquarios").document(data.aquario_id)\
                   .collection("leituras").document()

        doc_ref.set({
            "temperatura": data.temperatura,
            "ph": data.ph,
            "nivel_agua": data.nivel_agua,
            "timestamp": datetime.utcnow()
        })

        return {"mensagem": "Dados recebidos e armazenados com sucesso!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
