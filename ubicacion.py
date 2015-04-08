from openerp import models, fields, api

class ubicacion(models.Model):
    _name = 'it_tools.ubicacion'

    name        = fields.Char(string='Nombre Corto', required=True)
    nombre      = fields.Char(string='Nombre')
    direccion   = fields.Char(string='Direccion')
    phone       = fields.Char()
    short_phone = fields.Char()
    ext_it      = fields.Char()
    net_data    = fields.Char()
    net_phone   = fields.Char()
    net_info    = fields.Text(string='Datos de red')

    servers     = fields.Many2many('it_tools.server')

