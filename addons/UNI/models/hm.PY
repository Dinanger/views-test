from odoo import models, fields

class University(models.Model):
    _name = "hm.university"
    _description = "University Salary"

    # Contacto de Odoo
    po = fields.Many2one(
        'res.partner',
        string="Person",
        required=True
    )

    # Sueldo
    salary = fields.Integer(string="Salary")
