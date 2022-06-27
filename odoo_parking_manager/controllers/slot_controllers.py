import json
from odoo.exceptions import AccessError
from odoo.http import request, route, Controller


class SlotControllers(Controller):
    @route("/parking/slot", methods=["GET"], type="http", auth="user")
    def get_available_slots(self, section=False):

        domain = [("state", "=", "1")]
        if section:
            domain.append(("section_id", "=", section))
        slots = request.env["parking.slot"].search(domain, limit=10)

        return json.dumps(slots.read(["name", "section_id"]))

    @route(
        "/parking/slot/<int:slot_id>",
        methods=["POST"],
        type="http",
        auth="user",
        csrf=False,
    )
    def assign_slot(self, slot_id):

        user = request.env.ref("odoo_parking_manager.parking_api_user")
        if user.id != request.env.user.id:
            raise AccessError("Only API User can perform this action")

        slot = request.env["parking.slot"].browse(slot_id)
        slot.state = "2"

        return json.dumps({"message": "Slot % asigned" % slot.name})
