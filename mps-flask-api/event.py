from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

EVENT = {
    "1": {
        "event_id": "1",
        "event_data_hora": "03-17-2023",
        "event_descricao": "Passear no shopping e comprar o presente da mamãe na sapatinho de luxo ou renner na sexta.",
        "event_nome": "Ir ao shopping",
        "event_status": 0,
        "timestamp": get_timestamp(),
    },
    "2": {
        "event_id": "2",
        "event_data_hora": "03-31-2023",
        "event_descricao": "Fim do período, graças a Deus!!! Finalmente os dias de glória estão chegando.",
        "event_nome": "O dia mais feliz da minha vida",
        "event_status": 0,
        "timestamp": get_timestamp(),
    },
}

def read_all():
    return list(EVENT.values())


def create(event):
    event_id = event.get("user_id")
    event_data_hora = event.get("event_data_hora")
    event_descricao = event.get("event_descricao", "")
    event_nome = event.get("event_nome", "")
    event_status = event.get("event_status")

    if event_id and event_id not in EVENT:
        EVENT[event_id] = {
            "event_id": event_id,
            "event_data_hora": event_data_hora,
            "event_descricao": event_descricao,
            "event_nome": event_nome,
            "event_status": event_status,
            "timestamp": get_timestamp(),
        }
        return EVENT[event_id], 201
    else:
        abort(
            406,
            f"Event {event_id} already exists",
        )


def read_one(event_id):
    if event_id in EVENT:
        return EVENT[event_id]
    else:
        abort(
            404, f"Event with ID {event_id} not found"
        )


def update(event_id, event):
    if event_id in EVENT:
        EVENT[event_id]["event_nome"] = event.get("user_name", EVENT[event_id]["user_name"])
        EVENT[event_id]["timestamp"] = get_timestamp()
        return EVENT[event_id]
    else:
        abort(
            404,
            f"Event with ID {event_id} not found"
        )


def delete(event_id):
    if event_id in EVENT:
        del EVENT[event_id]
        return make_response(
            f"{event_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Event with ID {event_id} not found"
        )