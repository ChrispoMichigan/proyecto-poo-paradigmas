from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_items():
    return {"items": [
        {"id": 1, "name": "Producto 1", "price": 100},
        {"id": 2, "name": "Producto 2", "price": 200}
    ]}

@router.get("/{item_id}")
async def get_item(item_id: int):
    return {"id": item_id, "name": f"Producto {item_id}", "price": item_id * 50}

@router.post("/")
async def create_item(item: dict):
    return {"message": "Item creado", "item": item}

@router.put("/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"message": f"Item {item_id} actualizado", "item": item}

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} eliminado"}