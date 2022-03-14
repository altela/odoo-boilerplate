from odoo import models


class OverrideValidate(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        for _ in self:
        # Put Your Code Here
            res = super(OverrideValidate, self).process()
        return res
