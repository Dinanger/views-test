from odoo import models, fields

class University(models.Model):
    _name = "hm.university"
    _description = "HM University"

    po = fields.Many2one('res.partner', string="Person", required=True)
    salary = fields.Integer(string="Salary")
