from odoo import models, api, fields


class ResConfigSettingsInventoryNotification(models.TransientModel):
    _inherit = "res.config.settings"

    custom_emails = fields.Char('Custom Emails', config_parameter='my_module.custom_emails')