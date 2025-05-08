import pass_to_server

dbconfig_local = {
    'host': pass_to_server.host_l,
    'user': pass_to_server.user_l,
    'password': pass_to_server.password_l,
    'database': pass_to_server.database_l,
    'port': pass_to_server.port_l
}

dbconfig_server = {
    'host': pass_to_server.host_s,
    'user': pass_to_server.user_s,
    'password': pass_to_server.password_s,
    'database': pass_to_server.database_s,
    'port': pass_to_server.port_s
}

def get_dbconfig(use_local=True):
    return dbconfig_local if use_local else dbconfig_server
