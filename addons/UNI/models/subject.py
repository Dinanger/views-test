from odoo import models, fields, api
from odoo.exceptions import ValidationError



class subject(models.Model):
    _name = "subject.university"
    _description = "subject"

    name = fields.Char(string="name", required=True)
    value = fields.Integer(string="credit", required=True)  


    

    @api.constrains('value')
    def cheacker(self):
     for cheacker in self:
        if not(1 <= cheacker.value <=4):
            raise ValidationError("from 1 to 4")

