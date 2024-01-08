from ..app import login_manager
from .Spectateur import Spectateur

@login_manager.user_loader
def load_user(id) -> Spectateur:
    return Spectateur.query.get(id)