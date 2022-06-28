import logging
from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def migrate(cr, version):

    env = api.Environment(cr, SUPERUSER_ID, {})
    _logger.info("Starting upper_name data migration")
    query = """
    UPDATE parking_slot
    SET upper_name = UPPER(name);
    """
    env.cr.execute(query)
    _logger.info("Finish upper_name data migration")
