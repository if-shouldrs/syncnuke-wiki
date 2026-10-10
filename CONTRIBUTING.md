## Layout and styling

- Documentation uses the upstream `default` layout, retaining navigation, search,
  breadcrumbs, heading anchors, and table wrappers.
- `_layouts/home.html` is a small standalone homepage layout without a sidebar or JavaScript.
- `_includes/site_header.html` owns the shared site navigation. Documentation loads it
  through the supported `header_custom.html` hook; the homepage includes it directly.
- `_includes/head_custom.html` loads the same custom CSS for both layouts.
- `_sass/custom/setup.scss` sets typography and layout variables through the supported setup hook.
- `_sass/color_schemes/syncnuke.scss` supplies the theme palette through its color-scheme extension point.
- `_sass/_project.scss` owns project styling and CSS design tokens, compiled by
  `assets/css/syncnuke.scss`. Keep matching theme/CSS palette values aligned when changing colors.
- `_includes/footer_custom.html` links the licensing policy from documentation pages.
- `_includes/favicon.html` suppresses the upstream favicon; `head_custom.html` uses the SyncNuke logo.
- `_includes/nav_footer_custom.html` replaces the stock theme attribution with project information.

Keep theme structural overrides small. When upgrading Just the Docs, check its custom
include hooks and the `.main-header`, `.search`, and `.side-bar` selectors, then build and
run the verifier. Content and styling can evolve independently.
