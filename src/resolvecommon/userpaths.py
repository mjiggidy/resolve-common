"""
Function(s?) for getting relevant paths
"""

import pathlib, os, sys

def get_user_data_base_path(platform_name:str|None=None) -> pathlib.Path:
	"""Get the base user data location for the given platform"""

	platform_name = platform_name or sys.platform.lower()

	if platform_name == "darwin":
		return pathlib.Path.home() / "Library" / "Application Support"

	elif platform_name.startswith("win"):
		
		env_appdata = os.environ.get("APPDATA")
		return pathlib.Path(env_appdata) if env_appdata else pathlib.Path.home() / "AppData" / "Roaming"

	else:

		# NOTE: Supposedly Linux does not yet support Workflow Integrations.  FUTURE PROOFING?!
		env_appdata = os.environ.get("XDG_CONFIG_HOME")
		return pathlib.Path(env_appdata) if env_appdata else pathlib.Path.home() / ".config"

def workflow_integrations_path(platform_name:str|None=None) -> pathlib.Path:
	"""Get the base Workflow Integrations path for the given platform"""

	platform_name = platform_name or sys.platform.lower()

	if platform_name == "darwin":
		return pathlib.Path("/") / "Library" / "Application Support" / "Blackmagic Design" / "DaVinci Resolve" / "Workflow Integration Plugins"

	elif platform_name.startswith("win"):
		return pathlib.Path(os.environ.get("PROGRAMDATA")) /"Blackmagic Design" / "DaVinci Resolve" / "Support" / "Workflow Integration Plugins"

	else:
		raise OSError(f"{platform_name} is not a supported platform")