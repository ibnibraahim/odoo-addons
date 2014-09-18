# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class res_company(osv.osv):
    _inherit = 'res.company'

    _columns = {
        'sale_order_dummy_confirm' : fields.boolean('Sale Orders Dummy Confirmation'),
        }