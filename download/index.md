---
layout: default
title: Download
nav_order: 2
permalink: /download/
---
# Download

Get a SyncNuke client for shared media playback.
The builds below are pre-releases and are still in development.

<h2 id="desktop" class="download-heading">Desktop {% include os_icons.html platform="desktop" %}</h2>

SyncNuke Desktop connects your local media player to a SyncNuke session.
The current player integration supports mpv.

[Download SyncNuke Desktop 0.2.0 (ZIP)](https://github.com/if-shouldrs/syncnuke-desktop/releases/download/0.2.0/syncnuke-desktop-0.2.0.zip){: .project-button }

Extract the archive and launch with `start.sh` or `start.bat`.
See the setup instructions for requirements and configuration.

[Requirements](https://github.com/if-shouldrs/syncnuke-desktop/tree/main/README.md#requirements)
· [Setup and usage](https://github.com/if-shouldrs/syncnuke-desktop/tree/main/README.md#usage)
· [Release notes](https://github.com/if-shouldrs/syncnuke-desktop/releases/tag/0.2.0)
· [All releases](https://github.com/if-shouldrs/syncnuke-desktop/releases)
· [Source](https://github.com/if-shouldrs/syncnuke-desktop/tree/main)

<h2 id="android" class="download-heading">Android {% include os_icons.html platform="android" %}</h2>

SyncNuke Android adds SyncNuke support to Just Player.
This is a work-in-progress debug build, published as a prerelease.

[Download SyncNuke Android v0.216-syncnuke (APK)](https://github.com/if-shouldrs/syncnuke-android/releases/download/v0.216-syncnuke/Just.Player.v0.216-latest-accrescent-debug.apk){: .project-button }

Long-press the settings gear in the app to configure and enable synchronization.

[Release notes](https://github.com/if-shouldrs/syncnuke-android/releases/tag/v0.216-syncnuke)
· [All releases](https://github.com/if-shouldrs/syncnuke-android/releases)
· [Source](https://github.com/if-shouldrs/syncnuke-android/tree/main)

## Browser

A browser extension integration is planned. See the
[roadmap]({{ '/roadmap/' | relative_url }}#player-integrations).

## For developers

[SyncNuke Core](https://github.com/syncnuke/syncnuke-core/tree/main) provides the canonical implementation of the common contracts. See its
[usage instructions](https://github.com/syncnuke/syncnuke-core/tree/main/README.md#using-the-library) here. For contributions, please check
[Contributing]({{ '/contributing/' | relative_url }}#where-to-contribute).
