from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(
        selection_add=[('doctor', 'Doctor Address')],
        ondelete={'doctor': 'set default'}
    )