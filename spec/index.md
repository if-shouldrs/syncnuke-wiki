---
layout: default
title: Specification
nav_order: 1
has_children: true
permalink: /spec/
---
# SyncNuke specification

SyncNuke is a media synchronization standard. It provides a common framework for shared
media playback over the internet by defining expectations for player integrations,
synchronization clients, and networking.

## Reading the specification

Start with [Concepts]({{ '/spec/concepts/' | relative_url }}) for component responsibilities
and [Terminology]({{ '/spec/terminology/' | relative_url }}) for the vocabulary.

[Media player]({{ '/spec/media-player/' | relative_url }}),
[Sync client]({{ '/spec/sync-client/' | relative_url }}), and
[Networking]({{ '/spec/networking/' | relative_url }}) describe the individual components.

[Protocols]({{ '/spec/protocols/' | relative_url }}) introduces synchronization protocol support,
with [DataSaver]({{ '/spec/data-saver/' | relative_url }}) documenting the supported protocol.

[Coordination]({{ '/spec/coordination/' | relative_url }}#playback-information-flow) explains
how these components interact.

## Further information

See [Contributing]({{ '/contributing/' | relative_url }}) to get involved, or
[Download]({{ '/download/' | relative_url }}) for available clients.
