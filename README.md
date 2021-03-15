# zuul-results-gerrit-plugin

A polygerrit plugin to display zuul results.

## Install

Copy the `dist/ZuulResultsPlugin.bs.js` to `/var/gerrit/plugins/zuul-result.js`
and restart the service.

## Build from source

```
$ pnpm install --shamefully-hoist
$ pnpm dist
```

## Contribute

Contributions are most welcome.
Get started by running:

```sh
git clone https://github.com/softwarefactory-project/zuul-results-gerrit-plugin
cd zuul-results-gerrit-plugin
pnpm start
```

Apply change to a running gerrit service by:

Enable remote plugin reload by adding to gerrit.config:

```
[plugins]
    allowRemoteAdmin = true
```

Then reload using:

```
pnpm dist && \
  cp dist/ZuulResultsPlugin.bs.js /var/gerrit/plugins/zuul-results.js && \
  ssh -p 29418 admin@localhost gerrit plugin reload zuul-results
```

Make sure to read about [ReScript][rescript-lang] too.

## Changes

### 0.2.0

- Replace npm by pnpm.

### 0.1.2

- Set the table id so that it is cleared between reload.

### 0.1.1

- Support multiple CI result with optional pipeline.
- Detect dark-mode and adapt the colors.

### 0.1.0

- Initial release

[rescript-lang]: https://rescript-lang.org/docs/manual/v8.0.0/overview
