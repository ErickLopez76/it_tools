from openerp import models, fields, api

#class capacity(models.Model):
#    _name = 'ait_tools.capacity'

#    name = fields.Char(string='Title', required=True)
#    description = fields.Text()
#    servers = fields.One2many('ait_tools.server','capacity')

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
    useradmin = fields.Char(string="Admin User")
    adminpass = fields.Char(string="Admin Pass")
    capacity = fields.Many2one('ait_tools.capacity', required=False)

    services = fields.Many2many('ait_tools.services')

#    @api.onchange('capacity')
#    def _onchange_course(self):
#        if not self.name:
#            self.name = self.capacity.name

#    @api.onchange('server_service')
#    def _onchange_sever(self):
#        if not self.name:
#            self.name = self.server_service.servers
