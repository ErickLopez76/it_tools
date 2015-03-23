from openerp import models, fields

class test(models.Model):
    _name = 'it_tools.test'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()


