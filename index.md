---
layout: home
title: Home
permalink: /
nav_exclude: true
search_exclude: true
---
<h1 class="home-title"><img src="{{ "/assets/images/syncnuke-logo.png" | relative_url }}" alt="" width="64" height="64">SyncNuke</h1>

<p class="intro">An open standard for synchronized media playback.</p>

<div class="project-actions">
  <a class="project-button" href="{{ '/spec/' | relative_url }}">Read the specification</a>
  <a href="https://github.com/syncnuke">View on GitHub</a>
</div>

## How it works

SyncNuke separates [playback control]({{ '/spec/media-player/' | relative_url }}),
[synchronization logic]({{ '/spec/sync-client/' | relative_url }}), and
[network communication]({{ '/spec/networking/' | relative_url }}).
A player integration exposes playback state and controls; a synchronization client
coordinates that state with a shared session through a protocol.

These components can be developed independently. The
[specification]({{ '/spec/coordination/' | relative_url }}) describes how they work together.

## Why?

SyncNuke was born out of a necessity to simplify synchronized media playback, making it easier
for everyone to build their own reliable setups.

It provides a standardized way to connect media players and synchronization protocols,
alongside its own [DataSaver]({{ '/spec/data-saver/' | relative_url }}) protocol for reliable
synchronization.

## Get SyncNuke

Desktop and Android clients are available as development builds.

<div class="project-actions">
  <a class="project-button" href="{{ '/download/' | relative_url }}">Download a client</a>
</div>
