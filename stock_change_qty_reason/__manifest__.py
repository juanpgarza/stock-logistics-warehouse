# Copyright 2016-2017 ACSONE SA/NV (<http://acsone.eu>)
# Copyright 2019-2023 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Change Quantity Reason",
    "summary": """
        Stock Quantity Change Reason """,
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/stock-logistics-warehouse",
    "category": "Warehouse Management",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["stock"],
    "data": [
        "security/ir.model.access.csv",
        "security/stock_security.xml",
        "views/base_config_view.xml",
        "views/stock_move_line_view.xml",
        "views/stock_quant_reason_view.xml",
        "views/stock_quant_view.xml",
    ],
    "installable": True,
}
