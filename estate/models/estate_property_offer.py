from odoo import models, fields, api
from datetime import timedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float(string="Price", required=True)
    status = fields.Selection(string="Status", selection=[
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], copy=False)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    property_type_id = fields.Many2one(related='property_id.property_type_id',  string="Property type", store=True)
    date_deadline = fields.Date(string="Date deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline", store=True)
    validity = fields.Integer(string="Validity", default=7, store=True)
    
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date.date() + timedelta(days=record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                delta = (record.date_deadline - record.create_date.date()).days
                record.validity = delta

            elif record.date_deadline:
                delta = (record.date_deadline - fields.Date.today()).days
                record.validity = delta