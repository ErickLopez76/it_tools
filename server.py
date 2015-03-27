from openerp import models, fields, api

class server(models.Model):
    _name = 'ait_tools.server'

    name = fields.Char(string='Title', required=True)
    description =  fields.Text()
    cores = fields.Integer(string="Numero de cores")
    memory = fields.Integer(string="Memoria")
    os = fields.Char(string="OS")
    hdd = fields.Integer(string="Capacidad Disco")
    ip = fields.Char(string="Direccion IP")
    rootpass = fields.Char(string="Root Password")

    capacity = fields.Many2one('ait_tools.capacity', required=False)

    services = fields.One2many('ait_tools.services', 'server')

    server_services = fields.Many2one('ait_tools.server_services',required=False)

#    @api.onchange('capacity')
#    def _onchange_course(self):
#        if not self.name:
#            self.name = self.capacity.name

#    @api.onchange('server_service')
#    def _onchange_sever(self):
#        if not self.name:
#            self.name = self.server_service.servers
