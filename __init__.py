# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SIGC
                                 A QGIS plugin
 Sistema Integral de Gestión Catastral
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-12-15
        copyright            : (C) SyK Catastro Sistemas
        email                : sykcatastro.sistemas@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SIGC class from file SIGC.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sgc import SGC
    return SGC(iface)
