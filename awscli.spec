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

%setup -q -n %{name}-%{version}-src

%build
pip install awscli

TODO: Below this line.
%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/opt/%{name}
mkdir -p %{buildroot}/opt/%{name}/pid
mkdir -p %{buildroot}/opt/%{name}/webapps/
mkdir -p %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}/var/run/%{name}
%{__cp} -Rip ./output/build/{bin,conf,lib,logs,temp,webapps} %{buildroot}/opt/%{name}
%{__cp} %{_sourcedir}/%{name}.service %{buildroot}/etc/systemd/system/

%clean
rm -rf %{buildroot}

%pre
case "$1" in
  1)
    # This is an initial installation.
    getent group %{name} > /dev/null || groupadd -r %{name}
    getent passwd %{name} > /dev/null || useradd -r -g %{name} %{name}
  ;;
  2)
    # This is an upgrade.
    # Do nothing.
    :
  ;;
esac

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart {name}.service 

%files
%defattr(-,%{name},%{name},-)
%dir /opt/%{name}
%config /opt/%{name}/conf/*
/opt/%{name}/bin
/opt/%{name}/lib
/opt/%{name}/logs
/opt/%{name}/temp
/opt/%{name}/pid
%dir /opt/%{name}/webapps
/var/run/%{name}
%attr(0644,root,root) /etc/systemd/system/%{name}.service

%files manager
/opt/%{name}/webapps/manager

%files ROOT
/opt/%{name}/webapps/ROOT

%files docs
/opt/%{name}/webapps/docs

%files examples
/opt/%{name}/webapps/examples

%files host-manager
/opt/%{name}/webapps/host-manager

%changelog
* Thu Oct 29 2015 - robert (at) meinit.nl
- Cleaned up the RPM a bit.
* Fri Oct 23 2015 - robert (at) meinit.nl
- Changed apache-tomcat for %{name} and changed %pre logic.
* Thu Oct 22 2015 - robert (at) meinit.nl
- Importing to github and attempting to build in Travis CI
- Updating to 7.0.65
* Fri Aug 19 2011 - robert (at) meinit.nl
- Updated to apache tomcat 7.0.20
- Split (example) applications into their own RPM.
* Mon Jul 4 2011 - robert (at) meinit.nl
- Initial release.
