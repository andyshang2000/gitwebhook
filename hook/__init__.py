from flask import Blueprint

hook = Blueprint('hook', __name__)

from . import views