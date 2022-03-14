# This is the example of defining object from self and using cr (cursor) from psycopg connection to do queries

picking_id = self.id
self.env.cr.execute("SELECT name FROM stock_picking WHERE sale_id = %s", [picking_id])