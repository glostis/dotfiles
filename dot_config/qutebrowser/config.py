# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig()

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
    "https://web.whatsapp.com/",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0",
    "https://accounts.google.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36",
    "https://*.slack.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0",
    "https://docs.google.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0",
    "https://drive.google.com/*",
)

# Duration (in milliseconds) to wait before removing finished downloads.
# If set to -1, downloads are never removed.
# Type: Int
c.downloads.remove_finished = 6000

c.downloads.location.suggestion = "both"

c.downloads.position = "bottom"

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined:  * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ["alacritty", "-e", "nvim", "{file}", "-c", "normal {line}G{column0}l"]

# Mode to use for hints.
# Type: String
# Valid values:
#   - number: Use numeric hints. (In this mode you can also type letters from the hinted element to filter and reduce the number of elements that are hinted.)
#   - letter: Use the characters in the `hints.chars` setting.
#   - word: Use hints words based on the html elements and the extra words.
c.hints.mode = "number"

c.hints.auto_follow = "always"
c.hints.auto_follow_timeout = 500

c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
]

# Needed for the "click to copy URL" on Github clone URL to work
c.content.javascript.can_access_clipboard = True

# Duration (in milliseconds) to show messages in the statusbar for. Set
# to 0 to never clear messages.
# Type: Int
c.messages.timeout = 6000

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = "last-used"

c.tabs.mode_on_change = "restore"

c.tabs.background = True

# Include hyperlinks in the keyboard focus chain when tabbing.
# This setting supports URL patterns.
# Type: Bool
c.input.links_included_in_focus_chain = False

c.fonts.tabs.selected = "bold default_size default_family"

# Automatically enter insert mode if an editable element is focused after loading the page.
# c.input.insert_mode.auto_load = True

c.url.searchengines = {
    # "DEFAULT": "https://www.google.com/search?hl=en&q={}",
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "gh": "https://github.com/{}",
    "ghs": "https://github.com/search?q={}",
    "py": "https://pypi.org/search/?q={}",
}

c.url.default_page = "https://duckduckgo.com"
c.url.open_base_url = True

c.fileselect.handler = "external"
c.fileselect.single_file.command = "alacritty --class dropdown_ranger --option window.dimensions.columns=150 --option window.dimensions.lines=38 -e ranger --choosefile={}".split(" ")
c.fileselect.multiple_files.command = "alacritty --class dropdown_ranger --option window.dimensions.columns=150 --option window.dimensions.lines=38 -e ranger --choosefiles={}".split(" ")
c.fileselect.folder.command = "alacritty --class dropdown_ranger --option window.dimensions.columns=150 --option window.dimensions.lines=38 -e ranger --choosedir={}".split(" ")

# Bindings
config.bind("<Ctrl+l>", "spawn --userscript qute-lastpass", mode="insert")
config.bind("<Ctrl+t>", "open -t", mode="passthrough")
config.bind("<Ctrl+u>", "spawn --userscript qute-lastpass --username-only", mode="insert")
config.bind("<Ctrl+p>", "spawn --userscript qute-lastpass --password-only", mode="insert")
config.bind("J", "tab-prev")
config.bind("K", "tab-next")
config.bind("x", "tab-close")
config.bind("t", "open -t")
config.unbind("<Ctrl+h>")

# Taken from https://github.com/qutebrowser/qutebrowser/issues/2668
config.bind("<Escape>", "mode-leave ;; jseval -q document.activeElement.blur()", mode="insert")

# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova
# Gruvbox medium scheme by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)
import os
import yaml

with open(os.path.expanduser("~/.config/alacritty/alacritty.yml")) as f:
    y = yaml.load(f.read(), Loader=yaml.Loader)

colors = y["colors"]

base00 = colors["primary"]["background"]
base01 = colors["primary"]["background-alt"]
base02 = colors["primary"]["background-alt-alt"]
base03 = colors["normal"]["white"]
base04 = colors["bright"]["white"]
base05 = colors["primary"]["foreground"]
# base06 = None
# base07 = None
base08 = colors["bright"]["red"]
base09 = colors["bright"]["orange"]
base0A = colors["bright"]["yellow"]
base0B = colors["bright"]["green"]
base0C = colors["bright"]["cyan"]
base0D = colors["bright"]["blue"]
base0E = colors["bright"]["magenta"]
# base0F = None

# if colors["primary"]["background"] == y["schemes"]["gruvbox-dark"]["primary"]["background"]:
if False:
    c.colors.webpage.darkmode.enabled = True
    c.colors.webpage.bg = base00
else:
    c.colors.webpage.darkmode.enabled = False
    c.colors.webpage.bg = None

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base01

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0A

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base05

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base03

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = base03

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base03

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base09

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base09

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = base01

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = base04

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = base00

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg = base05

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = base02

# Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = base05

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base09

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base02

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base0B

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base00

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base0D

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base00

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base0C

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base00

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base01

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base05

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base00

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base05

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base00

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base00

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base0E

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base00

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base0D

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base05

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0C

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0A

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base02

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base02

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base02

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base05

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base02

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base05

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base00

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base05

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base00

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base05

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base05

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base00

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base05

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base00
