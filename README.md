# Current status: Stable Beta (Please Read)

Did your system just update itself from KDE Plasma 5 to Plasma 6, and Toshy stopped working? And you installed Toshy before January 2024? Just grab a new zip file from the big green **`  <> Code  ▼  `** button and reinstall. Your config customizations and preference choices should be preserved (if you made your config changes within the "slice marks").

WARNING: There is a very annoying "bug" (more of an implementation issue) going around where there is a problem with services like `xdg-desktop-portal` and `xdg-desktop-portal-gnome` (or `xdg-desktop-portal-gtk`) causing very long delays with launching certain applications (particularly GTK apps like Firefox, but also reportedly Qt apps sometimes) in a Wayland session. Some distros seem to have a fix for this, others have not fixed it yet. I think this occurs mainly on systems that have both KDE Plasma and some GTK-based desktop environment installed at the same time, leading to multiple desktop "portal" services trying to run at the same time.  

Symptoms for Toshy are that the systemd services can't start up properly until anywhere from 30 seconds to a minute or more after logging in. They will eventually start, and restarting the services later (after the glitchy desktop portal service times out) works without issue, which made this really difficult to diagnose. I've been observing this mostly on KDE in multiple Linux distros. One "fix" is to mask the offending `xdg-desktop-portal-gnome` (or `xdg-desktop-portal-gtk`) service to keep it from clogging things up:  

```sh
systemctl --user mask xdg-desktop-portal-gnome
```

Or:

```sh
systemctl --user mask xdg-desktop-portal-gtk
```

But you may need to unmask the service if you log into a GNOME desktop, in a Wayland session. Just replace `mask` with `unmask`.  

## Main issues you might run into

- KEYBOARD TYPE: The Toshy config file tries to automatically identify the "type" of your keyboard based on some pre-existing lists of keyboard device names, which do not have many entries, and there are thousands of keyboard name variants. So your keyboard may be misidentified, leading to modifier keys in the "wrong" place. BE PREPARED to identify the name of your keyboard device (try `toshy-devices` in a terminal) and enter it into the custom list (actually a Python "dictionary") in the config file to fix this problem. The custom entry is designed to be retained even if you reinstall later. There is a sub-menu in the tray icon menu intended to allow temporarily bypassing this problem while you find the device name and enter it in your config file.  

Go to this FAQ entry for more info:  

- [Keyboard Type Not Correct](https://github.com/RedBearAK/toshy/wiki/FAQ-(Frequently-Asked-Questions)#my-keyboard-is-not-recognized-as-the-correct-type)  

Other possible issues:  

- May have issues installing on distros not on the "tested" list below. If you think your distro is closely related to one on the list, try the `list-distros` command with the setup script, and then the `--override-distro` option for the `install` command. See the [**How to Install**](#how-to-install) section.  

- May seem to run at login, but not do any remapping, needing `toshy-config-verbose-start` in the terminal to troubleshoot. Or, it may just need a restart of the services from the tray icon or with `toshy-services-restart`. Check the output of `toshy-services-log` and `toshy-services-status` first to see if there is an obvious error message that explains the problem. Like not having a compatible GNOME Shell extension installed/enabled to support a Wayland+GNOME session. Other than the Wayland+GNOME situation, I don't really see this much anymore.  

- On a dual-init distro like MX Linux, if you install Toshy while using SysVinit (default on MX) the installer will avoid installing the `systemd` packages and service unit files. If you then switch to using `systemd` as init at the boot screen (from the "Advanced" menu) you'll need to re-run the Toshy installer (only once) while using `systemd` to make Toshy work automatically like it does on other distros where the default is `systemd`. Or, you can just keep running the config manually, like is currently necessary under SysVinit and any other init system besides `systemd`.  

# Toshy README

• • • • • • • 
![Toshy app icon inverse grayscale](./assets/toshy_app_icon_rainbow_inverse_grayscale.svg "Toshy app icon inverse grayscale")
• • • • • • • 
![Toshy app icon inverted](./assets/toshy_app_icon_rainbow_inverse.svg "Toshy app icon inverse")
• • • • • • • 
![Toshy app icon](./assets/toshy_app_icon_rainbow.svg "Toshy app icon")


## Make your Linux keyboard act like a 'Tosh! <br>(or, What the Heck is This?!?)

Toshy is a config file for the `xwaykeyz` Python-based keymapper for Linux (which was forked from `keyszer`, which was in turn forked from `xkeysnail`) along with some commands and apps to more conveniently interact with and manage the keymapper. The Toshy config is not strictly a fork of Kinto, but was based in the beginning entirely on the config file for Kinto.sh by Ben Reaves (https://github.com/rbreaves/kinto or https://kinto.sh). Without Kinto, Toshy would not exist. Using Toshy should feel basically the same as using Kinto, just with some new features and some problems solved.  

The purpose of Toshy is to match, as closely as possible, the behavior of keyboard shortcuts in macOS when working on similar applications in Linux. General system-wide shortcuts such as Cmd+Q/W/R/T/A/Z/X/C/V and so on are relatively easy to mimic by just moving the modifier key locations, with `modmaps` specific to each supported keyboard type. A lot of shortcuts in Linux just use `Ctrl` in the place of where macOS would use `Cmd`. But many other shortcut combos from macOS applications have to be remapped onto entirely different shortcut combos in the Linux equivalent application. This is done using application-specific `keymaps`, that only become active when you are using the specified application or window. Some of the keymaps apply to entire groups of apps, like "terminals" or "file managers".  

All of this basic functionality is inherited from Kinto. Toshy just tries to be a bit fancier in implementing it.  

## Toshifying an Application

If an app that you use frequently in Linux has some shortcut behavior that still doesn't match what you'd expect from the same application (or a similar application) in macOS, after Toshy's general remapping of the modifier keys, you can add a keymap that matches the app's "class" and/or "name/title" window attributes, to make that application behave as expected. By adding it to the default config file, every user will benefit!  

> [!TIP]  
> There's an easier way now, that works in both X11/Xorg and Wayland sessions:  
>
> - `Shift+Opt+Cmd+I,I` (quickly double-tap the "I" key)  
>
> This brings up a dialog showing app/window/keyboard info. Use the physical keys in the same position the keys with these names would be in on an Apple keyboard, even if you don't have an Apple keyboard.  
> 
> In a "remote" type of app (remote desktop or virtual machine apps), where most modmaps and the general keymap are disabled, the diagnostic shortcut will still work, but the physical keys will be different:  
> 
> - `Shift+Alt+RIGHT_CTRL+I,I` (quickly double-tap the "I" key)  
>
> In this case the literal physical keys matching these names must be used, including using the Ctrl key on the right side of the keyboard.  
> </br>

Still relevant, but unnecessary with the diagnostic tool in the note above:  

To do this, on X11 you need the tool `xprop` which lets you retrieve the window attributes by clicking on the window with the mouse. Use this command to get only the relevant attributes:  

```sh
xprop WM_CLASS _NET_WM_NAME
```

The mouse cursor will change to a cross shape. Click on the window in question and the attributes will appear in the terminal.  

If you're in one of the compatible Wayland environments (see the current list [here](#currently-working-desktop-environments-or-window-managers)), you'll have to rely on other tools, or the verbose logging output from `toshy-config-verbose-start`. When a window has the focus and you use a keyboard shortcut that gets remapped by the keymapper config file, you will see additional output in the terminal showing the window's class and name/title. A good shortcut to use for this that usually won't do anything unless the app has a tabbed UI is `Shift+Cmd+Left_Brace` or `Shift+Cmd+Right_Brace` (those are the defined names of the square bracket keys). Utilities like `xprop` will generally have no output in a Wayland session.  

## Windows Support

Toshy has no Windows version, unlike the Kinto.sh project. I was trying to solve a number of issues and add features to the Linux version of Kinto, so that's all I'm focused on for Toshy. The Windows version of Kinto works great. Go check it out if you need Mac-like keyboard shortcuts on Windows. I also contribute to Kinto on the Windows side.  

https://github.com/rbreaves/kinto  
https://kinto.sh  

## Keyboard Types

Four different keyboard types are supported by Toshy (Windows/PC, Mac/Apple, IBM and Chromebook), just as in Kinto. But Toshy does its best to automatically treat each keyboard device as the correct type in real-time, as you use it, rather than requiring you to change the keyboard type from a menu. This means that you _should_ be able to use an Apple keyboard connected to a PC laptop, or an IBM keyboard connected to a MacBook, and shortcut combos on both the external and internal keyboards should work as expected, with the modifier keys appearing to be in the correct place to "Act like a 'Tosh".  

## Option-key Special Characters

Toshy includes a complete implementation of the macOS Option-key special characters, including all the "dead key" accent keys, from two keyboard layouts. The standard US keyboard layout, and the "ABC Extended" layout (which is still a US keyboard layout otherwise). This adds up to somewhere over 600 special characters being available, between the two layouts. It works the same way it does on macOS, when you hold the Option or Shift+Option keys. For example, Option+E, then Shift+E, gets you an "E" with Acute accent: É.  

The special characters may not work as expected unless you add a bit of "throttle" delay to the macro output. This is an `xwaykeyz` API function that inserts timing delays in the output of combos that involve modifier keys. There is a general problem with Linux keymappers using `libinput` in a lot of situations, especially in virtual machines, with the modifier key presses being misinterpreted as occuring at a slightly different time, leading to problems with macro output.  

A slight delay will usually clear this right up, but a virtual machine environment may need a few dozen milliseconds to achieve macro stability. In fact it's not just macros, but many shortcuts in general may seem very flaky or unusuble in a VM, and this will impact the Option-key special characters, since it uses Unicode macro sequences.  

A dedicated Unicode processing function was added to `keyszer` (and inherited by `xwaykeyz`) that made it possible to bring the Option-key special characters to Linux, where previously I could only add it to the Windows version of Kinto using AutoHotkey.  

If you're curious about what characters are available and how to access them, the fully documented lists for each layout are available here:  

https://github.com/RedBearAK/optspecialchars

It's important to understand that your actual keyboard layout will have no effect on the layout used by the Option-key special character scheme. The keymapper generally has no idea what your keyboard layout is, and has a tendency to treat your keyboard as if it is always a US layout. This is a problem that needs a solution. I haven't found even so much as a way to reliably detect the active keyboard layout. So currently Toshy works best with a US layout.  

The other problem is that the Unicode entry shortcut only seems to work if you have `ibus` or `fcitx` (unconfirmed) set up as your input manager. If not, the special characters (or any other Unicode character sequence) will only work correctly in GTK apps, which seem to have the built-in ability to understand the Shift+Ctrl+U shortcut that invokes Unicode character entry.  

There's no simple way around this, since the keymapper is only designed to send key codes from a virtual keyboard. Unlike AutoHotkey in Windows, which can just "send" a character pasted in an AHK script to an application (although there are potential problems with that if the AHK file encoding is wrong). 

## General improvements over Kinto

This section was moved to a Wiki page to make the README shorter:  

https://github.com/RedBearAK/toshy/wiki/General-improvements-over-Kinto  

## Requirements

- Linux (no Windows support planned, use Kinto for Windows)

    - See [**list of working/tested distros**](#currently-workingtested-linux-distros)

- Python >=3.6 (to run the setup script)

- Python >=3.8 (to run the keymapper in its `venv`)

- [**`xwaykeyz`**](https://github.com/RedBearAK/xwaykeyz/) (keymapper for Linux, forked from `keyszer`)

    - Automatically installed by Toshy setup script

- X11/Xorg, or a supported Wayland environment

    - See [**list of working DEs/WMs**](#currently-working-desktop-environments-or-window-managers)

- `systemd` (but you can just manually run the config from terminal, shell script, GUI preferences app, or tray indicator menu, so the basic functionality of the Toshy config can work regardless of the init system in use)

- D-Bus, and `dbus-python`

### Specific requirements for certain DEs/WMs

On some Wayland environments it takes extra steps to get the per-app or per-app-group (e.g., "terminals") specific keymapping to work. Special methods need to be used to grab the window context info, and sometimes that means installing something external to Toshy.  

- **`Wayland+Plasma`** sessions have a small glitch where you have to change the focused window once after the Toshy KWin script is installed, to get the app-specific remapping to start working. I am trying a solution that uses a pop-up dialog to create a KWin event that "kickstarts" the KWin script. You should briefly see a dialog appear and then disappear shortly after you log in to a Wayland+Plasma session. This has been working well for some time now.  

- **`Wayland+GNOME`** sessions require one of the GNOME Shell extensions listed in this section to be installed and enabled (see the [**`next section`**](#managing-shell-extensions-in-gnome) below on how to easily download and install GNOME Shell extensions):

    ___
    - **Name: 'Xremap' (try this on older GNOME shells)**
    - UUID: `xremap@k0kubun.com`
    - URL: https://extensions.gnome.org/extension/5060/xremap/
    ___
    - **Name: 'Window Calls Extended'**
    - UUID: `window-calls-extended@hseliger.eu`
    - URL: https://extensions.gnome.org/extension/4974/window-calls-extended/
    ___
    - **Name: 'Focused Window D-Bus'**
    - UUID: `focused-window-dbus@flexagoon.com`
    - URL: https://extensions.gnome.org/extension/5592/focused-window-d-bus/
    ___

### Managing shell extensions in GNOME

It's very easy to search for and install GNOME Shell extensions now, if you install the "Extension Manager" Flatpak application from Flathub. No need to mess around with downloading a zip file from `extensions.gnome.org` and manually installing/enabling in the terminal, or trying to get the link between a native package and a browser extension working in a web browser. (Certain browsers and distros often make this a painful process.)  

Many distros with GNOME will need the `AppIndicator and KStatusNotifierItem` extension (or some other extension that enables indicator tray icons) to make the tray icon appear in the top bar, and if you want to use Wayland you'll need one of the extensions from the list above.  

Here's how to install "Extension Manager":  

```sh
flatpak install com.mattjakeman.ExtensionManager
```

... or just:

```sh
flatpak install extensionmanager
```

If it's not found you may need to enable the Flathub repo on your machine. Go to https://flathub.org/setup for instructions for your distro.  

> [!NOTE]
> The "Extension Manager" Flatpak app is NOT the same thing as the "Extensions" app that sometimes comes pre-installed on GNOME distros. That is a simpler app with no ability to browse the available extensions.  

When you get it installed, you can just use the "Browse" tab in this application to search for the extensions by name and quickly install them.  

There is no risk of any kind of conflict when installing more than one of the compatible shell extensions. Which might be advisable, to reduce the risk of not having a working extension for a while the next time you upgrade your system in-place and wind up with a newer version of GNOME that one or two of the extensions hasn't been updated to support. I expect at least one of the (now three) extensions will always be updated quickly to support the latest GNOME. 

The window context module of the keymapper installed by Toshy will seamlessly jump to trying the other compatible extensions in case one fails or is disabled/uninstalled for any reason. You just need to have at least one from the list installed and enabled, and when it responds over D-Bus to the query from the keymapper it will be marked as the "good" one and used from then on, unless it stops responding. Lather, rinse, repeat.  

The `Xremap` GNOME shell extension is the only one that supports older GNOME versions, so it's the only one that will show up when browsing the extensions list from an environment like Zorin OS 16.x (GNOME 3.38.x) or the distros based on Red Hat Enterprise Linux (clones or RHEL compatibles like AlmaLinux, Rocky Linux, Oracle Linux, EuroLinux, etc.) which are still using GNOME 40.x on the 9.x versions.  

There is a weird bug with searching for extensions by name sometimes, where you actually have to use the option "Show Unsupported" from the hamburger menu in order to get it to show up. This seems to happen at random, and may be dependent on what is going on with GNOME's extension site. Just make sure that the extension says in its details page that it is compatible with your version of the GNOME shell, and it should be fine to install.  

## How to Install  

> [!WARNING]
> **_DO NOT_** attempt to manually install Python dependencies 
> with `pip` using the `requirements.txt` file. That file only 
> exists to let GitHub show some dependency info. (This may 
> change at some point in the future, but ignore it for now.)

> [!NOTE]  
> Installer commands and options are now different from early Toshy releases.  

1. Click the big green **`  <> Code  ▼  `** button near the top of the page.
1. Download the latest zip file from the drop-down. ("Releases" are older.)  
1. Unzip the archive, and open a terminal in the resulting folder.  
1. Run the `setup_toshy.py` script in the terminal, like this:  

```sh
./setup_toshy.py install
```

(See the `--options` in the next section if the basic install doesn't work.)  

If for any reason the script is not executable, you can fix that with this command:  

```sh
chmod +x setup_toshy.py
```

### Options for installer script

The installer script has a few different `commands` and `--options` available, as shown in this section.  

```sh
./setup_toshy.py --help
```

Shows a short description of all available commands.  

```sh
./setup_toshy.py install --help
```

Shows a short description of all available options to modify the `install` command. The modifier options can be combined.  

```sh
./setup_toshy.py install --override-distro distro_name
```

This option will force the installer to attempt the install for that distro name/type. You can use this if you have a distro that is not on the distro list yet, but you think it is close enough to one of the existing distros in the list that the installer should do the right things. For instance if you have some very Arch-ish or very Debian-ish distro, or something based on Ubuntu (there are many!) that doesn't identify as one of the "known" distros when you use `show-env` and `list-distros` (see below), then you can try to make it install using one of the related distro names. This will probably work, if the distro is just a minor variation of its parent distro.  

```sh
./setup_toshy.py install --barebones-config
```

This special option will install a "barebones" config file that does no modmapping or keymapping by default (besides a simple example keymap that gives access to a couple of currency symbols, as a demo). The option will also convert an existing Toshy config into a "barebones" config file, but will ask for explicit confirmation. This config will of course not provide any of the features that a normal Toshy config would, other than the ability to use the keymapper in any of the [compatible environments](#currently-working-desktop-environments-or-window-managers).  

The Toshy installer should try to retain your changes inside any of the editable "slices" of the barebones config file, and avoid replacing your barebones config with a regular Toshy config file, **_even if you don't use the same CLI option the next time you run the installer_**. Submit an issue if it doesn't respect your barebones config. Even if that happens, the previous config file should be in the timestamped backup folder that the installer always creates.  

```sh
./setup_toshy.py install --skip-native
```

This is primarily a convenient **debug/development** option. It just bypasses the attempt to install any native package list.  

In theory, you could use this option to get Toshy working on a new distro type that is not currently supported. You could take one of the existing package lists (found inside the installer script file) from a distro type that is closely related to your distro, and try to manually install packages after using this `--skip-native` option, and the `--override-distro` option to provide the installer a "known" distro name. There will of course be errors, particularly during the process of installing/building the Python packages that get installed in the virtual environment folder via the `pip` command. Then you would search the web for what kind of package might fix that error, and try again, with the same options. There will often also be errors to overcome after the install is finished, when trying to launch the tray and GUI apps. Using the `toshy-tray` and `toshy-gui` commands in the terminal will display the errors that prevent those apps from launching or working correctly.  

If you go through this process I hope you'll keep track of exactly what packages you ended up needing to install, and take the time to submit an issue with the package list, distro details, and the native package command(s) you needed to use, so support for the the distro type can be added to the installer.  

One pitfall that is hard to avoid in this process is installing packages that don't actually solve any issue, and then not removing them to verify whether they are truly dependencies. Be careful about that.  

#### Avoiding package layering on Fedora atomic/immutable distros  

I've also recently found the `--skip-native` option to be useful on Fedora atomic/immutable distros, after running the installer initially inside a distrobox Fedora container (same version as the host). This is potentially a way to get Toshy's `venv` working without needing to use package layering on the host immutable. But the process of installing inside the container would probably need to be repeated any time the packages downloaded with `pip` change versions, because that process relies on some native packages to complete the build/caching step.  

Last, but definitely not least, the "extra" install option:  

```sh
./setup_toshy.py install --fancy-pants
```

This will do the full install, but also add various things that I find convenient, fun, or that somehow make the desktop environment behave more sensibly, which often means "more like macOS". (Note: For some reason KDE on stock Debian 12 doesn't have the "Large Icons" task switcher installed, so you have to fix the task switcher in the Task Switcher control panel after using this option.)  

At the moment this installer option will do the following: 

- ALL: Installs "Fantasque Sans Mono noLig" font
    - From a fork with no coding ligatures
    - LargeLineHeight-NoLoopK variant
    - Try it in terminals or code editors
    - May look a bit "heavy" on KDE due to forced "stem darkening" in Qt apps
- KDE: Installs "Application Switcher" KWin script (groups apps like macOS/GNOME)
- KDE: Disables task switcher option "Show selected window"
- KDE: Sets the task switcher to "Large Icons" (like macOS/GNOME task switcher)
- KDE: Enables task switcher option "Only one window per application" (makes the task switcher dialog show only a single icon for each application, like macOS/GNOME)

Note that any or all of the "--options" for the `install` command can be combined, as they modify independent aspects of what the `install` command will do:  

```sh
./setup_toshy.py install --override-distro distro-name --skip-native --barebones-config --fancy-pants
```

Here are some other things besides installing that the setup script can do. These commands are mutually exclusive, just like the `install` command.  

```sh
./setup_toshy.py list-distros
```

This command will print out a list of the distros that the Toshy installer theoretically "knows" how to deal with, as far as knowing the correct package manager to use and having a list of package names that would actually work. Entries from the displayed distro list can be used with the `--override-distro` option for the `install` command.  

```sh
./setup_toshy.py show-env
```

This will just show what the installer will see as the environment when you try to install, but won't actually run the full install process.  

```sh
./setup_toshy.py apply-tweaks
```

Just applies the "desktop tweaks" for the environment, does not do the full install. Might be handy if you have a system with multiple desktop environments.  

```sh
./setup_toshy.py remove-tweaks
```

Just removes the "desktop tweaks" the installer applied. Does not do the full uninstall.  

## How to Uninstall

This should work now:  

```sh
./setup_toshy.py uninstall
``` 

Please file an issue if you have some sort of trouble with the `uninstall` command. If you have a multi-desktop system you may need to run the uninstall procedure while logged into KDE if you ran the installer in KDE, due to the KDE-specific components that get installed for Wayland support.  

## Currently working/tested Linux distros:

This is a list of Linux distributions and desktop variants I've been able to test so far. For those with release versions provided, that is just what I happened to download and test. Older or newer versions of the same distro, within reason, may also work.  

As noted elsewhere in the README, there is no Windows version of Toshy, unlike Kinto.  

### Fedora and Fedora Variants

- Fedora 38/39/40 (upstream of CentOS Stream and RHEL)

    - Workstation (GNOME) works
    - Wayland+GNOME requires shell extension (see [**Requirements**](#requirements))
    - KDE Plasma variant works (X11/Xorg or Wayland session)
    - Sway spin variant works
    - Hyprland works (using JaKooLit Fedora-Hyprland setup script)
    - Other spins like Cinnamon, Budgie should work fine

- Fedora Asahi Remix 39 (Fedora for Apple Silicon Macs)

    - Reported working by user (See Toshy issue #98)

- Nobara 38 (Fedora-based)

    - Tested the usual GNOME desktop variant (X11/Xorg and Wayland)
    - Many Toshy dependencies are pre-installed on Nobara
    - Nobara pre-installs the Extension Manager app. Nice!
    - Enable the AppIndicator extension (pre-installed) for tray icon
    - Install an extension from [**Requirements**](#requirements) if using Wayland+GNOME

- Silverblue/Kinoite 38/39/40 (Fedora-based immutables)

    - Package layering is used during install (can be removed later?)
    - Wayland+GNOME session needs extension (see [**Requirements**](#requirements))

- Ultramarine Linux 38/39 (Fedora-based)

    - Ultramarine GNOME tested (Wayland session requires extension)

### Red Hat Enterprise Linux (RHEL), Clones, CentOS Stream

- AlmaLinux 9.3 (RHEL compatible)

    - Installed from KDE "live" ISO, updated from 9.2 to 9.3
    - KDE Plasma desktop tested (Wayland session supported)
    - Some non-default (but official) repos like CRB will be enabled

- [ AlmaLinux | Rocky Linux ] 9.2 (RHEL clones)

    - Tested with "Workstation" installer choice, not "Server with GUI"
    - Default GNOME desktop tested (Wayland session requires extension)
    - KDE Plasma desktop tested (Wayland session supported)
    - Some non-default (but official) repos like CRB will be enabled

- AlmaLinux 8.8 (RHEL clone) - Partial support:

    - Tested with "Workstation" installer choice, not "Server with GUI"
    - Default GNOME desktop tested, X11/Xorg session only
    - Wayland+GNOME session NOT supported, because:
        - GNOME is old, no compatible Shell extension available
    - Install AppIndicator extension from the Software app
    - RHEL 8.x and clones probably also work in a similar manner

- CentOS Stream 9 (RHEL 9 upstream)

    - Same info as the RHEL 9.x clones above
    - Tested with "Workstation" installer choice

- CentOS Stream 8 (RHEL upstream) - Partial support:

    - Tested with "Workstation" installer choice (GNOME)
    - Auto-start with systemd user services works
    - GNOME X11/Xorg session works (not the default!)
        - Choose "Standard (X11 display server)" at login
    - For tray icon support:
        - Install AppIndicator extension from GNOME Software app
    - NB: GNOME Wayland session WILL NOT WORK! Because:
        - GNOME shell too old, no compatible extension available

- CentOS 7 (RHEL 7 clone) - Partial support:

    - You must first install `python3` to run `setup_toshy.py`
    - GUI preferences app will not work (Tk too old for `sv_ttk` theme)
    - `systemd` "user" services are not supported in CentOS/RHEL 7
    - Auto-start at login with systemd services not available
    - Cmd+Space (Alt+F1) shortcut must be assigned to app launcher menu
    - To manually start Toshy config from tray icon menu:
        - "(Re)Start Toshy Script" option will start Toshy config
        - "Stop Toshy Script" option will stop background Toshy config
    - To manually start Toshy config from terminal:
        - Use `toshy-config-start` or `toshy-config-verbose-start`
        - Use `toshy-config-stop` to stop a background Toshy config

- Eurolinux 9.2 (RHEL clone)

    - Tested with "Server with GUI" installer choice
    - Default GNOME desktop tested (Wayland session requires extension)
    - Some non-default (but official) repos like CRB will be enabled

- RHEL and RHEL clones not listed should be supportable

    - Red Hat Enterprise Linux itself? Probably.
    - Try `./setup_toshy.py --override-distro=almalinux` or `=rhel`

### openSUSE (RPM-based packaging system)

- openSUSE Leap 15.5/15.6 (SLES-based, fixed release) **_WORKING!_**

    - GNOME desktop works (Wayland session needs extension, see [**Requirements**](#requirements))
    - KDE desktop works (X11/Xorg or Wayland)
    - Other desktop choices should work, if session is X11/Xorg

- openSUSE Aeon/Kalpa (OpenSUSE MicroOS-based, rolling release?)

    - Aeon Wayland needs GNOME shell extension (see [**Requirements**](#requirements))
    - Kalpa (KDE Plasma) fully supported
    - Uses `transactional-update` to install native packages

- openSUSE Tumbleweed (rolling release)

    - GNOME desktop works (Wayland session needs extension, see [**Requirements**](#requirements))
    - KDE desktop works (X11/Xorg or Wayland)
    - Other desktop choices should work, if session is X11/Xorg

### OpenMandriva (DNF/RPM-based, descended from Mandriva, Mandrake)

- OpenMandriva ROME 2023/2024 (rolling release variant)

    - Wayland+Plasma tested

- OpenMandriva 5.0 (fixed release variant)

    - Wayland+Plasma tested

### Ubuntu variants and Ubuntu-based distros

- Bodhi Linux 7.0 (Ubuntu-based)

    - Desktop is Enlightenment
    - Install package `xapp` to remove some errors from log

- Feren OS 2023.04 (Ubuntu LTS variant)

    - Current base is Ubuntu 20.04 LTS
    - Desktop is KDE Plasma 5.25.x

- elementary OS 7.0/7.1 (Ubuntu-based)

    - Tray icons are not supported in Pantheon desktop

- KDE Neon (based on Ubuntu LTS releases)

    - X11/Xorg or Wayland+Plasma session

- Linux Mint 21.1/21.2/21.3 (Ubuntu-based)

    - Cinnamon desktop (X11/Xorg or Wayland)
    - Xfce desktop (X11/Xorg only)
    - MATE desktop (X11/Xorg only)
    - All desktops can be installed on the same Mint system:
    - `sudo apt install mint-meta-mate mint-meta-xfce mint-meta-cinnamon`

- Pop!_OS 22.04 LTS (Ubuntu-based)

    - X11/Xorg or Wayland+GNOME (requires extension)

- Rhino Linux (Ubuntu rolling release variant)

    - Desktop is Xfce/Unicorn (X11/Xorg)

- Tuxedo OS 1/2 (Ubuntu LTS variant)

    - X11/Xorg
    - KDE Plasma desktop

- Ubuntu official variants tested:

    - Ubuntu 22.04/23.04/23.10
        - X11/Xorg or Wayland+GNOME (requires extension)
    - Kubuntu 22.04/23.04/23.10
        - X11/Xorg or Wayland+Plasma
    - Xubuntu 23.04/23.10
        - X11/Xorg only
    - Lubuntu 23.04/23.10
        - X11/Xorg only
    - Ubuntu Unity 23.10
        - X11/Xorg only
    - Ubuntu Budgie 23.04
        - X11/Xorg only
    - Ubuntu Kylin 24.04 - **_WORKING, BUT SEE [NOTE](#ubuntu-kylin-issues) BELOW_**
        - X11/Xorg only
    - Ubuntu Kylin 23.10 - **_NOT WORKING!_**
        - **_PACKAGE CONFLICT IN REPO_**
        - X11/Xorg only

- Zorin OS 17/17.1 Core/Lite (Ubuntu-based)

    - X11/Xorg or Wayland+GNOME (requires extension)
    - Wayland+GNOME requires extension (see [**Requirements**](#requirements))
    - GNOME Shell is version 43.x, any extension should work now

- Zorin OS 16.2/16.3 Core/Lite (Ubuntu-based)

    - X11/Xorg or Wayland+GNOME (requires extension)
    - NOTE: GNOME Shell on Zorin 16.x is old: 3.38
    - `Xremap` is the only compatible shell extension

#### Ubuntu Kylin issues

Toshy can finally be installed on Ubuntu Kylin 24.04, unlike the earlier 23.10 release, which had a fatal package version conflict that I couldn't resolve. But the UKUI desktop environment (at least in the tested 24.04 beta release) seems to have some strange issues with task switching, and with transferring keyboard focus properly after task switching. Since keymaps for an app like Peony (the default UKUI/Kylin file manager) are specific to the app class of `peony-qt`, the correct keymap only activates after clicking on the Peony window, even if it appears to already be the focused app (watch the highlights on the window controls).  

Using Cmd+Tab to switch from another app currently results in the keyboard focus (and the app class) remaining with the previous app. So if the previous app was Mate-terminal, the keyboard shortcuts will respond as if you are still in the Mate-terminal window, until you click on the Peony window. This probably affects other apps after task switching with the keyboard.  

Task switching is also broken with the 24.04 beta UKUI desktop, in the sense that you can't switch beyond the last app with the keyboard. The task switcher dialog doesn't respond to holding the modifier key and hitting Tab multiple times. This has nothing to do with Toshy (it's broken even before installing Toshy or when Toshy is disabled) and is similar to a longstanding bug in task switching on the Budgie desktop enironment. If you have any idea where to report these issues to the Ubuntu Kylin developers, please do so if you care about getting them fixed.  

### Debian and Debian-based distros

- antiX 22.x/23.x (Debian-based, related to MX Linux)

    - Preliminary support, no SysVinit services yet, so no auto-start.
    - Starting only the "config script" from the tray icon menu should work now.
    - Use `toshy-config-start` or `toshy-config-verbose-start` for manual start.
    - Only "rox-icewm" desktop verified/tested.

- Debian 12 tested and can be made to work:

    - If you gave root a password, your user will NOT be in the `sudo` group!
    - If necessary, add your user to `sudo` group (and reboot!)
        - `su -` (enter root's password)
        - `usermod -aG sudo yourusername`
        - Save a reboot step later by also doing this:
        - `usermod -aG input yourusername`
        - Seriously, reboot now!
    - Then, for Wayland+GNOME:
        - Install `flatpak` and the Flathub repo. Instructions here:
            - https://flatpak.org/setup/Debian
        - Do `flatpak install com.mattjakeman.ExtensionManager`
        - Reboot again! (So Flatpak folders are added to path.)
        - Install any compatible shell extension (see [**Requirements**](#requirements))
        - Recommended additional extensions:
            - AppIndicator and KStatusNotifierItem (for tray icon)
            - Logo Menu (enable power options in its settings)

- Deepin 23 (Debian-based)

    - NOTE: Long delay before services start (Zenity error?)

- Kali Linux 2023/2024 (Debian-based)

    - Tested with default desktop of Xfce
    - GNOME & KDE Plasma available in Kali installer

- LMDE 5/6 (Linux Mint Debian Edition)

    - Default desktop is Cinnamon, works

- MX Linux 21.x/23.x (Debian-based, related to antiX)

    - Preliminary support, no SysVinit services yet, so no auto-start.
    - Starting only the "config script" from the tray icon menu should work now.
    - Use `toshy-config-start` or `toshy-config-verbose-start` for manual start.
    - Choosing advanced options and booting with `systemd` will work fine.

- PeppermintOS (Debian-based)

    - New release based on Debian 12 tested
    - Desktop is Xfce4 v4.18

- Q4OS 5.2 (Debian-based)

    - Trinity desktop ISO tested.

- Window Maker Live 0.96 (Debian-based)

    - Tray icon may not auto-load at login. Gdk error?
    - Tray icon can be reloaded from the application finder. 

### Arch, Arch-based and related distros

- Arch in general? (maybe, needs more testing)

    - Installer will try to work on any distro that identifies as `arch`

- ArcoLinux (Arch-based)

    - ArcoLinuxL ISO (full installer) tested
    - Multiple desktops tested (GNOME, KDE, others)
    - X11/Xorg and Wayland (all working Wayland environments)
    - `plasma-wayland-session` can be installed
    - See FAQ Re: Application Menu shortcut fix

- EndeavourOS (Arch-based)

    - Most desktops should work in X11/Xorg
    - GNOME desktop should work in X11/Xorg and Wayland (requires extension)
    - KDE (Plasma) desktop should work in X11/Xorg and Wayland
    - `plasma-wayland-session` can be installed

- Garuda Linux (Arch-based)

    - KDE Dr460nized works
    - KDE Lite also works
    - GNOME will need shell extension (see [**Requirements**](#requirements))
    - Xfce, Cinnamon, i3wm, Qtile should work (not tested)
    - Sway should work (not tested)
    - Hyprland should work, but not tested, because:
        - Installer failed to run in testing VM

- Manjaro (Arch-based)

    - GNOME desktop variant tested
    - Xfce desktop variant tested
    - KDE Plasma desktop variant tested
    - `plasma-wayland-session` can be installed
    - See FAQ Re: Application Menu shortcut fix

### Independent distros

- Solus 4.4/4.5 (eopkg)

    - Budgie ISO tested, GNOME and MATE should work without issue

- Void Linux (xbps, rolling release) - PARTIAL SUPPORT

    - Void doesn't use `systemd`, no Runit scripts provided

    - Options to start the manual keymapper config script:
        - Tray icon menu: `Re/Start Toshy Script`
        - Terminal command: `nohup toshy-config-start &`
        - Runit service script to run terminal command
        - Put a desktop entry file in `~/.config/autostart`

## Currently working desktop environments or window managers

- X11/Xorg sessions

    - Any desktop environment should work

- Wayland sessions

    - Cinnamon 6.0 or later
    - GNOME 3.38 or later (needs shell extension, see [**Requirements**](#requirements))
    - Hyprland
    - Plasma 5 and 6 (KDE) [a KWin script gets installed]
    - Sway

If you are in an X11/Xorg login session, the desktop environment or window manager doesn't really matter. The keymapper gets the window class/name/title information directly from the X server with `Xlib`.  

On the other hand, if you are in a Wayland session, it is only possible to obtain the per-application or per-window information (for the app-specific shortcut keymaps) by using solutions that are custom to a limited set of desktop environments (or window managers).  

For Wayland+GNOME this requires at least one of the known compatible GNOME Shell extensions to be installed and enabled. See above in [**Requirements**](#requirements).  

There are specific remaps or overrides of default remaps for several common desktop environments (or distros which have shortcut peculiarities in their default desktop setups). They become active if the desktop environment is detected correctly by the `env.py` module used by the config file, or the information about the desktop can be placed in some `OVERRIDE` variables in the config file.  

## Usage (changing preferences)

See next section for usage of the Toshy terminal commands to manage the services and keymapper process. This section is about the preferences available via the tray icon menu, or the GUI "Toshy Preferences" app.

The tray icon menu has a few more convenient features that aren't entirely mirrored in the simple GUI app window.  

> [!TIP]  
> Note that changing the items in the submenus from the tray icon menu or the GUI app will cause the behavior of the keymapper config to change **_immediately_** (or within a couple of seconds), without requiring the keymapper process/services to be restarted. You only need to restart the services after editing the config file itself. Preferences are taken care of in memory, and the current state is stored in a small sqlite3 file (which gets preserved if you re-run the Toshy installer). Once you tweak a preference it should stay that way even if you reinstall.  

In the tray icon menu, you'll find a number of useful functions: 

- Top items show services status (not clickable)
- Toggle to disable/enable autostart of services
- Items to (re)start or stop the services
- Items to (re)start or stop just the config script
- Preferences submenu
- OptSpect Layout submenu
- Keyboard Type submenu
- Item to open the GUI app
- Item to open the Toshy config folder
- Item to show the services log (journal)
- Items to disable or remove the tray icon

### Why there are separate items for "services" and "script"

On some distros there may be some reason the `systemd` services can't run, or you simply don't want them to be enabled. For instance, CentOS 7 supports `systemd` services in general, but had the capacity for "user" services completely disabled, and Toshy uses "user" services. Some distros also don't use `systemd` at all as the init system, so the services won't exist. For these cases, the "Script" items provide a simple way to start just the keymapper config process, if you don't feel like setting up your own auto-start item that will run the `toshy-config-start` command. The lack of `systemd` and `loginctl` will mean that Toshy won't have the multi-user support that will otherwise be present. Not a big deal on a single-user system.  

### Preferences submenu

Here are the preferences that are currently available:  

- `Alt_Gr on Right Cmd`
- `CapsLock is Cmd`
- `CapsLock is Esc & Cmd`
- `Enter is Ent & Cmd`
- `Sublime3 in VSCode`
- `Forced Numpad`
- `Media Arrows Fix`

And what each of these preferences do:  

`Alt_Gr on Right Cmd` - International keyboard users will need to enable this to get to the additional ISO level 3 characters that they would normally reach by using the `Alt_Gr` key on the right side of the Space bar. Otherwise the Toshy config will turn that key into another Command key equivalent, like the key on the left side of the space bar. Note that this only fixes one aspect of the issues that non-US layout users may have with the keymapper.  

`CapsLock is Cmd` - Turns the CapsLock key into an additional Command key equivalent.  

`CapsLock is Esc & Cmd` - Turns the CapsLock key into a multi-purpose key. Escape if tapped, Command if held and combined with another key. (This can be easily modified to make the key `Esc & Ctrl` instead.)  

`Enter is Ent & Cmd` - Turns the Enter key into a multi-purpose key. Enter if tapped, Command if held and combined with another key.  

`Sublime3 in VSCode` - Enables Sublime 3 keyboard shortcut variations in VSCode variants, instead of native VSCode shortcuts.  

`Forced Numpad` - Enabled by default, this causes a PC keyboard's numeric keypad to simulate how a full-sized Apple keyboard behaves in macOS, where the keypad always acts like a numeric keypad. If you need the navigation functions, this can be disabled from the tray icon menu or GUI app, or with Option+NumLock (Fn+Clear also works on an Apple keyboard). The "Clear" key on an Apple keyboard is actually a NumLock key.  

`Media Arrows Fix` - If you have a laptop like mine where they put "media" functions (PlayPause/Stop/Rew/Fwd) on the arrow/cursor keys (when holding the `Fn` key), this preference option will "fix" them by letting the arrow keys behave like the arrow keys on a MacBook instead. They will be PgUp/PgDn/Home/End when holding the `Fn` key, and as long as the `Fn` key is included you can use them in keyboard shortcuts like `Fn+Shift+PgDn` (to select a page of text below the cursor, for example).  

### OptSpec Layout submenu

The `OptSpec Layout` submenu in the tray icon (or the radio buttons in the GUI app) shows which hard-coded Option-key special character layout is currently enabled in the Toshy config. Toggling one of the other items should almost immediately cause the layout to change or be disabled if desired.  

### Keyboard Type submenu

This submenu is a sort of temporary hack to force all attached keyboard devices to be seen as a specific type, which disables on-the-fly auto-adaptation, in case your keyboard type is being misidentified. You will receive a notification warning that this is only meant as a temporary fix while you follow the instructions to get the config file to correctly identify your keyboard type. If you restart Toshy, the setting will not be saved.  

The main reason you'd need to use this is when a keyboard that is not made by Apple either was made for use with macOS, or just has the modifier keys next to the Space bar swapped like an Apple keyboard (common in small keyboards made to work with multiple devices including iOS/iPadOS devices), so you need to force it to be treated like an Apple keyboard. These types of keyboards can't be easily identified as the correct type by just looking at the device name.  

After verifying that the forced keyboard type puts the modifiers in the correct place to work with muscle memory from using an Apple keyboard with macOS, you'll want to fix this permanently by opening your config file and editing the custom dictionary item to make the config see your device name as the correct type. See [here](#my-keyboard-is-not-recognized-as-the-correct-type) for more information.  

## Usage (terminal commands)

See above section for the GUI tools and preferences explanations. This section is only about the Toshy terminal commands. 

Toshy does its best to set itself up automatically on any Linux system that uses `systemd` and that is a "known" Linux distro type that the installer knows how to deal with (i.e., has a list of the correct native packages to install, and knows how to use the package manager). Generally this means distros that use any of these package managers:  

- `apt`
- `dnf`
- `eopkg`
- `pacman`
- `rpm-ostree`
- `transactional-update`
- `xbps-install`
- `zypper`

If the install was successful, there should be a number of different terminal commands available to check the status of the Toshy `systemd` user services (the services are not system-wide, in an attempt to support multi-user setups and support Wayland environments more easily) and stop/start/restart the services.  

Toshy actually consists of two separate `systemd` services meant to work together, with one monitoring the other, so the shell commands are meant to make working with the paired services much easier.  

(There is now a third service, but it is only active in a Wayland+Plasma environment, creating a D-Bus service to receive updates from the KWin script with the necessary window info.)  

The commands are copied into `~/.local/bin`, and you will be prompted to add that location to your shell's `PATH` if it is not present. Depends on the distro whether that location is already set up as part of the path or not.  

If you change your shell or reset your RC file and need to fix the path, an easy way to do that is to run this script that re-installs the terminal commands in the same way they were initially installed:  

```sh
~/.config/toshy/scripts/toshy-bincommands-setup.sh
```

These are the main commands for managing and checking the services:  

```
toshy-services-log      (shows journalctl output for Toshy services)
toshy-services-status   (shows the current state of all Toshy services)
toshy-services-start
toshy-services-stop
toshy-services-restart
```

To disable/enable the Toshy services (to prevent or restore autostart at login), use the commands below. It should still be possible to start/restart the services with the commands above if they are disabled. Using the "enable" command in turn will not automatically start the services immediately if they are not running (but the services will then autostart at the next login). If the services are enabled they can be stopped at any time with the command above, but the enabled services will start automatically at the next login. (NEW: This can finally also be dealt with in the tray icon menu, by toggling the `Autostart Toshy Services` item near the top of the menu.)  

```
toshy-services-disable  (services can still be started/stopped manually)
toshy-services-enable   (does not auto-start the service until next login)
```

If you'd like to completely uninstall or re-install the Toshy services, use the commands below. These are the same commands used by the Toshy installer to set up the services.  

```
toshy-systemd-remove    (stops and removes the systemd service units)
toshy-systemd-setup     (installs and starts the systemd service units)
```

The following commands are also available, and meant to allow manually running just the Toshy config file, without any reliance on `systemd`. These will automatically stop the `systemd` services so there is no conflict, for instance if you need to run the `verbose` version of the command to debug a shortcut that is not working as expected, or find out how you broke the config file.  

Restarting the Toshy services, either with one of the above commands or from the GUI preferences app or tray icon menu, will stop any manual config process and return to running the Toshy config as a `systemd` service. All the commands are designed to work together as conveniently as possible.  

```
toshy-config-restart
toshy-config-start
toshy-config-start-verbose  (show debugging output in the terminal)
toshy-config-verbose-start  (alias of 'toshy-config-start-verbose')
toshy-config-stop
```

And a command that will show what Toshy sees as the environment when you launch the config. This may be helpful when troubleshooting or making reports:  

```
toshy-env
```

For changing the function keys mode of a keyboard device that uses the `hid_apple` device driver/kernel module, use this command:  

```
toshy-fnmode                    (interactive prompts mode)
toshy-fnmode --help             (show usage/options)
toshy-fnmode --info             (show current status of fnmode)
toshy-fnmode [--option] [mode]  (change fnmode non-interactively)
```

To activate the Toshy Python virtual environment for doing things like running the keymapper directly, it is necessary to run this command:  

```
source toshy-venv
```

There are also some desktop apps that will be found in most Linux app launchers (like "Albert" or "Ulauncher") or application menus in Linux desktop environments:  

- Toshy Preferences
- Toshy Tray Icon

You may find them under a "Utilities" folder in some application menus (such as the IceWM menu). Or possibly under "Accessories" (LXDE menu).  

Both of these apps will show the current status of the `systemd` services, and allow the immediate changing of the exposed optional features, as well as stopping or restarting the Toshy services. The tray icon menu also allows opening the Preferences app, and opening the `~/.config/toshy` folder if you need to edit the config file.  

If the desktop apps aren't working for some reason, it may be useful to try to launch them from a terminal and see if they have any error output:  

```
toshy-gui
toshy-tray
```

## FAQ (Frequently Asked Questions)

FAQ section has been moved to a Wiki page to make the README shorter:  

https://github.com/RedBearAK/toshy/wiki/FAQ-(Frequently-Asked-Questions)

### Sponsor Me / Donate

This type of project takes extraordinary amounts of time and effort to work around weird problems in different distros. If you feel like I did something useful by creating this, and you'd like me to be able to spend time maintaining and improving it, buy me a coffee:  

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G34VVZW)

Thanks for checking out Toshy!  

§
