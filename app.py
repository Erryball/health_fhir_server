from flask import Flask, g
from flask_login import current_user
from common import tryton, login_manager, Api, recordConverter

def before_request():
    """Allows access to user object
        for every request
    """
    g.user = current_user

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('config.DebugConfig')
    if config is not None:
        app.config.from_object(config)
    app.config.from_envvar('FHIR_SERVER_CONFIG', silent=True)

    with app.app_context():
        import logging
        logging.basicConfig(filename='flask.log', level=logging.INFO,
                format='%(asctime)s:::%(levelname)s:::%(name)s: %(message)s')

        # Initialize tryton
        tryton.init_app(app)

        # Login
        login_manager.init_app(app)
        login_manager.login_view='auth_endpoint.login'
        login_manager.session_protection='strong'

        # Initiate the REST API
        api=Api(app)

        # The user model
        user = tryton.pool.get('res.user')

        # Setup tryton config
        @tryton.default_context
        def default_context():
            return user.get_preferences(context_only=True)

        # Add Model-ID-Field url converter
        app.url_map.converters['item']=recordConverter

        # Store current user in g.user
        app.before_request(before_request)

        #### ADD THE ROUTES ####
        from resources.system import Conformance
        api.add_resource(Conformance, '/', '/metadata')

        def add_fhir_routes(resource):
            """Adds complex FHIR routes"""

            for _, route in resource.routing_table.items():
                api.add_resource(route['handler'], *route['uri'])

        from resources.patient import routing as pat
        add_fhir_routes(pat)

        from resources.diagnostic_report import routing as dr
        add_fhir_routes(dr)

        from resources.observation import routing as obs
        add_fhir_routes(obs)

        from resources.practitioner import routing as hp
        add_fhir_routes(hp)

        from resources.procedure import routing as op
        add_fhir_routes(op)

        from resources.condition import routing as condition
        add_fhir_routes(condition)

        from resources.family_history import routing as fh
        add_fhir_routes(fh)

        from resources.medication import routing as med
        add_fhir_routes(med)

        from resources.medication_statement import routing as ms
        add_fhir_routes(ms)

        from resources.immunization import routing as imm
        add_fhir_routes(imm)

        from resources.organization import routing as org
        add_fhir_routes(org)

        # Handle the authentication blueprint
        #   TODO: Use OAuth or something robust
        from resources.auth import auth_endpoint
        app.register_blueprint(auth_endpoint, url_prefix='/auth')

    return app
