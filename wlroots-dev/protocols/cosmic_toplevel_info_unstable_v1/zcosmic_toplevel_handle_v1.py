# This file has been autogenerated by the pywayland scanner

# Copyright © 2018 Ilia Bozhinov
# Copyright © 2020 Isaac Freund
# Copytight © 2022 Victoria Brekenfeld
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

from ..cosmic_workspace_unstable_v1 import ZcosmicWorkspaceHandleV1
from ..wayland import WlOutput


class ZcosmicToplevelHandleV1(Interface):
    """An open toplevel

    A :class:`ZcosmicToplevelHandleV1` object represents an open toplevel
    window.  A single app may have multiple open toplevels.

    Each toplevel has a list of outputs it is visible on, exposed to the client
    via the output_enter and output_leave events.
    """

    name = "zcosmic_toplevel_handle_v1"
    version = 1

    class state(enum.IntEnum):
        maximized = 0
        minimized = 1
        activated = 2
        fullscreen = 3


class ZcosmicToplevelHandleV1Proxy(Proxy[ZcosmicToplevelHandleV1]):
    interface = ZcosmicToplevelHandleV1

    @ZcosmicToplevelHandleV1.request()
    def destroy(self) -> None:
        """Destroy the :class:`ZcosmicToplevelHandleV1` object

        This request should be called either when the client will no longer use
        the :class:`ZcosmicToplevelHandleV1` or after the closed event has been
        received to allow destruction of the object.
        """
        self._marshal(0)
        self._destroy()


class ZcosmicToplevelHandleV1Resource(Resource):
    interface = ZcosmicToplevelHandleV1

    @ZcosmicToplevelHandleV1.event()
    def closed(self) -> None:
        """The toplevel has been closed

        The server will emit no further events on the
        :class:`ZcosmicToplevelHandleV1` after this event. Any requests
        received aside from the destroy request will be ignored. Upon receiving
        this event, the client should make the destroy request to allow freeing
        of resources.
        """
        self._post_event(0)

    @ZcosmicToplevelHandleV1.event()
    def done(self) -> None:
        """All information about the toplevel has been sent

        This event is sent after all changes in the toplevel state have been
        sent.

        This allows changes to the :class:`ZcosmicToplevelHandleV1` properties
        to be seen as atomic, even if they happen via multiple events.

        Note: this is is not sent after the closed event.
        """
        self._post_event(1)

    @ZcosmicToplevelHandleV1.event(
        Argument(ArgumentType.String),
    )
    def title(self, title: str) -> None:
        """Title change

        This event is emitted whenever the title of the toplevel changes.

        :param title:
        :type title:
            `ArgumentType.String`
        """
        self._post_event(2, title)

    @ZcosmicToplevelHandleV1.event(
        Argument(ArgumentType.String),
    )
    def app_id(self, app_id: str) -> None:
        """App_id change

        This event is emitted whenever the app_id of the toplevel changes.

        :param app_id:
        :type app_id:
            `ArgumentType.String`
        """
        self._post_event(3, app_id)

    @ZcosmicToplevelHandleV1.event(
        Argument(ArgumentType.Object, interface=WlOutput),
    )
    def output_enter(self, output: WlOutput) -> None:
        """Toplevel entered an output

        This event is emitted whenever the toplevel becomes visible on the
        given output. A toplevel may be visible on multiple outputs.

        :param output:
        :type output:
            :class:`~pywayland.protocol.wayland.WlOutput`
        """
        self._post_event(4, output)

    @ZcosmicToplevelHandleV1.event(
        Argument(ArgumentType.Object, interface=WlOutput),
    )
    def output_leave(self, output: WlOutput) -> None:
        """Toplevel left an output

        This event is emitted whenever the toplevel is no longer visible on a
        given output. It is guaranteed that an output_enter event with the same
        output has been emitted before this event.

        :param output:
        :type output:
            :class:`~pywayland.protocol.wayland.WlOutput`
        """
        self._post_event(5, output)

    @ZcosmicToplevelHandleV1.event(
        Argument(ArgumentType.Object, interface=ZcosmicWorkspaceHandleV1),
    )
    def workspace_enter(self, workspace: ZcosmicWorkspaceHandleV1) -> None:
        """Toplevel entered an workspace

        This event is emitted whenever the toplevel becomes visible on the
        given workspace. A toplevel may be visible on multiple workspaces.

        :param workspace:
        :type workspace:
            :class:`~pywayland.protocol.cosmic_workspace_unstable_v1.ZcosmicWorkspaceHandleV1`
        """
        self._post_event(6, workspace)

    @ZcosmicToplevelHandleV1.event(
        Argument(ArgumentType.Object, interface=ZcosmicWorkspaceHandleV1),
    )
    def workspace_leave(self, workspace: ZcosmicWorkspaceHandleV1) -> None:
        """Toplevel left an workspace

        This event is emitted whenever the toplevel is no longer visible on a
        given workspace. It is guaranteed that an workspace_enter event with
        the same workspace has been emitted before this event.

        :param workspace:
        :type workspace:
            :class:`~pywayland.protocol.cosmic_workspace_unstable_v1.ZcosmicWorkspaceHandleV1`
        """
        self._post_event(7, workspace)

    @ZcosmicToplevelHandleV1.event(
        Argument(ArgumentType.Array),
    )
    def state(self, state: list) -> None:
        """The toplevel state changed

        This event is emitted once on creation of the
        :class:`ZcosmicToplevelHandleV1` and again whenever the state of the
        toplevel changes.

        :param state:
        :type state:
            `ArgumentType.Array`
        """
        self._post_event(8, state)


class ZcosmicToplevelHandleV1Global(Global):
    interface = ZcosmicToplevelHandleV1


ZcosmicToplevelHandleV1._gen_c()
ZcosmicToplevelHandleV1.proxy_class = ZcosmicToplevelHandleV1Proxy
ZcosmicToplevelHandleV1.resource_class = ZcosmicToplevelHandleV1Resource
ZcosmicToplevelHandleV1.global_class = ZcosmicToplevelHandleV1Global