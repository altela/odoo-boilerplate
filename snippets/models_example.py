from odoo import api, fields, models


class ModelsExample(models.Model):

    # If you inherit a model from other module, use _inherit instead of _name
    _inherit = "product.template"

    # If you intend to create a new module, use _name
    _name = "new.module"

    # Object examples
    boolean_example = fields.Boolean(string="Boolean Checkbox", store=True, help="Checkbox Example", ttype="boolean")
    textfield_example = fields.Text(string="Text field example", store=True, help="Text field example for storing text", ttype="text")
