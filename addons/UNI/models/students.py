from odoo import models, fields, api
from odoo.exceptions import ValidationError



class studens(models.Model):
    _name = "students.university"
    _description = "students" 

    name = fields.Char(string="name", required=True)
    age = fields.Integer(string="age", required=True)
    courses = fields.Many2many(
        "classroom.university",
        string="course")
    grade = fields.Selection([
        ("1RO", "1RO"),
        ("2nd",  "2nd"),
        ("3RO",  "3RO"),
    ],string="course", required=True, default='1RO')

    teacher = fields.Many2many(
        "teacher.university",
        string="teacher"
            )
    subject = fields.Many2many(
        "subject.university",
        string="subject"
    )
    university = fields.Many2one(
        "university",
        string="uni"
    )


  