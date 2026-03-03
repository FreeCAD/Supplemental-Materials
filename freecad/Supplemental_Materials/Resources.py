# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileNotice: Part of the Supplemental Materials addons.

import freecad.Supplemental_Materials as module
from importlib.resources import as_file , files

resources = files(module) / 'Resources'

materials = resources / 'Materials'
models = resources / 'Models'
icons = resources / 'Icons'


def asIcon ( name : str ):

    file = name + '.svg'

    icon = icons / file

    with as_file(icon) as path:
        return str( path )
