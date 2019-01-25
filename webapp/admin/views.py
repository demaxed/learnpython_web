#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
# from flask_login import current_user, login_required
from webapp.user.decorators import admin_required


blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@admin_required
def admin_index():
        return 'Привет админ'
