#!/usr/bin/env python

conexion = {
    'host': '****',
    'user': '****',
    'passwd': '***',
    'db': '****'
}

databaseConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(conexion['user'], conexion['passwd'], conexion['host'], conexion['db'])

