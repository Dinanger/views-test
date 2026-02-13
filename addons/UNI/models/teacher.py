from odoo import models, fields, api
from odoo.exceptions import ValidationError


class teacher(models.Model):
    _name = "teacher.university"
    _description = "teacher inf" 

    name = fields.Char(string="name", required=True)
    subjects = fields.Many2many(
        "subject.university",
        string="subjects")

    students = fields.Many2many(
        "students.university",
        string="studens"
    )
    classroom = fields.One2many(
        "classroom.university",
        "teacher",
        string="classroom"
    )
    university = fields.Many2one(
        "university",
        string="uni"
    )


