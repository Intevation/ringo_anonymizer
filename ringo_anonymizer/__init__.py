import logging
from ringo.lib.extension import register_modul
from ringo.lib.helpers import dynamic_import

log = logging.getLogger(__name__)

def includeme(config):
    """Registers a new modul for ringo.

    :config: Dictionary with configuration of the new modul

    """
    log.info("Registered anonymizer extension")
