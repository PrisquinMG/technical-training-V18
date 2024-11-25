from odoo import models, fields, api

from datetime import timedelta, datetime

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property"
    _inherit = ["mail.thread"]  # Héritage de mail.thread pour activer les threads

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Post code")
    date_availability = fields.Date("Date availability", default=lambda self: self._default_date_availability())
    expected_price = fields.Float("Expected price", required=True)
    selling_price = fields.Float("Selling price", readonly=True)
    best_price = fields.Float("Best price", readonly=True, compute="_compute_best_price", store=True)
    offer_ids = fields.One2many("estate.property.offer", 'property_id', string="Offers")
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Boolean("Garden area")
    garden_orientation = fields.Selection(selection=[
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], default="new", required=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property type")
    buyer = fields.Many2one("res.partner", string="Buyer")
    sales_person = fields.Many2one("res.users", string="Sales person")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    tag_ids = fields.Many2many("estate.property.tag", string="Estate Property Tag")
    total_area = fields.Float(string="Total area", compute="_compute_total_area")


    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = 10 * record.expected_price


    def _default_date_availability(self):
        return datetime.now().date() + timedelta(days=90)

    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'), default=0)