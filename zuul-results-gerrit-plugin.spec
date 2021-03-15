Name:          zuul-results-gerrit-plugin
Version:       0.2.0
Release:       1%{?dist}
Summary:       A polygerrit plugin to display zuul results

License:       APACHE-2
URL:           https://www.softwarefactory-project.io

Source0:       https://registry.npmjs.org/@softwarefactory-project/zuul-results-gerrit-plugin/-/zuul-results-gerrit-plugin-%{version}.tgz

%description
A polygerrit plugin to display zuul results

%prep
tar xzf %{SOURCE0}

%build

%install
install -p -D -m 755 ./package/dist/ZuulResultsPlugin.bs.js  %{buildroot}%{_sharedstatedir}/gerrit/plugins/zuul-results.js


%files
%attr(0644,gerrit,gerrit) %{_sharedstatedir}/gerrit/plugins/zuul-results.js


%changelog
* Mon Mar 15 2021 Tristan Cacqueray <tdecacqu@redhat.com> - 0.1.2-1
- Initial packaging
