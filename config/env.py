#!/usr/bin/env python

conexion = {
    'host': '127.0.0.1',
    'user': 'postgres',
    'passwd': '26059573',
    'db': 'clinica'
}

databaseConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(conexion['user'], conexion['passwd'], conexion['host'], conexion['db'])

