from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_discount = fields.Float(string="Discount", default=0.0, help="Direct discount on the unit price.")

    @api.depends('product_uom_qty', 'x_discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        for line in self:
            tax_results = self.env['account.tax'].with_company(line.company_id)._compute_taxes([
                line._convert_to_tax_base_line_dict()
            ])

            totals = list(tax_results['totals'].values())[0]
            amount_untaxed = totals['amount_untaxed']
            amount_tax = totals['amount_tax']

            line.update({
                'price_subtotal': amount_untaxed,
                'price_tax': amount_tax,
                'price_total': amount_untaxed + amount_tax,
            })

    def _convert_to_tax_base_line_dict(self):
        self.ensure_one()
        base_line_dict = super(SaleOrderLine, self)._convert_to_tax_base_line_dict()

        discounted_price_unit = self.price_unit - self.x_discount
        base_line_dict['price_unit'] = discounted_price_unit

        return base_line_dict
