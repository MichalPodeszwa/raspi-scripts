from handlers.common import start_server

from . import initialize, reset_matrix, Drawer
initialize()
reset_matrix()

drawer = Drawer()
drawer.run_demo()
start_server(drawer.handle_message)
