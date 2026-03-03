# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 David Carter <dcarter@davidcarter.ca>
# SPDX-FileNotice: Part of the Supplemental Materials addons.

from .Resources import materials , models , asIcon
from FreeCAD import ParamGet


Parameter = 'User parameter:BaseApp/Preferences/Mod/Material/Resources/Modules/Supplemental-Materials'


config = ParamGet(Parameter)
config.SetString('ModuleModelDir',str(models))
config.SetString('ModuleDir',str(materials))
config.SetString('ModuleIcon',asIcon('Addon'))
