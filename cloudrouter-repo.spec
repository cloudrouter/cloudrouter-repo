%define cloudrouter_release 1-6

Summary:	CloudRouter repository files
Name:		cloudrouter-repo
Version:	1
Release:	1
License:	AGPLv3
Group:		System Environment/Base
Source:		https://github.com/cloudrouter/cloudrouter-release/archive/%{cloudrouter_release}.tar.gz
BuildArch:	noarch

%description
CloudRouter repository files.


%prep
%setup -c -q

# filter what we need from the cloudrouter-release source
CR_RELEASE_DIR=cloudrouter-release-%{cloudrouter_release}
for src in "RPM-GPG-KEY-cloudrouter*" "cloudrouter.repo"; do
    mv ${CR_RELEASE_DIR}/cloudrouter-release/${src} .
done

rm -rf ${CR_RELEASE_DIR}

%build

%install
rm -rf $RPM_BUILD_ROOT

# Install the keys
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg

install -m 644 RPM-GPG-KEY* $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

# and add symlink for compat generic location
ln -s RPM-GPG-KEY-cloudrouter-%{version}-primary RPM-GPG-KEY-%{version}-cloudrouter

install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
for file in cloudrouter*repo ; do
  sed -ie 's/\$releasever/%{version}/' $file
  install -m 644 $file $RPM_BUILD_ROOT/etc/yum.repos.d
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/cloudrouter.repo
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/RPM-GPG-KEY-cloudrouter*

%changelog
* Sat Apr 18 2015 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 1-1
- Initial cloudrouter-repo package

