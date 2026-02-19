from odoo import models, api, fields
from odoo.exceptions import ValidationError


class university(models.Model):
    _name = "university"
    _description = "admin a uni" 

    name = fields.Char(string="name", required=True)
    description = fields.Text(string="logo/description")
    teacher= fields.One2many(
        "teacher.university",
        "university",
        string = "list of teacher"
    )
    students = fields.One2many(
        "students.university",
        "university",
        string="studentss"
    )

 