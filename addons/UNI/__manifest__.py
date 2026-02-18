{
    "name": "Universidad",
    "version": "1.0.0",
    "description": "Get all information about university",
    "depends": ["base", "website"],
    "installable": True,
   "data": [
    "security/ir.model.access.csv",

    "views/uni_view.xml",
    "views/students_view.xml",   # 👈 FALTA ESTO
    "views/teacher_view.xml",
    "views/subject_view.xml",
    "views/classroom.xml",
    "views/hm",
    "views/menu.xml",
],
}


