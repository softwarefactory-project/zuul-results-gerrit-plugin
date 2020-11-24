# zuul-results-gerrit-plugin

A polygerrit plugin to display zuul results.

## Install

Copy the `dist/ZuulResultsPlugin.bs.js` to `/var/gerrit/plugins/zuul-result.js`
and restart the service.

## Build from source

```
$ yarn add parcel
$ yarn build
$ npx parcel build src/ZuulResultsPlugin.re
```

## Contribute

Contributions are most welcome.
Get started by running:

```sh
git clone https://github.com/softwarefactory-project/zuul-results-gerrit-plugin
cd re-ansi
yarn install
yarn start
```

Apply change to a running gerrit service by:

Enable remote plugin reload by adding to gerrit.config:

```
[plugins]
    allowRemoteAdmin = true
```

Then reload using:

```
npx parcel build src/ZuulResultsPlugin.bs.js && \
  cp dist/ZuulResultsPlugin.bs.js /var/gerrit/plugins/zuul-results.js && \
  ssh -p 29418 admin@localhost gerrit plugin reload zuul-results
```

Make sure to read about [Reason][rescript-lang] too.

## Changes

### 0.1.0

- Initial release

[rescript-lang]: https://rescript-lang.org/docs/manual/v8.0.0/overview
