# models/patient.py

from odoo import models, fields, api, _

from server.odoo.api import depends


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='patient', required=True)
    age = fields.Integer(string='Age', related='patient_id.age')
    gender = fields.Selection(string='Gender', related='patient_id.gender', readonly=False)
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference', help="Reference from patient records.")
    prescription = fields.Html(string='Prescription', placeholder='Enter your prescription here .')
    pharmacy_lines_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines' )
    hide_sales_price = fields.Boolean(string='Hide sales price')

    priority = fields.Selection([
        ("0", "Normal"),
        ("1", "Low"),
        ("2", "High"),
        ("3", "Very high")
    ], string="Priority")

    state = fields.Selection([
        ("draft", "Draft"),
        ("in_consultation", "In Consultation"),
        ("done", "Done"),
        ("cancel", "Cancel")
    ], string="Status", default="draft", required=True)

    doctor_id = fields.Many2one('res.users', string='Doctor')

    # ---- single onchange in one function
    # @api.onchange('age')
    # def onchange_age(self):
    #     self.age = self.patient_id.age

    # two onchange in one function
    @api.onchange('patient_id', 'age')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
        self.age = self.patient_id.age

    def action_test(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Effect Test Successfully',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultant(self):
        for rec in self:
            rec.state = "in_consultation"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def action_draft(self):
        for rec in self:
            rec.state = "draft"


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy lines'

    product_id = fields.Many2one('product.product', string='Product')

    price_unit = fields.Float(related='product_id.lst_price', string='Price')

    qty = fields.Integer(string='Quantity', default=1)

    # ttl_price = fields.Float(string='Total')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')


