# Sale Order Discount Extension for Odoo

## Overview
This module extends the functionality of the Odoo Sales module by introducing a discount feature in the order lines. It enables users to apply percentage or fixed amount discounts directly to individual sale order lines, providing more flexibility in pricing and promotions.

## Features
- **Discount on Order Lines**: Add and manage discounts on individual sale order lines.
- **Discount Types**:
  - Percentage-based discounts.
  - Fixed amount discounts.
- **Automatic Calculations**: The module ensures the order line total reflects the applied discount.
- **Integration**: Works seamlessly with Odoo's existing sales workflows and reports.

## Repository
GitHub: [Sale Order Discount Extension](https://github.com/TH274/Sale-Order-Discount-Extension.git)

## Installation
1. Clone the repository into your Odoo custom addons directory:
   ```bash
   git clone https://github.com/TH274/Sale-Order-Discount-Extension.git
   ```
2. Restart the Odoo server to recognize the new module.
   ```bash
   ./odoo-bin -c /path/to/your/odoo.conf
   ```
3. Log in to your Odoo instance and go to **Apps**.
4. Update the app list by clicking the **Update App List** button.
5. Search for "Sale Order Discount Extension" and install the module.

## Usage
1. Navigate to the **Sales** module.
2. Create or edit a sale order.
3. Add a new order line and specify the discount type (percentage or fixed) and value.
4. Review the calculated totals, which automatically include the applied discounts.

## Compatibility
This module is compatible with Odoo version 14.0 and later. For earlier versions, modifications may be required.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes and push to the branch:
   ```bash
   git commit -m "Add your message here"
   git push origin feature/your-feature
   ```
4. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support
For issues or questions, please open an issue in the [GitHub repository](https://github.com/TH274/Sale-Order-Discount-Extension.git).

## Authors
- [Your Name] - Initial development and documentation.

---
Thank you for using the Sale Order Discount Extension! If you find this module helpful, consider giving it a star on GitHub.

