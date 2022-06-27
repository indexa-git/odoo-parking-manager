from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class ParkingSlotTest(TransactionCase):
    def test_001_slot_historical(self):
        """
        Checks everytime a slot state is changed,
        an historical record is created too
        """

        # first we create a new slot
        section_id = self.env["parking.section"].create({"name": "Section X"})
        slot_id = self.env["parking.slot"].create(
            {"name": "Slot 1A", "section_id": section_id.id}
        )
        slot_id.state = "2"

        # check an historical record is created
        historical_id = self.env["parking.slot.historical"].search([])
        self.assertEqual(len(historical_id), 1)

        self.assertRecordValues(
            historical_id,
            [
                {
                    "slot_id": slot_id.id,
                    "section_id": section_id.id,
                    "historical_type": "2"
                }
            ],
        )

        with self.assertRaises(UserError):
            historical_id.unlink()
