from odoo import models, fields, api


class subject(models.Model):
    _name = "subject.university"
    _description = "subject"

    name = fields.Char(string="name", required=True)
    value = fields.Integer(string="credit? from 1 to 4 scale", required=True)