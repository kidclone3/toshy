# This file has been autogenerated by the pywayland scanner

# Copyright © 2018 Ilia Bozhinov
# Copyright © 2020 Isaac Freund
# Copyright © 2022 wb9688
# Copyright © 2023 i509VCB
#
# Permission to use, copy, modify, distribute, and sell this
# software and its documentation for any purpose is hereby granted
# without fee, provided that the above copyright notice appear in
# all copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of
# the copyright holders not be used in advertising or publicity
# pertaining to distribution of the software without specific,
# written prior permission.  The copyright holders make no
# representations about the suitability of this software for any
# purpose.  It is provided "as is" without express or implied
# warranty.
#
# THE COPYRIGHT HOLDERS DISCLAIM ALL WARRANTIES WITH REGARD TO THIS
# SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS, IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY
# SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
# AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION,
# ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
# THIS SOFTWARE.

from __future__ import annotations

import enum

from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)

from ..ext_foreign_toplevel_list_v1 import ExtForeignToplevelHandleV1
from .ext_foreign_toplevel_handle_state_v1 import ExtForeignToplevelHandleStateV1


class ExtForeignToplevelStateV1(Interface):
    """Describe toplevel state

    The global object used to initialize the extension interfaces to get
    updates to the state of a toplevel.
    """

    name = "ext_foreign_toplevel_state_v1"
    version = 1

    class error(enum.IntEnum):
        already_constructed = 0


class ExtForeignToplevelStateV1Proxy(Proxy[ExtForeignToplevelStateV1]):
    interface = ExtForeignToplevelStateV1

    @ExtForeignToplevelStateV1.request()
    def destroy(self) -> None:
        """Destroy the :class:`ExtForeignToplevelStateV1` object

        Destroys the :class:`ExtForeignToplevelStateV1` object.

        This does not affect any existing
        :class:`~pywayland.protocol.ext_foreign_toplevel_state_v1.ExtForeignToplevelHandleStateV1`
        objects.
        """
        self._marshal(0)
        self._destroy()

    @ExtForeignToplevelStateV1.request(
        Argument(ArgumentType.Object, interface=ExtForeignToplevelHandleV1),
        Argument(ArgumentType.NewId, interface=ExtForeignToplevelHandleStateV1),
    )
    def get_handle_state(self, handle: ExtForeignToplevelHandleV1) -> Proxy[ExtForeignToplevelHandleStateV1]:
        """Create the object for toplevel state updates

        This request creates an extension object to receive state updates for
        the foreign toplevel.

        It is illegal to destroy the
        :class:`~pywayland.protocol.ext_foreign_toplevel_list_v1.ExtForeignToplevelHandleV1`
        before the
        :class:`~pywayland.protocol.ext_foreign_toplevel_state_v1.ExtForeignToplevelHandleStateV1`
        object is destroyed and must result in a orphaned error.

        It is also illegal to create more than one
        :class:`~pywayland.protocol.ext_foreign_toplevel_state_v1.ExtForeignToplevelHandleStateV1`
        object per toplevel handle instance and must result in a
        already_constructed error.

        :param handle:
        :type handle:
            :class:`~pywayland.protocol.ext_foreign_toplevel_list_v1.ExtForeignToplevelHandleV1`
        :returns:
            :class:`~pywayland.protocol.ext_foreign_toplevel_state_v1.ExtForeignToplevelHandleStateV1`
        """
        id = self._marshal_constructor(1, ExtForeignToplevelHandleStateV1, handle)
        return id


class ExtForeignToplevelStateV1Resource(Resource):
    interface = ExtForeignToplevelStateV1


class ExtForeignToplevelStateV1Global(Global):
    interface = ExtForeignToplevelStateV1


ExtForeignToplevelStateV1._gen_c()
ExtForeignToplevelStateV1.proxy_class = ExtForeignToplevelStateV1Proxy
ExtForeignToplevelStateV1.resource_class = ExtForeignToplevelStateV1Resource
ExtForeignToplevelStateV1.global_class = ExtForeignToplevelStateV1Global