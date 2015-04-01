from openerp import models, fields

class service2(models.Model):
    _name = 'ait_tools.services2'
    name  = fields.Char(string='Title', required=True)
    description= fields.Text()
