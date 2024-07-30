# This file has been autogenerated by the pywayland scanner

# Copyright © 2008-2011 Kristian Høgsberg
# Copyright © 2010-2011 Intel Corporation
# Copyright © 2012-2013 Collabora, Ltd.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice (including the
# next paragraph) shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

from .wl_surface import WlSurface


class WlKeyboard(Interface):
    """Keyboard input device

    The :class:`WlKeyboard` interface represents one or more keyboards
    associated with a seat.
    """

    name = "wl_keyboard"
    version = 9

    class keymap_format(enum.IntEnum):
        no_keymap = 0
        xkb_v1 = 1

    class key_state(enum.IntEnum):
        released = 0
        pressed = 1


class WlKeyboardProxy(Proxy[WlKeyboard]):
    interface = WlKeyboard

    @WlKeyboard.request(version=3)
    def release(self) -> None:
        """Release the keyboard object
        """
        self._marshal(0)
        self._destroy()


class WlKeyboardResource(Resource):
    interface = WlKeyboard

    @WlKeyboard.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.FileDescriptor),
        Argument(ArgumentType.Uint),
    )
    def keymap(self, format: int, fd: int, size: int) -> None:
        """Keyboard mapping

        This event provides a file descriptor to the client which can be
        memory-mapped in read-only mode to provide a keyboard mapping
        description.

        From version 7 onwards, the fd must be mapped with MAP_PRIVATE by the
        recipient, as MAP_SHARED may fail.

        :param format:
            keymap format
        :type format:
            `ArgumentType.Uint`
        :param fd:
            keymap file descriptor
        :type fd:
            `ArgumentType.FileDescriptor`
        :param size:
            keymap size, in bytes
        :type size:
            `ArgumentType.Uint`
        """
        self._post_event(0, format, fd, size)

    @WlKeyboard.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Object, interface=WlSurface),
        Argument(ArgumentType.Array),
    )
    def enter(self, serial: int, surface: WlSurface, keys: list) -> None:
        """Enter event

        Notification that this seat's keyboard focus is on a certain surface.

        The compositor must send the :func:`WlKeyboard.modifiers()` event after
        this event.

        :param serial:
            serial number of the enter event
        :type serial:
            `ArgumentType.Uint`
        :param surface:
            surface gaining keyboard focus
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        :param keys:
            the currently pressed keys
        :type keys:
            `ArgumentType.Array`
        """
        self._post_event(1, serial, surface, keys)

    @WlKeyboard.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Object, interface=WlSurface),
    )
    def leave(self, serial: int, surface: WlSurface) -> None:
        """Leave event

        Notification that this seat's keyboard focus is no longer on a certain
        surface.

        The leave notification is sent before the enter notification for the
        new focus.

        After this event client must assume that all keys, including modifiers,
        are lifted and also it must stop key repeating if there's some going
        on.

        :param serial:
            serial number of the leave event
        :type serial:
            `ArgumentType.Uint`
        :param surface:
            surface that lost keyboard focus
        :type surface:
            :class:`~pywayland.protocol.wayland.WlSurface`
        """
        self._post_event(2, serial, surface)

    @WlKeyboard.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def key(self, serial: int, time: int, key: int, state: int) -> None:
        """Key event

        A key was pressed or released. The time argument is a timestamp with
        millisecond granularity, with an undefined base.

        The key is a platform-specific key code that can be interpreted by
        feeding it to the keyboard mapping (see the keymap event).

        If this event produces a change in modifiers, then the resulting
        :func:`WlKeyboard.modifiers()` event must be sent after this event.

        :param serial:
            serial number of the key event
        :type serial:
            `ArgumentType.Uint`
        :param time:
            timestamp with millisecond granularity
        :type time:
            `ArgumentType.Uint`
        :param key:
            key that produced the event
        :type key:
            `ArgumentType.Uint`
        :param state:
            physical state of the key
        :type state:
            `ArgumentType.Uint`
        """
        self._post_event(3, serial, time, key, state)

    @WlKeyboard.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def modifiers(self, serial: int, mods_depressed: int, mods_latched: int, mods_locked: int, group: int) -> None:
        """Modifier and group state

        Notifies clients that the modifier and/or group state has changed, and
        it should update its local state.

        :param serial:
            serial number of the modifiers event
        :type serial:
            `ArgumentType.Uint`
        :param mods_depressed:
            depressed modifiers
        :type mods_depressed:
            `ArgumentType.Uint`
        :param mods_latched:
            latched modifiers
        :type mods_latched:
            `ArgumentType.Uint`
        :param mods_locked:
            locked modifiers
        :type mods_locked:
            `ArgumentType.Uint`
        :param group:
            keyboard layout
        :type group:
            `ArgumentType.Uint`
        """
        self._post_event(4, serial, mods_depressed, mods_latched, mods_locked, group)

    @WlKeyboard.event(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        version=4,
    )
    def repeat_info(self, rate: int, delay: int) -> None:
        """Repeat rate and delay

        Informs the client about the keyboard's repeat rate and delay.

        This event is sent as soon as the :class:`WlKeyboard` object has been
        created, and is guaranteed to be received by the client before any key
        press event.

        Negative values for either rate or delay are illegal. A rate of zero
        will disable any repeating (regardless of the value of delay).

        This event can be sent later on as well with a new value if necessary,
        so clients should continue listening for the event past the creation of
        :class:`WlKeyboard`.

        :param rate:
            the rate of repeating keys in characters per second
        :type rate:
            `ArgumentType.Int`
        :param delay:
            delay in milliseconds since key down until repeating starts
        :type delay:
            `ArgumentType.Int`
        """
        self._post_event(5, rate, delay)


class WlKeyboardGlobal(Global):
    interface = WlKeyboard


WlKeyboard._gen_c()
WlKeyboard.proxy_class = WlKeyboardProxy
WlKeyboard.resource_class = WlKeyboardResource
WlKeyboard.global_class = WlKeyboardGlobal
