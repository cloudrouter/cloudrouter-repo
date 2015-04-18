
Summary:	CloudRouter repository files
Name:		cloudrouter-repo
Version:	1
Release:	2
License:	AGPLv3
Group:		System Environment/Base
Source0:    cloudrouter.repo
Source1:    RPM-GPG-KEY-cloudrouter-1-primary
BuildArch:	noarch
Conflicts:  cloudrouter-release

%description
CloudRouter repository files.

%prep
%setup -q  -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

# Create dirs
install -dm 755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# Install repo
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Sat Apr 18 2015 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 1-2
- Conflict with cloudrouter-release package as this is meant to be installed
  only on non-release distros

* Sat Apr 18 2015 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 1-1
- Initial cloudrouter-repo package

