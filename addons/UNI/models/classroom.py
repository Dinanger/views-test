from odoo import models, fields, api


class classroom(models.Model):
    _name = "classroom.university"
    _description = "Classroom" 

    numid = fields.Integer(string="numid", required=True)
    
    teacher = fields.Many2one(
        "teacher.university",
        required=True
    )

   

