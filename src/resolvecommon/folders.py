from __future__ import annotations
import typing, logging

if typing.TYPE_CHECKING:
	import DaVinciResolveScript as dvrtypes

PATH_SEP = "/"
"""Path separator for media pool folder paths"""

def get_path_from_folder(target_folder:dvrtypes.Folder, relative_to:dvrtypes.Folder) -> str:
	"""Resolve a folder path from a given handle"""

	parts = []

	while target_folder:

		if target_folder.GetUniqueId() == relative_to.GetUniqueId():
			break
		
		parts.append(target_folder)
		target_folder = target_folder.GetParentFolder()

	return PATH_SEP.join(f.GetName() for f in reversed(parts))

def get_folder_from_path(path:str, root_folder:dvrtypes.Folder) -> dvrtypes.Folder:
	"""Get a Media Pool Folder object from a given pathlike string"""
	
	if not path:
		return root_folder
	
	current_folder = root_folder
	
	for search_folder_name in path.strip(PATH_SEP).split(PATH_SEP):
		
		logging.getLogger(__name__).debug("In \"%s\" looking for \"%s\"", current_folder.GetName(), search_folder_name)
		
		try:
			current_folder = next(f for f in current_folder.GetSubFolderList() if f.GetName() == search_folder_name)
		
		except StopIteration as e:
		
			logging.getLogger(__name__).debug("Did not find \"%s\" in \"%s\"", search_folder_name, current_folder.GetName())
			raise FileNotFoundError(f"{search_folder_name} not in {current_folder.GetName()}") from e
		
		logging.getLogger(__name__).debug("Found \"%s\" in \"%s\"", search_folder_name, current_folder.GetName())
	
	return current_folder

def get_clips_from_folder(
	folder        :dvrtypes.Folder,
	recursive     :bool=False,
	ignore_folder :dvrtypes.Folder|None=None
) -> typing.Iterator[dvrtypes.MediaPoolItem]:
	"""Yield clips from a given folder handle"""
	
	if ignore_folder and folder.GetUniqueId() == ignore_folder.GetUniqueId():
		
		logging.getLogger(__name__).debug("Hit an ignored folder: %s", folder.GetName())
		return
	
	yield from iter(folder.GetClipList())

	if recursive:
		for subfolder in folder.GetSubFolderList():
			yield from get_clips_from_folder(subfolder, recursive, ignore_folder=ignore_folder)