from openerp import models, fields, api

class capacity(models.Model):
    _name = 'it_tools.capacity'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    servers = fields.One2many('it_tools.server', 'capacity')
