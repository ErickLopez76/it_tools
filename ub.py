from openerp import models, fields, api

class ubicacion(models.Model):
    _name = 'it_tools.ubicacion'

    name = fields.Char(string='NombreCorto', required=True)
    description = fields.Text()

#    direccion   = fields.Char(string="Dirección")
#    num_phone   = fields.Char(string="Teléfono")
#    short_phone = fields.Char(string="Marcación Corta")
#    ext_it      = fields.Char(string="Extensión IT")
#    ips_data    = fields.Char(string="IP's Data")
#    ips_phone   = fields.Char(string="IP's Telefonía")
#    net_data    = fields.Text(string="Datos de red")

#    servers     = fields.Many2many('it_tools.server')

#    @api.onchange('capacity')
#    def _onchange_course(self):
#        if not self.name:
#            self.name = self.capacity.name

#    @api.onchange('server_service')
#    def _onchange_sever(self):
#        if not self.name:
#            self.name = self.server_service.servers
