from bgpb import app
import optparse

# def flaskrun(app, default_host="127.0.0.1",
#                   default_port="5000"):
#     """
#     Takes a flask.Flask instance and runs it. Parses
#     command-line flags to configure the app.
#     """
#
#     # Set up the command-line options
#     parser = optparse.OptionParser()
#     parser.add_option("-H", "--host",
#                       help="Hostname of the Flask app " + \
#                            "[default %s]" % default_host,
#                       default=default_host)
#     parser.add_option("-P", "--port",
#                       help="Port for the Flask app " + \
#                            "[default %s]" % default_port,
#                       default=default_port)
#
#     # Two options useful for debugging purposes, but
#     # a bit dangerous so not exposed in the help message.
#     parser.add_option("-d", "--debug",
#                       action="store_true", dest="debug",
#                       help=optparse.SUPPRESS_HELP)
#
#     options, _ = parser.parse_args()
#
#     app.run(
#         debug=options.debug,
#         host=options.host,
#         port=int(options.port)
#     )

if __name__ == '__main__':

    # flaskrun(app)
    app.run(debug=False)
