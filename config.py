from __future__ import annotations

import env


def get_variable(var_name, default='throw error'):
    value_from_env = getattr(env, var_name, default)
    if value_from_env == 'throw error':
        raise Exception('Missing value of {var_name} in environment!')
    return value_from_env


class Config:
    SQLALCHEMY_DATABASE_URL = get_variable('SQLALCHEMY_DATABASE_URL')
    SECRET_KEY = get_variable('SECRET_KEY')
