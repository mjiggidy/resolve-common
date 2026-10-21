"""
Function(s?) for getting relevant paths
"""

import pathlib, os, sys

def get_user_data_base_path() -> pathlib.Path:
	"""Get the base user data location depending on OS and such"""

	platform_name = sys.platform.lower()

	if platform_name == "darwin":
		app_data = pathlib.Path.home() / "Library" / "Application Support"

	elif platform_name.startswith("win"):
		env_appdata = os.environ.get("APPDATA")
		app_data    = pathlib.Path(env_appdata) if env_appdata else pathlib.Path.home() / "AppData" / "Roaming"

	else:

		# NOTE: Supposedly Linux does not yet support Workflow Integrations.  FUTURE PROOFING?!
		env_appdata = os.environ.get("XDG_CONFIG_HOME")
		app_data    = pathlib.Path(env_appdata) if env_appdata else pathlib.Path.home() / ".config"

	return app_data