Name: awscli
Version: 1.9.7
Release: 1.el7
Summary: This package provides a unified command line interface to Amazon Web Services.
Group: Productivity/Networking/Web/Servers
License: Apache Software License.
Url: https://pypi.python.org/pypi/awscli
Source: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: epel-release
BuildRequires: python-pip
Requires: python
BuildArch: noarch

%description
This package provides a unified command line interface to Amazon Web Services.

%prep
wget https://pypi.python.org/packages/source/a/%{name}/%{name}-%{version}.tar.gz

TODO: Below this line.
%install
rm -Rf %{buildroot}
pip install --install-option="--prefix=%{buildroot}" awscli

%clean
rm -rf %{buildroot}

%files

%changelog
* Mon Nov 16 2015 - robert (at) meinit.nl
- Initial release.
