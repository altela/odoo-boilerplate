picking_id = self.id
self.env.cr.execute("SELECT name FROM stock_picking WHERE sale_id = %s", [picking_id])