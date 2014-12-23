# -*- coding: utf-8 -*-
from openerp import models, SUPERUSER_ID, _
from openerp.exceptions import Warning


class res_users(models.Model):

    _inherit = "res.users"

    # def write(self, cr, uid, ids, vals, context=None):
    #     print 'asdasdadsas'
    #     if SUPERUSER_ID in ids and 'password' in vals:
    #         print 'SUPERUSER_ID', SUPERUSER_ID
    #         print 'vals', vals
    #         # raise Warning(_('You can not change admin password as it is protected for right catch all configuration and WS consumption'))
    #     return super(res_users, self).write(cr, uid, ids, vals, context)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
