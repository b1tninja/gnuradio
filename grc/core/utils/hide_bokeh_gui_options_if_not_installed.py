# Copyright 2008-2017 Free Software Foundation, Inc.
# This file is part of GNU Radio
#
# GNU Radio Companion is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# GNU Radio Companion is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA


def hide_bokeh_gui_options_if_not_installed(options_blk):
    try:
        import bokehgui
    except ImportError:
        pass
    else:
        try:
            for param in options_blk.parameters_data:
                if param['id'] == 'generate_options':
                    ind = param['options'].index('bokeh_gui')
                    del param['options'][ind]
                    del param['option_labels'][ind]
        except (AttributeError, ValueError, KeyError) as err:
            pass
