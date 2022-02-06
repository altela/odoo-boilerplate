from odoo import api, models


class WizardBoilerplateModel(models.Model):
    _inherit = "stock.picking"

    def wiz_open(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.boilerplate.wiz',
            'view_mode': 'form',
            'target': 'new',
            }
