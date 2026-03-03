# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 David Carter <dcarter@davidcarter.ca>
# SPDX-FileNotice: Part of the Supplemental Materials addons.

################################################################################
#                                                                              #
#   This addon is free software; you can redistribute it and/or modify it      #
#   under the terms of the GNU Lesser General Public License as published      #
#   by the Free Software Foundation; either version 3.0 of the License, or     #
#   (at your option) any later version.                                        #
#                                                                              #
#   This addon is distributed in the hope that it will be useful,              #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                       #
#                                                                              #
#   See the GNU Lesser General Public License for more details.                #
#                                                                              #
#   You should have received a copy of the GNU Lesser General Public License   #
#   along with this addon; if not, write to the Free Software Foundation,      #
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA           #
#                                                                              #
################################################################################

from .Resources import materials , models , asIcon
from FreeCAD import ParamGet


Parameter = 'User parameter:BaseApp/Preferences/Mod/Material/Resources/Modules/Supplemental-Materials'


config = ParamGet(Parameter)
config.SetString('ModuleModelDir',str(models))
config.SetString('ModuleDir',str(materials))
config.SetString('ModuleIcon',asIcon('Addon'))
