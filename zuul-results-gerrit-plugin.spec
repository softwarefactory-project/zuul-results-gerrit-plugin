%global debug_package %{nil}

# Enable fedora built rpm to be installable on el7
%define _source_payload w9.gzdio
%define _binary_payload w9.gzdio

Name:          zuul-results-gerrit-plugin
Version:       0.2.0
Release:       1%{?dist}
Summary:       A polygerrit plugin to display zuul results

License:       APACHE-2
URL:           https://www.softwarefactory-project.io

Source0:       HEAD.tgz
BuildArch:     noarch

%description
A polygerrit plugin to display zuul results

%prep
%autosetup -n dist

%build

%install
install -p -D -m 755 ZuulResultsPlugin.bs.js  %{buildroot}%{_sharedstatedir}/gerrit/plugins/zuul-results.js

%files
%{_sharedstatedir}/gerrit/plugins/zuul-results.js


%changelog
* Mon Mar 15 2021 Tristan Cacqueray <tdecacqu@redhat.com> - 0.1.2-1
- Initial packaging
