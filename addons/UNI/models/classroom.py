from odoo import models, fields, api
from odoo.exceptions import ValidationError


class classroom(models.Model):
    _name = "classroom.university"
    _description = "Classroom" 

    num_id = fields.Integer(string="numid", required=True)
    
    teacher = fields.Many2one(
        "teacher.university",
        required=True

    )
    @api.constrains('num_id')
    def cheacker(self):
       for cheacker in self:
          if not(4 <= cheacker.value <=28):
            raise ValidationError("from 1 to 28")



   

