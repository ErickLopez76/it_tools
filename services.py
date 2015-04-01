from openerp import models, fields

class services(models.Model):
    _name = 'ait_tools.services'
    name  = fields.Char(string='Servicio', required=True)
    description= fields.Text()
