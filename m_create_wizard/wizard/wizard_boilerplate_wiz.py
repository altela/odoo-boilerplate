from odoo import api, models, fields


class ChangeEffectiveWiz(models.TransientModel):
    _name = "wizard.boilerplate.wiz"

    @api.multi
    def do_something(self):
        for record in self.env['stock.picking'].browse(self._context.get('active_ids', [])):
            pulled_picking_name = record.name

            # When user clicking save, Code below will be executed
            # Put your code here
