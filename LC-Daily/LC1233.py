# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        out = [folders[0]]
        for folder in folders[1:]:
            if folder.startswith(out[-1]+'/'):
                continue
            out.append(folder)
        return out
