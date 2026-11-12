import DaVinciResolveScript as bmd
from resolvecommon import folders

resolve = bmd.scriptapp("resolve")
mp = resolve.GetProjectManager().GetCurrentProject().GetMediaPool()
current_folder = mp.GetCurrentFolder()

print("Folder name:\t", current_folder.GetName())

relative_folder_path = "x100 Working Bins/MJ Working/Continuity/"
relative_folder_handle = folders.get_folder_from_path(relative_folder_path, mp.GetRootFolder())

folder_path = folders.get_path_from_folder(current_folder, relative_to=relative_folder_handle)

print("At path:\t", folder_path)

resolved_folder = folders.get_folder_from_path(folder_path, root_folder=relative_folder_handle)

print("Resolved:\t", resolved_folder.GetName())

print("Resolve path:\t", folders.get_path_from_folder(resolved_folder, relative_to=mp.GetRootFolder()))