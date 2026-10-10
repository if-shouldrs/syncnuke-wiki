# SyncNuke website and specification

The repository for SyncNuke's [website](https://syncnuke.com).  Acts as an introduction to the stack, download page & general Wiki for understanding how it works and how to contribute.
## Local development

Install Ruby 3.3 and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve --livereload
```

Open **http://localhost:4000**. Build and verify without starting a server:

```sh
bundle exec jekyll build --trace
python3 scripts/verify_site.py
```

Commit `Gemfile.lock` when updating dependencies.






## Licensing

This repository is **source available**. All SyncNuke-authored content in `syncnuke-wiki`
is licensed under **PolyForm Noncommercial 1.0.0**. See [LICENSE.md](LICENSE.md) for the unchanged license text.

Third-party dependencies and components retain their respective licenses ([THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)).


