Name: awscli
Version: 1.9.7
Release: 1.el7
Summary: This package provides a unified command line interface to Amazon Web Services.
Group: Productivity/Networking/Web/Servers
License: Apache Software License.
Url: https://pypi.python.org/pypi/awscli
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: python
Requires: python, python-docutils, python-jmespath, python-pyasn1, python-rsa, python-botocore, python-colorama, python-dateutil, python-six
BuildArch: noarch

%description
This package provides a unified command line interface to Amazon Web Services.

%prep
curl -s -o /data/rpmbuild/SOURCES/%{package}-${version}.tar.gz https://pypi.python.org/packages/source/a/%{name}/%{name}-%{version}.tar.gz

%setup
python setup.py build

%install
rm -Rf %{buildroot}
python setup.py install --prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files

%changelog
* Mon Nov 16 2015 - robert (at) meinit.nl
- Initial release.
